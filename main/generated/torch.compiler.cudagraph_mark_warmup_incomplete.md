# torch.compiler.cudagraph_mark_warmup_incomplete

torch.compiler.cudagraph_mark_warmup_incomplete()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/compiler/__init__.py#L531)

Request another warmup for the active CUDA Graph Trees function.

Call this synchronously from an autotuner or other code running during CUDA
Graph Trees warmup when the current function needs another warmup iteration.
The function will run eagerly again on its next invocation instead of being
recorded. This is a no-op outside CUDA Graph Trees warmup, including during
recording and replay or when CUDA Graph Trees are disabled.