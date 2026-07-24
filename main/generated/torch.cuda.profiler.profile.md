# torch.cuda.profiler.profile

torch.cuda.profiler.profile()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/profiler.py#L38)

Enable profiling.

Context Manager to enabling profile collection by the active profiling tool from CUDA backend.
.. rubric:: Example

```
>>> import torch
>>> model = torch.nn.Linear(20, 30).cuda()
>>> inputs = torch.randn(128, 20).cuda()
>>> with torch.cuda.profiler.profile() as prof:
... model(inputs)
```