# torch.Tensor.to

Tensor.to(**args*, ***kwargs*) → [Tensor](../tensors.html#torch.Tensor)

Performs Tensor dtype and/or device conversion. A [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device) are
inferred from the arguments of `self.to(*args, **kwargs)`.

Note

If the `self` Tensor already
has the correct [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device), then `self` is returned.
Otherwise, the returned tensor is a copy of `self` with the desired
[`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device).

Note

If `self` requires gradients (`requires_grad=True`) but the target
`dtype` specified is an integer type, the returned tensor will implicitly
set `requires_grad=False`. This is because only tensors with
floating-point or complex dtypes can require gradients.

Here are the ways to call `to`:

to(*dtype*, *non_blocking=False*, *copy=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with the specified [`dtype`](../tensor_attributes.html#torch.dtype)
> 
> 
> 
> Args:
> 
> memory_format ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional): the desired memory format of
> returned Tensor. Default: `torch.preserve_format`.

Note

According to [C++ type conversion rules](https://en.cppreference.com/w/cpp/language/implicit_conversion.html),
converting floating point value to integer type will truncate the fractional part.
If the truncated value cannot fit into the target type (e.g., casting `torch.inf` to `torch.long`),
the behavior is undefined and the result may vary across platforms.

torch.to(*device=None*, *dtype=None*, *non_blocking=False*, *copy=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with the specified [`device`](../tensor_attributes.html#torch.device) and (optional)
> [`dtype`](../tensor_attributes.html#torch.dtype). If [`dtype`](../tensor_attributes.html#torch.dtype) is `None` it is inferred to be `self.dtype`.
> When `non_blocking` is set to `True`, the function attempts to perform
> the conversion asynchronously with respect to the host, if possible. This
> asynchronous behavior applies to both pinned and pageable memory. However,
> caution is advised when using this feature. For more information, refer to the
> [tutorial on good usage of non_blocking and pin_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html).
> When `copy` is set, a new Tensor is created even when the Tensor
> already matches the desired conversion.
> 
> 
> 
> Args:
> 
> memory_format ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional): the desired memory format of
> returned Tensor. Default: `torch.preserve_format`.

torch.to(*other*, *non_blocking=False*, *copy=False*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device) as
> the Tensor `other`.
> When `non_blocking` is set to `True`, the function attempts to perform
> the conversion asynchronously with respect to the host, if possible. This
> asynchronous behavior applies to both pinned and pageable memory. However,
> caution is advised when using this feature. For more information, refer to the
> [tutorial on good usage of non_blocking and pin_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html).
> When `copy` is set, a new Tensor is created even when the Tensor
> already matches the desired conversion.

Note

When `non_blocking` is `True` and the conversion is issued on
a non-default CUDA stream, the caller is responsible for proper
cross-stream synchronization. See [CUDA streams](../notes/cuda.html#cuda-stream-semantics) for
the required pattern.

Example:

```
>>> tensor = torch.randn(2, 2) # Initially dtype=float32, device=cpu
>>> tensor.to(torch.float64)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64)

>>> cuda0 = torch.device('cuda:0')
>>> tensor.to(cuda0)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], device='cuda:0')

>>> tensor.to(cuda0, dtype=torch.float64)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')

>>> other = torch.randn((), dtype=torch.float64, device=cuda0)
>>> tensor.to(other, non_blocking=True)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')
```