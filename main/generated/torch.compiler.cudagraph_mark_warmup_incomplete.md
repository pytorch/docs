# torch.compiler.cudagraph_mark_warmup_incomplete

torch.compiler.cudagraph_mark_warmup_incomplete()[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/compiler/__init__.py#L532)

Request another warmup for the active CUDA Graph Trees function.

Call this synchronously from an autotuner or other code running during CUDA
Graph Trees warmup when the current function needs another warmup iteration.
The function will run eagerly again on its next invocation instead of being
recorded. This is a no-op outside CUDA Graph Trees warmup, including during
recording and replay or when CUDA Graph Trees are disabled.