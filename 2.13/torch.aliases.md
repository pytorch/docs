# Aliases in torch

The following are aliases in `torch` to their counterparts in the nested namespaces
in which they are defined. Feel free to use either the top-level version in `torch`
(e.g. `torch.broadcast_tensors()`) or the nested version `torch.functional.broadcast_tensors()`.

| [`atleast_1d`](generated/torch.functional.atleast_1d.html#torch.functional.atleast_1d) | Returns a 1-dimensional view of each input tensor with zero dimensions. |
| --- | --- |
| [`atleast_2d`](generated/torch.functional.atleast_2d.html#torch.functional.atleast_2d) | Returns a 2-dimensional view of each input tensor with zero dimensions. |
| [`atleast_3d`](generated/torch.functional.atleast_3d.html#torch.functional.atleast_3d) | Returns a 3-dimensional view of each input tensor with zero dimensions. |
| [`block_diag`](generated/torch.functional.block_diag.html#torch.functional.block_diag) | Create a block diagonal matrix from provided tensors. |
| [`broadcast_shapes`](generated/torch.functional.broadcast_shapes.html#torch.functional.broadcast_shapes) | Similar to [`broadcast_tensors()`](generated/torch.functional.broadcast_tensors.html#torch.functional.broadcast_tensors) but for shapes. |
| [`broadcast_tensors`](generated/torch.functional.broadcast_tensors.html#torch.functional.broadcast_tensors) | Broadcasts the given tensors according to [Broadcasting semantics](notes/broadcasting.html#broadcasting-semantics). |
| [`cartesian_prod`](generated/torch.functional.cartesian_prod.html#torch.functional.cartesian_prod) | Do cartesian product of the given sequence of tensors. |
| [`cdist`](generated/torch.functional.cdist.html#torch.functional.cdist) | Computes batched the p-norm distance between each pair of the two collections of row vectors. |
| [`chain_matmul`](generated/torch.functional.chain_matmul.html#torch.functional.chain_matmul) | Returns the matrix product of the NNN 2-D tensors. |
| [`einsum`](generated/torch.functional.einsum.html#torch.functional.einsum) | Sums the product of the elements of the input `operands` along dimensions specified using a notation based on the Einstein summation convention. |
| [`lu`](generated/torch.functional.lu.html#torch.functional.lu) | Computes the LU factorization of a matrix or batches of matrices `A`. |
| [`meshgrid`](generated/torch.functional.meshgrid.html#torch.functional.meshgrid) | Creates grids of coordinates specified by the 1D inputs in attr:tensors. |
| [`norm`](generated/torch.functional.norm.html#torch.functional.norm) | Returns the matrix norm or vector norm of a given tensor. |
| [`split`](generated/torch.functional.split.html#torch.functional.split) | Splits the tensor into chunks. |
| [`stft`](generated/torch.functional.stft.html#torch.functional.stft) | Short-time Fourier transform (STFT). |
| [`tensordot`](generated/torch.functional.tensordot.html#torch.functional.tensordot) | Returns a contraction of a and b over multiple dimensions. |
| [`unique`](generated/torch.functional.unique.html#torch.functional.unique) | Returns the unique elements of the input tensor. |
| [`unique_consecutive`](generated/torch.functional.unique_consecutive.html#torch.functional.unique_consecutive) | Eliminates all but the first element from every consecutive group of equivalent elements. |
| [`unravel_index`](generated/torch.functional.unravel_index.html#torch.functional.unravel_index) | Converts a tensor of flat indices into a tuple of coordinate tensors that index into an arbitrary tensor of the specified shape. |