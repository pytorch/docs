# LocalizedAllocator

*class*torch.cuda.memory.LocalizedAllocator(*locality_domain_id*, ***, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/cuda/memory.py#L1764)

Allocate physical CUDA memory on one locality domain.

Use `MemPool(allocator=allocator.allocator())` to cache and suballocate
this memory. Requires CUDA driver and cuda.bindings 13.4+ and a multi-domain
GPU. Construction initializes CUDA to validate the actual device topology.
Kernel execution is not localized by this allocator.

Parameters:

- **locality_domain_id** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Locality domain to allocate from, excluding bool.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Owning CUDA device.
Defaults to the current device.

Note

Use this allocator only on its owning device; access from other devices
is not supported. Callback owners are retained for the process lifetime,
so tensors may outlive the Python allocator and pool objects.
One owner and primary-context reference per device/domain are deliberately
retained, including during interpreter shutdown.
Releasing physical memory waits for its allocation stream.
Running out of device memory fails the allocation, so the caching
allocator can free cached memory and retry; other CUDA errors raise.
Freeing is best-effort: failures are logged, not raised. Memory that
cannot safely be unmapped is left for the driver to reclaim at exit.

*property*device_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

Return the CUDA device index associated with this allocator.

*property*locality_domain_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

Return the locality domain ID associated with this allocator.