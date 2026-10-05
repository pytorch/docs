# torch.Tensor.get_device

Tensor.get_device(*) -> Device ordinal (Integer*)

For CUDA tensors, this function returns the device ordinal of the GPU on which the tensor resides.
For CPU tensors, this function returns -1.

Example:

```
>>> x = torch.randn(3, 4, 5, device='cuda:0')
>>> x.get_device()
0
>>> x.cpu().get_device()
-1
```