# GdsFile

*class*torch.cuda.gds.GdsFile(*filename*, *flags*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/cuda/gds.py#L102)

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
>>> file.save_storage(src2.untyped_storage(), offset=src1.nbytes)
>>> dest1 = torch.empty(1024, device="cuda")
>>> dest2 = torch.empty(2, 1024, device="cuda")
>>> file.load_storage(dest1.untyped_storage(), offset=0)
>>> file.load_storage(dest2.untyped_storage(), offset=src1.nbytes)
>>> torch.equal(src1, dest1)
True
>>> torch.equal(src2, dest2)
True
```

deregister_handle()[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/cuda/gds.py#L158)

Deregisters file descriptor from the GDS driver.

This is a wrapper around `cuFileHandleDeregister` (CUDA) / `hipFileHandleDeregister` (ROCm).

load_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/cuda/gds.py#L168)

Loads data from the file into the storage.

This is a wrapper around `cuFileRead` (CUDA) / `hipFileRead` (ROCm).
`storage.nbytes()` of data will be loaded from the file at `offset`
into the storage.

Parameters:

- **storage** (*Storage*) - Storage to load data into.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start loading from. (Default: 0)

register_handle()[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/cuda/gds.py#L149)

Registers file descriptor to the GDS driver.

This is a wrapper around `cuFileHandleRegister` (CUDA) / `hipFileHandleRegister` (ROCm).

save_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/cuda/gds.py#L183)

Saves data from the storage into the file.

This is a wrapper around `cuFileWrite` (CUDA) / `hipFileWrite` (ROCm).
All bytes of the storage will be written to the file at `offset`.

Parameters:

- **storage** (*Storage*) - Storage to save data from.
- **offset** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Offset into the file to start saving to. (Default: 0)