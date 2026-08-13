# torch.compiler.cudagraph_mark_warmup_incomplete

torch.compiler.cudagraph_mark_warmup_incomplete()[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/compiler/__init__.py#L532)

Request another warmup for the active CUDA Graph Trees function.

Call this synchronously from an autotuner or other code running during CUDA
Graph Trees warmup when the current function needs another warmup iteration.
The function will run eagerly again on its next invocation instead of being
recorded. This is a no-op outside CUDA Graph Trees warmup, including during
recording and replay or when CUDA Graph Trees are disabled.