# torch.mps.current_allocated_memory

torch.mps.current_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/mps/__init__.py#L110)

Returns the current GPU memory occupied by tensors in bytes.

Note

The returned size does not include cached allocations in
memory pools of MPSAllocator.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)