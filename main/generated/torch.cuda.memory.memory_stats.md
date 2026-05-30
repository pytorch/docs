# torch.cuda.memory.memory_stats

torch.cuda.memory.memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/cuda/memory.py#L231)

Return a dictionary of CUDA memory allocator statistics for a given device.

The return value of this function is a dictionary of statistics, each of
which is a non-negative integer.

Core statistics:

- `"allocated.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of allocation requests received by the memory allocator.
- `"allocated_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of allocated memory.
- `"segment.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
number of reserved segments from `cudaMalloc()`.
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

- `"num_alloc_retries"`: number of failed `cudaMalloc` calls that
result in a cache flush and retry.
- `"num_ooms"`: number of out-of-memory errors thrown.
- `"num_sync_all_streams"`: number of `synchronize_and_free_events` calls.
- `"num_device_alloc"`: number of CUDA allocation calls. This includes both
cuMemMap and cudaMalloc.
- `"num_device_free"`: number of CUDA free calls. This includes both cuMemUnmap
and cudaFree.
- `"num_oom_rejections"`: number of allocations preemptively rejected by the

throw_on_cudamalloc_oom + per_process_memory_fraction policy.

The caching allocator can be configured via ENV to not split blocks larger than a
defined size (see Memory Management section of the Cuda Semantics documentation).
This helps avoid memory fragmentation but may have a performance
penalty. Additional outputs to assist with tuning and evaluating impact:

- `"max_split_size"`: blocks above this size will not be split.
- `"oversize_allocations.{current,peak,allocated,freed}"`:
number of over-size allocation requests received by the memory allocator.
- `"oversize_segments.{current,peak,allocated,freed}"`:
number of over-size reserved segments from `cudaMalloc()`.

The caching allocator can be configured via ENV to round memory allocations in order
to reduce fragmentation. Sometimes the overhead from rounding can be higher than
the fragmentation it helps reduce. The following stat can be used to check if
rounding adds too much overhead:

- `"requested_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
memory requested by client code, compare this with allocated_bytes to check if
allocation rounding adds too much overhead.
- `"reserved_bytes_by_private_pools"`: nested dictionary keyed by
`torch.cuda.MemPool.id` tuples. Each value has the same
`{all,large_pool,small_pool}.{current,peak,allocated,freed}` structure
as `reserved_bytes`, but scoped to a single private pool. In
`memory_stats()`, tuple keys are flattened by joining
their stringified elements with `"_"`, so `(0, 1)` becomes `"0_1"`.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistics for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.

Note

With [backend:cudaMallocAsync](../notes/cuda.html#cuda-memory-envvars), some stats are not
meaningful, and are always reported as zero.