# torch.xpu.get_device_properties

torch.xpu.get_device_properties(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/xpu/__init__.py#L484)

Get the properties of a device. Returns _XpuDeviceProperties containing the following device properties:

- `name` (str): device name.
- `platform_name` (str): SYCL platform name.
- `vendor` (str): device vendor.
- `device_id` (int): device identifier (product ID).
- `driver_version` (str): driver version.
- `version` (str): runtime version.
- `max_compute_units` (int): number of parallel compute units.
- `gpu_eu_count` (int): number of EUs (Execution Unit).
- `max_work_group_size`: (int): maximum number of work-items permitted in a work-group.
- `max_num_sub_groups` (int): maximum number of sub-groups supported in a work-group.
- `memory_clock_rate` (int) maximum clock rate of device's global memory in MHz.
- `memory_bus_width` (int) maximum bus width between device and memory in bits.
- `sub_group_sizes`: (list[int]): a list of supported sub-group sizes.
- `local_mem_size` (int): device local memory capacity that can be allocated per work-group in bytes.
- `last_level_cache_size` (int): size in bytes of the device's last-level memory cache, shared across all Xe Cores (analogous to CUDA `L2_cache_size`).
- `has_fp16` (bool): whether float16 dtype is supported.
- `has_fp64` (bool): whether float64 dtype is supported.
- `has_atomic64` (bool): whether 64-bit atomic operations are supported.
- `has_bfloat16_conversions` (bool): whether bfloat16 conversions are supported.
- `has_subgroup_matrix_multiply_accumulate` (bool): whether DPAS (Dot Product Accumulate Systolic) is supported.
- `has_subgroup_matrix_multiply_accumulate_tensor_float32` (bool): whether DPAS with tf32 inputs is supported.
- `has_subgroup_2d_block_io` (bool): whether 2D block I/O for efficient matrix multiplication is supported.
- `is_integrated_gpu` (bool): whether the device is an integrated GPU (iGPU).
- `total_memory` (int): device global memory in bytes.
- `gpu_subslice_count` (int): number of subslice.
- `architecture` (int): device architecture identifier (experimental).
- `type` (str): device type, e.g. 'cpu', 'gpu', accelerator', 'host', 'unknown'.
- `uuid` (Any): device UUID (Universal Unique ID), 16 bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - device for which to return the
properties of the device.

Returns:

the properties of the device

Return type:

_XpuDeviceProperties