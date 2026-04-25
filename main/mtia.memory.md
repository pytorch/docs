# torch.mtia.memory

The MTIA backend is implemented out of the tree, only interfaces are defined here.

This package adds support for device memory management implemented in MTIA.

| [`max_memory_allocated`](generated/torch.mtia.memory.max_memory_allocated.html#torch.mtia.memory.max_memory_allocated) | Return the maximum memory allocated in bytes for a given device. |
| --- | --- |
| [`memory_stats`](generated/torch.mtia.memory.memory_stats.html#torch.mtia.memory.memory_stats) | Return a dictionary of MTIA memory allocator statistics for a given device. |
| [`memory_allocated`](generated/torch.mtia.memory.memory_allocated.html#torch.mtia.memory.memory_allocated) | Return the current MTIA memory occupied by tensors in bytes for a given device. |