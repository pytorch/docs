# Understanding CUDA Memory Usage

To debug CUDA memory use, PyTorch provides a way to generate memory snapshots that record the state of allocated CUDA memory
at any point in time, and optionally record the history of allocation events that led up to that snapshot.

The generated snapshots can then be drag and dropped onto the interactiver viewer hosted at [pytorch.org/memory_viz](https://pytorch.org/memory_viz) which
can be used to explore the snapshot.

Note

The memory profiler and visualizer described in this document only have visibility into the CUDA memory that is
allocated and managed through the PyTorch allocator. Any memory allocated directly from CUDA APIs will not be
visible in the PyTorch memory profiler.

NCCL (used for distributed communication on CUDA devices) is a common example of a library that allocates some
GPU memory that is invisible to the PyTorch memory profiler. See Identifying Non-PyTorch allocations for more info.

## Generating a Snapshot

The common pattern for recording a snapshot is to enable memory history, run the code to be observed, and then save a file with a pickled snapshot:

```
# enable memory history, which will
# add tracebacks and event history to snapshots
torch.cuda.memory._record_memory_history()

run_your_code()
torch.cuda.memory._dump_snapshot("my_snapshot.pickle")
```

## Using the visualizer

Open [https://pytorch.org/memory_viz](https://pytorch.org/memory_viz) and drag/drop the pickled snapshot file into the visualizer.
The visualizer is a javascript application that runs locally on your computer. It does not upload any snapshot data.

## Active Memory Timeline

The Active Memory Timeline shows all the live tensors over time in the snapshot on a particular GPU. Pan/Zoom over the plot to look at smaller allocations.
Mouse over allocated blocks to see a stack trace for when that block was allocated, and details like its address. The detail slider can be adjusted to
render fewer allocations and improve performance when there is a lot of data.

![_images/active_memory_timeline.png](_images/active_memory_timeline.png)

## Allocator State History

The Allocator State History shows individual allocator events in a timeline on the left. Select an event in the timeline to see a visual summary of the
allocator state at that event. This summary shows each individual segment returned from cudaMalloc and how it is split up into blocks of individual allocations
or free space. Mouse over segments and blocks to see the stack trace when the memory was allocated. Mouse over events to see the stack trace when the event occurred,
such as when a tensor was freed. Out of memory errors are reported as OOM events. Looking at the state of memory during an OOM may provide insight into why
an allocation failed even though reserved memory still exists.

![_images/allocator_state_history.png](_images/allocator_state_history.png)

The stack trace information also reports the address at which an allocation occurred.
The address b7f064c000000_0 refers to the (b)lock at address 7f064c000000 which is the "_0"th time this address was allocated.
This unique string can be looked up in the Active Memory Timeline and searched
in the Active State History to examine the memory state when a tensor was allocated or freed.

## Identifying Non-PyTorch allocations

If you suspect CUDA memory is being allocated outside of PyTorch, you can collect the raw CUDA allocation info using
the pynvml package, and compare that to the allocation reported by pytorch.

To collect raw memory usage outside pytorch, use `device_memory_used()`

```
import torch
device_idx = ...
print(torch.cuda.device_memory_used(device_idx))
```

## Snapshot API Reference

torch.cuda.memory._record_memory_history(*enabled='all'*, *context='all'*, *stacks='all'*, *max_entries=9223372036854775807*, *device=None*, *clear_history=False*, *compile_context=False*, *global_record_annotations=False*, *skip_actions=None*)[[source]](https://github.com/pytorch/pytorch/blob/v2.13.0/torch/cuda/memory.py#L892)

Enable recording of stack traces associated with memory
allocations, so you can tell what allocated any piece of memory in
`torch.cuda.memory._snapshot()`.

In addition to keeping stack traces with each current allocation and free,
this will also enable recording of a history of all alloc/free events.

Use `torch.cuda.memory._snapshot()` to retrieve this information,
and the tools in _memory_viz.py to visualize snapshots.

### Buffer behavior

This will store up to max_entries instances of TraceEntry when enabled.
Python trace collection defaults to sys.maxsize, meaning long-running
or indefinitely running jobs should set a reasonable limit to avoid excessive
memory use. Expect each entry to be several KB.

Longer running workflows or those with smaller max_entries values will only
store the last accumulated max_entries entries, meaning new entries overwrite
older entries.

C++ implementation for reference to ring buffer implementation:

```
if (record_history) {
 if (alloc_trace->size() < alloc_trace_max_entries_) {
 alloc_trace->emplace_back(te);
 } else {
 (*alloc_trace)[alloc_trace_next++] = te;
 if (alloc_trace_next == alloc_trace_max_entries_) {
 alloc_trace_next = 0;
 }
 }
}
```

### Latency impact

The Python trace collection is fast (2us per trace), so you may consider
enabling this on production jobs if you anticipate ever having to debug
memory issues.

C++ trace collection is also fast (~50ns/frame), which for many typical programs
works out to ~2us per trace, but can vary depending on stack depth.

param enabled:

None, disable recording memory history.
"state", keep information for currently allocated memory.
"all", additionally keep a history of all alloc/free calls.
Defaults to "all".

type enabled:

Literal[None, "state", "all"], optional

param context:

None, Do not record any tracebacks.
"state", Record tracebacks for currently allocated memory.
"alloc", additionally keep tracebacks for alloc calls.
"all", additionally keep tracebacks for free calls.
Defaults to "all".

type context:

Literal[None, "state", "alloc", "all"], optional

param stacks:

"python", include Python, TorchScript, and inductor frames in tracebacks
"all", additionally include C++ frames
Defaults to "all".

type stacks:

Literal["python", "all"], optional

param max_entries:

Keep a maximum of max_entries
alloc/free events in the recorded history recorded.

type max_entries:

int, optional

param clear_history:

Clear history when enabling, defaults to False.

type clear_history:

bool, optional

param skip_actions:

List of action types to skip when recording
memory history. This can be used to reduce memory overhead by excluding
certain types of events from being recorded. Valid action types are:

- "alloc": Memory allocation events
- "free_requested": Free requests (memory marked for freeing)
- "free_completed": Completed free operations (memory actually freed)
- "segment_alloc": Segment allocation from cudaMalloc
- "segment_free": Segment freed back to CUDA via cudaFree
- "oom": Out-of-memory exceptions
- "snapshot": Memory snapshot generation events

For example, to skip recording free_requested events:
skip_actions=["free_requested"]

Defaults to None (record all actions).

type skip_actions:

list[str], optional

torch.cuda.memory._snapshot(*device=None*, *augment_with_fx_traces=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.13.0/torch/cuda/memory.py#L1027)

Save a snapshot of CUDA memory state at the time it was called.

The state is represented as a dictionary with the following structure.

```
class Snapshot(TypedDict):
 segments: List[Segment]
 device_traces: List[List[TraceEntry]]

class Segment(TypedDict):
 # Segments are memory returned from a cudaMalloc call.
 # The size of reserved memory is the sum of all Segments.
 # Segments are cached and reused for future allocations.
 # If the reuse is smaller than the segment, the segment
 # is split into more then one Block.
 # empty_cache() frees Segments that are entirely inactive.
 address: int
 total_size: int # cudaMalloc'd size of segment
 stream: int
 segment_type: Literal["small", "large"] # 'large' (>1MB)
 segment_pool_id: Tuple[
 int, int
 ] # id of the memory pool owning this segment
 allocated_size: int # size of memory in use
 active_size: int # size of memory in use or in active_awaiting_free state
 blocks: List[Block]

class Block(TypedDict):
 # A piece of memory returned from the allocator, or
 # current cached but inactive.
 size: int
 requested_size: int # size requested during malloc, may be smaller than
 # size due to rounding
 address: int
 state: Literal[
 "active_allocated", # used by a tensor
 "active_awaiting_free", # waiting for another stream to finish using
 # this, then it will become free
 "inactive",
 ] # free for reuse
 frames: List[Frame] # stack trace from where the allocation occurred

class Frame(TypedDict):
 filename: str
 line: int
 name: str
 # Optional FX debug fields (present when augment_with_fx_traces=True
 # and the frame corresponds to FX-generated code)
 fx_node_op: str # FX node operation type (e.g., 'call_function', 'output')
 fx_node_name: str # FX node name (e.g., 'linear', 'relu_1')
 fx_original_trace: str # Original model source code stack trace

class TraceEntry(TypedDict):
 # When `torch.cuda.memory._record_memory_history()` is enabled,
 # the snapshot will contain TraceEntry objects that record each
 # action the allocator took.
 action: Literal[
 "alloc" # memory allocated
 "free_requested", # the allocated received a call to free memory
 "free_completed", # the memory that was requested to be freed is now
 # able to be used in future allocation calls
 "segment_alloc", # the caching allocator ask cudaMalloc for more memory
 # and added it as a segment in its cache
 "segment_free", # the caching allocator called cudaFree to return memory
 # to cuda possibly trying free up memory to
 # allocate more segments or because empty_caches was called
 "oom", # the allocator threw an OOM exception. 'size' is
 # the requested number of bytes that did not succeed
 "snapshot", # the allocator generated a memory snapshot
 # useful to coorelate a previously taken
 # snapshot with this trace
 ]
 addr: int # not present for OOM
 frames: List[Frame]
 size: int
 stream: int
 device_free: int # only present for OOM, the amount of
 # memory cuda still reports to be free
 pool_id: Tuple[int, int] # id of the memory pool for this entry
```

Parameters:

- **device** (*Device*) - Device to capture snapshot for. If None, captures for current device.
- **augment_with_fx_traces** - If True, augment stack trace frames with FX debug information
that maps generated FX code back to original model source code.
This adds fx_node_op, fx_node_name, fx_original_trace, and
fx_node_info fields to Frame objects. Default: False.

Returns:

The Snapshot dictionary object

torch.cuda.memory._dump_snapshot(*filename='dump_snapshot.pickle'*, *augment_with_fx_traces=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.13.0/torch/cuda/memory.py#L1129)

Save a pickled version of the torch.memory._snapshot() dictionary to a file.

This file can be opened by the interactive snapshot viewer at pytorch.org/memory_viz

Snapshot file sizes scale with max_entries and stack trace depth per entry,
with several KB per entry. These can easily be in the GB range for longer running
workflows with large max_entries.

Parameters:

- **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Name of the file to create. Defaults to "dump_snapshot.pickle".
- **augment_with_fx_traces** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, augment the snapshot with FX debug information
before dumping. This maps generated FX code stack traces
back to original model source code. Defaults to False.