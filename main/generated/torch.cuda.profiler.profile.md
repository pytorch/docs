# torch.cuda.profiler.profile

torch.cuda.profiler.profile()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/profiler.py#L38)

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