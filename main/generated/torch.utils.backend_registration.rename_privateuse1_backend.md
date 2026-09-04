# torch.utils.backend_registration.rename_privateuse1_backend

torch.utils.backend_registration.rename_privateuse1_backend(*backend_name*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/utils/backend_registration.py#L76)

Rename the privateuse1 backend device to make it more convenient to use as a device name within PyTorch APIs.

The steps are:

1. (In C++) implement kernels for various torch operations, and register them
to the PrivateUse1 dispatch key.
2. (In python) call torch.utils.rename_privateuse1_backend("foo")

You can now use "foo" as an ordinary device string in python.

Note: this API can only be called once per process. Attempting to change
the external backend after it's already been set will result in an error.

Note(AMP): If you want to support AMP on your device, you can register a custom backend module.
The backend must register a custom backend module with `torch._register_device_module("foo", BackendModule)`.
BackendModule needs to have the following API's:

1. `get_amp_supported_dtype() -> List[torch.dtype]`
get the supported dtypes on your "foo" device in AMP, maybe the "foo" device supports one more dtype.

Note(random): If you want to support to set seed for your device, BackendModule needs to have the following API's:

1. `_is_in_bad_fork() -> bool`
Return `True` if now it is in bad_fork, else return `False`.
2. `manual_seed_all(seed int) -> None`
Sets the seed for generating random numbers for your devices.
3. `device_count() -> int`
Returns the number of "foo"s available.
4. `get_rng_state(device: Union[int, str, torch.device] = 'foo') -> Tensor`
Returns a list of ByteTensor representing the random number states of all devices.
5. `set_rng_state(new_state: Tensor, device: Union[int, str, torch.device] = 'foo') -> None`
Sets the random number generator state of the specified "foo" device.

Note(inductor): To defer the Inductor integration of the device out of import
time, BackendModule may define an optional `_inductor_backend_init` no-arg
callable. Inductor invokes it on each torch.compile / `compile_fx()` /
AOTInductor compilation until the device is registered; it must call
`torch._inductor.codegen.common.register_backend_for_device` itself. See
`docs/source/accelerator/autoload.md` for details.

And there are some common funcs:

1. `is_available() -> bool`
Returns a bool indicating if "foo" is currently available.
2. `current_device() -> int`
Returns the index of a currently selected device.

For more details, see [https://pytorch.org/tutorials/advanced/extend_dispatcher.html#get-a-dispatch-key-for-your-backend](https://pytorch.org/tutorials/advanced/extend_dispatcher.html#get-a-dispatch-key-for-your-backend)
For an existing example, see [bdhirsh/pytorch_open_registration_example](https://github.com/bdhirsh/pytorch_open_registration_example)

Example:

```
>>> torch.utils.rename_privateuse1_backend("foo")
# This will work, assuming that you've implemented the right C++ kernels
# to implement torch.ones.
>>> a = torch.ones(2, device="foo")
```