# torch.cuda.memory.host_memory_stats

torch.cuda.memory.host_memory_stats()[[source]](https://github.com/pytorch/pytorch/blob/dff44973f3eba04a92de8499c17cd237997140f2/torch/cuda/memory.py#L385)

Return a dictionary of pinned (host) allocator statistics.

Core statistics (host pinned allocator):

- `"allocations.{current,peak,allocated,freed}"`:
pinned blocks owned by the allocator (active + cached). Grows when a new
block is created via CUDA and shrinks when cached blocks are returned.
- `"allocated_bytes.{current,peak,allocated,freed}"`:
bytes of pinned blocks owned by the allocator (active + cached), using
the rounded block size requested from CUDA.
- `"active_requests.{current,peak,allocated,freed}"`:
blocks currently checked out to callers (increments on handout, decrements
when the block becomes reusable after stream deps finish).
- `"active_bytes.{current,peak,allocated,freed}"`:
bytes corresponding to active blocks.

Metric type:

- `current`: current value.
- `peak`: maximum value.
- `allocated`: historical total increase.
- `freed`: historical total decrease.

Event/timing counters:

- `"num_host_alloc"` / `"num_host_free"`: blocks created to grow the
pool / cached blocks returned to CUDA (matches allocations allocated/freed).
- `"host_alloc_time.{total,max,min,count,avg}"`: time in CUDA alloc calls
when growing the pool (microseconds).
- `"host_free_time.{total,max,min,count,avg}"`: time in CUDA free calls
when cached blocks are returned (microseconds).

Block sizes are rounded up to the next power of two before calling CUDA, so
byte stats reflect the rounded size. Peak values are aggregated per bucket
and are a best-effort approximation of the true peak.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]