# SDPBackend

*class*torch.nn.attention.SDPBackend

An enum-like class that contains the different backends for scaled dot product attention.

Warning

This class is in beta and subject to change.

This backend class is designed to be used with the sdpa_kernel context manager. See [`torch.nn.attention.sdpa_kernel()`](torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel) for more details.

The following members are available:

- `ERROR`: Represents an error while determining the backend.
- `MATH`: Selects the PyTorch implementation defined in C++ that matches the formulation in [`torch.nn.functional.scaled_dot_product_attention()`](torch.nn.functional.scaled_dot_product_attention.html#torch.nn.functional.scaled_dot_product_attention).
- `FLASH_ATTENTION`: Selects the FlashAttention backend. The default CUDA implementation uses [FlashAttention-2](https://arxiv.org/abs/2307.08691): Faster Attention with Better Parallelism and Work Partitioning.
- `EFFICIENT_ATTENTION`: Selects [Memory-Efficient Attention](https://github.com/facebookresearch/xformers).
- `CUDNN_ATTENTION`: Selects the cuDNN scaled dot product attention implementation.
- `OVERRIDEABLE`: Selects an overrideable backend provided by an extension.