# PyTorch Symmetric Memory

Note

`torch.distributed._symmetric_memory` is currently in alpha state and under
development. API changes may be possible.

## Why Symmetric Memory?

With rapidly evolving parallelization techniques, existing frameworks and
libraries often struggle to keep up, and developers increasingly rely on custom
implementations directly scheduling communications and computations. In recent
years we've witnessed a shift from primarily relying on one-dimensional
data-parallelism techniques to multi-dimensional parallelism ones. The latter
have different latency requirements for different types of communications and
thus require fine-grained overlapping of compute and communications.

To minimize compute interference, they also require the use of copy engines and
network interface cards (NICs) to drive communication. Network transport
protocols such as remote direct memory access (RDMA) enhance the performance by
enabling direct, high-speed, and low-latency communication between processors
and memory. This increase in variety indicates the need for finer-grained
communication primitives than are offered today by high-level collective APIs,
ones that would enable developers to implement specific algorithms tailored for
their use cases, such as low-latency collectives, fine-grained
compute-communications overlap, or custom fusions.

Furthermore, today's advanced AI systems connect GPUs with high-bandwidth links
(such as NVLinks, InfiniBand or RoCE), making GPU global memory directly
accessible to peers. Such connections present a great opportunity for
programmers to program the system as a single, gigantic GPU with vast accessible
memory, instead of programming singular "GPU islands."

In this document, we will show how you can use PyTorch Symmetric Memory to
program modern GPU systems as a "single GPU" and achieve fine-grained remote
access.

## What PyTorch Symmetric Memory unlocks?

PyTorch Symmetric Memory unlocks three new capabilities:

- **Customized communication patterns**: Increased flexibility in kernel writing
allows developers to write custom kernels that implement their custom
computations and communications, directly tailored to the need of the
application. It will also be straightforward to add support for new data types
along with the special compute that those data types might require, even if it's
not present yet in the standard libraries.
- **In-kernel compute-comm fusion**: Device-initiated communication capability
allows developers to write kernels with both computation and communication
instructions, allowing for the fusion of computation and data movement in the
smallest possible granularity.
- **Low-latency remote access**: Network transport protocols like RDMA enhance the
performance of symmetric memory in networked environments by enabling direct,
high-speed, and low-latency communication between processors and memory. RDMA
eliminates the overhead associated with the traditional network stack and CPU
involvement. It also offloads data transfer from the compute to the NICs,
freeing up compute resources for computational tasks.

Next, we will show you how PyTorch Symmetric Memory (SymmMem) enables new
applications with the above capabilities.

## A "Hello World" example

The PyTorch SymmMem programming model involves two key elements:

- creating symmetric tensors
- creating SymmMem kernels

To create symmetric tensors, one can use the
`torch.distributed._symmetric_memory` package:

```
import torch.distributed._symmetric_memory as symm_mem

t = symm_mem.empty(128, device=torch.device("cuda", rank))
hdl = symm_mem.rendezvous(t, group)
```

The `symm_mem.empty` function creates a tensor that is backed by a symmetric
memory allocation. The `rendezvous` function establishes a rendezvous with peers
in the group, and returns a handle to the symmetric memory allocation. The
handle provides method to access information related to the symmetric memory
allocation, such as pointers to symmetric buffer on peer ranks, multicast
pointer (if supported), and signal pads.

The `empty` and `rendezvous` functions must be called in the same order on all
ranks in the group.

Then, collectives can be called on these tensors. For example, to perform a
one-shot all-reduce:

```
# Most SymmMem ops are under the torch.ops.symm_mem namespace
torch.ops.symm_mem.one_shot_all_reduce(t, "sum", group)
```

Please note that `torch.ops.symm_mem` is an "op namespace" instead of a python
module. Therefore, you can't import it by `import torch.ops.symm_mem`, neither
can you import an op by `from torch.ops.symm_mem import one_shot_all_reduce`.
You can call the op directly as in the example above.

## Write your own kernel

To write your own kernel doing communications with symmetric memory, you'll need
access to the addresses of mapped peer buffers and access to signal pads that
are required for synchronization. In the kernel you'll also need to perform
correct synchronizations to make sure that peers are ready for communication,
and signal to them that this GPU is ready.

PyTorch Symmetric Memory provides CUDA Graph-compatible synchronization
primitives that operate on the signal pad accompanying each symmetric memory
allocation. Kernels using symmetric memory can be written both in CUDA and in
Triton. Here's an example allocating symmetric tensor and exchanging handles:

```
import torch.distributed._symmetric_memory as symm_mem

dist.init_process_group()
rank = dist.get_rank()

# Allocate a tensor
t = symm_mem.empty(4096, device=f"cuda:{rank}")
# Establish symmetric memory and obtain the handle
hdl = symm_mem.rendezvous(t, dist.group.WORLD)
```

Access to buffer pointers, multimem pointer, and signal pads is provided via:

```
hdl.buffer_ptrs
hdl.multicast_ptr
hdl.signal_pad_ptrs
```

Data pointed to by `buffer_ptrs` can be accessed just like regular local data,
and any necessary compute can also be performed in the usual ways. As with local
data, you can and should use vectorized accesses to improve efficiency.

Symmetric memory is especially convenient for writing kernels in Triton. While
previously Triton removed the barriers to writing efficient CUDA code, now
communications can be added easily to Triton kernels. The kernel below
demonstrates a low-latency, all-reduce kernel written in Triton.

```
@triton.jit
def one_shot_all_reduce_kernel(
 buf_tuple,
 signal_pad_ptrs,
 output_ptr,
 numel: tl.constexpr,
 rank: tl.constexpr,
 world_size: tl.constexpr,
 BLOCK_SIZE: tl.constexpr,
):
 ptx_utils.symm_mem_sync(
 signal_pad_ptrs, None, rank, world_size, hasSubsequenceMemAccess=True
 )

 pid = tl.program_id(axis=0)
 block_start = pid * BLOCK_SIZE

 while block_start < numel:
 offsets = block_start + tl.arange(0, BLOCK_SIZE)
 mask = offsets < numel
 acc = tl.zeros((BLOCK_SIZE,), dtype=tl.bfloat16)

 for i in tl.static_range(world_size):
 buffer_rank = buf_tuple[i]
 x = tl.load(buffer_rank + offsets, mask=mask)
 acc += x

 tl.store(output_ptr + offsets, acc, mask=mask)
 block_start += tl.num_programs(axis=0) * BLOCK_SIZE

 ptx_utils.symm_mem_sync(
 signal_pad_ptrs, None, rank, world_size, hasPreviousMemAccess=True
 )
```

Synchronizations at the beginning and the end of the kernel above guarantee that
all the processes see consistent data. The bulk of the kernel is recognizable
Triton code, and Triton will optimize it behind the scene, making sure memory
accesses are performed in an efficient way with vectorization and unrolling. As
with all Triton kernels, it is easily modifiable to add extra computations or
change the communication algorithm. Visit
https://github.com/meta-pytorch/kraken/blob/main/kraken to see additional
utilities and examples of using symmetric memory to implement common patterns in
Triton.

## One-sided get

Symmetric memory also exposes a small one-sided `get` API for copying data from
a peer's symmetric allocation into a local tensor:

```
src = symm_mem.empty(1024, device=device)
hdl = symm_mem.rendezvous(src, group)

if dist.get_rank(group) == 0:
 dst = torch.empty((512,), device=device)
 # Copy the last 512 elements of the peer's allocation into dst.
 symm_mem.get(dst, hdl, peer=1, offset=512)
```

`hdl` is the symmetric memory handle returned by `rendezvous`; the remote
source is the peer's allocation backing that handle. The number of elements
copied is inferred from `dst`, so pass a view (e.g. `dst[:n]`) to fill only
part of a tensor; `offset` is given in elements of `dst`'s dtype and defaults
to `0`. `dst` may be a regular CUDA tensor or another symmetric tensor; it must
be on the same device as `hdl` and backed by contiguous memory. The copy is
issued on the current CUDA stream.

## Scale out

Large language models distribute experts onto more than 8 GPUs, hence requiring
multi-node access capability. NICs capable of RDMA come to help. In addition,
software libraries such as NVSHMEM or rocSHMEM abstract away the programming
difference between intra-node access and inter-node access with primitives that
are slightly higher level than pointer access, such as put and get.

PyTorch provides NVSHMEM plugins to augment Triton kernels' cross-node
capabilities. As shown in the code snippet below, one can initiate a cross-node
put command within the kernel.

```
import torch.distributed._symmetric_memory._nvshmem_triton as nvshmem
from torch.distributed._symmetric_memory._nvshmem_triton import requires_nvshmem

@requires_nvshmem
@triton.jit
def my_put_kernel(
 dest,
 src,
 nelems,
 pe,
):
 nvshmem.put(dest, src, nelems, pe)
```

The `requires_nvshmem` decorator is used to indicate that the kernel requires
the NVSHMEM device library as an external dependency. When Triton compiles the
kernel, the decorator will search your system paths for the NVSHMEM device
library. If it is available, Triton will include the necessary device assembly
to use the NVSHMEM functions.

## Using Memory Pool

Memory pool allows PyTorch SymmMem to cache memory allocations that have been
rendezvoused, saving time when creating new tensors. For convenience, PyTorch
SymmMem has added a `get_mem_pool` API to return a symmetric memory pool. Users
can use the returned MemPool with the `torch.cuda.use_mem_pool` context manager.
In the example below, tensor `x` will be created from symmetric memory:

```
import torch.distributed._symmetric_memory as symm_mem

 mempool = symm_mem.get_mem_pool(device)

 with torch.cuda.use_mem_pool(mempool):
 x = torch.arange(128, device=device)

 torch.ops.symm_mem.one_shot_all_reduce(x, "sum", group_name)
```

Similarly, you can put a compute operation under the MemPool context, and the
result tensor will be created from symmetric memory too.

```
dim = 1024
 w = torch.ones(dim, dim, device=device)
 x = torch.ones(1, dim, device=device)

 mempool = symm_mem.get_mem_pool(device)
 with torch.cuda.use_mem_pool(mempool):
 # y will be in symmetric memory
 y = torch.mm(x, w)
```

As of torch 2.11, the `CUDA` and `NVSHMEM` backends support MemPool. MemPool
support of the `NCCL` backend is in progress.

## Copy Engine Collectives

Note

Copy Engine Collectives require NCCL 2.28 or later, and GPUs with peer-to-peer (P2P) access.

Copy Engine (CE) Collectives are an optimization for NCCL collective operations that offload
data movement to the GPU's copy engines (DMA engines) instead of using CUDA streaming
multiprocessors (SMs). This frees up SMs for compute work, enabling better overlap of
communication and computation during distributed training.

To use CE collectives, you need to:

1. Configure the NCCL process group with the zero-CTA policy
2. Set up symmetric memory with the NCCL backend
3. Allocate tensors using symmetric memory
4. Register the tensors with symmetric memory via rendezvous

Once set up, standard collective functions like `all_gather_single()` and
`all_to_all_single()` will automatically use the copy engines when operating
on symmetric memory tensors.

**Example**

```
import torch
import torch.distributed as dist
import torch.distributed._symmetric_memory as symm_mem

# Initialize process group with zero-CTA policy for CE collectives
opts = dist.ProcessGroupNCCL.Options()
opts.config.cta_policy = dist.ProcessGroupNCCL.NCCL_CTA_POLICY_ZERO
device = torch.device("cuda", rank)
dist.init_process_group(backend="nccl", pg_options=opts, device_id=device)

# Set up symmetric memory with NCCL backend
symm_mem.set_backend("NCCL")
group_name = dist.group.WORLD.group_name

# Allocate tensors using symmetric memory
numel = 1024 * 1024
inp = symm_mem.empty(numel, device=device)
out = symm_mem.empty(numel * world_size, device=device)

# Register tensors for symmetric memory operations
symm_mem.rendezvous(inp, group=group_name)
symm_mem.rendezvous(out, group=group_name)

# Perform collective operation using copy engines
# This now runs on DMA engines instead of SMs
work = dist.all_gather_single(out, inp, async_op=True)
work.wait()
```

**Benefits**

- **SM offloading**: Communication runs on copy engines, leaving SMs free for computation
- **Better overlap**: Enables more efficient computation/communication overlap
- **Transparent API**: Uses the same collective API, just with symmetric memory tensors

**Requirements and Limitations**

- NCCL version 2.28 or later
- GPUs must have peer-to-peer (P2P) access enabled
- Tensors must be allocated using `torch.distributed._symmetric_memory()` and rendezvoused
- The NCCL process group must be configured with `NCCL_CTA_POLICY_ZERO` or the
environment variable `NCCL_CTA_POLICY` be set to 2
- As of NCCL 2.28, CE collectives cannot run with the default stream, so you
would need to use the `async_op=True` flag to activate the internal stream of
`ProcessGroupNCCL` or create a side stream yourself

## Higher-Precision Reduction

When tensors are allocated with symmetric memory, NCCL's symmetric kernel
implementation enables internal reduction with higher precision. For example, with
BF16 inputs, NCCL will automatically accumulate in FP32 internally before producing
BF16 outputs (BF16 in → FP32 accumulate → BF16 out). This improves numerical
accuracy of reduction operations without changing the collective call.

**Scope**

- **Applicable operations**: `reduce_scatter` and `all_reduce` only
- **Domain**: Within the NVLink domain as of torch 2.9 (NCCL 2.27);
NVLink + network for `reduce_scatter` as of torch 2.11 (NCCL 2.29)
- **Precision**: BF16/FP16 in → FP32 internal accumulation → BF16/FP16 out

**Example**

```
import torch.distributed as dist
import torch.distributed._symmetric_memory as symm_mem

# Allocate tensors using NCCL symmetric memory
symm_mem.set_backend("NCCL")
inp = symm_mem.empty(1024, 1024, device=device, dtype=torch.bfloat16)
symm_mem.rendezvous(inp, group_name)

# reduce_scatter and all_reduce on symmetric memory tensors
# automatically benefit from FP32 internal accumulation
dist.all_reduce(inp)
```

Note

This higher-precision accumulation is enabled transparently by NCCL when
using symmetric memory tensors. No additional configuration is required
beyond the symmetric tensor creation and rendezvous described above. This
currently applies to `reduce_scatter` and `all_reduce` within the
supported domains only; other collectives (e.g., `all_gather`) and
inter-node communication are not affected.

## Rendezvous at Scale

By default, `rendezvous` exchanges metadata via the TCPStore. Each rank in the
symmetric memory group issues one store set and N-1 store gets (where N is the
group size, typically 8-72 for NVLink domains). At large world sizes the
TCPStore (~200k QPS capacity) becomes a bottleneck: for example, with 72-rank
NVLink groups at 10k total ranks, a single rendezvous takes ~3.6s via TCPStore;
at 100k ranks this grows to ~36s.

To use the process group's NCCL allgather instead, set
`use_pg_for_symm_mem_rendezvous` in the process group options:

```
opts = dist.ProcessGroupNCCL.Options()
opts.use_pg_for_symm_mem_rendezvous = True
pg = dist.new_group(ranks, pg_options=opts)

t = symm_mem.empty(size, device=device)
hdl = symm_mem.rendezvous(t, group=pg)
```

If the process group is only used for symmetric memory and won't be used for
regular collectives afterwards (e.g., an expert-parallelism group), you can
release the NCCL communicator after rendezvous via `abort()`. The symmetric
memory handle remains usable since it only depends on the mapped memory, not the
communicator:

```
opts = dist.ProcessGroupNCCL.Options()
opts.use_pg_for_symm_mem_rendezvous = True
ep_pg = dist.new_group(ep_ranks, pg_options=opts)

t = symm_mem.empty(size, device=device)
hdl = symm_mem.rendezvous(t, group=ep_pg)

# Release the NCCL communicator since ep_pg won't be used for collectives.
# The symm_mem handle is still usable -- it only needs the mapped memory.
ep_pg.abort()
```

Note

Enabling `use_pg_for_symm_mem_rendezvous` will lazily create the NCCL
communicator for the process group if it doesn't already exist.

## API Reference

torch.distributed._symmetric_memory.empty(**size: _int*, *dtype: _dtype | [None](https://docs.python.org/3/library/constants.html#None) = None*, *device: _device | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2098)

torch.distributed._symmetric_memory.empty(*size: Sequence[_int]*, ***, *dtype: _dtype | [None](https://docs.python.org/3/library/constants.html#None) = None*, *device: _device | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Tensor](tensors.html#torch.Tensor)

Similar to [`torch.empty()`](generated/torch.empty.html#torch.empty). The returned tensor can be used by
`torch._distributed._symmetric_memory.rendezvous()` to establish a
symmetric memory tensor among participating processes.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.
Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

- **dtype** ([`torch.dtype`](tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](generated/torch.set_default_dtype.html#torch.set_default_dtype)).
- **device** ([`torch.device`](tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](generated/torch.set_default_device.html#torch.set_default_device)). `device` will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.

torch.distributed._symmetric_memory.rendezvous(*tensor*, *group*) → _SymmetricMemory[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2156)

Establish a symmetric memory tensor among participating processes. This is
a collective operation.

Parameters:

- **tensor** ([`torch.Tensor`](tensors.html#torch.Tensor)) - the local tensor used to establish the symmetric memory tensor.
It must be allocated via `torch._distributed._symmetric_memory.empty()`. The shape,
dtype, and device type must be identical across all participating processes.
- **group** (Union[str, `torch.distributed.ProcessGroup`]) - The group identifying the
participating processes. This can be either a group name or a process group object.

Return type:

_SymmetricMemory

torch.distributed._symmetric_memory.get(*dst*, *hdl*, *peer*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2334)

Copy `dst.numel()` elements starting at `offset` from `peer`'s
symmetric allocation into local `dst` using one-sided symmetric memory
access.

`hdl` is the symmetric memory handle returned by
`torch.distributed._symmetric_memory.rendezvous()`; the remote source
is `peer`'s allocation backing that handle. The number of elements copied
is inferred from `dst`; pass a view (e.g. `dst[:n]`) to fill only part
of a tensor. `offset` is expressed in elements of `dst`'s dtype.
`dst` can be a regular CUDA tensor or a symmetric-memory tensor; it must
be on the same device as `hdl` and backed by contiguous memory. The copy
is issued on the current CUDA stream.

Parameters:

- **dst** ([*Tensor*](tensors.html#torch.Tensor)) - local destination tensor.
- **hdl** (*SymmetricMemory*) - handle whose peer allocation is the remote
source.
- **peer** ([*int*](https://docs.python.org/3/library/functions.html#int)) - rank to copy from.
- **offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - element offset into the peer allocation to
start reading from. Defaults to `0`.

torch.distributed._symmetric_memory.is_nvshmem_available() → [bool](https://docs.python.org/3/library/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2176)

Check if NVSHMEM (CUDA) or rocSHMEM (ROCm) is available in the current
build and usable at runtime. On ROCm, rocSHMEM `VERSION` must be at
least 3.3.0 (see `rocshmem/rocshmem.hpp`).

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.distributed._symmetric_memory.set_backend(*name*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2194)

Set the backend for symmetric memory allocation. This is a global setting
and affects all subsequent calls to
`torch._distributed._symmetric_memory.empty()`. Note that the backend
cannot be changed once a symmetric memory tensor has been allocated.

Parameters:

**backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the backend for symmetric memory allocation. Currently,
only "NVSHMEM", "CUDA", "NCCL" are supported.

torch.distributed._symmetric_memory.get_backend(*device*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2208)

Get the backend for symmetric memory allocation for a given device. If not
found, return None.

Parameters:

**device** (torch.device or str) - the device for which to get the backend.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | None

torch.distributed._symmetric_memory.get_mem_pool(*device*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2278)

Get the symmetric memory pool for a given device. If not found, create a new
pool.

The tensor allocations with this pool must be symmetric across ranks. The
allocated tensors can be used with symmetric operations, for example,
operations defined under torch.ops.symm_mem.

Parameters:

**device** (torch.device or str) - the device for which to get the symmetric memory pool.

Returns:

the symmetric memory pool for the given device.

Return type:

torch.cuda.MemPool

Example:

```
>>> pool = torch.distributed._symmetric_memory.get_mem_pool("cuda:0")
>>> with torch.cuda.use_mem_pool(pool):
>>> tensor = torch.randn(1000, device="cuda:0")
>>> tensor = torch.ops.symm_mem.one_shot_all_reduce(tensor, "sum", group_name)
```

torch.distributed._symmetric_memory.is_symm_mem_tensor(*tensor*) → [bool](https://docs.python.org/3/library/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2516)

Returns `True` if `tensor` was allocated via symmetric memory
(i.e. via `torch.distributed._symmetric_memory.empty()` or
`_SymmetricMemory.empty_strided_p2p()`).

This is a non-collective, O(1) check.

Parameters:

**tensor** ([`torch.Tensor`](tensors.html#torch.Tensor)) - the tensor to check.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.distributed._symmetric_memory.set_signal_pad_size(*size*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2230)

Set the signal pad size for future symmetric memory allocations.

Signal pads are P2P-accessible memory regions used for synchronization in
symmetric memory. This function allows users to configure
the signal pad size to be proportional to their workload requirements.

Warning

This must be called before any symmetric memory allocations are made.
The size cannot be changed after allocations have been performed.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the signal pad size in bytes. The size should be
proportional to the number of blocks launched and the world size.

Example:

```
>>> # Set a larger signal pad size before any allocations
>>> torch.distributed._symmetric_memory.set_signal_pad_size(1024 * 1024) # 1MB
```

torch.distributed._symmetric_memory.get_signal_pad_size()[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2255)

Get the current signal pad size for symmetric memory allocations.

Returns the user-configured size if set via `set_signal_pad_size()`,
otherwise returns the default size.

Returns:

the signal pad size in bytes.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Example:

```
>>> size = torch.distributed._symmetric_memory.get_signal_pad_size()
>>> print(f"Signal pad size: {size} bytes")
```

## Op Reference

Note

The following ops are hosted in the `torch.ops.symm_mem` namespace. You can call
them directly via `torch.ops.symm_mem.<op_name>`.

torch.distributed._symmetric_memory.reduce_scatter_offset(*input*, *out*, *group*, ***, *dim*, *offsets*, *dst_ranks*, *red_op='sum'*) → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/distributed/_symmetric_memory/__init__.py#L2441)

Simultaneously reduce N blocks of a 2-D `input` tensor from a symmetric
memory buffer, routing each block to a specific destination rank. Only
`dst_ranks[i]` writes the reduced result for block `i`; the result is
written to a contiguous output tensor, with the same shape as block `i`.

The `dim` argument controls which dimension is sharded:

- `dim=0` (row sharding): block `i` spans
`input[offsets[i-1] : offsets[i], :]`. Each `out[j]` has shape
`(size_j, input.size(1))`.
- `dim=1` (column sharding): block `i` spans
`input[:, offsets[i-1] : offsets[i]]`. Each `out[j]` has shape
`(input.size(0), size_j)`.

Blocks are described by `offsets`, an inclusive prefix-sum of block sizes
along `dim` (first block starts at index 0 by convention). Block offsets
can be even or uneven; when uneven, the following condition must be met: for
each `j`, the `j`-th owned block must have the same size across all
ranks (so that `out[j]` has a uniform shape); different `j`'s may
differ.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - 2-D tensor allocated via symmetric memory (innermost
dimension must be contiguous).
- **out** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](tensors.html#torch.Tensor)*]*) - Output tensors for this rank's owned blocks. Must
have length equal to the number of blocks owned by this rank (i.e.
the count of `i` where `dst_ranks[i] == my_rank`). Each
`out[j]` must be contiguous with the same dtype as `input`.
- **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the `ProcessGroup` to perform the operation on.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Dimension along which blocks are defined (0 or 1).
- **offsets** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**None*) - Inclusive prefix-sum of block sizes along
`dim`, length N. If not provided, `input.size(dim)` is divided
into equal-size blocks based on the size of the `group`.
- **dst_ranks** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|**None*) - Destination rank for each block. If not
provided, blocks are distributed round-robin across ranks.
- **red_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Reduction operation; currently only `'sum'` is supported.

Example:

```
>>> # Each rank holds a Grouped GEMM gradient buffer in symmetric memory.
>>> # The buffer has W experts laid out as equal column blocks; each expert
>>> # is reduced to a specific rank (dst_ranks[i] == i % world_size).
>>> buf = symm_mem.empty(H, W * C, dtype=torch.bfloat16, device="cuda")
>>> symm_mem.rendezvous(buf, group=group_name)
>>> offsets = [i * C for i in range(1, W + 1)] # inclusive prefix-sum
>>> dst_ranks = [i % world_size for i in range(W)]
>>> n_owned = sum(r == rank for r in dst_ranks)
>>> out = [torch.empty(H, C, dtype=torch.bfloat16, device="cuda") for _ in range(n_owned)]
>>> symm_mem.reduce_scatter_offset(buf, out, group_name, dim=1, offsets=offsets, dst_ranks=dst_ranks)
```

torch.ops.symm_mem.multimem_all_reduce_(*input: [Tensor](tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*) → [Tensor](tensors.html#torch.Tensor)

Performs a multimem all-reduce operation on the input tensor. This operation
requires hardware support for multimem operations. On NVIDIA GPUs, NVLink
SHARP is required.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.multimem_all_gather_out(*input: [Tensor](tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *out: [Tensor](tensors.html#torch.Tensor)*) → [Tensor](tensors.html#torch.Tensor)

Performs a multimem all-gather operation on the input tensor. This operation requires hardware support for multimem operations. On NVIDIA GPUs, NVLink SHARP is required.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-gather on.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-gather on.
- **out** ([*Tensor*](tensors.html#torch.Tensor)) - Output tensor to store the result of the all-gather operation. Must be symmetric.

torch.ops.symm_mem.one_shot_all_reduce(*input: [Tensor](tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*) → [Tensor](tensors.html#torch.Tensor)

Performs a one-shot all-reduce operation on the input tensor.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.one_shot_all_reduce_out(*input: [Tensor](tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *out: [Tensor](tensors.html#torch.Tensor)*) → [Tensor](tensors.html#torch.Tensor)

Performs a one-shot all-reduce operation based on the input tensor and writes the result to the output tensor.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-reduce on.
- **out** ([*Tensor*](tensors.html#torch.Tensor)) - Output tensor to store the result of the all-reduce operation. Can be a regular tensor.

torch.ops.symm_mem.two_shot_all_reduce_(*input: [Tensor](tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*) → [Tensor](tensors.html#torch.Tensor)

Performs a two-shot all-reduce operation on the input tensor.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.all_to_all_vdev(*input: [Tensor](tensors.html#torch.Tensor)*, *out: [Tensor](tensors.html#torch.Tensor)*, *in_splits: [Tensor](tensors.html#torch.Tensor)*, *out_splits_offsets: [Tensor](tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*) → [None](https://docs.python.org/3/library/constants.html#None)

Performs an all-to-all-v operation using NVSHMEM, with split information provided on device.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing splits of data to send to each peer. Must be symmetric. Must be of size (group_size,). The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-to-all on.

torch.ops.symm_mem.all_to_all_vdev_2d(*input: Tensor*, *out: Tensor*, *in_splits: Tensor*, *out_splits_offsets: Tensor*, *group_name: str*[, *major_align: int = None*]) → [None](https://docs.python.org/3/library/constants.html#None)

Perform a 2D all-to-all-v operation using NVSHMEM, with split information provided on device. In Mixture of Experts models, this operation can be used to dispatch tokens.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing the splits of data to send to each expert. Must be symmetric. Must be of size (group_size * ne,), where ne is the number of experts per rank. The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size * ne). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-to-all on.
- **major_align** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Optional alignment for the major dimension of the output chunk for each expert. If not provided, the alignment is assumed to be 1. Any alignment adjustment will be reflected in the output offsets.

A 2D AllToAllv shuffle is illustrated below:
(world_size = 2, ne = 2, total number of experts = 4):

```
Source: | Rank 0 | Rank 1 |
 | c0 | c1 | c2 | c3 | d0 | d1 | d2 | d3 |

Dest : | Rank 0 | Rank 1 |
 | c0 | d0 | c1 | d1 | c2 | d2 | c3 | d3 |
```

where each c_i / d_i are slices of the input tensor, targeting expert
i, with length indicated by input splits. That is, the 2D AllToAllv
shuffle achieves a transpose from rank-major order at input to expert-major
order at output.

If major_align is not 1, the output offsets of c1, c2, c3 will be
up-aligned to this value. For example, if c0 has length 5 and d0 has
length 7 (making a total of 12), and if the major_align is set to 16,
the output offset of c1 will be 16. Similar for c2 and c3. This value has
no effect on the offset of the minor dimension, i.e. d0, d1, d2 and d3.
Note: since cutlass does not support empty bins, we set the aligned length
to major_align if it is 0. See
[pytorch/pytorch#152668](https://github.com/pytorch/pytorch/issues/152668).

torch.ops.symm_mem.all_to_all_vdev_2d_offset(*Tensor input*, *Tensor out*, *Tensor in_splits_offsets*, *Tensor out_splits_offsets*, *str group_name*) → [None](https://docs.python.org/3/library/constants.html#None)

Perform a 2D AllToAllv shuffle operation, with input split and offset
information provided on device. The input offsets are not required to be
exact prefix sum of the input splits, i.e. paddings are allowed between the
split chunks. The paddings, however, will not be transferred to peer
ranks.

In Mixture of Experts models, this operation can be used to combine tokens
processed by experts on parallel ranks. This operation can be viewed as an
"reverse" operation to the all_to_all_vdev_2d operation (which shuffles
tokens to experts).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits_offsets** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data to send to each expert. Must be symmetric. Must be of size (2, group_size * ne), where ne is the number of experts. The rows are (in order): input splits and input offsets. The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size * ne). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the group to perform all-to-all on.

torch.ops.symm_mem.tile_reduce(*in_tile: Tensor*, *out_tile: Tensor*, *root: int*, *group_name: str*[, *reduce_op: str = 'sum'*]) → [None](https://docs.python.org/3/library/constants.html#None)

Reduces a 2D tile from all ranks to a specified root rank within a process group.

Parameters:

- **in_tile** ([*Tensor*](tensors.html#torch.Tensor)) - Input 2D tensor to be reduced. Must be symmetrically allocated.
- **out_tile** ([*Tensor*](tensors.html#torch.Tensor)) - Output 2D tensor to contain the result of the reduction. Must be symmetric and have the same shape, dtype, and device as in_tile.
- **root** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The rank of the process in the specified group that will receive the reduced result.
- **group_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the symmetric memory process group to perform the reduction in.
- **reduce_op** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The reduction operation to perform. Currently, only `"sum"` is supported. Defaults to `"sum"`.

This function reduces in_tile tensors from all members of the group, writing the result to out_tile at the root rank. All ranks must participate and provide the same group_name and tensor shapes.

Example:

```
>>> 
>>> # Reduce the bottom-right quadrant of a tensor
>>> tile_size = full_size // 2
>>> full_inp = symm_mem.empty(full_size, full_size)
>>> full_out = symm_mem.empty(full_size, full_size)
>>> s = slice(tile_size, 2 * tile_size)
>>> in_tile = full_inp[s, s]
>>> out_tile = full_out[s, s]
>>> torch.ops.symm_mem.tile_reduce(in_tile, out_tile, root=0, group_name)
```

torch.ops.symm_mem.multi_root_tile_reduce(*in_tiles: list[Tensor], out_tile: Tensor, roots: list[int], group_name: str, [reduce_op: str = 'sum']*) → [None](https://docs.python.org/3/library/constants.html#None)

Perform multiple tile reductions concurrently, with each tile reduced to a separate root.

: param list[Tensor] in_tiles: A list of input tensors.
: param Tensor out_tile: Output tensor to contain the reduced tile.
: param list[int] roots: A list of root ranks each corresponding to an input tile in in_tiles, in the same order. A rank cannot be a root more than once.
: param str group_name: Name of the group to use for the collective operation.
: param str reduce_op: Reduction operation to perform. Currently only "sum" is supported.

Example:

```
>>> 
>>> # Reduce four quadrants of a tensor, each to a different root
>>> tile_size = full_size // 2
>>> full_inp = symm_mem.empty(full_size, full_size)
>>> s0 = slice(0, tile_size)
>>> s1 = slice(tile_size, 2 * tile_size)
>>> in_tiles = [ full_inp[s0, s0], full_inp[s0, s1], full_inp[s1, s0], full_inp[s1, s1] ]
>>> out_tile = symm_mem.empty(tile_size, tile_size)
>>> roots = [0, 1, 2, 3]
>>> torch.ops.symm_mem.multi_root_tile_reduce(in_tiles, out_tile, roots, group_name)
```