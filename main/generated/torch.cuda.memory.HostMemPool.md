# HostMemPool

*class*torch.cuda.memory.HostMemPool(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/memory.py#L1842)

HostMemPool represents a pool of pinned (page-locked) host memory in the
CUDA host caching allocator, with no device memory.

Pinned allocations of a thread inside `use_mem_pool(host_pool)` come from
this pool, and blocks freed by any thread return to it. The pool keeps its
cached blocks apart from other pools; it does not choose where memory is
placed. A typical use is one pool per NUMA node, entered by the loader
threads bound to that node; see [Pinned host memory pools](../notes/cuda.html#cuda-pinned-host-memory-pools).

Creating a pool allocates no memory. A HostMemPool cannot be a CUDA graph's
`pool`, but a graph keeps the pool until it is reset if the pool's
context is entered while the current stream is capturing into the graph.
Deleting the pool frees its cached blocks, or, if a graph keeps the pool,
the reset of the last such graph does; what remains is freed by a later
`torch.accelerator.empty_host_cache()`.

*property*id*: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]*

Returns the ID of this pool as a tuple of two ints.

use_count()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/memory.py#L1865)

Returns the reference count of this pool: 1 for the pool object, plus
one for each open `use_mem_pool` context and each graph that keeps it.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)