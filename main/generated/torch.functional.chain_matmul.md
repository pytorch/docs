# torch.functional.chain_matmul

torch.functional.chain_matmul(**matrices*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/functional.py#L2062)

Returns the matrix product of the NNN 2-D tensors. This product is efficiently computed
using the matrix chain order algorithm which selects the order in which incurs the lowest cost in terms
of arithmetic operations ([[CLRS]](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)). Note that since this is a function to compute the product, NNN
needs to be greater than or equal to 2; if equal to 2 then a trivial matrix-matrix product is returned.
If NNN is 1, then this is a no-op - the original matrix is returned as is.

Warning

[`torch.chain_matmul()`](torch.chain_matmul.html#torch.chain_matmul) is deprecated and will be removed in a future PyTorch release.
Use [`torch.linalg.multi_dot()`](torch.linalg.multi_dot.html#torch.linalg.multi_dot) instead, which accepts a list of two or more tensors
rather than multiple arguments.

Parameters:

- **matrices** (*Tensors**...*) - a sequence of 2 or more 2-D tensors whose product is to be determined.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor. Ignored if `out` = `None`.

Returns:

if the ithi^{th}ith tensor was of dimensions pi×pi+1p_{i} \times p_{i + 1}pi​×pi+1​, then the product
would be of dimensions p1×pN+1p_{1} \times p_{N + 1}p1​×pN+1​.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> a = torch.randn(3, 4)
>>> b = torch.randn(4, 5)
>>> c = torch.randn(5, 6)
>>> d = torch.randn(6, 7)
>>> # will raise a deprecation warning
>>> torch.chain_matmul(a, b, c, d)
tensor([[ -2.3375, -3.9790, -4.1119, -6.6577, 9.5609, -11.5095, -3.2614],
 [ 21.4038, 3.3378, -8.4982, -5.2457, -10.2561, -2.4684, 2.7163],
 [ -0.9647, -5.8917, -2.3213, -5.2284, 12.8615, -12.2816, -2.5095]])
```