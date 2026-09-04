# torch.cuda.profiler.profile

torch.cuda.profiler.profile()[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/cuda/profiler.py#L38)

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