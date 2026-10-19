# torch.mps.current_allocated_memory

torch.mps.current_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/mps/__init__.py#L110)

Returns the current GPU memory occupied by tensors in bytes.

Note

The returned size does not include cached allocations in
memory pools of MPSAllocator.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)