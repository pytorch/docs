# torch.cuda.profiler.profile

torch.cuda.profiler.profile()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/profiler.py#L38)

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