# torch.accelerator.memory.memory_stats

torch.accelerator.memory.memory_stats(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/accelerator/memory.py#L45)

Return a dictionary of accelerator device memory allocator statistics for a given device index.

The return value of this function is a dictionary of statistics, each of
which is a non-negative integer.

Core statistics:

- `"allocated.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of allocation requests received by the memory allocator.
- `"allocated_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of allocated memory.
- `"segment.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of reserved segments from device memory allocation.
- `"reserved_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of reserved memory.
- `"active.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of active memory blocks.
- `"active_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of active memory.
- `"inactive_split.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of inactive, non-releasable memory blocks.
- `"inactive_split_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of inactive, non-releasable memory.

For these core statistics, values are broken down as follows.

Pool type:

- `all`: combined statistics across all memory pools.
- `large_pool`: statistics for the large allocation pool
(as of June 2025, for size >= 1MB allocations).
- `small_pool`: statistics for the small allocation pool
(as of June 2025, for size < 1MB allocations).

Metric type:

- `current`: current value of this metric.
- `peak`: maximum value of this metric.
- `allocated`: historical total increase in this metric.
- `freed`: historical total decrease in this metric.

In addition to the core statistics, we also provide some simple event
counters:

- `"num_alloc_retries"`: number of failed device memory allocation calls that
result in a cache flush and retry.
- `"num_ooms"`: number of out-of-memory errors thrown.
- `"num_sync_all_streams"`: number of `synchronize_and_free_events` calls.
- `"num_device_alloc"`: number of device memory allocation calls.
- `"num_device_free"`: number of device memory free calls.

Parameters:

**device_index** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - the index of the device to target.
If not given, use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.
If a [`torch.device`](../tensor_attributes.html#torch.device) or str is provided, its type must match the current
[accelerator](../torch.html#accelerators) device type.

Returns:

an ordered dictionary mapping statistic names to their values.

Return type:

OrderedDict[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]