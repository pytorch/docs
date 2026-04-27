# torch.xpu.memory.memory_stats

torch.xpu.memory.memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/xpu/memory.py#L77)

Return a dictionary of XPU memory allocator statistics for a given device.

The return value of this function is a dictionary of statistics, each of
which is a non-negative integer.

Core statistics:

- `"allocated_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of allocated memory.
- `"reserved_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of reserved memory.
- `"active_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
amount of active memory.
- `"requested_bytes.{all,large_pool,small_pool}.{current,peak,allocated,freed}"`:
memory requested by client code, compare this with allocated_bytes to check if
allocation rounding adds too much overhead.

For these core statistics, values are broken down as follows.

Pool type:

- `all`: combined statistics across all memory pools.
- `large_pool`: statistics for the large allocation pool (for size >= 1MB allocations).
- `small_pool`: statistics for the small allocation pool (for size < 1MB allocations).

Metric type:

- `current`: current value of this metric.
- `peak`: maximum value of this metric.
- `allocated`: historical total increase in this metric.
- `freed`: historical total decrease in this metric.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - selected device. Returns
statistics for the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `device` is `None` (default).

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]