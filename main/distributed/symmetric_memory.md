# PyTorch Symmetric Memory

Note

`torch.distributed._symmetric_memory` is currently in alpha state and under
development. Its Python APIs and every operator in `torch.ops.symm_mem` may
change without notice. A dispatcher-visible operator is not necessarily a
user-facing API. The maturity table below identifies which operators are
intended for direct use and which are implementation details.

## API status and operator guide

The module-level alpha label applies to every operator intended for direct use.
The table separates maturity from runtime scope so that hardware or backend
requirements are not presented as a lower maturity level. These classifications
summarize the current implementations and tests; they do not establish new
project-wide PyTorch stability levels or backward-compatibility guarantees:

- **Alpha** identifies operators intended for direct use under the module-wide
alpha disclaimer.
- **Experimental** identifies especially incomplete or compiler-oriented
interfaces that may change rapidly.
- **Internal** identifies compiler targets or implementation details that
should not be called directly.

| Operations | Maturity | Scope or requirements | When to use them |
| --- | --- | --- | --- |
| `empty`, `rendezvous`, `get`, and `get_mem_pool` | Alpha | General | Allocate, establish, access, and reuse symmetric memory. |
| `fused_all_gather_matmul` and `fused_matmul_reduce_scatter` | Alpha | General | Overlap an unscaled matrix multiplication with a tensor-parallel collective. Ordinary accelerator tensors are accepted; the operators manage a symmetric workspace. These are also targets of the compiler's tensor-parallel fusion pass. |
| `fused_all_gather_scaled_matmul` and `fused_scaled_matmul_reduce_scatter` | Experimental | Hardware-specific | FP8 or other scaled matrix multiplication when the accelerator supports `aten._scaled_mm`. Their interfaces closely follow compiler lowering requirements. |
| `one_shot_all_reduce`, `one_shot_all_reduce_out`, and `two_shot_all_reduce_` | Alpha | Hardware-specific | Low-latency, direct-access all-reduce on a symmetric tensor. |
| `multimem_all_reduce_` and `multimem_all_gather_out` | Alpha | Hardware-specific | NVIDIA systems with multicast and multimem support, such as NVLink SHARP. |
| `multimem_one_shot_all_reduce`, `multimem_one_shot_all_reduce_out`, and `multimem_one_shot_reduce_out` | Experimental | Hardware-specific | Compiler-oriented multimem variants. Their reduction order is not fixed, so all ranks are not guaranteed to receive bitwise-identical results. |
| `get_remote_tensors` | Alpha | Hardware-specific | Create local tensor views of peer allocations when every peer is directly addressable. The views require explicit cross-rank synchronization. |
| `nvshmem_*`, `all_to_all_vdev*`, `tile_reduce`, and `multi_root_tile_reduce` | Alpha | Backend-specific | NVSHMEM or rocSHMEM transport and device-driven collectives. Availability differs by operation and SHMEM implementation. |
| `reduce_scatter_offset` and `all_to_all_nd` | Alpha | Backend-specific | NCCL-backend routing and multidimensional all-to-all. |
| `put_signal` and `wait_signal` | Experimental | Backend-specific | One-sided signaling; currently implemented only for the NCCL backend. |
| `_low_contention_*`, `_async_input_mm`, `_rendezvous`, and `_barrier` | Internal | Compiler-facing | Compiler and dispatcher implementation details. |
| `one_shot_all_reduce_copy`, `one_shot_all_reduce_copy_out`, `two_shot_all_reduce_out`, and `reduce_scatter_out` | Internal | Compiler-facing | Compiler buffer-planning variants. Use the documented allocating or in-place operator instead. |
| `stream_write_value32_`, `memset32_`, `memcpy_to_multicast_`, and raw `nccl_*` operators | Internal | Backend implementation | Kernel composition or backend dispatch. Use a documented Python wrapper instead. |

The scaled fused operators, hardware-specific collectives, and internal
operators are the least portable parts of the surface. In particular, do not
infer support from an operator being present in `torch.ops.symm_mem`: some
kernels are compiled only for particular backends or require runtime hardware
features.

The `torch.ops.symm_mem` namespace also does not provide a stable public
autograd contract. For training graphs, prefer expressing the unfused
collective and computation with higher-level PyTorch APIs and allowing the
compiler to select a Symmetric Memory fusion when applicable.

### Stream ordering

Built-in CUDA-backend barriers, signal operations, and collectives serialize
their signal-pad use across streams for each process group and device. This
serialization also participates in CUDA graph capture. It does not cover
NVSHMEM operations, `ncclPutSignal`/`ncclWaitSignal`, or custom kernels that use
a raw signal-pad tensor. Issue those uncovered operations for a group from one
stream, or explicitly order their streams.

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
 x = torch.arange(128, device=device, dtype=torch.float32)

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

Note

The pool returned by `get_mem_pool` feeds `torch.ops.symm_mem.*`
kernels, though it does not register the allocation with NCCL. To drive
`dist.*` collectives onto NCCL's symmetric memory
backed kernels, you can register the mempool for NCCL to auto-select.
For more details, see NCCL Symmetric Kernels.

## NCCL Symmetric Kernels

Note

Requires NCCL 2.27 or later and a single NVLink domain (every rank reachable
over direct NVLink).

NCCL 2.27+ added a family of device kernels -- "SymK" internally -- written
specifically for symmetric, window-registered buffers. Because each rank knows
every peer's buffer address up front, these kernels skip the generic
proxy/ring machinery and instead use LL (low-latency), multimem/NVLS, and TMA
variants. NCCL picks one per call from message size, so the same
`dist.all_reduce` gets a latency-optimized kernel for small messages and a
bandwidth-optimized one for large ones.

Symmetric kernels are driven through the *standard* collective API --
`dist.all_reduce`, `dist.all_gather_single`, `dist.reduce_scatter_single` --
with no change at the call site. What matters is that the buffers were
registered with NCCL as symmetric windows. There are two ways to arrange that.

### Option 1: register a memory pool with the process group

This route puts NCCL's allocator behind a `torch.cuda.MemPool`, so *any*
tensor allocated inside the pool's context is window-registered, including
tensors produced by compute ops. It is usually the better fit for an existing
model, since allocations do not have to be rewritten as `symm_mem.empty`.

```
import torch
import torch.distributed as dist

device = torch.device("cuda", rank)

# `device_id` eagerly initializes the NCCL communicator. `register_mem_pool`
# requires a communicator that already exists, and raises otherwise.
dist.init_process_group(backend="nccl", device_id=device)
pg = dist.group.WORLD

backend = dist.get_backend_impl(pg, device)

# A MemPool backed by `ncclMemAlloc` / `ncclMemFree`.
pool = torch.cuda.MemPool(backend.mem_allocator)

# `symm=True` registers each segment with `ncclCommWindowRegister` using
# `NCCL_WIN_COLL_SYMMETRIC`, which is what makes the symmetric kernels
# eligible. The default `symm=False` performs ordinary user-buffer
# registration, which does not.
backend.register_mem_pool(pool, symm=True)

with torch.cuda.use_mem_pool(pool):
 x = torch.ones(1024 * 1024, dtype=torch.bfloat16, device=device)

# Dispatches to a NCCL symmetric kernel.
dist.all_reduce(x, op=dist.ReduceOp.SUM)

# De-register before the pool is torn down.
backend.deregister_mem_pool(pool)
```

`register_mem_pool` registers the segments already in the pool *and* installs an
allocator hook, so later allocations in the pool are registered as well.

### Option 2: allocate through the NCCL symmetric memory backend

If the tensors are already symmetric-memory tensors -- for example because
custom kernels need the handle, its peer pointers, or its signal pads -- select
the `NCCL` backend and rendezvous as usual. `rendezvous` window-registers the
allocation, so `dist.*` collectives on it become eligible too.

```
import torch.distributed as dist
import torch.distributed._symmetric_memory as symm_mem

symm_mem.set_backend("NCCL")

x = symm_mem.empty(1024 * 1024, dtype=torch.bfloat16, device=device)
symm_mem.rendezvous(x, group=dist.group.WORLD.group_name)

dist.all_reduce(x, op=dist.ReduceOp.SUM)
```

### When NCCL uses a symmetric kernel

Only these collective / reduction / dtype combinations currently have a symmetric
implementation:

| Collective | Reduction ops | Data types |
| --- | --- | --- |
| `all_gather` | n/a | any |
| `all_reduce` | `SUM`, `AVG` | `float32`, `float16`, `bfloat16`, `float8_e4m3fn`, `float8_e5m2` |
| `reduce_scatter` | `SUM`, `AVG` | `float32`, `float16`, `bfloat16`, `float8_e4m3fn`, `float8_e5m2` |

Note in particular that `float64` and the integer dtypes are excluded for the
two reducing collectives, as are `MIN` / `MAX` / `PRODUCT`. Collectives outside
the table (`broadcast`, `reduce`, `all_to_all`, point-to-point) currently have no
symmetric implementation, and fall back to the regular ring/tree path silently.

To confirm, you can use NCCL logs to check kernel names:

```
NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=TUNING python train.py
```

```
AllReduce [Symmetric]: 2097152 Bytes -> Kernel AllReduce_RSxLDMC_AGxSTMC nchannels 16 nthreads 512 nWorks 1
```

Also, if you are looking at a profiler,
device kernel names should resemble `ncclSymkDevKernel_*`.
For example, `ncclSymkDevKernel_AllReduce_AGxLLMC_R_sum_bf16`, as opposed to
`ncclDevKernel_*` for the generic NCCL path.

### CFT logical-endpoint handles

Note

Requires NCCL 2.31.2+, a Blackwell-class GPU (sm_100 or newer), and a driver
reporting CUDA 13.3 or later (an r610-or-newer driver). NCCL itself must also
be built with CUDA 13.3+.

CFT (Compute Fabric Transport) exposes a peer's window-registered memory as a
*logical endpoint*: an opaque `(le_id, le_offset)` pair that a custom device
kernel can hand to the `ncclCft` put/get/reduce device API to reach that
peer's copy of a symmetric buffer -- without constructing a `ncclDevComm`.
When the symmetric-memory backend is `NCCL`, the rendezvous handle exposes
the coordinates:

- `hdl.get_peer_cft_handle(peer)` returns the `(le_id, le_offset)` pair
addressing `peer`'s copy of the buffer.
- `hdl.get_multimem_cft_handle()` returns the multicast endpoint (requires
NVLS; the first call may be collective, so all ranks must reach it).

Handles are only meaningful for the group the tensor was rendezvoused with --
each group owns a separate set of logical endpoints over the same allocation.

Two knobs control availability:

- `host_cft_mode` on the communicator config
(`ProcessGroupNCCL.Options().config.host_cft_mode`) decides whether the
endpoints are created and what happens when the stack cannot support them:
`1` (enable -- fail communicator init if unsupported), `2` (disable), `3`
(fallback -- create them if possible, silently proceed without otherwise).
The default is **disable**: host-side CFT is opt-in per communicator, since
endpoints are a limited per-device resource. The mode must be identical on
every rank and must be set before the communicator is created -- the
endpoints are made during window registration.
- The `NCCL_CFT_ENABLE` environment variable (default `1`) is NCCL's global
kill switch; `NCCL_CFT_ENABLE=0` makes NCCL report no CFT support
regardless of `host_cft_mode`.

Under `host_cft_mode=3` (fallback), an unsupported GPU, driver, or NCCL build
is not an error at init -- the handle queries simply raise `RuntimeError`.

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
- Tensors must be allocated using `torch.distributed._symmetric_memory.empty()` and rendezvoused
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

torch.distributed._symmetric_memory.empty(**size: _int*, *dtype: _dtype | [None](https://docs.python.org/3/builtins/constants.html#None) = None*, *device: _device | [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2276)

torch.distributed._symmetric_memory.empty(*size: Sequence[_int]*, ***, *dtype: _dtype | [None](https://docs.python.org/3/builtins/constants.html#None) = None*, *device: _device | [None](https://docs.python.org/3/builtins/constants.html#None) = None*) → [Tensor](../tensors.html#torch.Tensor)

Similar to [`torch.empty()`](../generated/torch.empty.html#torch.empty). The returned tensor can be used by
`torch._distributed._symmetric_memory.rendezvous()` to establish a
symmetric memory tensor among participating processes.

Note

This is a host-synchronous allocation. Together with
`rendezvous()`, it is intended as an initialization-time
operation: allocate a symmetric memory tensor once and reuse it,
rather than allocating in hot code paths. It cannot be captured in a
CUDA graph; the CUDA backend raises an error if it is called while
the current stream is capturing. Allocate before capture instead.

Parameters:

**size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.
Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](../generated/torch.set_default_dtype.html#torch.set_default_dtype)).
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](../generated/torch.set_default_device.html#torch.set_default_device)). `device` will be the CPU
for CPU tensor types, the current CUDA device for CUDA tensor types,
and the current XPU device for XPU tensor types.

torch.distributed._symmetric_memory.rendezvous(*tensor*, *group*) → _SymmetricMemory[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2341)

Establish a symmetric memory tensor among participating processes. This is
a collective operation.

Note

This is a host-blocking initialization operation: the first rendezvous
of a tensor performs handle exchange and mapping across processes, and
synchronizes the host with the device. It cannot be ordered onto a
CUDA stream or captured in a CUDA graph; the CUDA backend raises an
error if the first rendezvous of a tensor happens while the current
stream is capturing. Rendezvous a buffer once and reuse the returned
handle rather than calling this in hot code paths; subsequent calls on
the same tensor return the cached handle and are safe to capture.
Symmetric memory collectives on a rendezvoused buffer can be captured
after they have run once eagerly. Every rank must then replay the
captured graph the same number of times, because each replay performs
the peer synchronization for that rank.

Parameters:

- **tensor** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - the local tensor used to establish the symmetric memory tensor.
It must be allocated via `torch._distributed._symmetric_memory.empty()`. The shape,
dtype, and device type must be identical across all participating processes.
- **group** (Union[str, [`torch.distributed.ProcessGroup`](../distributed.html#torch.distributed.ProcessGroup)]) - The group identifying the
participating processes. This can be either a group name or a process group object.

Return type:

_SymmetricMemory

torch.distributed._symmetric_memory.get(*dst*, *hdl*, *peer*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2535)

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

- **dst** ([*Tensor*](../tensors.html#torch.Tensor)) - local destination tensor.
- **hdl** (*SymmetricMemory*) - handle whose peer allocation is the remote
source.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - rank to copy from.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - element offset into the peer allocation to
start reading from. Defaults to `0`.

torch.distributed._symmetric_memory.put_signal(*src*, *hdl*, *peer*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2599)

Put data to a peer's symmetric memory and signal the peer.

Parameters:

- **src** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the source tensor to read data from.
- **hdl** (*SymmetricMemory*) - the symmetric memory to put data to.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - the peer to put data to.

torch.distributed._symmetric_memory.wait_signal(*hdl*, *peer*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2622)

Wait for a signal from a peer.

Parameters:

- **hdl** (*SymmetricMemory*) - the symmetric memory handle on which to wait for a signal.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - the peer to wait for a signal from.

torch.distributed._symmetric_memory.is_nvshmem_available() → [bool](https://docs.python.org/3/builtins/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2375)

Check if NVSHMEM (CUDA) or rocSHMEM (ROCm) is available in the current
build and usable at runtime. On ROCm, rocSHMEM `VERSION` must be at
least 3.5.0 (see `rocshmem/rocshmem.hpp`).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

torch.distributed._symmetric_memory.set_backend(*name*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2393)

Set the backend for symmetric memory allocation. This is a global setting
and affects all subsequent calls to
`torch.distributed._symmetric_memory.empty()`. Note that the backend
cannot be changed once a symmetric memory tensor has been allocated.

Parameters:

**name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - the backend for symmetric memory allocation. Currently,
only "NVSHMEM", "CUDA", "NCCL" are supported.

torch.distributed._symmetric_memory.get_backend(*device*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2407)

Get the backend for symmetric memory allocation for a given device. If not
found, return None.

Parameters:

**device** (torch.device or str) - the device for which to get the backend.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str) | None

torch.distributed._symmetric_memory.get_mem_pool(*device*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2477)

Get the symmetric memory pool for a given device. If not found, create a new
pool.

The tensor allocations with this pool must be symmetric across ranks. The
allocated tensors can be used with symmetric operations, for example,
operations defined under torch.ops.symm_mem.

Parameters:

**device** (torch.device or str) - the device for which to get the symmetric memory pool.

Returns:

the symmetric memory pool for the given device, e.g. a
torch.cuda.MemPool for a CUDA device or a torch.xpu.MemPool for an
XPU device.

Return type:

torch.cuda.MemPool | torch.xpu.MemPool

Example:

```
>>> pool = torch.distributed._symmetric_memory.get_mem_pool("cuda:0")
>>> with torch.cuda.use_mem_pool(pool):
>>> tensor = torch.randn(1000, device="cuda:0")
>>> tensor = torch.ops.symm_mem.one_shot_all_reduce(tensor, "sum", group_name)
```

torch.distributed._symmetric_memory.is_symm_mem_tensor(*tensor*) → [bool](https://docs.python.org/3/builtins/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2717)

Returns `True` if `tensor` was allocated via symmetric memory
(i.e. via `torch.distributed._symmetric_memory.empty()` or
`_SymmetricMemory.empty_strided_p2p()`).

This is a non-collective, O(1) check.

Parameters:

**tensor** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - the tensor to check.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

torch.distributed._symmetric_memory.set_signal_pad_size(*size*)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2429)

Set the signal pad size for future symmetric memory allocations.

Signal pads are P2P-accessible memory regions used for synchronization in
symmetric memory. This function allows users to configure
the signal pad size to be proportional to their workload requirements.

Warning

This must be called before any symmetric memory allocations are made.
The size cannot be changed after allocations have been performed.

Parameters:

**size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - the signal pad size in bytes. The size should be
proportional to the number of blocks launched and the world size.

Example:

```
>>> # Set a larger signal pad size before any allocations
>>> torch.distributed._symmetric_memory.set_signal_pad_size(1024 * 1024) # 1MB
```

torch.distributed._symmetric_memory.get_signal_pad_size()[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2454)

Get the current signal pad size for symmetric memory allocations.

Returns the user-configured size if set via `set_signal_pad_size()`,
otherwise returns the default size.

Returns:

the signal pad size in bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Example:

```
>>> size = torch.distributed._symmetric_memory.get_signal_pad_size()
>>> print(f"Signal pad size: {size} bytes")
```

torch.distributed._symmetric_memory.all_to_all_nd(*input*, *out*, *scatter_dim*, *gather_dim*, ***, *group*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2733)

Permute-free all-to-all: shards along `scatter_dim` of `input` are exchanged
so each rank receives one shard per peer; results are laid out along `gather_dim`
of `out`. Supported pairs are `(scatter_dim=1, gather_dim=0)` and
`(scatter_dim=0, gather_dim=1)`.

For `scatter_dim=1`, `gather_dim=0` (let `G` be the group size): `input` is
`[rows, G * local_cols]` or equivalently `[rows, G, local_cols]`;
each rank `r` reads column block `r` from every peer and writes peer `j` into
`out[j]`. `out` must be contiguous with shape `[G, rows, local_cols]` or the
flattened equivalent `[G * rows, local_cols]`.

For `scatter_dim=0`, `gather_dim=1` (`G` is the group size): `input` is
`[G * local_rows, cols]` or equivalently `[G, local_rows, cols]`;
each rank `r` reads row block `r` from every peer; peer `j` is stored in
`out[:, j, :]`. `out` must be contiguous with shape `[local_rows, G, cols]` or
`[local_rows, G * cols]` (flattened gather and inner dims).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - For `(scatter_dim=1, gather_dim=0)`, 2-D `[rows, G*local_cols]` or
3-D `[rows, G, local_cols]` in symmetric memory (innermost dimension contiguous).
For `(scatter_dim=0, gather_dim=1)`, 2-D `[G*local_rows, cols]` or 3-D
`[G, local_rows, cols]` (same layout).
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Contiguous buffer (see shapes above; 2-D allowed where noted).
- **scatter_dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - `0` or `1` -- dimension along which the input is partitioned.
- **gather_dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - `0` or `1` -- dimension along which peer chunks are
concatenated in `out`.
- **group** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - The name of the `ProcessGroup` to perform the operation on.

## Op Reference

Note

The following ops are hosted in the `torch.ops.symm_mem` namespace. You can call
them directly via `torch.ops.symm_mem.<op_name>`.

torch.distributed._symmetric_memory.reduce_scatter_offset(*input*, *out*, *group*, ***, *dim*, *offsets*, *dst_ranks*, *red_op='sum'*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/89a8b1cfbad1eafcade9ad8ed84db0d2399b0ce4/torch/distributed/_symmetric_memory/__init__.py#L2642)

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

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - 2-D tensor allocated via symmetric memory (innermost
dimension must be contiguous).
- **out** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Output tensors for this rank's owned blocks. Must
have length equal to the number of blocks owned by this rank (i.e.
the count of `i` where `dst_ranks[i] == my_rank`). Each
`out[j]` must be contiguous with the same dtype as `input`.
- **group** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - The name of the `ProcessGroup` to perform the operation on.
- **dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Dimension along which blocks are defined (0 or 1).
- **offsets** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**|**None*) - Inclusive prefix-sum of block sizes along
`dim`, length N. If not provided, `input.size(dim)` is divided
into equal-size blocks based on the size of the `group`.
- **dst_ranks** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**|**None*) - Destination rank for each block. If not
provided, blocks are distributed round-robin across ranks.
- **red_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Reduction operation; currently only `'sum'` is supported.

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

torch.ops.symm_mem.fused_all_gather_matmul(*A_shard: [Tensor](../tensors.html#torch.Tensor)*, *Bs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]*, *gather_dim: [int](https://docs.python.org/3/builtins/functions.html#int)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, ***, *return_A: [bool](https://docs.python.org/3/builtins/functions.html#bool) = True*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None), [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]]

Overlaps an all-gather of `A_shard` with one or more matrix
multiplications. It is semantically equivalent to:

```
A = all_gather_single(A_shard, gather_dim, group)
outputs = [torch.matmul(A, B) for B in Bs]
```

The tensors in `Bs` must be 2-D and compatible with `A` for matrix
multiplication. `A_shard` may be an ordinary accelerator tensor; the
operator allocates and reuses symmetric workspace internally. All ranks
must call the operator with matching shapes and arguments.

For best performance, arrange `A_shard` so that
`A_shard.movedim(gather_dim, 0)` is contiguous. Set `return_A=False`
when only the matrix-multiplication results are needed; this can avoid
materializing the gathered tensor on supported systems. Run the operator
once before CUDA graph capture so that its workspace is large enough.

Parameters:

- **A_shard** ([*Tensor*](../tensors.html#torch.Tensor)) - Rank-local shard of the left matrix.
- **Bs** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Right-hand matrices. Multiple matrices reuse the
same gathered input.
- **gather_dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Dimension of `A_shard` to gather.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the process group.
- **return_A** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether to return the gathered `A`. Defaults to
`True`.

Returns:

The gathered tensor (or `None`) and the list of matrix-
multiplication results.

torch.ops.symm_mem.fused_all_gather_scaled_matmul(*A_shard: [Tensor](../tensors.html#torch.Tensor)*, *Bs: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]*, *A_scale: [Tensor](../tensors.html#torch.Tensor)*, *B_scales: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]*, *gather_dim: [int](https://docs.python.org/3/builtins/functions.html#int)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *biases: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None)]*, *result_scales: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None)]*, *out_dtypes: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/builtins/constants.html#None)]*, *use_fast_accum: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)]*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]]

Scaled-matrix-multiplication variant of
`fused_all_gather_matmul()`. Each entry of `B_scales`, `biases`,
`result_scales`, `out_dtypes`, and `use_fast_accum` corresponds to
the entry at the same position in `Bs` and is forwarded to
`aten._scaled_mm`.

`A_scale` may be a tensor-wise scalar, a row-wise scale sharded like
`A_shard`, or a row-wise scale for the fully gathered tensor. The exact
dtype, scale-layout, and accelerator requirements are those of
`aten._scaled_mm`. This is a specialized compiler fusion target; support
for a particular FP8 format or shape must be checked on the target
accelerator.

Returns:

The gathered `A` and the list of scaled-matmul results.

torch.ops.symm_mem.fused_matmul_reduce_scatter(*A: [Tensor](../tensors.html#torch.Tensor)*, *B: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *scatter_dim: [int](https://docs.python.org/3/builtins/functions.html#int)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Overlaps matrix multiplication with a reduce-scatter. It is semantically
equivalent to:

```
C = torch.matmul(A, B)
out = reduce_scatter_single(C, reduce_op, scatter_dim, group)
```

`A` must have at least two dimensions, `B` must be 2-D, and the size
of the matrix-multiplication result along `scatter_dim` must be divisible
by the process-group size. `reduce_op` may be `"sum"` or `"avg"`.
`A` and `B` may be ordinary accelerator tensors; symmetric workspace
is managed internally.

For best performance, arrange `A` so that
`A.movedim(scatter_dim, 0)` is contiguous. Run the operator once before
CUDA graph capture so that its workspace is large enough.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - Left matrix or batch of matrices.
- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - 2-D right-hand matrix.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - `"sum"` or `"avg"`.
- **scatter_dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Result dimension to scatter.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the process group.

torch.ops.symm_mem.fused_scaled_matmul_reduce_scatter(*A: [Tensor](../tensors.html#torch.Tensor)*, *B: [Tensor](../tensors.html#torch.Tensor)*, *A_scale: [Tensor](../tensors.html#torch.Tensor)*, *B_scale: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *orig_scatter_dim: [int](https://docs.python.org/3/builtins/functions.html#int)*, *scatter_dim_after_maybe_reshape: [int](https://docs.python.org/3/builtins/functions.html#int)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *output_shape: [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]*, *bias: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None) = None*, *result_scale: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/builtins/constants.html#None) = None*, *out_dtype: [dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/builtins/constants.html#None) = None*, *use_fast_accum: [bool](https://docs.python.org/3/builtins/functions.html#bool) = False*) → [Tensor](../tensors.html#torch.Tensor)

Scaled-matrix-multiplication variant of
`fused_matmul_reduce_scatter()`. The two scatter dimensions and
`output_shape` preserve the shape information from the compiler pattern
`reshape -> aten._scaled_mm -> reshape -> reduce_scatter`. For a direct
call without those reshapes, pass the same value for both scatter
dimensions and pass `[*A.shape[:-1], B.shape[1]]` as `output_shape`.

This operator is primarily a compiler target. Its supported dtypes, scale
layouts, and hardware follow `aten._scaled_mm` and are narrower than the
unscaled operator.

torch.ops.symm_mem.get_remote_tensors(*x: [Tensor](../tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Returns tensor views of the allocation belonging to every rank in
`group_name`, ordered by rank. `x` must be a symmetric-memory tensor
and every peer must be directly addressable, for example within one NVLink
domain. The operation does not work across a network transport.

The returned tensors alias peer memory. PyTorch does not automatically
synchronize peer reads and writes through these views; coordinate access
with a barrier, signal, or another suitable protocol.

Parameters:

- **x** ([*Tensor*](../tensors.html#torch.Tensor)) - Local tensor naming the symmetric allocation.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the process group used to rendezvous the
allocation.

torch.ops.symm_mem.multimem_all_reduce_(*input: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Performs a multimem all-reduce operation on the input tensor. This operation
requires hardware support for multimem operations. On NVIDIA GPUs, NVLink
SHARP is required.

The built-in CUDA implementation orders this operation with other built-in
signal-pad operations for the same group. See
Stream ordering for the operations not covered by
that ordering.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.multimem_all_gather_out(*input: [Tensor](../tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *out: [Tensor](../tensors.html#torch.Tensor)*) → [Tensor](../tensors.html#torch.Tensor)

Performs a multimem all-gather operation on the input tensor. This operation requires hardware support for multimem operations. On NVIDIA GPUs, NVLink SHARP is required.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-gather on.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-gather on.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-gather operation. Must be symmetric.

torch.ops.symm_mem.one_shot_all_reduce(*input: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Performs a one-shot all-reduce operation on the input tensor.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.one_shot_all_reduce_out(*input: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *out: [Tensor](../tensors.html#torch.Tensor)*) → [Tensor](../tensors.html#torch.Tensor)

Performs a one-shot all-reduce operation based on the input tensor and writes the result to the output tensor.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-reduce on.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-reduce operation. Can be a regular tensor.

torch.ops.symm_mem.two_shot_all_reduce_(*input: [Tensor](../tensors.html#torch.Tensor)*, *reduce_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Performs a two-shot all-reduce operation on the input tensor.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-reduce on. Must be symmetric.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Reduction operation to perform. Currently only "sum" is supported.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-reduce on.

torch.ops.symm_mem.nvshmem_broadcast(*input: [Tensor](../tensors.html#torch.Tensor)*, *root: [int](https://docs.python.org/3/builtins/functions.html#int)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Broadcasts the input tensor from the root rank to all ranks in the group
using NVSHMEM, in place. This op is host/stream-initiated and works both
intra-node and across nodes. On non-root ranks the contents of input are
overwritten with the data from the root; on the root rank they are unchanged.
The operation is issued on the current CUDA stream and returns input.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor to broadcast (on the root) or receive into (on other ranks). Must be symmetric.
- **root** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Rank within the group that holds the source data. Must be smaller than the group size.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform the broadcast on.

torch.ops.symm_mem.nvshmem_put(*tensor: [Tensor](../tensors.html#torch.Tensor)*, *peer: [int](https://docs.python.org/3/builtins/functions.html#int)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Performs a one-sided, host/stream-initiated put over NVSHMEM: copies the
local tensor into the same symmetric allocation on peer. Works both
intra-node and across nodes (e.g. over RDMA/RoCE). The op only issues the
transfer on the current CUDA stream; it does not wait for remote completion,
so you must provide your own synchronization (e.g. nvshmem_put_with_signal
/ nvshmem_wait_for_signal) before consuming the data on the peer.

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - Symmetric, contiguous tensor whose data is sent, and which also names the destination allocation on the peer.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Rank to send the data to. Must be smaller than the world size.

torch.ops.symm_mem.nvshmem_get(*tensor: [Tensor](../tensors.html#torch.Tensor)*, *peer: [int](https://docs.python.org/3/builtins/functions.html#int)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Performs a one-sided, host/stream-initiated get over NVSHMEM: copies the data
from the same symmetric allocation on peer into the local tensor. Works
both intra-node and across nodes. The transfer is issued on the current CUDA
stream.

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - Symmetric, contiguous tensor that receives the data, and which also names the source allocation on the peer.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Rank to read the data from. Must be smaller than the world size.

torch.ops.symm_mem.nvshmem_get_out(*dst: [Tensor](../tensors.html#torch.Tensor)*, *hdl: SymmetricMemory*, *offset: [int](https://docs.python.org/3/builtins/functions.html#int)*, *size: [int](https://docs.python.org/3/builtins/functions.html#int)*, *peer: [int](https://docs.python.org/3/builtins/functions.html#int)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Low-level, host/stream-initiated get that copies size elements starting at
element offset from the peer's symmetric allocation (the one backing hdl)
into dst. This is the primitive backing the higher-level
`get()` helper; most users should
prefer that helper. The copy is issued on the current CUDA stream.

Parameters:

- **dst** ([*Tensor*](../tensors.html#torch.Tensor)) - Local CUDA tensor to receive the data. Must be contiguous, on the same device as hdl, and hold at least size elements.
- **hdl** (*SymmetricMemory*) - Handle returned by rendezvous, identifying the peer's symmetric allocation to read from.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Starting element (in dst's dtype) within the peer allocation. Must be non-negative.
- **size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Number of elements to copy. Must be non-negative.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Rank to read the data from. Must be a valid rank in the group.

torch.ops.symm_mem.nvshmem_put_with_signal(*tensor: [Tensor](../tensors.html#torch.Tensor)*, *sigpad: [Tensor](../tensors.html#torch.Tensor)*, *signal: [int](https://docs.python.org/3/builtins/functions.html#int)*, *peer: [int](https://docs.python.org/3/builtins/functions.html#int)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Performs a one-sided put of tensor to the same symmetric allocation on
peer, and atomically sets the peer's signal location sigpad to signal
once the data transfer has completed. This lets the peer detect arrival of
the data via nvshmem_wait_for_signal. Issued on the current CUDA stream.

Parameters:

- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - Symmetric tensor whose data is sent, and which also names the destination allocation on the peer.
- **sigpad** ([*Tensor*](../tensors.html#torch.Tensor)) - Symmetric signal pad on the peer to set once the transfer completes.
- **signal** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Value to set the peer's sigpad to.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Rank to send the data to.

torch.ops.symm_mem.nvshmem_wait_for_signal(*sigpad: [Tensor](../tensors.html#torch.Tensor)*, *signal: [int](https://docs.python.org/3/builtins/functions.html#int)*, *peer: [int](https://docs.python.org/3/builtins/functions.html#int)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Blocks the current CUDA stream until the local signal location sigpad
equals signal. Typically paired with nvshmem_put_with_signal on the
sender side to wait for incoming data.

Parameters:

- **sigpad** ([*Tensor*](../tensors.html#torch.Tensor)) - Local signal pad to poll.
- **signal** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Value to wait for.
- **peer** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Reserved for future use.

torch.ops.symm_mem.nvshmem_all_to_all(*input: [Tensor](../tensors.html#torch.Tensor)*, *out: [Tensor](../tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [Tensor](../tensors.html#torch.Tensor)

Performs an equal-split all-to-all operation using NVSHMEM. Unlike the
pointer-based collectives, this op is host/stream-initiated and runs over the
NVSHMEM transport, so it works both intra-node and across nodes (e.g. over
RDMA/RoCE) without requiring peer buffers to be directly addressable from the
GPU.

The input is divided into group_size equal-sized chunks; chunk i is sent
to rank i, and the chunk received from rank i is placed at position i in
the output.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric and contiguous. Its number of elements must be divisible by the group size.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric and contiguous, and have the same number of elements and dtype as input.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-to-all on.

torch.ops.symm_mem.all_to_all_vdev(*input: [Tensor](../tensors.html#torch.Tensor)*, *out: [Tensor](../tensors.html#torch.Tensor)*, *in_splits: [Tensor](../tensors.html#torch.Tensor)*, *out_splits_offsets: [Tensor](../tensors.html#torch.Tensor)*, *group_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

Performs an all-to-all-v operation using NVSHMEM, with split information provided on device.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing splits of data to send to each peer. Must be symmetric. Must be of size (group_size,). The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-to-all on.

torch.ops.symm_mem.all_to_all_vdev_2d(*input: Tensor*, *out: Tensor*, *in_splits: Tensor*, *out_splits_offsets: Tensor*, *group_name: str*[, *major_align: int = None*]) → [None](https://docs.python.org/3/builtins/constants.html#None)

Perform a 2D all-to-all-v operation using NVSHMEM, with split information provided on device. In Mixture of Experts models, this operation can be used to dispatch tokens.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing the splits of data to send to each expert. Must be symmetric. Must be of size (group_size * ne,), where ne is the number of experts per rank. The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size * ne). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-to-all on.
- **major_align** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Optional alignment for the major dimension of the output chunk for each expert. If not provided, the alignment is assumed to be 1. Any alignment adjustment will be reflected in the output offsets.

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

torch.ops.symm_mem.all_to_all_vdev_2d_offset(*Tensor input*, *Tensor out*, *Tensor in_splits_offsets*, *Tensor out_splits_offsets*, *str group_name*) → [None](https://docs.python.org/3/builtins/constants.html#None)

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

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Input tensor to perform all-to-all on. Must be symmetric.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)) - Output tensor to store the result of the all-to-all operation. Must be symmetric.
- **in_splits_offsets** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data to send to each expert. Must be symmetric. Must be of size (2, group_size * ne), where ne is the number of experts. The rows are (in order): input splits and input offsets. The splits are in the unit of elements in the 1st dimension.
- **out_splits_offsets** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group_size * ne). The rows are (in order): output splits and output offsets.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the group to perform all-to-all on.

torch.ops.symm_mem.tile_reduce(*in_tile: Tensor*, *out_tile: Tensor*, *root: int*, *group_name: str*[, *reduce_op: str = 'sum'*]) → [None](https://docs.python.org/3/builtins/constants.html#None)

Reduces a 2D tile from all ranks to a specified root rank within a process group.

Parameters:

- **in_tile** ([*Tensor*](../tensors.html#torch.Tensor)) - Input 2D tensor to be reduced. Must be symmetrically allocated.
- **out_tile** ([*Tensor*](../tensors.html#torch.Tensor)) - Output 2D tensor to contain the result of the reduction. Must be symmetric and have the same shape, dtype, and device as in_tile.
- **root** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The rank of the process in the specified group that will receive the reduced result.
- **group_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - The name of the symmetric memory process group to perform the reduction in.
- **reduce_op** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - The reduction operation to perform. Currently, only `"sum"` is supported. Defaults to `"sum"`.

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

torch.ops.symm_mem.multi_root_tile_reduce(*in_tiles: list[Tensor], out_tile: Tensor, roots: list[int], group_name: str, [reduce_op: str = 'sum']*) → [None](https://docs.python.org/3/builtins/constants.html#None)

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