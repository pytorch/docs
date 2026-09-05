# torch.nn.attention.register_flash_attention_impl

torch.nn.attention.register_flash_attention_impl(*impl*, ***, *register_fn*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/nn/attention/_registry.py#L28)

Register the callable that activates a flash attention impl.

Note

This function is intended for SDPA backend providers to register their
implementations. End users should use [`activate_flash_attention_impl()`](torch.nn.attention.activate_flash_attention_impl.html#torch.nn.attention.activate_flash_attention_impl)
to activate a registered implementation.

Parameters:

- **impl** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'FA3'**,**'FA4'**]*) - Implementation identifier (e.g., `"FA4"`).
- **register_fn** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**...**]**,**FlashAttentionHandle**|**None**]*) - Callable that performs the actual dispatcher registration.
This function will be invoked by [`activate_flash_attention_impl()`](torch.nn.attention.activate_flash_attention_impl.html#torch.nn.attention.activate_flash_attention_impl)
and should register custom kernels with the PyTorch dispatcher.
It may optionally return a handle implementing
`FlashAttentionHandle` to keep any necessary state alive.

Example

```
>>> def my_impl_register(module_path: str = "my_flash_impl"):
... # Register custom kernels with torch dispatcher
... pass 
>>> register_flash_attention_impl(
... "MyImpl", register_fn=my_impl_register
... )
```