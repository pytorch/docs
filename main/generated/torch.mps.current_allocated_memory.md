# torch.mps.current_allocated_memory

torch.mps.current_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/mps/__init__.py#L110)

Returns the current GPU memory occupied by tensors in bytes.

Note

The returned size does not include cached allocations in
memory pools of MPSAllocator.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)