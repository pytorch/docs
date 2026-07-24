# torch.mps.compile_shader

torch.mps.compile_shader(*source*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/mps/__init__.py#L140)

Compiles compute shader from source and allows one to invoke kernels
defined there from the comfort of Python runtime
Example:

```
>>> lib = torch.mps.compile_shader(
... "kernel void full(device float* out, constant float& val, uint idx [[thread_position_in_grid]]) { out[idx] = val; }"
... )
>>> x = torch.zeros(16, device="mps")
>>> lib.full(x, 3.14)
```