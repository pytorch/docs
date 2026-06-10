# Device Management

## Background

Device management covers basics such as querying how many devices are available and switching between them. Accelerator backends wrap their device‑runtime APIs and expose them to PyTorch.

## Design

Accelerator vendors should implement these core functions:

| Function name | Description | Application scenarios |
| --- | --- | --- |
| `device_count()` | Query the total number of available devices in the system | - Application initialization - Multi-device workload distribution - Validating device indices before use |
| `current_device()` | Get the currently active device for the calling thread | - Debugging and logging - Determining tensor placement - Guard implementations |
| `set_device()` | Change the active device for subsequent operations | - Switching context between devices - Initializing specific device resources - Multi-GPU training loops |
| `exchange_device()` | Atomically swap device and return the previous device | - Implementing device guards - Temporarily switching device context - RAII-based device management |
| `maybe_exchange_device()` | Conditionally exchange device only if the index is valid (−1 allowed) | - Safe device switching with optional indices - Guard implementations with nullable device values |

These functions are the building blocks for streams, events, and memory management. Validate inputs and handle errors properly.

## Implementation

This section illustrates device management using `set_device` as an example. The implementation requires:

1. C++ wrappers around the device runtime
2. Python bindings to expose the C++ functions
3. User-friendly Python APIs

For illustration, OpenReg (Open Registration) is a PyTorch integration example that fills the gap for out‑of‑tree accelerator backend integration. Its implementation ([`OpenRegFunctions.h/cpp`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/csrc/runtime/OpenRegFunctions.cpp)) demonstrates how to wrap a third‑party runtime cleanly. These functions are reused across the backend--for streams, events, generators, and Python bindings.

### C++ side

Wrap the device‑runtime API and add error handling. The `SetDevice` function shows this pattern:

```
1orError_t SetDevice(DeviceIndex device) {
2 int cur_device = -1;
3 OPENREG_CHECK(orGetDevice(&cur_device));
4 if (device == cur_device) {
5 return orSuccess;
6 }
7 return orSetDevice(device);
8}
```

```
1OPENREG_EXPORT void set_device(DeviceIndex device) {
2 check_device_index(device);
3 OPENREG_CHECK(SetDevice(device));
4}
```

### Bindings

Expose the C++ functions to Python using pybind11:

```
1PyObject* _setDevice(PyObject* self, PyObject* arg) {
 2 HANDLE_TH_ERRORS
 3 TORCH_CHECK(THPUtils_checkLong(arg), "invalid argument to setDevice");
 4 auto device = THPUtils_unpackDeviceIndex(arg);
 5 torch::utils::device_lazy_init(at::kPrivateUse1);
 6 c10::openreg::set_device(device);
 7
 8 Py_RETURN_NONE;
 9 END_HANDLE_TH_ERRORS
10}
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

### Python side

Wrap the C++ bindings with user-friendly Python functions:

```
1def set_device(device) -> None:
2 if device >= 0:
3 torch_openreg._C._set_device(device)
4
5
```

Here's the complete mapping from C++ to Python:

| C++ binding function | C++ binding API (pybind11) | Python user API | Description |
| --- | --- | --- | --- |
| `_getDeviceCount` | `torch_openreg._C._get_device_count()` | `torch.openreg.device_count()` | Returns the total number of devices |
| `_getDevice` | `torch_openreg._C._get_device()` | `torch.openreg.current_device()` | Returns the current active device index |
| `_setDevice` | `torch_openreg._C._set_device(idx)` | `torch.openreg.set_device(idx)` | Sets the active device |
| `_exchangeDevice` | `torch_openreg._C._exchange_device(idx)` | N/A (internal use only) | Atomically swaps device and returns previous |

## Guard

Device guards provide automatic device switching with exception safety. They're similar to C++ lock guards--they switch devices on construction and restore on destruction.

Implement `DeviceGuardImplInterface` to integrate with PyTorch's guard system:

```
1 /**
 2 * Return the type of device managed by this guard implementation.
 3 */
 4 DeviceType type() const override {
 5 return static_type;
 6 }
 7 /**
 8 * Set the current device to device d, and return the previous Device.
 9 */
10 // LITERALINCLUDE START: OPENREG GUARD DEVICE MANAGEMENT
11 Device exchangeDevice(Device d) const override {
12 TORCH_CHECK(d.is_privateuseone(), "Expected a PrivateUse1 device, but got ", d);
13
14 auto old_device_index = ExchangeDevice(d.index());
15 return Device(static_type, old_device_index);
16 }
17 // LITERALINCLUDE END: OPENREG GUARD DEVICE MANAGEMENT
18
19 /**
20 * Get the current device.
21 */
22 Device getDevice() const override {
23 int device_index = current_device();
24 return c10::Device(static_type, device_index);
25 }
26
27 /**
28 * Get the device capability for a given device.
29 * By default, OpenReg has 2 same devices with the same capability.
30 */
31 DeviceCapability getDeviceCapability(Device /*unused*/) const override {
32 return DeviceCapability();
33 }
34
35 /**
36 * Set the current device to c10::Device.
37 */
38 void setDevice(Device d) const override {
39 TORCH_CHECK(d.is_privateuseone(), "Expected a PrivateUse1 device, but got ", d);
40
41 set_device(d.index());
42 }
43
44 /**
45 * Set the current device to device d, without checking for errors
46 * (so, e.g., this can be called from a destructor).
47 */
48 void uncheckedSetDevice(Device d) const noexcept override {
49 set_device(d.index());
50 }
51
52 /**
53 * Get the number of devices.
54 *
55 * WARNING: This is REQUIRED to not raise an exception.
56 * If there is some sort of problem, e.g., driver error,
57 * you should report that there are zero available devices.
58 */
59 DeviceIndex deviceCount() const noexcept override {
60 return device_count();
61 }
62
63 /**
64 * Wait (by blocking the calling thread) until all the work has
65 * completed running on the device.
66 */
67 void synchronizeDevice(const DeviceIndex device_index) const override {
68 OPENREG_CHECK(orDeviceSynchronize());
69 }
```

This makes the guard available in PyTorch for the `PrivateUse1` device type; users can then use standard PyTorch device guards with the custom backend.