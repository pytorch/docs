# One-sided tensor transports (experimental)

`torch.distributed._transport` moves registered tensor byte ranges between
independently managed workers. It does not require a process group, global rank
assignment, or matching receives.

An endpoint may connect to multiple peers; remote descriptors identify their
peer. Exchange `bind()` bytes and remote memory descriptors through a trusted
application control plane, or connect peers by rank through a trusted Store with
`Transport.connect_rank`. Exchange descriptors only with authorized peers. A write copies from a local view to the remote base; a read
copies from the remote base to a writable local view. Offsets and lengths are bytes;
shape and dtype agreement is the application's responsibility.

Synchronous reads/writes return zero; `async_op=True` returns
[`torch.distributed.Work`](../distributed.html#torch.distributed.Work). Successful completion means the transfer completed,
not that the remote application consumed or acknowledged the data. Asyncio callers
can use `read_async`, `write_async`, or `wait_all`. Registration remains valid
until unregistration or close, and tensors must not be resized or have their storage replaced.

Ordinary reads and writes are not ordered on CUDA streams. The API does not
provide tracing or batching. Views and remote buffers support `slice(offset, length)`
and step-1 `[a:b]` byte ranges. Like Python sequences, `[a:b]` counts negative
bounds from the end and clamps out-of-range ones, while `slice` raises; a
transfer of a clamped view copies fewer bytes. Non-slice keys raise `TypeError`
and steps other than 1 raise `ValueError`. A remote slice does not
restrict the peer's access to the rest of the registration. Descriptor classes define explicit
`serialize()`/`deserialize()` methods.
The built-in backends declare their fields in a versioned JSON envelope; binary
metadata is base64-encoded. Unknown fields, versions, backends, and invalid field
types are rejected. Tensor contents and native handles are never serialized.

torch.distributed._transport.new_transport(*backend*, *device=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_registry.py#L72)

Construct a one-sided transport, optionally restricting tensor devices.

Parameters:

- **backend** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name registered with `register_transport` or an installed
`torch.distributed.transports` entry point.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*|*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*|**None*) - Optional CPU/CUDA device restriction; otherwise infer each tensor's
device at registration.
- ****kwargs** (*Any*) - Options forwarded to the selected backend's constructor.
Backend modules are imported only when selected.

Return type:

Transport

Example:

```
import torch
from torch.distributed._transport import new_transport

backend = "my_backend" # An installed or process-registered backend.

# Both endpoints are shown locally. Across processes, exchange bind()
# results and remote descriptors through your application's control plane.
with (
 new_transport(backend, "cpu") as trainer,
 new_transport(backend, "cpu") as replica,
):
 trainer_url, replica_url = trainer.bind(), replica.bind()
 trainer.connect(replica_url)
 replica.connect(trainer_url)
 weights = torch.arange(8, dtype=torch.float32)
 received = torch.empty_like(weights)
 source = trainer.register_memory(weights)
 target = replica.register_memory(received)
 descriptor = target.to_remote_buffer()
 # Exchange these bytes through the application control plane.
 remote = type(descriptor).deserialize(descriptor.serialize())
 work = trainer.write(source.to_view(), remote, async_op=True)
 work.wait()
 torch.testing.assert_close(received, weights)
 # Coordinate with peers before closing either endpoint.

# Inside an asyncio application, after registration and metadata exchange:
async def push_weights(trainer, source, remote):
 await trainer.write_async(source.to_view(), remote, timeout=30.0)
 # Coordinate with peers before cleanup; cancellation does not cancel DMA.
 await trainer.close_async(timeout=30.0)
```

*class*torch.distributed._transport.Transport(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L134)

Base class for one-sided tensor transports.

`read` and `write` return zero on synchronous success. With
`async_op=True`, they return a [`torch.distributed.Work`](../distributed.html#torch.distributed.Work) whose
`wait` blocks until completion and propagates transfer errors.
`is_completed` includes failed operations. Work futures resolve to an
empty list on success.

`read_async` and `write_async` are asyncio coroutines. Cancellation or
timeout may leave transfers pending. `wait_all` awaits their completion
futures without blocking the event loop.

Operations use byte ranges, not tensor shapes or dtypes. An endpoint may
connect to multiple peers, and remote descriptors identify their peer. No
process group, ranks, or matching receives are needed.
Exchange connection bytes and remote descriptors through a trusted control
plane. Registration is valid until unregistration or close, including after bind/connect.

`timeout` is a nonnegative, finite number of seconds; `None` selects the
backend default. A timeout bounds the caller's wait, not the transfer's
lifetime: it does not cancel DMA. Pending work retains its local buffers.
After a timeout, wait for the Work or successfully close the transport before
reusing buffers. A timed-out close rejects new operations but retains resources
until close is retried successfully.
Independent transfers may overlap; wait before submitting dependent or
overlapping reads/writes. There is no implicit completion ordering.

Never resize, replace storage, or modify buffers while registered/exposed to
a peer. The application must coordinate remote access and notify peers before
unregistering memory or closing; local completion does not establish that a peer has stopped accessing
this endpoint. Descriptors are invalid after unregistration or their owner closes.

`read_stream` and `write_stream` order transfers on the current CUDA
stream: the transfer starts after prior work on the stream, and later work
waits for it to complete. They return after enqueueing, without holding SMs
while the transfer is in flight, and can be captured in CUDA graphs.
Transfer failures terminate the process, since consumers may already be
enqueued. Ordinary `read` and `write` do not interact with CUDA streams.

*abstract*bind(***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L192)

Bind the endpoint and return its opaque connection URL.

Implementations must support repeated calls on an open transport,
returning its current connection bytes; `connect_rank` binds on each
call.

Return type:

[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes)

*abstract*close(***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L483)

Drain outstanding operations and release transport resources.

*async*close_async(***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L487)

Await cleanup when supported by the backend.

Unlike `close`, this must not block the event loop while waiting for
transfers. Blocking prototype backends do not implement this method.

*abstract*connect(*peer_url*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L201)

Connect to a bound peer and return zero on success.

Connecting to additional peers keeps existing connections; reconnecting
with the same connection bytes is a no-op. There is no per-peer
disconnect; `close` releases all peers. Transfers to descriptors naming
an unconnected peer raise `ValueError`.

Peers are addressed by opaque connection bytes; `connect_rank`
exchanges them through a Store by rank.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

connect_rank(*peer_rank*, ***, *store=None*, *rank=None*, *tag*, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L214)

Connect to the peer identified by `peer_rank` through a Store.

Both peers call this with each other's identity. It binds, exchanges
connection bytes through the Store, connects, and returns zero on
success. It blocks until the peer makes the matching call or a timeout
expires.

Parameters:

- **peer_rank** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Nonnegative integer identifying the peer in this Store namespace.
- **store** ([*Store*](../distributed.html#torch.distributed.Store)*|**None*) - Trusted rendezvous Store, such as `torch.distributed.TCPStore`;
defaults to the default process group's Store. No collectives are
performed. `bind()` bytes may describe registered memory, such
as NIXL agent metadata; each peer deletes the peer bytes it reads,
best effort. Per-pair attempt counters persist, as can endpoint
bytes and small markers after timeouts and other failures. The
Store must implement an atomic `compare_set`.
- **rank** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None*) - Local identity; defaults to `torch.distributed.get_rank()`. An
explicit override requires no initialized process group. Identities
need not be contiguous, but must be distinct for the two peers.
- **tag** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Rendezvous namespace; both peers must pass the same tag. Use
a distinct tag for each component connecting the same rank pair.
- **timeout** ([*float*](https://docs.python.org/3/builtins/functions.html#float)*|*[*timedelta*](https://docs.python.org/3/library/datetime.html#datetime.timedelta)*|**None*) - Timeout for each of bind, the Store wait, and connect, in
seconds or as a `timedelta`, from 1 ms to about 24.8 days (Store
waits use 32-bit milliseconds). `None` uses the transport's
default timeout, such as NIXL's constructor `timeout`, which must
then be in this range. Without one, the backend's and the Store's
timeouts apply; with `store=None`, the wait then holds the
default Store's client, shared with the default process group, for
up to the Store's timeout.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Calls are matched in order per rank pair and tag: the Nth call on each
peer connects to the other's Nth call, including calls that failed after
validating their arguments. When connecting to several peers, call in a
consistent order on all ranks, such as ascending peer rank, or from
separate threads if the backend's `bind` and `connect` are
thread-safe, as NIXL's are. Give each thread its own Store client, such
as `store.clone()`: a `TCPStore` client blocks other calls while it
waits, and `store=None` shares the default Store's client. Cyclic
waits time out. A call whose wait fails, such as by timing out, claims
the peer's slot, so the peer's matching call fails too, unless the peer
already published and both proceed. Other failures, such as in
`connect`, do not imply that the peer's call failed.

*abstract*connected()[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L325)

Return whether the endpoint is connected to any peer.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

*abstract*read(*local_buffer*, *remote_buffer*, ***, *async_op=False*, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L363)

Read into a local view; return Work for async_op=True, otherwise zero.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int) | [*Work*](../distributed.html#torch.distributed.Work)

*async*read_async(*local_buffer*, *remote_buffer*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L461)

Read into a local view, yielding to asyncio until the transfer finishes.

read_stream(*local_buffer*, *remote_buffer*, ***, *stream=None*, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L395)

Read into a local view in order on `stream` (default: current).

*abstract*register_memory(*tensor*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L329)

Register a contiguous tensor, including after bind/connect or transfers.

Exchange its remote-buffer descriptor with peers before remote access.

Return type:

*Memory*

*abstract static*supported()[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L187)

Return whether the transport can be used in this process.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

unregister_memory(*memory*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L338)

Unregister memory after coordinating with peers to stop remote access.

Wait for locally submitted transfers using this registration first.
Reused registrations share one lifetime: unregistering any handle
invalidates all aliases, existing views, and exported descriptors.
Register the tensor again and exchange fresh descriptors before reuse.
Repeating unregistration on the same handle is a no-op while open.
Backends without this operation raise `NotImplementedError`.

*abstract*write(*local_buffer*, *remote_buffer*, ***, *async_op=False*, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L352)

Write a local view; return Work for async_op=True, otherwise zero.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int) | [*Work*](../distributed.html#torch.distributed.Work)

*async*write_async(*local_buffer*, *remote_buffer*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L439)

Write a local view, yielding to asyncio until the transfer finishes.

write_stream(*local_buffer*, *remote_buffer*, ***, *stream=None*, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L374)

Write a local view in order on `stream` (default: current).

Returns once enqueued. Backends with native stream support may override this.

*class*torch.distributed._transport.Memory(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L119)

Memory registered with a transport.

*class*torch.distributed._transport.MemoryView(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L51)

A read-only view of registered memory.

slice(*offset=None*, *length=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L57)

Return a view of a byte range of this one.

`offset` is relative to this view and defaults to 0; `length`
defaults to the rest. Raises `ValueError` unless the range lies within
this view.

Return type:

[*Self*](https://docs.python.org/3/library/typing.html#typing.Self)

*class*torch.distributed._transport.MutableMemoryView(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L76)

A view explicitly permitting writes to its registered memory.

*class*torch.distributed._transport.RemoteBuffer(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L84)

A backend-defined wire descriptor, excluding tensor contents/native handles.

Exchange `serialize()` bytes and reconstruct them with the matching backend
descriptor class's `deserialize()`. Decoders validate their schema and
version without executing code or importing classes named by the payload.
Descriptors grant memory access: exchange them only with authorized peers.

slice(*offset=None*, *length=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_api.py#L99)

Return a descriptor for a byte range of this one.

`offset` is relative to this descriptor and defaults to 0; `length`
defaults to the rest. Raises `ValueError` unless the range lies within
this descriptor. The result shares this descriptor's registration and
lifetime, and does not restrict access to the rest of the registration.

Return type:

[*Self*](https://docs.python.org/3/library/typing.html#typing.Self)

*async*torch.distributed._transport.wait_all(*works*, ***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_work.py#L64)

Await Work futures without blocking the asyncio loop.

Timeout and cancellation stop waiting, not transfers. Retain buffers and
wait again (or close the transport) before reusing them. Transfer errors and
iterable errors are reported after draining submitted work, unless this wait
is timed out or cancelled first. Each Work must support `get_future`.
This adapter does not select CUDA streams or establish consumer-stream
ordering; callers must follow their backend's CUDA synchronization contract.

torch.distributed._transport.available_transports()[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_registry.py#L65)

Return registered and discoverable transport names.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), ...]

torch.distributed._transport.register_transport(*name*, *factory*, ***, *replace=False*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/_registry.py#L20)

Register a transport factory for this process.

## CUDA streams

`read_stream` and `write_stream` order a transfer on `stream`, or the
current CUDA stream if `None`. The transfer starts after prior work on the
stream; later work waits for it to complete. Calls return after enqueueing and
no kernel runs while the transfer is in flight.

```
with torch.cuda.stream(stream):
 source.copy_(producer)
 transport.write_stream(source_view, remote_destination)
 transport.read_stream(destination_view, remote_source)
 consume(destination)
```

Stream transfers can be captured with `torch.cuda.graph`; each replay submits
a new transfer. Register buffers and warm up transfers before capture. Captured
buffers stay registered until `close`; replaying after `close` terminates
the process.

```
graph = torch.cuda.CUDAGraph()
with torch.cuda.graph(graph):
 source.copy_(producer)
 transport.write_stream(source_view, remote_destination)
graph.replay()
```

The default implementation awaits `write_async`/`read_async` on a shared
asyncio loop thread and gates the stream with a CUDA stream memory wait. It requires Linux
and GPUDirect RDMA write ordering, and allows 64 outstanding transfers per
stream; captured transfers hold their slot until `close`. Since consumers may
already be enqueued, a failed transfer terminates the process. Backends with
native stream support may override these methods.

## NIXL backend

The initial backend is NIXL, installed separately with `pip install nixl`.
Its default UCX plugin supports CPU and CUDA memory, subject to the installed
NIXL/UCX build and hardware.

Peers are identified by NIXL agent name. Connecting again with the same
`bind()` bytes is a no-op. While NIXL holds a peer, connecting a restarted peer
under the same agent name raises the backend error. A descriptor whose
well-formed metadata names a different connected peer is rejected without
unloading that peer. Malformed metadata naming a connected peer, even in a
descriptor carrying the sender's own `agent_name`, drops that peer's
descriptors: its pending transfers never complete, `connected()` stays True,
and `close` times out with memory still registered. An endpoint serving
several peers must therefore trust every peer's descriptor metadata; checking
`agent_name` does not prevent this. Peer state grows with each connected peer
and is released only by `close`, which waits for pending transfers to all
peers. The transport does not tie a descriptor to the peer that sent it, so
such an endpoint must also authorize each request, for example by assigning
each client an `agent_name` and checking that the request's
`remote_buffer.agent_name` matches.

`unregister_memory(memory)` deregisters a local allocation without closing the
transport. Wait for local transfers first and coordinate with peers to stop remote
access; the backend cannot detect incoming DMA. All handles sharing a registration,
including previously created views, exported descriptors, and their slices, become invalid.
Register again and exchange fresh descriptors before resuming transfers.

NIXL transfers return Work objects that retain their request handles until
completion. `wait_all`, `read_async`, and `write_async` await Work futures.
The NIXL adapter resolves those futures by checking native transfer status.
Each live transfer owns a distinct request handle.
Independent requests may overlap; explicitly wait before issuing dependent or
overlapping reads/writes. Completion ordering is not implicit.

NIXL's default wait timeout is 30 seconds. `timeout` is in seconds; `None`
selects the backend default and zero polls without waiting. `Work.wait` instead
takes a `datetime.timedelta`; its zero default selects the transfer's timeout.
Timeout and asyncio cancellation stop waiting, not DMA. The transport retains
pending requests and buffers, even if the caller drops its Work. Wait again or
successfully close before reusing buffers. Coordinate with peers before closing
exposed memory; close only drains locally submitted operations.

`NIXLTransport.close_async` awaits pending transfers before native cleanup.
A timed-out or cancelled close rejects new work and retains resources; retry
close to finish cleanup. Registrations keep the transport alive even after its last outgoing transfer,
because peers may still access exposed memory. Forgotten registrations may retain
resources indefinitely:
call `unregister_memory` or `close` after coordinating with peers.
Checking `is_completed` also releases completed requests.
For pending NIXL work, `get_future` requires a running asyncio loop; the loop
must remain running to drive that future. Completed work needs no event loop.

Native metadata, registration, request submission, status checks, and cleanup
calls execute synchronously on the calling thread. Their timeouts bound lock
acquisition and transfer completion waits, not execution inside NIXL. Python
cannot interrupt a blocked native call, even when it releases the GIL.

*class*torch.distributed._transport.nixl.NIXLTransport(*device=None*, ***, *plugin='UCX'*, *agent_name=None*, *num_threads=0*, *enable_prog_thread=True*, *capture_telemetry=False*, *backend_options=None*, *timeout=30.0*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/nixl/_transport.py#L41)

One-sided tensor transport backed by a NIXL plugin.

Backend options accepted by `new_transport()` include `plugin="UCX"`,
`agent_name=None`, `num_threads=0`, `enable_prog_thread=True`,
`capture_telemetry=False`, `backend_options=None`, and `timeout=30.0`.
`backend_options` maps plugin parameter names to strings and is forwarded
to NIXL's `create_backend`. NIXL is an optional dependency, imported only
when selected. Transfers require registered views; raw tensors are rejected
rather than allocated or registered implicitly.

*async*close_async(***, *timeout=None*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/distributed/_transport/nixl/_transport.py#L472)

Await outstanding DMA before synchronous native resource cleanup.

Cancellation/timeout retains resources and rejects new submissions.
Retry close after pending work completes. Native cleanup is not
interruptible; peer access must already have been stopped externally.