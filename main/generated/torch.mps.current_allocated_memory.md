# torch.mps.current_allocated_memory

torch.mps.current_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/mps/__init__.py#L110)

Returns the current GPU memory occupied by tensors in bytes.

Note

The returned size does not include cached allocations in
memory pools of MPSAllocator.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)