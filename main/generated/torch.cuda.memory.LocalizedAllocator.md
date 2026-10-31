# LocalizedAllocator

*class*torch.cuda.memory.LocalizedAllocator(*locality_domain_id*, ***, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/cuda/memory.py#L1785)

Allocate physical CUDA memory on one locality domain.

Use `MemPool(allocator=allocator.allocator())` to cache and suballocate
this memory. Requires CUDA driver and cuda.bindings 13.4+ and a multi-domain
GPU. Construction initializes CUDA to validate the actual device topology.
Kernel execution is not localized by this allocator.

Parameters:

- **locality_domain_id** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Locality domain to allocate from, excluding bool.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Owning CUDA device.
Defaults to the current device.

Warning

Concurrent allocator activity is unsupported. Allocation, freeing, and
allocator-state queries (including `MemPool.use_count()`) from other
threads must not overlap use of this allocator. Native allocator
callbacks acquire the GIL while holding the allocator mutex, which can
deadlock with a thread holding the GIL while waiting for that mutex.

Note

Use this allocator only on its owning device; access from other devices
is not supported. Callback owners are retained for the process lifetime,
so tensors may outlive the Python allocator and pool objects.
One owner and primary-context reference per device/domain are deliberately
retained, including during interpreter shutdown.
Releasing physical memory waits for its allocation stream.
Freeing is best-effort: failures are logged, not raised. Memory that
cannot safely be unmapped is left for the driver to reclaim at exit.

*property*device_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

Return the CUDA device index associated with this allocator.

*property*locality_domain_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

Return the locality domain ID associated with this allocator.