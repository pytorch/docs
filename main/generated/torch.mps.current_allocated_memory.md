# torch.mps.current_allocated_memory

torch.mps.current_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/mps/__init__.py#L110)

Returns the current GPU memory occupied by tensors in bytes.

Note

The returned size does not include cached allocations in
memory pools of MPSAllocator.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)