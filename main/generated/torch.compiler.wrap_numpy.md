# torch.compiler.wrap_numpy

torch.compiler.wrap_numpy(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/compiler/__init__.py#L546)

Decorator that turns a function from `np.ndarray`s to `np.ndarray`s into a function
from `torch.Tensor`s to `torch.Tensor`s.

It is designed to be used with [`torch.compile()`](torch.compile.html#torch.compile) with `fullgraph=True`. It allows you to
compile a NumPy function as if it were a PyTorch function. This allows you to run NumPy code
on CUDA or compute its gradients.

Note

This decorator does not work without [`torch.compile()`](torch.compile.html#torch.compile).

Example:

```
>>> # Compile a NumPy function as a Tensor -> Tensor function
>>> @torch.compile(fullgraph=True)
>>> @torch.compiler.wrap_numpy
>>> def fn(a: np.ndarray):
>>> return np.sum(a * a)
>>> # Execute the NumPy function using Tensors on CUDA and compute the gradients
>>> x = torch.arange(6, dtype=torch.float32, device="cuda", requires_grad=True)
>>> out = fn(x)
>>> out.backward()
>>> print(x.grad)
tensor([ 0., 2., 4., 6., 8., 10.], device='cuda:0')
```