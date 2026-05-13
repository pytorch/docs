# Operator Registration

For new accelerators, one of the most important and fundamental aspects of integration is supporting high-performance operators. To facilitate operator adaptation for users and accelerator developers, PyTorch provides multiple methods for developing and registering operators in both `Python` and `C++`. The following sections detail some of PyTorch's fundamental capabilities for operator registration.

Note

`Dispatch Key` is used to uniquely identify accelerator within PyTorch, such as `CPU`, `CUDA`, `MPS`, and `PrivateUse1`. In theory, all subsequent new accelerators will share `PrivateUse1`, leveraging its built-in comprehensive scaffolding capabilities to complete the integration of new accelerators. Please refer to [Let's talk about the PyTorch dispatcher](https://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/) if you are interested with dispatcher.

## Operator Set

PyTorch currently has over 3500 built-in operators (including related operator variants). This represents a significant workload from any perspective, and supporting this massive number of operators in a short period of time is no easy task. Therefore, as the first step in developing new backend operators, our goal should be to focus on the essential operators. For other operators, we can first use the community's fallback mechanism to support the feature as the first priority. After that, we can gradually complete other operators to improve the performance of the new backend.

The required operator set is listed below, primarily consisting of low-level operators required by factory functions and fallback operators:

| Operator Name | Dispatch Key | Description |
| --- | --- | --- |
| empty.memory_format | PrivateUse1 | Create an uninitialized Tensor with the specified shape and memory layout (the stride is automatically calculated) |
| empty_strided | PrivateUse1 | Create an uninitialized Tensor of the specified shape and stride (more degrees of freedom) |
| as_strided | PrivateUse1 | Create a shared view of the input Tensor with new shape, stride, and offset (without allocating new memory) |
| view | PrivateUse1 | Create a shared view of the input Tensor with new shape, but the original Tensor must be memory-contiguous |
| _reshape_alias | PrivateUse1 | Creates a shared view without safety checks(Internal version of reshape) |
| resize_ | PrivateUse1 | Modify the shape of the Tensor in place and reallocate memory if capacity is insufficient |
| _copy_from | PrivateUse1 | The underlying core function of Tensor.copy_ is responsible for the actual cross-device data copying |
| _copy_from_and_resize | PrivateUse1 | Combine `resize_` and `_copy_from` to resize first and then copy |
| _local_scalar_dense | PrivateUse1 | The underlying implementation of `.item()`, extracting values from Tensor to CPU scalars |
| set_.source_Tensor | PrivateUse1 | Set the current Tensor using the specified Tensor |
| set_.source_Storage | PrivateUse1 | Set the current Tensor using the specified Storage |
| set_.source_Storage_storage_offset | PrivateUse1 | Set the current Tensor using the specified Storage with the storage offset |
| fallback | PrivateUse1 | Fallback to CPU |

## Basics

Now that we have defined the initial scope of operator support, we can begin developing operator adaptations. This section will explain these implementations in `Python` and `C++` based on actual scenarios.

### Step 1

The operators mentioned above share a common characteristic: They are built-in PyTorch operators with defined `namespaces` and `Schemas`, and these operators' built-in accelerators (`CPU`, `CUDA`, etc.) have been implemented. What we have to do next is to implement these operators for the new accelerators.

C++

```
1at::Tensor empty_memory_format(
 2 c10::IntArrayRef size,
 3 std::optional<c10::ScalarType> dtype_opt,
 4 std::optional<c10::Layout> layout_opt,
 5 std::optional<c10::Device> device_opt,
 6 std::optional<bool> pin_memory_opt,
 7 std::optional<c10::MemoryFormat> memory_format_opt) {
 8 const auto device = c10::device_or_default(device_opt);
 9 const auto dtype = c10::dtype_or_default(dtype_opt);
10 TORCH_CHECK(device.is_privateuseone());
11 TORCH_CHECK(
12 c10::layout_or_default(layout_opt) == c10::Layout::Strided,
13 "Non strided layout not supported");
14 TORCH_CHECK(
15 !c10::pinned_memory_or_default(pin_memory_opt),
16 "Pin memory can only be on CPU");
17 const c10::DeviceGuard device_guard(device);
18 constexpr c10::DispatchKeySet pu1_dks(c10::DispatchKey::PrivateUse1);
19 auto allocator = at::GetAllocator(at::kPrivateUse1);
20 return at::detail::empty_generic(
21 size, allocator, pu1_dks, dtype, memory_format_opt);
22}
```

```
1at::Tensor wrapper_empty_memory_format(
 2 c10::IntArrayRef size,
 3 std::optional<c10::ScalarType> dtype_opt,
 4 std::optional<c10::Layout> layout_opt,
 5 std::optional<c10::Device> device_opt,
 6 std::optional<bool> pin_memory_opt,
 7 std::optional<c10::MemoryFormat> memory_format_opt) {
 8 return at::native::openreg::empty_memory_format(
 9 size,
10 dtype_opt,
11 layout_opt,
12 device_opt,
13 pin_memory_opt,
14 memory_format_opt);
15}
```

Taking the `empty.memory_format` operator as an example, we first need to query the operator's `schema` information in `native_functions.yaml`, which contains detailed signature information. Then, we can implement the operator based on the capabilities of the new accelerator.

```
- func: empty.memory_format(SymInt[] size, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None, MemoryFormat? memory_format=None) -> Tensor
dispatch:
 CPU: empty_cpu
 CUDA: empty_cuda
 ...
```

C++

```
1TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
 2 m.impl("empty.memory_format", wrapper_empty_memory_format);
 3 m.impl("empty_strided", wrapper_empty_strided);
 4 m.impl("as_strided", wrapper_as_strided);
 5 m.impl("resize_", wrapper_resize_);
 6 m.impl("_reshape_alias", wrapper__reshape_alias);
 7 m.impl("_copy_from", wrapper__copy_from);
 8 m.impl("_copy_from_and_resize", wrapper__copy_from_and_resize);
 9 m.impl("_local_scalar_dense", wrapper__local_scalar_densor);
10 m.impl(
11 "_has_compatible_shallow_copy_type",
12 wrapper_has_compatible_shallow_copy_type);
13 m.impl("set_.source_Tensor", wrapper_set_source_Tensor_);
14 m.impl("set_.source_Storage", wrapper_set_source_Storage_);
15 m.impl(
16 "set_.source_Storage_storage_offset",
17 wrapper_set_source_Storage_storage_offsetset_);
18 m.impl("view", wrapper_view);
19}
```

After completing the `wrapper_empty_memory_format`, we can register `aten::empty.memory_format` for `PrivateUse1` through `TORCH_LIBRARY_IMPL`.

### Step 2

By following Step 1, we can complete the development and registration of all operators except `fallback`. Next, to support operators related to operations (such as mathematical operations and convolution operations), we need to implement the registration of fallback semantics. This is a built-in capability provided by the PyTorch framework that can fallback some operations that are not supported by new accelerators to the CPU for execution. For new backends in development, this is an extremely effective way to ensure functionality at the expense of performance.

C++

```
1void cpu_fallback(const c10::OperatorHandle& op, torch::jit::Stack* stack) {
 2 static const std::unordered_set<c10::OperatorName> cpu_fallback_blocklist = {
 3 c10::OperatorName("aten::abs", ""),
 4 c10::OperatorName("aten::abs", "out"),
 5 };
 6
 7 const auto& op_name = op.schema().operator_name();
 8 if (cpu_fallback_blocklist.count(op_name)) {
 9 TORCH_CHECK(
10 false,
11 "Operator '",
12 op_name,
13 "' is not implemented for device openreg.");
14 } else {
15 at::native::cpu_fallback(op, stack);
16 }
17}
```

```
1void wrapper_cpu_fallback(
2 const c10::OperatorHandle& op,
3 torch::jit::Stack* stack) {
4 at::native::openreg::cpu_fallback(op, stack);
5}
```

```
1TORCH_LIBRARY_IMPL(_, PrivateUse1, m) {
2 m.fallback(
3 torch::CppFunction::makeFromBoxedFunction<&wrapper_cpu_fallback>());
4}
```

`wrapper_cpu_fallback` wraps the `at::native::cpu_fallback` method provided by PyTorch and is registered with `PrivateUse1` in PyTorch via `TORCH_LIBRARY_IMPL`. Subsequent operations not supported by the new backend will automatically fall back to the CPU for execution, and the results will be passed back to the new backend after execution.

## Advanced

### Selective Fallback

Enabling the fallback mechanism only for certain operators, while following PyTorch's default behavior for other operators (an error will be reported if the accelerator does not have a corresponding operator implementation), this is a very reasonable scenario as well.

C++

```
1void wrapper_cpu_fallback(
2 const c10::OperatorHandle& op,
3 torch::jit::Stack* stack) {
4 at::native::openreg::cpu_fallback(op, stack);
5}
```

```
1TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
2 m.impl(
3 "sub.Tensor",
4 torch::CppFunction::makeFromBoxedFunction<&wrapper_cpu_fallback>());
5}
```

Per-operator fallbacks are very similar to global fallbacks, the only difference being the registration method: calling `m.impl` registers an implementation for a specific operator, while `m.fallback` registers a default implementation for all operators.

C++

```
1void cpu_fallback(const c10::OperatorHandle& op, torch::jit::Stack* stack) {
 2 static const std::unordered_set<c10::OperatorName> cpu_fallback_blocklist = {
 3 c10::OperatorName("aten::abs", ""),
 4 c10::OperatorName("aten::abs", "out"),
 5 };
 6
 7 const auto& op_name = op.schema().operator_name();
 8 if (cpu_fallback_blocklist.count(op_name)) {
 9 TORCH_CHECK(
10 false,
11 "Operator '",
12 op_name,
13 "' is not implemented for device openreg.");
14 } else {
15 at::native::cpu_fallback(op, stack);
16 }
17}
```

Of course, global fallbacks can also be combined with a blacklist of fallbacks, which is a common approach, especially when only a few operators do not support fallbacks.

### PyTorch STUB

PyTorch also provides another approach for built-in operators: `STUB`. This method is essentially based on the Step 1 approach, but adds secondary scheduling capabilities (for example, scheduling based on CPU characteristics).

Note

The `STUB` method currently supports only a limited set of operators. For new accelerator devices, the advantage of the `STUB` method is that it significantly reduces the cost of development at the cost of a small performance overhead. PyTorch currently does not clearly list the set of operators that can be registered through `STUB`. Due to the large number of related operators, only the query method for the supported operator list is provided here.

```
pushd ${TORCH_ROOT}

find aten -type f -a -name "*.h" | xargs -I {} grep -wl "^DECLARE_DISPATCH" {}

popd
```

`DECLARE_DISPATCH` is a macro used to explicitly declare `STUB`. It is currently distributed in the `aten` directory. Based on this macro, you can find all operators that can be integrated using the `STUB` method.

```
...
aten/src/ATen/native/Activation.h
aten/src/ATen/native/FusedSGD.h
aten/src/ATen/native/nested/NestedTensorBinaryOps.h
aten/src/ATen/native/TensorCompare.h
aten/src/ATen/native/Sorting.h
...
```

```
using unary_fn = void(*)(TensorIteratorBase&);

DECLARE_DISPATCH(unary_fn, abs_stub)
```

The above listing contains the file that declares the `STUB` operator, where you can clearly see the STUB name and the associated function signature. Next, we will take `abs_stub` as an example to briefly introduce the path to support operators through `STUB`.

C++

```
1void abs_kernel(at::TensorIteratorBase& iter) {
 2 TORCH_CHECK(iter.ntensors() == 2, "Abs kernel expects 2 tensors");
 3 TORCH_CHECK(
 4 iter.common_dtype() == at::ScalarType::Float,
 5 "Abs kernel only supports float type");
 6
 7 auto& output_tensor = iter.tensor(0);
 8 auto& input_tensor = iter.tensor(1);
 9
10 TORCH_CHECK(
11 input_tensor.sizes() == output_tensor.sizes(),
12 "Input and output tensor sizes must match.");
13
14 auto abs_loop = [](float* out_ptr, const float* in_ptr, int64_t n) {
15 for (int64_t i = 0; i < n; ++i) {
16 out_ptr[i] = std::abs(in_ptr[i]);
17 }
18 };
19
20 MemoryGuard guard(input_tensor, output_tensor);
21
22 if (iter.is_contiguous()) {
23 abs_loop(
24 static_cast<float*>(iter.data_ptr(0)),
25 static_cast<float*>(iter.data_ptr(1)),
26 iter.numel());
27 } else {
28 TORCH_CHECK(
29 input_tensor.is_contiguous(), "Input tensor must be contiguous.")
30
31 auto output = at::empty(
32 input_tensor.sizes(),
33 input_tensor.options().memory_format(
34 input_tensor.suggest_memory_format()));
35
36 MemoryGuard guard(output);
37
38 abs_loop(
39 static_cast<float*>(output.data_ptr()),
40 static_cast<float*>(iter.data_ptr(1)),
41 iter.numel());
42
43 output_tensor.copy_(output);
44 }
45}
```

```
1REGISTER_PRIVATEUSE1_DISPATCH(abs_stub, &wrapper_abs_stub);
2REGISTER_PRIVATEUSE1_DISPATCH(
3 quantize_tensor_per_tensor_affine_stub,
4 &wrapper_quantize_tensor_per_tensor_affine_stub);
5REGISTER_PRIVATEUSE1_DISPATCH(
6 _fused_sdp_choice_stub,
7 &wrapper__fused_sdp_choice);
```

From the signature, we can see that the input of `abs_stub` is `TensorIteratorBase`, a powerful helper class provided by PyTorch that contains all input and output operators, as well as some other auxiliary methods. Based on it, we can develop the `abs_kernel` operator and then call `REGISTER_PRIVATEUSE1_DISPATCH` to specify `abs_stub` to complete the registration.

### Custom Operators

In addition to PyTorch's built-in operators, custom accelerator operators are also very common to improve performance in specific scenarios. These can be categorized into three main approaches:

- Forward-only
- Forward and backward: Separate registration
- Forward and backward: Implemented using `torch.autograd.Function`

Note

There are more details in PyTorch tutorials, so refer to [PyTorch Custom Operators](https://docs.pytorch.org/tutorials/advanced/custom_ops_landing_page.html) if you are interested.

#### Forward Only

Here, we'll briefly introduce the implementation process of custom operators, focusing on the forward-only approach. The implementation can be summarized into the following three points:

1. **Define Schema:**

C++

```
1TORCH_LIBRARY(openreg, m) {
2 m.def("custom_abs(Tensor input)-> Tensor");
3}
```

- Namespace Name: `openreg`
- Function Name: `custom_abs`
- Input Parameters:

- Type: `Tensor`
- Name: `input`
- Output Type: `Tensor`
2. **Register Operator**

C++

```
1TORCH_LIBRARY_IMPL(openreg, PrivateUse1, m) {
2 m.impl("custom_abs", &wrapper_custom_abs);
3}
```

Use `TORCH_LIBRARY_IMPL` to register the `wrapper_custom_abs` implementation for the `custom_abs` operator in `PrivateUse1`. Because `Autograd` is always enabled in PyTorch, PyTorch defaults to finding and executing the corresponding backward implementation even if only forward computation is required(will fallthrough in backward implementation). Fortunately, PyTorch have implemented a general `Autograd Fallback` for PrivateUse1 as well, if only forward computation is involved, it is equivalent to a fallthrough operation, selecting the next DispatchKey for computation; if backward computation is involved, an error is thrown.
3. **Register Metadata(optional, but required by the graph mode, etc.):**

PYTHON

```
1lib = torch.library.Library("openreg", "IMPL", "Meta") # noqa: TOR901
2
3
4@torch.library.impl(lib, "custom_abs")
5def custom_abs(self):
6 return torch.empty_like(self)
7
8
```

PyTorch supports registering `Meta` in both C++ and Python. Since Python registration is simpler, Python is used as an example here. Similar to the `TORCH_LIBRARY_IMPL` function in C++, Python provides the more user-friendly `torch.library.impl` decorator.

## Tools

Operator registration in PyTorch is complex, with diverse registration methods and numerous scenarios. Therefore, the PyTorch community has provided a number of tools to help developers quickly understand the underlying principles and assist in troubleshooting. Here we briefly introduce several commonly used tools:

### Commands

PyTorch provides a set of commands prefixed with `torch._C._dispatch_` around its Dispatch feature. You can query all related interfaces using the following command:

```
python -c 'import torch; print("\n".join([x for x in dir(torch._C) if x.startswith("_dispatch_")]))'

...
_dispatch_dump
_dispatch_dump_table
_dispatch_has_kernel
_dispatch_has_kernel_for_any_dispatch_key
_dispatch_has_kernel_for_dispatch_key
_dispatch_isTensorSubclassLike
_dispatch_is_alias_key
_dispatch_is_included_in_alias
_dispatch_is_main_interpreter
_dispatch_kernel_for_dispatch_key_is_fallthrough
_dispatch_key_for_device
_dispatch_key_name
_dispatch_key_parse
_dispatch_key_set
...
```

Here are explanations for several commonly used commands:

- `torch._C._dispatch_key_set`:

Displays the DispatchKey of the current Tensor, with priority increasing from left to right.

```
>>> import torch
>>> a = torch.randn(3,3,device="cuda")
>>> torch._C._dispatch_key_set(a)
'DispatchKeySet(CUDA, ADInplaceOrView, AutogradCUDA, AutocastCUDA)'
```
- `torch._C._dispatch_dump_table`:

Queries the support status of a given operator across different Dispatch Keys, making it easy to locate the corresponding implementation code.

```
>>> import torch
>>> print(torch._C._dispatch_dump_table("aten::add.Tensor"))
>>> ...
 CPU: registered at ./build/aten/src/ATen/RegisterCPU_0.cpp:1309 [kernel]
 CUDA: registered at ./build/aten/src/ATen/RegisterCUDA_0.cpp:2420 [kernel]
 HIP: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 MPS: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 IPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 XPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 HPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 VE: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 MTIA: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 MAIA: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 PrivateUse1: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional_0.cpp:1373 [default backend kernel]
 ...
```

You can easily query the corresponding implementation of the `aten::add.Tensor` operator on other platforms, so that you can track the entire operator calling process from the source code level.

### Environment Variables

PyTorch also provides some dispatcher-related environment variables that can help with learning and quickly locating issues.

- TORCH_SHOW_DISPATCH_TRACE

Displays detailed internal dispatch key scheduling during PyTorch execution.

```
export TORCH_SHOW_DISPATCH_TRACE=1
```

```
>>> import torch
>>> a = torch.randn(3,3)
 [call] op=[aten::randn], key=[BackendSelect]
 [redispatch] op=[aten::randn], key=[CPU]
 [call] op=[aten::empty.memory_format], key=[BackendSelect]
 [redispatch] op=[aten::empty.memory_format], key=[CPU]
 [call] op=[aten::normal_], key=[CPU]
```

You can clearly see all the underlying operators called by Python-level operators within PyTorch: including the operator name, calling hierarchy, and corresponding `Dispatch Key`.