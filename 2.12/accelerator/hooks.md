# Accelerator Hooks

## Background

Accelerator hooks are the mechanism for integrating custom accelerator devices into PyTorch's runtime.

## Design

The tables below list the hooks accelerator vendors should implement when integrating a new device backend. These hooks are categorized into two priority levels:

- **High‑priority hooks**: Core APIs that the PyTorch runtime directly depends on. Vendors should implement all high‑priority hooks to ensure core compatibility and basic device functionality.
- **Low‑priority hooks**: Device‑management and utility APIs that PyTorch does not directly depend on. These hooks enhance user experience and multi‑device support and are optional. Vendors can implement them based on specific requirements and use cases.

### High‑priority hooks

| Hook method | Description | Application scenarios |
| --- | --- | --- |
| `init()` | Initializes the accelerator runtime and device contexts | Set up necessary state when PyTorch first accesses the device |
| `hasPrimaryContext(DeviceIndex)` | Checks if a primary context exists for the device | Determine whether device initialization has occurred |
| `getDefaultGenerator(DeviceIndex)` | Returns the default random number generator for a device | Access the device's primary RNG for reproducible random operations |
| `getNewGenerator(DeviceIndex)` | Creates a new independent random number generator | Create isolated RNG instances for parallel operations |
| `getDeviceFromPtr(void*)` | Determines which device a memory pointer belongs to | Identify the accelerator device associated with a memory allocation |
| `getPinnedMemoryAllocator()` | Returns an allocator for pinned (page-locked) host memory | Allocate host memory that can be efficiently transferred to/from the accelerator |
| `isPinnedPtr(void*)` | Checks if a pointer points to pinned memory | Validate memory types before performing operations |

### Low‑priority hooks

| Hook method | Description | Application scenarios |
| --- | --- | --- |
| `isBuilt()` | Returns whether the accelerator backend is built/compiled into the extension | Check whether the accelerator library is available at compile time |
| `isAvailable()` | Returns whether the accelerator hardware is available at runtime | Verify whether accelerator devices can be detected and initialized |
| `deviceCount()` | Returns the number of available accelerator devices | Enumerate all available accelerator devices for device selection |
| `setCurrentDevice(DeviceIndex)` | Sets the active device for the current thread | Switch the current thread's context to a specific accelerator device |
| `getCurrentDevice()` | Returns the currently active device index | Query which accelerator device is active in the current thread |
| `exchangeDevice(DeviceIndex)` | Atomically exchanges the current device and returns the previous one | Temporarily switch devices and restore the previous device afterward |
| `maybeExchangeDevice(DeviceIndex)` | Conditionally exchanges device only if the index is valid | Safely attempt device switching with validation |

## Implementation

For illustration, OpenReg (Open Registration) is a PyTorch integration example that fills the gap for out‑of‑tree accelerator backend integration. It demonstrates how vendors can register custom device backends--without modifying PyTorch core--by implementing the hooks interface (see [`at::PrivateUse1HooksInterface`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/detail/PrivateUse1HooksInterface.h#L15-L72)).

We use `getDefaultGenerator` as an example:

```
1 const at::Generator& getDefaultGenerator(DeviceIndex device_index) const override {
2 return getDefaultOpenRegGenerator(device_index);
3 }
```

In this implementation:

1. **Override the base interface**: The `getDefaultGenerator` method overrides the virtual method from [`at::PrivateUse1HooksInterface`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/detail/PrivateUse1HooksInterface.h#L15-L72).
2. **Delegate to the device‑specific implementation**: Call `getDefaultOpenRegGenerator(device_index)`, which manages a per‑device generator instance.
3. **Return a device‑specific generator**: The returned `at::Generator` wraps an `OpenRegGeneratorImpl` that implements device‑specific random number generation.

This pattern applies to all hooks: override the interface method, validate inputs, delegate to your device‑specific API, and return results in PyTorch's expected format.

## Integration Example

The following sections demonstrate how PyTorch integrates with accelerator hooks when accessing the default random number generator. The example traces the complete flow from user-facing Python code down to the device-specific implementation.

### Layer 1: User Code

User code sets a deterministic seed by calling `manual_seed`:

```
import torch
torch.openreg.manual_seed(42)
```

### Layer 2: Extension Python API

The Python API layer manages device selection and calls into the C++ extension (defined in [`torch_openreg/openreg/random.py`](https://github.com/pytorch/pytorch/tree/main/test/cpp_extensions/open_registration_extension/torch_openreg/torch_openreg/openreg/random.py#L48-L53)):

```
1def manual_seed(seed: int) -> None:
2 seed = int(seed)
3
4 idx = current_device()
5 default_generator = torch_openreg._C._get_default_generator(idx)
6 default_generator.manual_seed(seed)
7
8
```

The `manual_seed` function obtains the current device index, calls `torch_openreg._C._get_default_generator(idx)` to get the device‑specific generator, and sets its seed.

### Layer 3: Python/C++ Bridge

The C++ extension exposes `_getDefaultGenerator` to Python, which bridges into PyTorch core:

```
1static PyObject* _getDefaultGenerator(PyObject* self, PyObject* arg) {
 2 HANDLE_TH_ERRORS
 3 TORCH_CHECK(
 4 THPUtils_checkLong(arg),
 5 "_get_default_generator expects an int, but got ",
 6 THPUtils_typename(arg));
 7 auto idx = static_cast<int>(THPUtils_unpackLong(arg));
 8
 9 torch::utils::register_fork_handler_for_device_init(at::kPrivateUse1);
10 return THPGenerator_initDefaultGenerator(
11 at::globalContext().defaultGenerator(
12 c10::Device(c10::DeviceType::PrivateUse1, idx)));
13
14 END_HANDLE_TH_ERRORS
15}
```

```
1static PyMethodDef methods[] = {
2 {"_init", _initExtension, METH_NOARGS, nullptr},
3 {"_isInBadFork", _isInBadFork, METH_NOARGS, nullptr},
4 {"_get_default_generator", _getDefaultGenerator, METH_O, nullptr},
5 {"_get_device", _getDevice, METH_NOARGS, nullptr},
6 {"_set_device", _setDevice, METH_O, nullptr},
7 {"_exchangeDevice", _exchangeDevice, METH_O, nullptr},
8 {"_get_device_count", _getDeviceCount, METH_NOARGS, nullptr},
9 {nullptr, nullptr, 0, nullptr}};
```

This function unpacks the device index from Python, creates a `PrivateUse1` device object, and calls `at::globalContext().defaultGenerator()`. PyTorch's context then dispatches to the registered hooks.

### Layer 4: PyTorch Core Context

PyTorch's `Context` class dispatches to the appropriate accelerator hooks ([`aten/src/ATen/Context.h`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/Context.h#L61-L102)):

```
1 const Generator& defaultGenerator(Device device) {
 2 c10::DeviceType device_type = device.type();
 3 lazyInitDevice(device_type);
 4
 5 if (device_type == at::kCPU) {
 6 return at::detail::getDefaultCPUGenerator();
 7 } else {
 8 return getAcceleratorHooksInterface(device_type)
 9 .getDefaultGenerator(device.index());
10 }
11 }
12
13 const AcceleratorHooksInterface& getAcceleratorHooksInterface(
14 std::optional<c10::DeviceType> opt_device_type = std::nullopt) {
15 if (!opt_device_type.has_value()) {
16 opt_device_type = at::getAccelerator(true);
17 }
18 if (opt_device_type == at::kCUDA) {
19 return at::detail::getCUDAHooks();
20 } else if (opt_device_type == at::kXPU) {
21 return at::detail::getXPUHooks();
22 } else if (opt_device_type == at::kMPS) {
23 return at::detail::getMPSHooks();
24 } else if (opt_device_type == at::kPrivateUse1) {
25 return at::detail::getPrivateUse1Hooks();
26 } else if (opt_device_type == at::kMTIA) {
27 return at::detail::getMTIAHooks();
28 } else if (opt_device_type == at::kHIP) {
29 return at::detail::getHIPHooks();
30 } else if (opt_device_type == at::kHPU) {
31 return at::detail::getHPUHooks();
32 } else if (opt_device_type == at::kXLA) {
33 return at::detail::getXLAHooks();
34 } else {
35 TORCH_CHECK(
36 false,
37 opt_device_type.has_value()
38 ? c10::DeviceTypeName(opt_device_type.value())
39 : "None",
40 " device type not an accelerator.");
41 }
42 }
```

This layered architecture keeps PyTorch device‑agnostic while delegating hardware‑specific operations to accelerator implementations. Hooks are registered once at module load time:

```
1namespace c10::openreg {
2
3static bool register_hook_flag [[maybe_unused]] = []() {
4 at::RegisterPrivateUse1HooksInterface(new OpenRegHooksInterface());
5
6 return true;
7}();
8
9} // namespace c10::openreg
```

### Layer 5: Accelerator Hooks

The hooks interface provides the abstraction PyTorch uses to delegate to device‑specific implementations:

```
1 const at::Generator& getDefaultGenerator(DeviceIndex device_index) const override {
2 return getDefaultOpenRegGenerator(device_index);
3 }
```

The `getDefaultGenerator` hook method overrides the base interface and delegates to `getDefaultOpenRegGenerator`, which manages the actual generator instances.

### Layer 6: Device-Specific Implementation

The device‑specific implementation manages per‑device generator instances:

```
1const at::Generator& getDefaultOpenRegGenerator(c10::DeviceIndex device_index) {
 2 static bool flag [[maybe_unused]] = []() {
 3 auto deivce_nums = device_count();
 4 default_generators.resize(deivce_nums);
 5 for (auto i = 0; i < deivce_nums; i++) {
 6 default_generators[i] = at::make_generator<OpenRegGeneratorImpl>(i);
 7 default_generators[i].seed();
 8 }
 9 return true;
10 }();
11
12 c10::DeviceIndex idx = device_index;
13 if (idx == -1) {
14 idx = current_device();
15 } else {
16 TORCH_CHECK(idx >= 0 && idx < device_count());
17 }
18 return default_generators[idx];
19}
```

This function maintains a static vector of generators (one per device), initializes them on first access, validates the device index, and returns the appropriate generator instance.