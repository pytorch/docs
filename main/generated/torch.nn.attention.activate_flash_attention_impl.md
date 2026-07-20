# torch.nn.attention.activate_flash_attention_impl

torch.nn.attention.activate_flash_attention_impl(*impl*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/nn/attention/_registry.py#L61)

Activate into the dispatcher a previously registered flash attention impl.

Note

Backend providers should NOT automatically activate their implementation
on import. Users should explicitly opt-in by calling this function or via
environment variables to ensure multiple provider libraries can coexist.

Parameters:

**impl** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'FA3'**,**'FA4'**]*) - Implementation identifier to activate. See
[`list_flash_attention_impls()`](torch.nn.attention.list_flash_attention_impls.html#torch.nn.attention.list_flash_attention_impls) for available
implementations.
If the backend's [`register_flash_attention_impl()`](torch.nn.attention.register_flash_attention_impl.html#torch.nn.attention.register_flash_attention_impl) callable
returns a `FlashAttentionHandle`, the registry keeps that
handle alive for the lifetime of the process (until explicit
uninstall support exists).

Example

```
>>> activate_flash_attention_impl("FA4")
```