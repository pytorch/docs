# Distributed Checkpoint - torch.distributed.checkpoint

Distributed Checkpoint (DCP) supports loading and saving models from multiple ranks in parallel.
It handles load-time resharding which enables saving in one cluster topology and loading into another.

DCP is different than `torch.save` and `torch.load` in a few significant ways:

- It produces multiple files per checkpoint, with at least one per rank.
- It operates in place, meaning that the model should allocate its data first and DCP uses that storage instead.

The entrypoints to load and save a checkpoint are the following:

## Additional resources:

- [Getting Started with Distributed Checkpoint (DCP)](https://pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)
- [Asynchronous Saving with Distributed Checkpoint (DCP)](https://pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html)
- [TorchTitan Checkpointing Docs](https://github.com/pytorch/torchtitan/blob/main/docs/checkpoint.md)
- [TorchTitan DCP Implementation](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py)

torch.distributed.checkpoint.optimizer.load_sharded_optimizer_state_dict(*model_state_dict*, *optimizer_key*, *storage_reader*, *planner=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/optimizer.py#L218)

Load a state_dict in conjunction with FSDP sharded optimizer state.

This is the current recommended way to checkpoint FSDP.

Examples:

```
>>> import torch.distributed.checkpoint as dist_cp
>>> # Save
>>> model: torch.nn.Model
>>> optim_params = model.parameters()
>>> optim = torch.optim.SGD(optim_params, lr=0.01)
>>> # Save
>>> with FSDP.state_dict_type(model, StateDictType.SHARDED_STATE_DICT):
>>> state_dict = {
>>> "optimizer": FSDP.optim_state_dict(model, optim),
>>> "model": model.state_dict()
>>> }
>>> dist_cp.save_state_dict(
>>> state_dict=optim_state,
>>> storage_writer=dist_cp.FileSystemWriter("checkpoint"),
>>> planner=dist_cp.DefaultSavePlanner(),
>>> )
>>>
>>> # Load
>>> with FSDP.state_dict_type(model_tp, StateDictType.SHARDED_STATE_DICT):
>>> model_state_dict = model_tp.state_dict()
>>> checkpoint = {
>>> "model": model_state_dict
>>> }
>>> dist_cp.load_state_dict(
>>> state_dict=checkpoint,
>>> storage_reader=dist_cp.FileSystemReader(checkpoint_file),
>>> planner=dist_cp.DefaultLoadPlanner(),
>>> )
>>> model.load_state_dict(checkpoint["model_state"])
>>>
>>> optim_state = dist_cp.load_sharded_optimizer_state_dict(
>>> model_state_dict,
>>> optimizer_key="optimizer",
>>> storage_reader=dist_cp.FileSystemReader("checkpoint"),
>>> )
>>>
>>> flattened_osd = FSDP.optim_state_dict_to_load(
>>> model, optim, optim_state["optimizer"]
>>> )
>>>
>>> optim.load_state_dict(flattened_osd)
```

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

torch.distributed.checkpoint.planner_helpers.create_read_items_for_chunk_list(*fqn*, *checkpoint_md*, *local_chunks*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner_helpers.py#L280)

Create a list of `ReadItem` based on the checkpoint and local chunks.

This applies the resharding algorithm and computes the reads needed
to satisfy `local_chunks` with a checkpoint described by `checkpoint_md`.

Parameters:

- **fqn** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The state_dict FQN to pass to `ReadItem`.
- **checkpoint_md** (*TensorStorageMetadata*) - metadata for a given tensor
from a checkpoint.
- **local_chunks** (*List**[**ChunkStorageMetadata**]*) - Local chunks that needs to be
loaded.

Returns:

A list of `ReadItem` that will satisfy all input chunks.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*ReadItem*]

torch.distributed.checkpoint.default_planner.create_default_global_load_plan(*all_plans*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L525)

Create global load plan used by DefaultLoadPlanner.

The default load behavior involved no global coordination and this function
currently doesn't change the local plans.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*LoadPlan*]

torch.distributed.checkpoint.default_planner.create_default_global_save_plan(*all_plans*, *rewrite_index_hints=True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L564)

Create the global plan and metadata used by DefaultSavePlanner.

Metadata is produced by concatenating the metadata of all `WriteItem` from the supplied plans.

The only global planning change is to update index hints in all `MetadataIndex` objects if
`rewrite_index_hints` is True.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*SavePlan*], *Metadata*]

torch.distributed.checkpoint.default_planner.create_default_local_save_plan(*state_dict*, *is_coordinator*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L537)

Create the `SavePlan` used by DefaultSavePlanner.

On non-coordinator ranks, this function ignores tensors and non-tensor objects,
only producing writes for ShardedTensor objects.

On the coordinator rank, produce writes for all values.

Return type:

*SavePlan*

*class*torch.distributed.checkpoint.state_dict_saver.AsyncCheckpointerType(*value*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_saver.py#L52)

Enum for async checkpointer type.

*class*torch.distributed.checkpoint.state_dict_saver.AsyncSaveResponse(*staging_completion*, *upload_completion*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_saver.py#L206)

This class contains futures for staging and upload completion.
It is returned by async_save().
staging_completion is a future that indicates when local copy
of state_dict is complete.
upload_completion is a future that indicates when a checkpoint
completed saving.

torch.distributed.checkpoint.state_dict_saver.save(*state_dict*, ***, *checkpoint_id=None*, *storage_writer=None*, *planner=None*, *process_group=None*, *no_dist=False*, *use_collectives=True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_saver.py#L87)

Save a distributed model in SPMD style.

This function is different from `torch.save()` as it handles
`ShardedTensor` , and `DTensor` by having each rank only save their local shards.

For each `Stateful` object (having both a `state_dict` and a `load_state_dict`),
save will call `state_dict` before serialization.

Warning

There are no guarantees of Backwards Compatibility across PyTorch versions
for saved state_dicts.

Warning

If using the process_group argument, make sure that only its ranks
call save_state_dict and that all data in state_dict belong to it.

Note

When saving checkpoint for FSDP's ShardingStrategy.HYBRID_SHARD, only one of
the shard_group should be calling save_state_dict and the corresponding process
group needs to be passed in.

Note

If no process group is available, this function assumes the intention is to save the

state_dict in the local process.

Parameters:

- **state_dict** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]*) - The state_dict to save.
- **checkpoint_id** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*,**None**]*) - The ID of this checkpoint instance. The meaning of the checkpoint_id
depends on the storage. It can be a path to a folder or to a file.
It can also be a key if the storage is a key-value store.
(Default: `None`)
- **storage_writer** (*Optional**[**StorageWriter**]*) - Instance of StorageWriter used to perform writes. If this is not
specified, DCP will automatically infer the writer based on the
checkpoint_id. If checkpoint_id is also None, an exception will
be raised. (Default: `None`)
- **planner** (*Optional**[**SavePlanner**]*) - Instance of SavePlanner. If this is not specified, the default
planner will be used. (Default: `None`)
- **process_group** (*Optional**[**ProcessGroup**]*) - ProcessGroup to be used for cross-rank synchronization.
(Default: `None`)
- **no_dist** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, this function will assume the intent is to load
a checkpoint on a single rank/process.
(Default: `False`)
- **use_collectives** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `False`, this function will assume the intent is to save
a checkpoint without using cross-rank synchronization.
(Default: `True`)
This configuration is experimental and should be used with caution.
It will change the format of the saved checkpoint and may not be backward compatible.

Returns:

Metadata object for the saved checkpoint.

Return type:

Metadata

Example

```
>>> my_model = MyModule()
```

```
>>> state_dict = {"model": my_model}
```

```
>>> fs_storage_writer = torch.distributed.checkpoint.FileSystemWriter(
... "/checkpoint/1"
... )
>>> torch.distributed.checkpoint.save(
>>> state_dict=state_dict,
>>> storage_writer=fs_storage_writer,
>>> )
```

Note

save_state_dict uses collectives to coordinate writes across ranks.
For NCCL-based process groups, internal tensor representations of
objects must be moved to the GPU device before communication takes place.
In this case, the device used is given by `torch.cuda.current_device()`
and it is the user's responsibility to ensure that this is set so that
each rank has an individual GPU, via `torch.cuda.set_device()`.

torch.distributed.checkpoint.state_dict_saver.async_save(*state_dict*, ***, *checkpoint_id=None*, *storage_writer=None*, *planner=None*, *process_group=None*, *async_checkpointer_type=AsyncCheckpointerType.THREAD*, *async_stager=None*, *no_dist=False*, *use_collectives=True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_saver.py#L220)

Asynchronous version of `save`. This code first de-stages the state_dict on to the
staging storage (defaults to CPU memory), and then calls the save in a separate thread.

Warning

This feature is experimental and subject to change.
If you provide an `async_stager`, call `close()` after the last
checkpoint is saved. Internally created default stagers are closed
automatically.

Parameters:

- **state_dict** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]*) - The state_dict to save.
- **checkpoint_id** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*,**None**]*) - The ID of this checkpoint instance. The meaning of the checkpoint_id
depends on the storage. It can be a path to a folder or to a file.
It can also be a key if the storage is a key-value store.
(Default: `None`)
- **storage_writer** (*Optional**[**StorageWriter**]*) - Instance of StorageWriter used to perform 'stage' and 'save'. If
this is not specified, DCP will automatically infer the writer based on the
checkpoint_id. If checkpoint_id is also None, an exception will
be raised. (Default: `None`)
- **planner** (*Optional**[**SavePlanner**]*) - Instance of SavePlanner. If this is not specified, the default
planner will be used. (Default: `None`)
- **process_group** (*Optional**[**ProcessGroup**]*) - ProcessGroup to be used for cross-rank synchronization.
(Default: `None`)
- **async_checkpointer_type** (*AsyncCheckpointerType*) - whether to do checkpoint in separate thread or process
(Default: `AsyncCheckpointerType.THREAD`)
- **async_stager** (*AsyncStager*) - provides staging implementation. If `storage_writer` implements
`AsyncStager` and `async_stager` is not provided, `storage_writer`
will be used for staging. User-provided stagers remain owned by the
caller and should be closed after the last checkpoint is saved.
- **no_dist** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, this function will assume the intent is to save
a checkpoint on a single rank/process.
(Default: `False`)
- **use_collectives** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If False, Save the checkpoint without rank coordination. (Default: `True`)
This configuration is experimental and should be used with caution.
It will change the format of the saved checkpoint and may not be backward compatible.

Returns:

A future holding the resultant Metadata object from save.

Return type:

[Future](futures.html#torch.futures.Future)

Example

```
>>> my_model = MyModule()
```

```
>>> state_dict = {"model": my_model}
```

```
>>> fs_storage_writer = torch.distributed.checkpoint.FileSystemWriter(
... "/checkpoint/1"
... )
>>> checkpoint_future = torch.distributed.checkpoint.async_save(
>>> state_dict=state_dict,
>>> storage_writer=fs_storage_writer,
>>> )
>>>
>>> # ... do some work ...
>>>
>>> checkpoint_future.result()
```

torch.distributed.checkpoint.state_dict_saver.save_state_dict(*state_dict*, *storage_writer*, *process_group=None*, *coordinator_rank=0*, *no_dist=False*, *planner=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_saver.py#L59)

This method is deprecated. Please switch to 'save'.

Return type:

*Metadata*

torch.distributed.checkpoint.state_dict_loader.load(*state_dict*, ***, *checkpoint_id=None*, *storage_reader=None*, *planner=None*, *process_group=None*, *no_dist=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_loader.py#L58)

Load a checkpoint into a distributed state dict in SPMD style.

Each rank must have the same keys in their `state_dict` provided to this
API. Mismatched keys may result in hangs or errors. If unsure, you can use
the `utils._assert_same_keys` API to check (but may incur communication
costs).

Each rank will try to read the least amount of data necessary
to fulfill the requested state_dict. When loading `ShardedTensor`
or `DTensor` instances, each rank only reads data for their local shards.

For each `Stateful` object (having both a `state_dict` and a `load_state_dict`),
load will first call `state_dict` before attempting deserialization, followed by
`load_state_dict` once the deserialization is complete.
For each non-`Stateful` object, load will deserialize the object, and then replace
it in the `state_dict` with the deserialized object.

Warning

All tensors in `state_dict` must be allocated on their
destination device *prior to* calling this function.

All non-tensor data is loaded using torch.load() and modified in place
on state_dict.

Warning

Users must call load_state_dict on the root module to ensure load
post-processing and non-tensor data properly propagates.

Parameters:

- **state_dict** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]*) - The state_dict to load the checkpoint into.
- **checkpoint_id** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*,**None**]*) - The ID of this checkpoint instance. The meaning of the checkpoint_id
depends on the storage. It can be a path to a folder or to a file.
It can also be a key if the storage is a key-value store.
(Default: `None`)
- **storage_reader** (*Optional**[**StorageReader**]*) - Instance of StorageWriter used to perform reads. If this is not
specified, DCP will automatically infer the reader based on the
checkpoint_id. If checkpoint_id is also None, an exception will
be raised. (Default: `None`)
- **planner** (*Optional**[**LoadPlanner**]*) - Instance of LoadPlanner. If this is not specified, the default
planner will be used. (Default: `None`)
- **process_group** (*Optional**[**ProcessGroup**]*) - ProcessGroup to be used for cross-rank synchronization.
(Default: `None`)
- **no_dist** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, this function will assume the intent is to load
a checkpoint without using cross-rank synchronization. (Default: `False`)

Returns:

None.

Return type:

None

Examples

```
>>> my_model = MyModule()
>>> optimizer = Adagrad(my_model.parameters())
>>> model_state_dict = my_model.state_dict()
>>> fs_storage_reader = torch.distributed.checkpoint.FileSystemReader(
... "/checkpoint/1"
... )
```

```
>>> torch.distributed.checkpoint.load_state_dict(
>>> state_dict=model_state_dict,
>>> storage_reader=fs_storage_reader,
>>> )
```

```
>>> # module.load_state_dict() function might have customized steps
>>> # to flush the state_dict, must call it to
>>> # ensure correct behavior.
>>> my_model.load_state_dict(model_state_dict)
```

Note

load_state_dict uses collectives to coordinate reads across ranks.
For NCCL-based process groups, internal tensor representations of
objects must be moved to the GPU device before communication takes place.
In this case, the device used is given by `torch.cuda.current_device()`
and it is the user's responsibility to ensure that this is set so that each
rank has an individual GPU, via `torch.cuda.set_device()`.

torch.distributed.checkpoint.state_dict_loader.load_state_dict(*state_dict*, *storage_reader*, *process_group=None*, *coordinator_rank=0*, *no_dist=False*, *planner=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict_loader.py#L31)

This method is deprecated. Please switch to 'load'.

The following module is also useful for additional customization of the staging mechanisms used for asynchronous checkpointing (`torch.distributed.checkpoint.async_save`):

*class*torch.distributed.checkpoint.staging.AsyncStager(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L39)

This protocol is meant to provide customization and extensibility for dcp.async_save, allowing users
to customize how data is staged previous to executing the usual dcp.save path in parallel.
The expected order of operations (concretely defined in torch.distributed.state_dict_saver.async_save)
is the following:

1. AsyncStager.stage_data(state_dict):

This call gives the AsyncStager the opportunity to 'stage'
the state_dict. The expectation and purpose of staging in this context is to create a "training-safe"
representation of the state dict, meaning that any updates to module data after staging is complete
should not be reflected in the state dict returned from this method. For example, in the default
case a copy of the entire state dict is created on CPU RAM and returned here, allowing users
to continue training without risking changes to data which is being serialized.
2. dcp.save is called on the state_dict returned from stage in parallel. This call is responsible

for serializing the state_dict and writing it to storage.
3. If AsyncStager.should_synchronize_after_execute is True, this method will be called immediately after

the serialization thread starts and before returning from dcp.async_save. If this is set to False,
the assumption is the user has defined a custom synchronization point for the purpose of further
optimizing save latency in the training loop (for example, by overlapping staging with the
forward/backward pass), and it is the respondsibility of the user to call AsyncStager.synchronize_staging
at the appropriate time.

close()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L99)

Clean up all resources used by the stager.

*property*should_synchronize_after_execute*: [bool](https://docs.python.org/3/library/functions.html#bool)*

Whether to synchronize after executing the stage.

stage(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L77)

Returns a "staged" copy of state_dict. The expectation of the staged copy is that it is
inoculated from any updates incurred after the stage call is complete.

Return type:

*Future*[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

synchronize_staging()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L88)

In the case stage is async in some way, this method should be called to ensure staging
is complete and it is safe to begin modifying the original state_dict

*class*torch.distributed.checkpoint.staging.DefaultStager(*config=StagingOptions(use_pinned_memory=True, use_shared_memory=True, use_async_staging=True, use_non_blocking_copy=True)*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L133)

DefaultStager provides a full-featured staging implementation that combines
multiple optimization techniques for efficient checkpoint preparation.

The staging process works as follows:
1. State dictionary is submitted for staging (sync or async)
2. Tensors are copied from GPU to optimized CPU storage
3. CUDA operations are synchronized if non-blocking copies are used
4. Staged state dictionary is returned or made available via Future

Usage Patterns:

# Synchronous staging
stager = DefaultStager(StagingOptions(use_async_staging=False))
staged_dict = stager.stage(state_dict)
stager.close()

# Asynchronous staging
stager = DefaultStager(StagingOptions(use_async_staging=True))
future = stager.stage(state_dict)
# ... do other work ...
staged_dict = future.result()
stager.close()

Performance Considerations:

- Async staging provides best performance when model computation
can overlap with staging operations
- Pinned memory improves CPU-GPU transfer speeds but uses more memory
- Shared memory allows efficient IPC to checkpoint process
- Non-blocking copies reduce GPU idle time during memory transfers

Thread Safety:

DefaultStager is not thread-safe. Each thread should use its own
instance, or external synchronization should be provided.

close()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L246)

Clean up all resources used by the DefaultStager. Shuts down the ThreadPoolExecutor
used for async staging operations and cleans up the underlying StateDictStager's
cached storages. Should be called when the stager is no longer needed to prevent
resource leaks, especially in long-running applications. After calling close(),
the stager should not be used for further staging operations.

Example Usage:

stager = DefaultStager(StagingOptions(use_async_staging=True))
future = stager.stage(state_dict)
result = future.result()
stager.close() # Clean up all resources

stage(*state_dict*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L196)

This function is responsible for staging staging the state_dict.
See class docstring for more details on staging.
If use_async_staging is True, it will return a Future object that will be
fulfilled when staging is complete.
If use_async_staging is False, it will return the fully staged state_dict.

Parameters:

**state_dict** (*STATE_DICT_TYPE*) - The state_dict to be staged.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)] | *Future*[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]]

synchronize_staging()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L264)

When use_async_staging is True, this method will wait until staging is complete.
If use_async_staging is False, this method is a no-op.

*class*torch.distributed.checkpoint.staging.StagingOptions(*use_pinned_memory=True*, *use_shared_memory=True*, *use_async_staging=True*, *use_non_blocking_copy=True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L105)

Configuration options for checkpoint staging behavior.

Variables:

- **use_pinned_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Enable pinned memory allocation for faster
CPU-GPU transfers. Requires CUDA to be available. Default: True
- **use_shared_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Enable shared memory for multi-process
scenarios. Useful when multiple processes need access to the
same staged data. Default: True
- **use_async_staging** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Enable asynchronous staging using a
background thread pool. Allows overlapping computation with
staging operations. Requires CUDA. Default: True
- **use_non_blocking_copy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Use non-blocking device memory
copies with stream synchronization. Improves performance by
allowing CPU work to continue during GPU transfers. Default: True

Note

CUDA-dependent features will raise exception if CUDA is not available.

*class*torch.distributed.checkpoint.staging.BlockingAsyncStager(*cache_staged_state_dict=False*, *type_check=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L273)

An implementation of AsyncStager which stages the state_dict on CPU RAM and blocks until the copy is complete.
This implementation also provides an option to optimize stage latency using pinned memory.

N.B. synchronize_staging is a no-op in this case.

stage(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L305)

Returns a copy of state_dict on the CPU.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

synchronize_staging()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/staging.py#L319)

No-op function, since staging is blocking.

In addition to the above entrypoints, `Stateful` objects, as described below, provide additional customization during saving/loading

*class*torch.distributed.checkpoint.stateful.Stateful(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/stateful.py#L8)

Stateful protocol for objects that can be checkpointed and restored.

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/stateful.py#L31)

Restore the object's state from the provided state_dict.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) - The state dict to restore from

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/stateful.py#L14)

Objects should return their state_dict representation as a dictionary.
The output of this function will be checkpointed, and later restored in
load_state_dict().

Warning

Because of the inplace nature of restoring a checkpoint, this function
is also called during torch.distributed.checkpoint.load.

Returns:

The objects state dict

Return type:

Dict

This [example](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/examples/fsdp_checkpoint_example.py) shows how to use PyTorch Distributed Checkpoint to save a FSDP model.

The following types define the IO interface used during checkpoint:

*class*torch.distributed.checkpoint.StorageReader[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L168)

Interface used by `load_state_dict` to read from storage.

One StorageReader instance acts as both the coordinator and the follower
in a distributed checkpoint. As part of initialization, each instance
is told its role.

A subclass should expected the following sequence of calls by `load_state_dict`:

1. (all ranks) set checkpoint_id if users pass a valid checkpoint_id.
2. (all ranks) read_metadata()
3. (all ranks) set_up_storage_reader()
4. (all ranks) prepare_local_plan()
5. (coordinator) prepare_global_plan()
6. (all ranks) read_data()

*abstract*prepare_global_plan(*plans*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L242)

Perform centralized planning of storage loading.

This method is only called on the coordinator instance.

While this method can produce a completely different plan, the preferred
way is to store storage specific data in LoadPlan::storage_data.

Parameters:

**plans** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**LoadPlan**]*) - A list of `LoadPlan` instances, one for each rank.

Returns:

A list of transformed `LoadPlan` after storage global planning

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*LoadPlan*]

*abstract*prepare_local_plan(*plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L227)

Perform storage-specific local planning.

While this method can produce a completely different plan, the recommended
way is to store storage specific data in LoadPlan::storage_data.

Parameters:

**plan** (*LoadPlan*) - The local plan from the `LoadPlan` in use.

Returns:

A transformed `LoadPlan` after storage local planning

Return type:

*LoadPlan*

*abstract*read_data(*plan*, *planner*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L259)

Read all items from `plan` using `planner` to resolve the data.

A subclass should call `LoadPlanner::load_bytes` to deserialize a BytesIO
object into the right place.

A subclass should call `LoadPlanner::resolve_tensor` to get access to the
tensors that in should load data into.

It's the StorageLayer responsibility to properly schedule any cross device copies
required.

Parameters:

- **plan** (*LoadPlan*) - The local plan to execute on
- **planner** (*LoadPlanner*) - The planner object to use to resolve items.

Returns:

A future that completes once all reads are finished.

Return type:

[*Future*](futures.html#torch.futures.Future)[None]

*abstract*read_metadata(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L204)

Read the checkpoint metadata.

Returns:

The metadata object associated with the checkpoint being loaded.

Return type:

*Metadata*

*abstract*reset(*checkpoint_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L186)

Calls to indicates a brand new checkpoint read is going to happen.
A checkpoint_id may be present if users set the checkpoint_id for
this checkpoint read. The meaning of the checkpoint_id is
storage-dependent. It can be a path to a folder/file or a key for
a key-value storage.

Parameters:

**checkpoint_id** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*,**None**]*) - The ID of this checkpoint instance. The meaning of the checkpoint_id
depends on the storage. It can be a path to a folder or to a file.
It can also be a key if the storage is more like a key-value store.
(Default: `None`)

*abstract*set_up_storage_reader(*metadata*, *is_coordinator*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L214)

Initialize this instance.

Parameters:

- **metadata** (*Metadata*) - The metadata schema to use.
- **is_coordinator** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this instance is responsible for coordinating
the checkpoint.

*abstract classmethod*validate_checkpoint_id(*checkpoint_id*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L281)

Check if the given checkpoint_id is supported by the storage. This allow
us to enable automatic storage selection.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch.distributed.checkpoint.StorageWriter[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L27)

Interface used by `save_state_dict` to write to storage.

One StorageWriter instance acts as both the coordinator and the follower
in a distributed checkpoint. As part of initialization, each instance
is told its role.

A subclass should expect the following sequence of calls.

1. (all ranks) set checkpoint_id if users pass a valid checkpoint_id.
2. (all ranks) set_up_storage_writer()
3. (all ranks) prepare_local_plan()
4. (coordinator) prepare_global_plan()
5. (all ranks) write_data()
6. (coordinator) finish()

*abstract*finish(*metadata*, *results*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L131)

Write the metadata and marks the current checkpoint as successful.

The actual format/schema used for serializing metadata is an
implementation detail. The only requirement is that it's recoverable
in to the same object graph.

Parameters:

- **metadata** (*Metadata*) - metadata for the new checkpoint
- **results** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**WriteResult**]**]*) - A list of WriteResults from all ranks.

Returns:

None

Return type:

None

*abstract*prepare_global_plan(*plans*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L90)

Perform centralized planning of storage.

This method is only called on the coordinator instance.

While this method can produce a completely different plan, the preferred
way is to store storage specific data in SavePlan::storage_data.

Parameters:

**plans** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**SavePlan**]*) - A list of `SavePlan` instances, one for each rank.

Returns:

A list of transformed `SavePlan` after storage global planning

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*SavePlan*]

*abstract*prepare_local_plan(*plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L75)

Perform storage-specific local planning.

While this method can produce a completely different plan, the recommended
way is to store storage specific data in SavePlan::storage_data.

Parameters:

**plan** (*SavePlan*) - The local plan from the `SavePlanner` in use.

Returns:

A transformed `SavePlan` after storage local planning

Return type:

*SavePlan*

*abstract*reset(*checkpoint_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L45)

Calls to indicates a brand new checkpoint write is going to happen.
A checkpoint_id may be present if users set the checkpoint_id for
this checkpoint write. The meaning of the checkpoint_id is
storage-dependent. It can be a path to a folder/file or a key for
a key-value storage.

Parameters:

**checkpoint_id** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*os.PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*,**None**]*) - The ID of this checkpoint instance. The meaning of the checkpoint_id
depends on the storage. It can be a path to a folder or to a file.
It can also be a key if the storage is a key-value store.
(Default: `None`)

*abstract*set_up_storage_writer(*is_coordinator*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L63)

Initialize this instance.

Parameters:

**is_coordinator** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this instance is responsible for coordinating
the checkpoint.

storage_meta()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L157)

Return the storage-specific metadata. This is used to store additional information
in a checkpoint that can be useful for providing request-level observability. StorageMeta
is passed to the `SavePlanner` during save calls. Returns None by default.

TODO: provide an example

Return type:

*StorageMeta* | None

*abstract classmethod*validate_checkpoint_id(*checkpoint_id*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L148)

Check if the given checkpoint_id is supported by the storage. This allow
us to enable automatic storage selection.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*abstract*write_data(*plan*, *planner*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/storage.py#L107)

Write all items from `plan` using `planner` to resolve the data.

A subclass should call `SavePlanner::resolve_data` on each item
from the plan to get access to the underlying object to write.

Subclasses should lazily call resolve_data as it can allocate memory.
In case of tensors, make following assumptions:

- They might be on any device, including not matching the one on `WriteItem::tensor_data`
- They might be views or not contiguous. Only the projection needs to be saved.

Parameters:

- **plan** (*SavePlan*) - The save plan to execute.
- **planner** (*SavePlanner*) - Planner object to be used to resolve items to data.

Returns:

A future that completes to a list of WriteResult

Return type:

[*Future*](futures.html#torch.futures.Future)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*WriteResult*]]

The following types define the metadata used during checkpoint:

*class*torch.distributed.checkpoint.metadata.StorageMeta(*checkpoint_id: str | os.PathLike | None = None*, *save_id: str | None = None*, *load_id: str | None = None*, *modules: list[str] = <factory>*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/metadata.py#L129)

*class*torch.distributed.checkpoint.metadata.TensorProperties(*dtype=<factory>*, *layout=torch.strided*, *requires_grad=False*, *memory_format=torch.contiguous_format*, *pin_memory=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/metadata.py#L42)

Properties used to create `Tensor`

*class*torch.distributed.checkpoint.metadata.TensorStorageMetadata(*properties: torch.distributed.checkpoint.metadata.TensorProperties*, *size: [torch.Size](size.html#torch.Size)*, *chunks: [list](https://docs.python.org/3/library/stdtypes.html#list)[torch.distributed.checkpoint.metadata.ChunkStorageMetadata]*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/metadata.py#L113)

The following types define the planner interface used during checkpoint:

*class*torch.distributed.checkpoint.LoadPlanner[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L304)

Abstract class defining the protocol used by load_state_dict to plan the load process.

LoadPlanner are stateful objects that can be used to customize the whole load process.

LoadPlanner acts as an access proxy to the state_dict, so any transformation done to it
will be visible to the whole process.

A planner subclass can expect the following sequence of calls during load_state_dict:

1. set_up_planner - called on all ranks.

Signals the start of loading a checkpoint.
2. create_local_plan - called on all ranks.

Process the state_dict and produces a LoadPlan that will be sent for global planning.
3. create_global_plan - called on the coordinator rank only.

Takes the LoadPlan from all ranks and make any global decision.
4. load_bytes - called multiple times on each rank

This is called once per non-tensor value in state_dict.
5. resolve_tensor and commit_tensor - called multiple times on each rank

They are called in pair for each Tensor value in state_dict.

Users are recommended to extend DefaultLoadPlanner instead of this interface directly as
most changes can be expressed by changes in a single method.

There are two usual patterns of extension:

Rewriting state_dict. This is the simplest way to extend the load process as it
doesn't require understanding the intricacies of how LoadPlan works. We need
to keep a reference to the original state_dict as load happens in place so
we need to be able to perform it in place

```
>>> class RenamePlanner(DefaultLoadPlanner):
>>> def set_up_planner(
>>> self,
>>> state_dict: STATE_DICT_TYPE,
>>> metadata: Metadata,
>>> is_coordinator: bool,
>>> ) -> None:
>>> self.original_state_dict = state_dict
>>> state_dict = {"foo_" + k: v for k, v in state_dict.items()}
>>>
>>> if self.flatten_sharded_tensors:
>>> state_dict = _flatten_sharded_tensors(state_dict)
>>>
>>> if self.flatten_state_dict:
>>> state_dict, self.mappings = flatten_state_dict(state_dict)
>>>
>>> self.state_dict = state_dict
>>> self.metadata = metadata
>>> self.is_coordinator = is_coordinator
>>>
>>> def load_bytes(self, read_item, value):
>>> # Remove the "foo_" prefix
>>> self.original_state_dict[read_item.dest_index.fqn[4:]] = torch.load(value, weights_only=False)
```

Modifying resolve_tensor and commit_tensor to handle load time transformation.

```
>>> class MetaModelMaterialize(DefaultSavePlanner):
>>> def resolve_tensor(self, read_item):
>>> tensor = super().resolve_tensor(read_item)
>>> return torch.empty_like(tensor, device="cpu")
>>>
>>> def commit_tensor(self, read_item, tensor):
>>> self.state_dict[read_item.dest_index.fqn] = tensor
```

*abstract*commit_tensor(*read_item*, *tensor*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L440)

Call once the StorageReader finished loading data into `tensor`.

The provided tensor is the same one returned by the call to `resolve_tensor`.
This method is only needed if this LoadPlanner needs to post process `tensor` prior to
copying it back to the one in the state_dict.

The contents of tensor will follow its device synchronization model.

*abstract*create_global_plan(*global_plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L399)

Compute the global load plan and return plans for each rank.

. N.B. This is called on the coordinator rank only

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*LoadPlan*]

*abstract*create_local_plan()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L391)

Create a LoadPlan based on state_dict and metadata provided by set_up_planner.

. N.B. This is called on every rank.

Return type:

*LoadPlan*

*abstract*finish_plan(*central_plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L407)

Accept the plan from coordinator and return final LoadPlan.

Return type:

*LoadPlan*

*abstract*load_bytes(*read_item*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L411)

Load the item described by read_item``and ``value.

This method is expected to modify in-place the underlying state_dict.

The contents of `value` are defined by the SavePlanner used to produce
the checkpoint being loaded.

resolve_bytes(*read_item*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L422)

Return the BytesIO to be used by the StorageReader to load read_item.

The BytesIO should alias with one on the underlying state_dict as StorageReader will replace its contents.

Return type:

*BytesIO*

*abstract*resolve_tensor(*read_item*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L430)

Return the tensor described by `read_item` to be used by the StorageReader to load read_item.

The tensor should alias with one on the underlying state_dict as StorageReader will replace its contents.
If, for any reason, that's not possible, the planner can use the `commit_tensor` method to copy the data
back to the one in state_dict.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*abstract*set_up_planner(*state_dict*, *metadata=None*, *is_coordinator=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L378)

Initialize this instance to load data into `state_dict`.

. N.B. This is called on every rank.

*class*torch.distributed.checkpoint.LoadPlan(*items: [list](https://docs.python.org/3/library/stdtypes.html#list)[torch.distributed.checkpoint.planner.ReadItem]*, *storage_data: Any = None*, *planner_data: Any = None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L114)

*class*torch.distributed.checkpoint.ReadItem(*type: torch.distributed.checkpoint.planner.LoadItemType*, *dest_index: torch.distributed.checkpoint.metadata.MetadataIndex*, *dest_offsets: [torch.Size](size.html#torch.Size)*, *storage_index: torch.distributed.checkpoint.metadata.MetadataIndex*, *storage_offsets: [torch.Size](size.html#torch.Size)*, *lengths: [torch.Size](size.html#torch.Size)*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L85)

*class*torch.distributed.checkpoint.SavePlanner[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L121)

Abstract class defining the protocol used by save_state_dict to plan the save process.

SavePlanners are stateful objects that can be used to customize the whole save process.

SavePlanner acts as an access proxy to the state_dict, so any transformation done to it
will be visible to the whole process.

A planner subclass can expect the following sequence of calls during save_state_dict:

1. set_up_planner - called on all ranks.

Signals the start of a checkpoint save.
2. create_local_plan - called on all ranks.

Process the state_dict and produces a SavePlan that will be sent for global planning.
3. create_global_plan - called on the coordinator rank only.

Takes the SavePlan from all ranks and make any global decision.
4. finish_plan - called on all ranks.

This gives each rank a chance to adjust to global planning decisions.
5. resolve_data - called multiple times on each rank

Lookups a value on the state_dict for the storage layer to write.

Users are recommended to extend DefaultSavePlanner instead of this interface directly as
most changes can be expressed by changes in a single method.

There are 3 usual patterns of extension:

Rewriting state_dict. This is the simplest way to extend the save process as it
doesn't require understanding the intricacies of how SavePlan works:

```
>>> class RenamePlanner(DefaultSavePlanner):
>>> def set_up_planner(
>>> self,
>>> state_dict: STATE_DICT_TYPE,
>>> storage_meta: Optional[StorageMeta],
>>> is_coordinator: bool,
>>> ) -> None:
>>> # prefix all keys with `foo_``
>>> super().set_up_planner({"foo_" + k: v for k, v in state_dict.items()}, storage_meta, is_coordinator)
```

Modifying local plan and lookup in tandem. This is useful when fine control of how data is persisted

```
>>> class FP16Planner(DefaultSavePlanner):
>>> def create_local_plan(self):
>>> plan = super().create_local_plan()
>>> for p in plan:
>>> if p.tensor_data is not None:
>>> p.tensor_data.properties.dtype = torch.float16
>>> return plan
>>>
>>> def resolve_data(self, write_item):
>>> item = super().resolve_data(write_item)
>>> return item if write_item.type == WriteItemType.BYTE_IO else item.to(torch.float16)
```

Using the global planning step to make central decisions that can't be made individually by each rank

```
>>> from itertools import zip_longest
>>> from dataclasses import replace
>>> class DDPLoadBalancingPlanner(DefaultSavePlanner):
>>> # This uses the default local plan behavior of having all non-sharded writes in rank 0
>>> # This sample doesn't handle ShardedTensors
>>> def create_global_plan(self, all_plans):
>>> iters = [iter(all_plans[0].items)] * len(all_plans)
>>> items_per_rank = [
>>> [item for item in items if item is not None]
>>> for items in zip(*zip_longest(*iters), strict=True)
>>> ]
>>> all_plans = [
>>> replace(plan, items=items)
>>> for plan, items in zip(all_plans, items_per_rank, strict=True)
>>> ]
>>> return super().create_global_plan(all_plans)
```

Finally, some planners need to save additional metadata in the checkpoint, this is
accomplished by having each rank contribute their data items in the local plan and
the global planner aggregate them:

```
>>> class SaveExtraDataPlanner(DefaultSavePlanner):
>>> def create_local_plan(self) -> SavePlan:
>>> plan = super().create_local_plan()
>>> return replace(plan, planner_data="per-rank-data")
>>>
>>> def create_global_plan(self, all_plans: List[SavePlan]) -> Tuple[List[SavePlan], Metadata]:
>>> global_plan, metadata = super().create_global_plan(all_plans)
>>> merged_data = [p.planner_data for p in global_plan]
>>> metadata = replace(metadata, planner_data=merged_data)
>>> return global_plan, metadata
```

*abstract*create_global_plan(*all_plans*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L265)

Compute the global checkpoint plan and return the local plan of each rank.

This is called on the coordinator rank only.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*SavePlan*], *Metadata*]

*abstract*create_local_plan()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L254)

Compute the save plan for the current rank.

This will be aggregated and passed to create_global_plan.
Planner specific data can be passed through SavePlan::planner_data.

This is called on all ranks.

Return type:

*SavePlan*

*abstract*finish_plan(*new_plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L275)

Merge the plan created by create_local_plan and the result of create_global_plan.

This is called on all ranks.

Return type:

*SavePlan*

*abstract*resolve_data(*write_item*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L283)

Transform and prepare `write_item` from `state_dict` for storage, ensuring idempotency and thread-safety.

Lookup the object associated with `write_item` in `state_dict` and apply any
transformation (such as serialization) prior to the storage layer consuming it.

Called on each rank multiple times, at least once per WriteItem in the final SavePlan.

This method should be idempotent and thread-save. StorageWriter implementations
are free to call it as frequently as they need.

Any transformation that allocates memory should be lazily done when his method
is called in order to reduce peak memory required by checkpointing.

When returning tensors, they can be on any device or format, they can be views too.
It's the storage layer responsibility to figure out how to save them.

Return type:

[*Tensor*](tensors.html#torch.Tensor) | *BytesIO*

*abstract*set_up_planner(*state_dict*, *storage_meta=None*, *is_coordinator=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L239)

Initialize this planner to save `state_dict`.

Implementations should save those values as they won't be provided later in the save process.

This is called on all ranks.

*class*torch.distributed.checkpoint.SavePlan(*items: [list](https://docs.python.org/3/library/stdtypes.html#list)[torch.distributed.checkpoint.planner.WriteItem]*, *storage_data: Any = None*, *planner_data: Any = None*, *usable: [bool](https://docs.python.org/3/library/functions.html#bool) = True*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L104)

*class*torch.distributed.checkpoint.planner.WriteItem(*index*, *type*, *bytes_io_data=None*, *tensor_data=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L57)

Dataclass which holds information about what needs to be written to storage.

tensor_storage_size()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L70)

Calculates the storage size of the underlying tensor, or None if this is not a tensor write.

Returns:

Optional[int] storage size, in bytes of underlying tensor if any.

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | None

*class*torch.distributed.checkpoint.planner.BytesIOWriteData(*nbytes: [int](https://docs.python.org/3/library/functions.html#int)*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L45)

*class*torch.distributed.checkpoint.planner.TensorWriteData(*chunk: torch.distributed.checkpoint.metadata.ChunkStorageMetadata*, *properties: torch.distributed.checkpoint.metadata.TensorProperties*, *size: [torch.Size](size.html#torch.Size)*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/planner.py#L50)

We provide a filesystem based storage layer:

*class*torch.distributed.checkpoint.filesystem.FileSystemBase[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L485)

*class*torch.distributed.checkpoint.filesystem.FileSystem[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L517)

*class*torch.distributed.checkpoint.filesystem.SerializationFormat(*value*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L92)

An enumeration.

*class*torch.distributed.checkpoint.FileSystemReader(*path*, *_extension_registry=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L845)

*property*checkpoint_id*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike)*

return the checkpoint_id that will be used to load the checkpoint.

*class*torch.distributed.checkpoint.FileSystemWriter(*path*, *single_file_per_rank=True*, *sync_files=True*, *thread_count=1*, *per_thread_copy_ahead=10000000*, *cache_staged_state_dict=False*, *overwrite=True*, *_extensions=None*, *serialization_format=SerializationFormat.TORCH_SAVE*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L973)

Basic implementation of StorageWriter using file IO.

This implementation makes the following assumptions and simplifications:

- The checkpoint path is an empty or non-existing directory.
- File creation is atomic

The checkpoint consist of one file per write request plus
a global .metadata file with the serialized metadata if rank coordination is enabled.
a rank local __{rank}.metadata file with the serialized metadata if rank coordination is NOT enabled.

stage(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/filesystem.py#L1033)

Override of AsyncStager.stage

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *StatefulT* | [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

We also provide other storage layers, including ones to interact with HuggingFace safetensors:

.. autoclass:: torch.distributed.checkpoint.HuggingFaceStorageReader
:members:

.. autoclass:: torch.distributed.checkpoint.HuggingFaceStorageWriter
:members:

.. autoclass:: torch.distributed.checkpoint.QuantizedHuggingFaceStorageReader
:members:

We provide default implementations of `LoadPlanner` and `SavePlanner` that
can handle all of torch.distributed constructs such as FSDP, DDP, ShardedTensor and DistributedTensor.

*class*torch.distributed.checkpoint.DefaultSavePlanner(*flatten_state_dict=True*, *flatten_sharded_tensors=True*, *dedup_replicated_tensors=None*, *dedup_save_to_lowest_rank=False*, *enable_plan_caching=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L71)

lookup_object(*index*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L279)

Extension from the planner interface to make it easy to extend the default planner.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

transform_object(*write_item*, *object*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L283)

Extension from the planner interface to make it easy to extend the default planner.

*class*torch.distributed.checkpoint.DefaultLoadPlanner(*flatten_state_dict=True*, *flatten_sharded_tensors=True*, *allow_partial_load=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L292)

DefaultLoadPlanner that adds multiple features on top of LoadPlanner.

In particular it adds the following:

flatten_state_dict: Handle state_dict with nested dicts
flatten_sharded_tensors: For FSDP in 2D parallel mode
allow_partial_load: If False, will raise a runtime error if a key is present in state_dict, but not in the checkpoint.

lookup_tensor(*index*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L402)

Extension from the planner interface to make it easy to extend the default planner.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

transform_tensor(*read_item*, *tensor*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/default_planner.py#L406)

Extension from the planner interface to make it easy to extend the default planner.

Due to legacy design decisions, the state dictionaries of `FSDP` and `DDP` may have different keys or fully qualified names (e.g., layer1.weight) even when the original unparallelized model is identical. Moreover, `FSDP` offers various types of model state dictionaries, such as full and sharded state dictionaries. Additionally, optimizer state dictionaries employ parameter IDs instead of fully qualified names to identify parameters, potentially causing issues when parallelisms are used (e.g., pipeline parallelism).

To tackle these challenges, we offer a collection of APIs for users to easily manage state_dicts. `get_model_state_dict()` returns a model state dictionary with keys consistent with those returned by the unparallelized model state dictionary. Similarly, `get_optimizer_state_dict()` provides the optimizer state dictionary with keys uniform across all parallelisms applied. To achieve this consistency, `get_optimizer_state_dict()` converts parameter IDs to fully qualified names identical to those found in the unparallelized model state dictionary.

Note that results returned by these APIs can be used directly with the `torch.distributed.checkpoint.save()` and `torch.distributed.checkpoint.load()` methods without requiring any additional conversions.

`set_model_state_dict()` and `set_optimizer_state_dict()` are provided to load the model and optimizer state_dict generated by their respective getter APIs.

Note that `set_optimizer_state_dict()` can only be called before `backward()` or after `step()` is called on optimizers.

Note that this feature is experimental, and API signatures might change in the future.

torch.distributed.checkpoint.state_dict.get_state_dict(*model*, *optimizers*, ***, *submodules=None*, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1271)

Return the model state_dict and optimizers state_dict.

`get_state_dict` can process any module that is parallelized by PyTorch
FSDP/fully_shard, DDP/replicate, tensor_parallel/parallelize_module, and any
combination of these parallelisms. The main functions of `get_state_dict`
are: 1.) returning a model and optimizer state_dict that can be resharded
with a different number of trainers and/or different parallelisms.
2.) hiding the parallelism-specific state_dict APIs. Users don't have to call
these APIs.
3.) sanity checking the result state_dict.

The keys of the result state dictionary are the canonical FQNs (Fully
Qualified Names). A canonical FQN refers to the FQN based on a parameter's
position in an nn.Module hierarchy. More specifically, a canonical FQN to a
parameter is the FQN returned by `module.named_parameters()` or
`module.named_buffers()` when the module is not distributed by any
parallelisms. Since the optimizer internally uses parameter IDs to represent
a parameter, there will be a conversion from the parameter IDs to the
canonical FQNs when calling this API.

`get_state_dict` can also process a module that is not parallelized. In
such a case, `get_state_dict` only performs one function - converting the
optimizer parameter IDs to the canonical FQNs.

Example

```
>>> import torch
>>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
>>> from torch.nn.parallel import DistributedDataParallel as DDP
>>> from torch.distributed.checkpoint.state_dict import get_state_dict
```

```
>>> fsdp_model = FSDP(copy.deepcopy(model))
>>> fsdp_optim = torch.optim.Adam(model.parameters(), lr=1e-3)
>>> ddp_model = DDP(copy.deepcopy(model))
>>> ddp_optim = torch.optim.Adam(model.parameters(), lr=1e-3)
```

```
>>> ddp_state_dict, ddp_optim_state_dict = get_state_dict(ddp_model, ddp_optim)
>>> fsdp_state_dict, fsdp_optim_state_dict = get_state_dict(
... fsdp_model, fsdp_optim
... )
```

```
>>> # if we simply call ddp_model.state_dict() and fsdp_model.state_dict(),
>>> # the asserts will fail.
>>> assert ddp_state_dict == fsdp_state_dict
>>> assert ddp_optim_state == fsdp_optim_state_dict
```

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **optimizers** (*Union**[**None**,*[*Optimizer*](optim.html#torch.optim.Optimizer)*,**Iterable**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*]**]*) - The optimizers that are used to optimize `model`.
- **submodules** (*deprecated*) - Optional[set[nn.Module]]: only return the model parameters
that belong to the submodules.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be returned. See
StateDictOptions for the details.

Returns:

`Tuple` that contain model state_dict and optimizer state_dict.

Return type:

[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)[[*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), ValueType], OptimizerStateType]

torch.distributed.checkpoint.state_dict.get_model_state_dict(*model*, ***, *submodules=None*, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1189)

Return the model state_dict of `model`.

See `get_state_dict` for the detail usage.

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **submodules** (*deprecated*) - Optional[set[nn.Module]]: only return the model parameters
that belong to the submodules.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be returned. See
StateDictOptions for the details.

Returns:

The state_dict for `model`.

Return type:

[*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), ValueType]

torch.distributed.checkpoint.state_dict.get_optimizer_state_dict(*model*, *optimizers*, ***, *submodules=None*, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1226)

Return the combined state_dict for optimizers.

See `get_state_dict` for the detail usage.

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **optimizers** (*Union**[**None**,*[*Optimizer*](optim.html#torch.optim.Optimizer)*,**Iterable**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*]**]*) - The optimizers that are used to optimize `model`.
- **submodules** (*deprecated*) - Optional[set[nn.Module]]: only return the model parameters
that belong to the submodules.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be returned. See
StateDictOptions for the details.

Returns:

The state_dict for `optimizers`.

Return type:

OptimizerStateType

torch.distributed.checkpoint.state_dict.set_state_dict(*model*, *optimizers*, ***, *model_state_dict*, *optim_state_dict*, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1481)

Load the model state_dict and optimizers state_dict.

The counterpart of `get_state_dict` to set the state_dict to the model and
optimizers. The given `model_state_dict` and `optim_state_dict` do not
have to be returned by `get_state_dict` but must meet the following
requirements: 1) all FQNs are canonical FQNs as defined in `get_state_dict`,
2) if a tensor is sharded, it must be either a ShardedTensor or DTensor,
3) optimizer state_dict cannot contain the parameter IDs; the keys should be
the canonical FQNs.

WARN: `set_state_dict` can only be called before `backward()` or after `step()`

is called on the optimizers. Otherwise, the optimizer states won't be initialized
correctly.

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **optimizers** (*Union**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*,**Iterable**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*]**]*) - The optimizers that are used to optimize `model`.
- **model_state_dict** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**ValueType**]*) - (Union[Dict[nn.Module, Dict[str, ValueType]], Dict[str, ValueType]]):
the model state_dict to load. If the key of the `model_state_dict`
is nn.Module, the key is a submodule of `model` and the value should
be the state_dict of the submodule. When loading the state_dict,
the prefix of the submodule will be append to the state_dict.
- **optim_state_dict** (*OptimizerStateType*) - OptimizerStateType:
the optimizer state_dict to load.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be loaded. See
StateDictOptions for the details.

Returns:

- **missing_keys** is a list of str containing the missing keys of the model state_dict.
- **unexpected_keys** is a list of str containing the unexpected keys of the model state_dict.

Return type:

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

torch.distributed.checkpoint.state_dict.set_model_state_dict(*model*, *model_state_dict*, ***, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1399)

Load the model state_dict.

The counterpart of `get_model_state_dict` to set the state_dict to the
model. See `set_state_dict` for the detail usage.

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **model_state_dict** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**ValueType**]*) - (Dict[str, ValueType]):
the model state_dict to load. If the key of the `model_state_dict`
is nn.Module, the key is a submodule of `model` and the value should
be the state_dict of the submodule. When loading the state_dict,
the prefix of the submodule will be append to the state_dict.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be loaded. See
StateDictOptions for the details.

Returns:

- **missing_keys** is a list of str containing the missing keys
- **unexpected_keys** is a list of str containing the unexpected keys

Return type:

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

torch.distributed.checkpoint.state_dict.set_optimizer_state_dict(*model*, *optimizers*, *optim_state_dict*, ***, *options=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L1438)

Load the optimizers state_dict.

The counterpart of `get_optimizer_state_dict` to set the state_dict to the
optimizers. See `set_state_dict` for the detail usage.

WARN: `set_optimizer_state_dict` can only be called before `backward()` or after

`step()` is called on the optimizers. Otherwise, the optimizer states won't be
initialized correctly.

Parameters:

- **model** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the nn.Module to the model.
- **optimizers** (*Union**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*,**Iterable**[*[*Optimizer*](optim.html#torch.optim.Optimizer)*]**]*) - The optimizers that are used to optimize `model`.
- **optim_state_dict** (*OptimizerStateType*) - OptimizerStateType:
the optimizer state_dict to load.
- **options** (*StateDictOptions*) - the options to control how
model state_dict and optimizer state_dict should be loaded. See
StateDictOptions for the details.

Returns:

None

Return type:

None

*class*torch.distributed.checkpoint.state_dict.StateDictOptions(*full_state_dict=False*, *cpu_offload=False*, *ignore_frozen_params=False*, *keep_submodule_prefixes=True*, *strict=True*, *broadcast_from_rank0=False*, *flatten_optimizer_state_dict=False*, *dsd_fqn_modifiers='_fqn_modifiers'*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/state_dict.py#L93)

This dataclass specifies how get_state_dict/set_state_dict will work.

- `full_state_dict`: if this is set to True, all the tensors in the
returned state_dict will be gathered. No ShardedTensor and DTensor
will be in the returned state_dict.
- `cpu_offload`: offload all the tensors to cpu. To prevent CPU OOM, if
`full_state_dict` is also true, then only the rank0 will get the
state_dict and all other ranks will get empty state_dict.
- `ignore_frozen_params`: if the value is True, the returned state_dict
won't contain any frozen parameters - the `requires_grad` is False.
The default value is False.
- `keep_submodule_prefixes` (deprecated): when `submodules` is not None, this option
indicates whether to keep the submodule prefixes from the state_dict keys.
or example, if the submodule is `module.pretrain` and the full FQN of
the parameter is `pretrain.layer1.weight` of the param. When this option
is True, the parameter's key in the returned state_dict will be
`pretrain.layer1.weight`. If the options is False, the key will be
`layer1.weight`.
Note that if `keep_submodule_prefixes` is False, there may be conflicted
FQNs, hence there should be only one submodule in `submodules`.
- `strict`: the `strict` option when `set_state_dict` calls
model.load_state_dict().
- `broadcast_from_rank0`: when the option is True, rank0 should receive a

full state_dict and will broadcast the tensors in the state_dict/
optim_state_dict one by one to other ranks. Other ranks will receive
the tensors and shard according to the local shards in the model and
optimizer. `full_state_dict` must be set to True when using this option.
This option currently only supports DTensor, not the legacy ShardedTensor.

For users which are used to using and sharing models in the `torch.save` format, the following methods are provided which provide offline utilities for converting between formats.

torch.distributed.checkpoint.format_utils.dcp_to_torch_save(*dcp_checkpoint_dir*, *torch_save_path*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L208)

Given a directory containing a DCP checkpoint, this function will convert it into a
Torch save file.

Parameters:

- **dcp_checkpoint_dir** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)) - Directory containing the DCP checkpoint.
- **torch_save_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)) - Filename to store the converted Torch save file.

Warning

To avoid OOM, it's recommended to only run this function on a single rank.

torch.distributed.checkpoint.format_utils.torch_save_to_dcp(*torch_save_path*, *dcp_checkpoint_dir*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L233)

Given the location of a torch save file, converts it into a DCP checkpoint.

Parameters:

- **torch_save_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)) - Filename of the Torch save file.
- **dcp_checkpoint_dir** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)) - Directory to store the DCP checkpoint.

Warning

To avoid OOM, it's recommended to only run this function on a single rank.

The following classes can also be utilized for online loading and resharding of models from the torch.save format.

*class*torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader(*checkpoint_id=None*, *coordinator_rank=0*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L39)

StorageReader for reading a Torch Save file. This reader will read the entire checkpoint
on the coordinator rank, and then broadcast and shard each tensor to all ranks.

. N.B. Intended to be used with DynamicMetaLoadPlanner

Warning

Current implementation only supports loading Tensors.

```
>>> sd = {"mode": model}
>>> dcp.load(
>>> sd,
>>> storage_reader=BroadcastingTorchSaveReader(),
>>> planner=DynamicMetaLoadPlanner(),
>>> checkpoint_id="path_to_model.pt"
>>> )
```

prepare_global_plan(*global_plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L148)

Implementation of the StorageReader method

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*LoadPlan*]

prepare_local_plan(*plan*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L144)

Implementation of the StorageReader method

Return type:

*LoadPlan*

read_data(*plan*, *planner*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L74)

Reads torch save data on the coordinator rank, and broadcast afterwards
this incurrs a communication cost, but avoids having to load
the entire checkpoint on each rank, hopefully preventing OOM issues

Return type:

[*Future*](futures.html#torch.futures.Future)[None]

read_metadata()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L68)

Extends the default StorageReader to support building the metadata file

Return type:

*Metadata*

reset(*checkpoint_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L152)

Implementation of the StorageReader method

set_up_storage_reader(*metadata*, *is_coordinator*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L129)

Implementation of the StorageReader method

*classmethod*validate_checkpoint_id(*checkpoint_id*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L156)

Implementation of the StorageReader method

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch.distributed.checkpoint.format_utils.DynamicMetaLoadPlanner(*flatten_state_dict=True*, *flatten_sharded_tensors=True*, *allow_partial_load=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L162)

Extension of DefaultLoadPlanner, which creates a new Metadata object based on the passed in state dict,
avoiding the need to read metadata from disk. This is useful when reading formats which don't have a
metadata file, like Torch Save files.

. N.B. Intended to be used with BroadcastingTorchSaveReader

Warning

Current implementation only supports loading Tensors.

```
>>> sd = {"mode": model}
>>> dcp.load(
>>> sd,
>>> storage_reader=BroadcastingTorchSaveReader(),
>>> planner=DynamicMetaLoadPlanner(),
>>> checkpoint_id="path_to_model.pt"
>>> )
```

set_up_planner(*state_dict*, *metadata=None*, *is_coordinator=False*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/checkpoint/format_utils.py#L183)

Setups of the planner, extnding default behavior by creating the Metadata object from the state dict

The following experimental interfaces are provided for improved observability in production environments: