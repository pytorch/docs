# torch.cuda.memory.memory_snapshot

torch.cuda.memory.memory_snapshot(*mempool_id=None*, *include_traces=True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/memory.py#L635)

Return a snapshot of the CUDA memory allocator state across all devices.

Interpreting the output of this function requires familiarity with the
memory allocator internals.

Parameters:

- **mempool_id** - Optional memory pool ID to get snapshot for a specific pool
- **include_traces** - Whether to include trace entries in the snapshot.
If True (default), all trace entries are included.
If False, no trace entries are included (lightweight/fast snapshot).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.