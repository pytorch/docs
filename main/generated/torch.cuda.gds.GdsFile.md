# GdsFile

*class*torch.cuda.gds.GdsFile(*filename*, *flags*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/gds.py#L86)

Wrapper around cuFile.

cuFile is a file-like interface to the GPUDirect Storage (GDS) API.

See the [cufile docs](https://docs.nvidia.com/gpudirect-storage/api-reference-guide/index.html#cufile-io-api)
for more details.

Parameters:

- **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the file to open.
- **flags** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Flags to pass to `os.open` when opening the file. `os.O_DIRECT` will
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

deregister_handle()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/gds.py#L141)

Deregisters file descriptor from cuFile Driver.

This is a wrapper around `cuFileHandleDeregister`.

load_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/gds.py#L151)

Loads data from the file into the storage.

This is a wrapper around `cuFileRead`. `storage.nbytes()` of data
will be loaded from the file at `offset` into the storage.

Parameters:

- **storage** (*Storage*) - Storage to load data into.
- **offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Offset into the file to start loading from. (Default: 0)

register_handle()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/gds.py#L132)

Registers file descriptor to cuFile Driver.

This is a wrapper around `cuFileHandleRegister`.

save_storage(*storage*, *offset=0*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/gds.py#L165)

Saves data from the storage into the file.

This is a wrapper around `cuFileWrite`. All bytes of the storage
will be written to the file at `offset`.

Parameters:

- **storage** (*Storage*) - Storage to save data from.
- **offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Offset into the file to start saving to. (Default: 0)