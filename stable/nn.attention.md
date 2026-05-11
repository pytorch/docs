# torch.nn.attention

This module contains functions and classes that alter the behavior of torch.nn.functional.scaled_dot_product_attention

## Utils

| [`sdpa_kernel`](generated/torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel) | Context manager to select which backend to use for scaled dot product attention. |
| --- | --- |
| [`SDPBackend`](generated/torch.nn.attention.SDPBackend.html#torch.nn.attention.SDPBackend) | An enum-like class that contains the different backends for scaled dot product attention. |
| [`register_flash_attention_impl`](generated/torch.nn.attention.register_flash_attention_impl.html#torch.nn.attention.register_flash_attention_impl) | Register the callable that activates a flash attention impl. |
| [`activate_flash_attention_impl`](generated/torch.nn.attention.activate_flash_attention_impl.html#torch.nn.attention.activate_flash_attention_impl) | Activate into the dispatcher a previously registered flash attention impl. |
| [`list_flash_attention_impls`](generated/torch.nn.attention.list_flash_attention_impls.html#torch.nn.attention.list_flash_attention_impls) | Return the names of all available flash attention implementations. |
| [`current_flash_attention_impl`](generated/torch.nn.attention.current_flash_attention_impl.html#torch.nn.attention.current_flash_attention_impl) | Return the currently activated flash attention impl name, if any. |
| [`restore_flash_attention_impl`](generated/torch.nn.attention.restore_flash_attention_impl.html#torch.nn.attention.restore_flash_attention_impl) | Restore the default FA2 implementation |

## Submodules

| [`flex_attention`](nn.attention.flex_attention.html#module-torch.nn.attention.flex_attention) | This module implements the user facing API for flex_attention in PyTorch. |
| --- | --- |
| [`bias`](nn.attention.bias.html#module-torch.nn.attention.bias) | Defines bias subclasses that work with scaled_dot_product_attention |
| [`experimental`](nn.attention.experimental.html#module-torch.nn.attention.experimental) | |
| [`varlen`](nn.attention.varlen.html#module-torch.nn.attention.varlen) | Variable-length attention implementation using Flash Attention. |