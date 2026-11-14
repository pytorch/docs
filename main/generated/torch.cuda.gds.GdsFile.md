# GdsFile

*class*torch.cuda.gds.GdsFile(*filename*, *flags*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L117)

Wrapper around a file registered with the GPUDirect Storage (GDS) driver.

cuFile (CUDA) and hipFile (ROCm) are file-like interfaces to the GDS API.

See the [cufile docs](https://docs.nvidia.com/gpudirect-storage/api-reference-guide/index.html#cufile-io-api)
and the [hipFile docs](https://rocm.docs.amd.com/projects/hipFile/en/latest/)
for more details, and [hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds) for ROCm specifics.

Parameters:

- **filename** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the file to open.
- **flags** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Flags to pass to `os.open` when opening the file. `os.O_DIRECT` will
be added automatically.

Example:

```
>>> src1 = torch.randn(1024, device="cuda")
>>> src2 = torch.randn(2, 1024, device="cuda")
>>> file = torch.cuda.gds.GdsFile(f, os.O_CREAT | os.O_RDWR)
>>> file.save_storage(src1.untyped_storage(), offset=0)
4096
>>> file.save_storage(src2.untyped_storage(), offset=src1.nbytes)
8192
>>> dest1 = torch.empty(1024, device="cuda")
>>> dest2 = torch.empty(2, 1024, device="cuda")
>>> file.load_storage(dest1.untyped_storage(), offset=0)
4096
>>> file.load_storage(dest2.untyped_storage(), offset=src1.nbytes)
8192
>>> torch.equal(src1, dest1)
True
>>> torch.equal(src2, dest2)
True
```

deregister_handle()[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L183)

Deregisters file descriptor from the GDS driver.

This is a wrapper around `cuFileHandleDeregister` (CUDA) / `hipFileHandleDeregister` (ROCm).
It first blocks until every `load_storage_async()` and
`save_storage_async()` issued through this file has run.

load_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L217)

Loads data from the file into the storage.

This is a wrapper around `cuFileRead` (CUDA) / `hipFileRead` (ROCm).
`storage.nbytes()` of data will be loaded from the file at `offset`
into the storage. On ROCm, a storage larger than `2**31` bytes minus
the page size raises a `RuntimeError` (see [hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds)).

`cuFileRead` is not ordered with respect to any stream, so this first
waits for the work already enqueued on the current stream of
`storage`'s device, then blocks until the load completes. As with a
blocking [`copy_()`](torch.Tensor.copy_.html#torch.Tensor.copy_), the caller must synchronize work on
other streams (see [CUDA streams](../notes/cuda.html#cuda-stream-semantics)), and making a
dedicated stream current avoids waiting on unrelated work. Raises a
`RuntimeError` during CUDA graph capture.

For a load that returns without waiting, use `load_storage_async()`.
It is enqueued on the stream rather than waiting for it on the host,
so it is fully stream ordered.

Parameters:

- **storage** (*Storage*) - Storage to load data into.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start loading from. (Default: 0)

Returns:

The number of bytes read. A value less than `storage.nbytes()`
means the end of the file was reached, and the bytes of the storage
past that count were not written. A short read does not raise.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

load_storage_async(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L251)

Loads data from the file into the storage, ordered on the current stream.

This is a wrapper around `cuFileReadAsync` (CUDA) / `hipFileReadAsync` (ROCm).
`storage.nbytes()` of data will be loaded from the file at `offset`
into the storage. On ROCm, a storage larger than `2**31` bytes minus
the page size raises a `RuntimeError` (see [hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds)).

The load is enqueued on the current stream of `storage`'s device,
and this function returns without waiting for it to run. It runs after
work previously enqueued on that stream, and work enqueued on that
stream afterwards sees the loaded data. As with a kernel launch, other
streams and the host must synchronize with the stream before using the
storage or the file (see [CUDA streams](../notes/cuda.html#cuda-stream-semantics)).
`deregister_handle()`, and therefore deleting this object, waits
for the load to run.

If `storage` was allocated on another stream, keep a reference to it
until that stream has waited for the load (for example with
[`wait_stream()`](torch.cuda.Stream_class.html#torch.cuda.Stream.wait_stream)), or call
[`record_stream()`](torch.Tensor.record_stream.html#torch.Tensor.record_stream) with the current stream on a tensor
that uses it. Otherwise the CUDA caching allocator can give its memory
to a new allocation while the load is still pending.

Note

cuFile's stream APIs do not support CUDA graphs, so this raises a
`RuntimeError` if called during graph capture.

Example:

```
>>> dest = torch.empty(1024, device="cuda")
>>> nbytes = file.load_storage_async(dest.untyped_storage())
>>> torch.cuda.current_stream().synchronize()
>>> assert nbytes.item() == dest.nbytes
```

Parameters:

- **storage** (*Storage*) - Storage to load data into.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start loading from. (Default: 0)

Returns:

A 0-dim `torch.int64` CPU tensor that, once the load has
run, holds the number of bytes read. A negative value means the
read failed. A value less than `storage.nbytes()` means the end
of the file was reached. The value is not meaningful until the
stream has been synchronized. Errors detected before the load is
enqueued raise instead.

Return type:

[Tensor](../tensors.html#torch.Tensor)

register_handle()[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L174)

Registers file descriptor to the GDS driver.

This is a wrapper around `cuFileHandleRegister` (CUDA) / `hipFileHandleRegister` (ROCm).

save_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L308)

Saves data from the storage into the file.

This is a wrapper around `cuFileWrite` (CUDA) / `hipFileWrite` (ROCm).
The bytes of the storage are written to the file at `offset`; check
the returned count to confirm all of them were. On ROCm, a storage
larger than `2**31` bytes minus the page size raises a
`RuntimeError` (see [hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds)).

`cuFileWrite` is not ordered with respect to any stream, so this first
waits for the work already enqueued on the current stream of
`storage`'s device, then blocks until the save completes. As with a
blocking [`copy_()`](torch.Tensor.copy_.html#torch.Tensor.copy_), the caller must synchronize work on
other streams (see [CUDA streams](../notes/cuda.html#cuda-stream-semantics)), and making a
dedicated stream current avoids waiting on unrelated work. Raises a
`RuntimeError` during CUDA graph capture.

For a save that returns without waiting, use `save_storage_async()`.
It is enqueued on the stream rather than waiting for it on the host,
so it is fully stream ordered.

Parameters:

- **storage** (*Storage*) - Storage to save data from.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start saving to. (Default: 0)

Returns:

The number of bytes written. A value less than
`storage.nbytes()` means the bytes of the storage past that count
were not written. A short write does not raise.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

save_storage_async(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/cuda/gds.py#L343)

Saves data from the storage into the file, ordered on the current stream.

This is a wrapper around `cuFileWriteAsync` (CUDA) / `hipFileWriteAsync` (ROCm).
The bytes of the storage are written to the file at `offset`; check
the returned count to confirm all of them were. On ROCm, a storage
larger than `2**31` bytes minus the page size raises a
`RuntimeError` (see [hipFile (GPUDirect Storage)](../notes/hip.html#rocm-gds)).

The save is enqueued on the current stream of `storage`'s device,
and this function returns without waiting for it to run. It runs after
work previously enqueued on that stream, so it writes the data that
work produced. As with a kernel launch, other streams and the host must
synchronize with the stream before modifying the storage or using the
file (see [CUDA streams](../notes/cuda.html#cuda-stream-semantics)). `deregister_handle()`,
and therefore deleting this object, waits for the save to run.

If `storage` was allocated on another stream, keep a reference to it
until that stream has waited for the save (for example with
[`wait_stream()`](torch.cuda.Stream_class.html#torch.cuda.Stream.wait_stream)), or call
[`record_stream()`](torch.Tensor.record_stream.html#torch.Tensor.record_stream) with the current stream on a tensor
that uses it. Otherwise the CUDA caching allocator can give its memory
to a new allocation, and the save can write that allocation's data.

Note

cuFile's stream APIs do not support CUDA graphs, so this raises a
`RuntimeError` if called during graph capture.

Example:

```
>>> src = torch.randn(1024, device="cuda")
>>> # No synchronize needed: the save runs after torch.randn.
>>> nbytes = file.save_storage_async(src.untyped_storage())
>>> torch.cuda.current_stream().synchronize()
>>> assert nbytes.item() == src.nbytes
```

Parameters:

- **storage** (*Storage*) - Storage to save data from.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start saving to. (Default: 0)

Returns:

A 0-dim `torch.int64` CPU tensor that, once the save has
run, holds the number of bytes written. A negative value means the
write failed. The value is not meaningful until the stream has
been synchronized. Errors detected before the save is enqueued
raise instead.

Return type:

[Tensor](../tensors.html#torch.Tensor)