# torch.Storage

In PyTorch, a regular tensor is a multi-dimensional array that is defined by the following components:

- Storage: The actual data of the tensor, stored as a contiguous, one-dimensional array of bytes.
- `dtype`: The data type of the elements in the tensor, such as torch.float32 or torch.int64.
- `shape`: A tuple indicating the size of the tensor in each dimension.
- Stride: The step size needed to move from one element to the next in each dimension.
- Offset: The starting point in the storage from which the tensor data begins. This will usually be 0 for newly
created tensors.

These components together define the structure and data of a tensor, with the storage holding the
actual data and the rest serving as metadata.

## Untyped Storage API

A `torch.UntypedStorage` is a contiguous, one-dimensional array of elements. Its length is equal to the number of
bytes of the tensor. The storage serves as the underlying data container for tensors.
In general, a tensor created in PyTorch using regular constructors such as [`zeros()`](generated/torch.zeros.html#torch.zeros), [`zeros_like()`](generated/torch.zeros_like.html#torch.zeros_like)
or [`new_zeros()`](generated/torch.Tensor.new_zeros.html#torch.Tensor.new_zeros) will produce tensors where there is a one-to-one correspondence between the tensor
storage and the tensor itself.

However, a storage is allowed to be shared by multiple tensors.
For instance, any view of a tensor (obtained through [`view()`](generated/torch.Tensor.view.html#torch.Tensor.view) or some, but not all, kinds of indexing
like integers and slices) will point to the same underlying storage as the original tensor.
When serializing and deserializing tensors that share a common storage, the relationship is preserved, and the tensors
continue to point to the same storage. Interestingly, deserializing multiple tensors that point to a single storage
can be faster than deserializing multiple independent tensors.

A tensor storage can be accessed through the [`untyped_storage()`](generated/torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage) method. This will return an object of
type `torch.UntypedStorage`.
Fortunately, storages have a unique identifier accessed through the `torch.UntypedStorage.data_ptr()` method.
In regular settings, two tensors with the same data storage will have the same storage `data_ptr`.
However, tensors themselves can point to two separate storages, one for its data attribute and another for its grad
attribute. Each will require a `data_ptr()` of its own. In general, there is no guarantee that a
[`torch.Tensor.data_ptr()`](generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr) and `torch.UntypedStorage.data_ptr()` match and this should not be assumed to be true.

Untyped storages are somewhat independent of the tensors that are built on them. Practically, this means that tensors
with different dtypes or shape can point to the same storage.
It also implies that a tensor storage can be changed, as the following example shows:

```
>>> t = torch.ones(3)
>>> s0 = t.untyped_storage()
>>> s0
 0
 0
 128
 63
 0
 0
 128
 63
 0
 0
 128
 63
[torch.storage.UntypedStorage(device=cpu) of size 12]
>>> s1 = s0.clone()
>>> s1.fill_(0)
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
[torch.storage.UntypedStorage(device=cpu) of size 12]
>>> # Fill the tensor with a zeroed storage
>>> t.set_(s1, storage_offset=t.storage_offset(), stride=t.stride(), size=t.size())
tensor([0., 0., 0.])
```

Warning

Please note that directly modifying a tensor's storage as shown in this example is not a recommended practice.
This low-level manipulation is illustrated solely for educational purposes, to demonstrate the relationship between
tensors and their underlying storages. In general, it's more efficient and safer to use standard `torch.Tensor`
methods, such as [`clone()`](generated/torch.Tensor.clone.html#torch.Tensor.clone) and [`fill_()`](generated/torch.Tensor.fill_.html#torch.Tensor.fill_), to achieve the same results.

Other than `data_ptr`, untyped storage also have other attributes such as `filename`
(in case the storage points to a file on disk), `device` or
`is_cuda` for device checks. A storage can also be manipulated in-place or
out-of-place with methods like `copy_`, `fill_` or
`pin_memory`. For more information, check the API
reference below. Keep in mind that modifying storages is a low-level API and comes with risks!
Most of these APIs also exist on the tensor level: if present, they should be prioritized over their storage
counterparts.

## Special cases

We mentioned that a tensor that has a non-None `grad` attribute has actually two pieces of data within it.
In this case, [`untyped_storage()`](generated/torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage) will return the storage of the `data` attribute,
whereas the storage of the gradient can be obtained through `tensor.grad.untyped_storage()`.

```
>>> t = torch.zeros(3, requires_grad=True)
>>> t.sum().backward()
>>> assert list(t.untyped_storage()) == [0] * 12 # the storage of the tensor is just 0s
>>> assert list(t.grad.untyped_storage()) != [0] * 12 # the storage of the gradient isn't
```

There are also special cases where tensors do not have a typical storage, or no storage at all:

- Tensors on `"meta"` device: Tensors on the `"meta"` device are used for shape inference
and do not hold actual data.
- Fake Tensors: Another internal tool used by PyTorch's compiler is
[FakeTensor](https://pytorch.org/docs/stable/torch.compiler_fake_tensor.html) which is based on a similar idea.

Tensor subclasses or tensor-like objects can also display unusual behaviours. In general, we do not
expect many use cases to require operating at the Storage level!

*class*torch.UntypedStorage(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L467)

bfloat16()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L327)

Casts this storage to bfloat16 type.

bool()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L323)

Casts this storage to bool type.

byte()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L319)

Casts this storage to byte type.

byteswap(*dtype*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L419)

Swap bytes in underlying data.

char()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L315)

Casts this storage to char type.

clone()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L253)

Return a copy of this storage.

complex_double()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L331)

Casts this storage to complex double type.

complex_float()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L335)

Casts this storage to complex float type.

copy_()

cpu()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L261)

Return a CPU copy of this storage if it's not already on the CPU.

cuda(*device=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L82)

Returns a copy of this object in CUDA memory.

If this object is already in CUDA memory and on the correct device, then
no copy is performed and the original object is returned.

Parameters:

- **device** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The destination GPU id. Defaults to the current device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host. Otherwise,
the argument has no effect.

Return type:

*_StorageBase* | *TypedStorage*

data_ptr()

device*: [device](tensor_attributes.html#torch.device)*

double()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L291)

Casts this storage to double type.

element_size()

*property*filename*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

Returns the file name associated with this storage.

The file name will be a string if the storage is on CPU and was created via
[`from_file()`](generated/torch.from_file.html#torch.from_file) with `shared` as `True`. This attribute is `None` otherwise.

fill_()

float()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L295)

Casts this storage to float type.

float8_e4m3fn()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L343)

Casts this storage to float8_e4m3fn type

float8_e4m3fnuz()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L351)

Casts this storage to float8_e4m3fnuz type

float8_e5m2()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L339)

Casts this storage to float8_e5m2 type

float8_e5m2fnuz()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L347)

Casts this storage to float8_e5m2fnuz type

*static*from_buffer()

*static*from_file(*filename*, *shared=False*, *nbytes=0*) → Storage

Creates a CPU storage backed by a memory-mapped file.

If `shared` is `True`, then memory is shared between all processes.
All changes are written to the file. If `shared` is `False`, then the changes on
the storage do not affect the file.

`nbytes` is the number of bytes of storage. If `shared` is `False`,
then the file must contain at least `nbytes` bytes. If `shared` is
`True` the file will be created if needed. (Note that for `UntypedStorage`
this argument differs from that of `TypedStorage.from_file`)

Parameters:

- **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - file name to map
- **shared** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the
underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html))
- **nbytes** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of bytes of storage

get_device()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L115)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

half()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L299)

Casts this storage to half type.

hpu(*device=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L97)

Returns a copy of this object in HPU memory.

If this object is already in HPU memory and on the correct device, then
no copy is performed and the original object is returned.

Parameters:

- **device** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The destination HPU id. Defaults to the current device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host. Otherwise,
the argument has no effect.

Return type:

*_StorageBase* | *TypedStorage*

int()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L307)

Casts this storage to int type.

*property*is_cuda

*property*is_hpu

is_pinned(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L355)

Determine whether the CPU storage is already pinned on device.

Parameters:

**device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*torch.device*](tensor_attributes.html#torch.device)) - The device to pin memory on (default: `'cuda'`).
This argument is discouraged and subject to deprecated.

Returns:

A boolean variable.

is_shared()

is_sparse*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

is_sparse_csr*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

long()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L303)

Casts this storage to long type.

mps()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L267)

Return a MPS copy of this storage if it's not already on the MPS.

nbytes()

new()

pin_memory(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L371)

Copy the CPU storage to pinned memory, if it's not already pinned.

Parameters:

**device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*torch.device*](tensor_attributes.html#torch.device)) - The device to pin memory on (default: `'cuda'`).
This argument is discouraged and subject to deprecated.

Returns:

A pinned CPU storage.

resizable()

resize_()

share_memory_(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L490)

Moves the storage to shared memory.

This is a no-op for storages already in shared memory and for CUDA
storages, which do not need to be moved for sharing across processes.
Storages in shared memory cannot be resized.

Note that to mitigate issues like [this](https://github.com/pytorch/pytorch/issues/95606)
it is thread safe to call this function from multiple threads on the same object.
It is NOT thread safe though to call any other function on self without proper
synchronization. Please see [Multiprocessing best practices](notes/multiprocessing.html) for more details.

Note

When all references to a storage in shared memory are deleted, the associated shared memory
object will also be deleted. PyTorch has a special cleanup process to ensure that this happens
even if the current process exits unexpectedly.

It is worth noting the difference between `share_memory_()` and [`from_file()`](generated/torch.from_file.html#torch.from_file) with `shared = True`

1. `share_memory_` uses [shm_open(3)](https://man7.org/linux/man-pages/man3/shm_open.3.html) to create a
POSIX shared memory object while [`from_file()`](generated/torch.from_file.html#torch.from_file) uses
[open(2)](https://man7.org/linux/man-pages/man2/open.2.html) to open the filename passed by the user.
2. Both use an [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html) with `MAP_SHARED`
to map the file/object into the current virtual address space
3. `share_memory_` will call `shm_unlink(3)` on the object after mapping it to make sure the shared memory
object is freed when no process has the object open. `torch.from_file(shared=True)` does not unlink the
file. This file is persistent and will remain until it is deleted by the user.

Returns:

`self`

short()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L311)

Casts this storage to short type.

size()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L74)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

to(***, *device*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L286)

tolist()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L257)

Return a list containing the elements of this storage.

type(*dtype=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L77)

Return type:

*_StorageBase* | *TypedStorage*

untyped()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L416)

## Legacy Typed Storage

Warning

For historical context, PyTorch previously used typed storage classes, which are
now deprecated and should be avoided. The following details this API in case you
should encounter it, although its usage is highly discouraged.
All storage classes except for `torch.UntypedStorage` will be removed
in the future, and `torch.UntypedStorage` will be used in all cases.

`torch.Storage` is an alias for the storage class that corresponds with
the default data type ([`torch.get_default_dtype()`](generated/torch.get_default_dtype.html#torch.get_default_dtype)). For example, if the
default data type is `torch.float`, `torch.Storage` resolves to
`torch.FloatStorage`.

The `torch.<type>Storage` and `torch.cuda.<type>Storage` classes,
like `torch.FloatStorage`, `torch.IntStorage`, etc., are not
actually ever instantiated. Calling their constructors creates
a `torch.TypedStorage` with the appropriate [`torch.dtype`](tensor_attributes.html#torch.dtype) and
[`torch.device`](tensor_attributes.html#torch.device). `torch.<type>Storage` classes have all of the
same class methods that `torch.TypedStorage` has.

A `torch.TypedStorage` is a contiguous, one-dimensional array of
elements of a particular [`torch.dtype`](tensor_attributes.html#torch.dtype). It can be given any
[`torch.dtype`](tensor_attributes.html#torch.dtype), and the internal data will be interpreted appropriately.
`torch.TypedStorage` contains a `torch.UntypedStorage` which
holds the data as an untyped array of bytes.

Every strided [`torch.Tensor`](tensors.html#torch.Tensor) contains a `torch.TypedStorage`,
which stores all of the data that the [`torch.Tensor`](tensors.html#torch.Tensor) views.

*class*torch.TypedStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L675)

bfloat16()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1374)

Casts this storage to bfloat16 type.

bool()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1369)

Casts this storage to bool type.

byte()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1364)

Casts this storage to byte type.

char()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1359)

Casts this storage to char type.

clone()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1152)

Return a copy of this storage.

complex_double()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1379)

Casts this storage to complex double type.

complex_float()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1384)

Casts this storage to complex float type.

copy_(*source*, *non_blocking=None*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1028)

cpu()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1162)

Return a CPU copy of this storage if it's not already on the CPU.

cuda(*device=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1061)

Returns a copy of this object in CUDA memory.

If this object is already in CUDA memory and on the correct device, then
no copy is performed and the original object is returned.

Parameters:

- **device** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The destination GPU id. Defaults to the current device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host. Otherwise,
the argument has no effect.

Return type:

*Self*

data_ptr()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1252)

*property*device

double()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1329)

Casts this storage to double type.

dtype*: [dtype](tensor_attributes.html#torch.dtype)*

element_size()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1104)

*property*filename*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

Returns the file name associated with this storage if the storage was memory mapped from a file.
or `None` if the storage was not created by memory mapping a file.

fill_(*value*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L692)

float()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1334)

Casts this storage to float type.

float8_e4m3fn()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1394)

Casts this storage to float8_e4m3fn type

float8_e4m3fnuz()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1404)

Casts this storage to float8_e4m3fnuz type

float8_e5m2()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1389)

Casts this storage to float8_e5m2 type

float8_e5m2fnuz()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1399)

Casts this storage to float8_e5m2fnuz type

*classmethod*from_buffer(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1279)

*classmethod*from_file(*filename*, *shared=False*, *size=0*) → Storage[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1409)

Creates a CPU storage backed by a memory-mapped file.

If `shared` is `True`, then memory is shared between all processes.
All changes are written to the file. If `shared` is `False`, then the changes on
the storage do not affect the file.

`size` is the number of elements in the storage. If `shared` is `False`,
then the file must contain at least `size * sizeof(Type)` bytes
(`Type` is the type of storage). If `shared` is `True` the file will be created if needed.

Parameters:

- **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - file name to map
- **shared** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the
underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html))
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of elements in the storage

get_device()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1112)

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

half()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1339)

Casts this storage to half type.

hpu(*device=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1074)

Returns a copy of this object in HPU memory.

If this object is already in HPU memory and on the correct device, then
no copy is performed and the original object is returned.

Parameters:

- **device** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The destination HPU id. Defaults to the current device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host. Otherwise,
the argument has no effect.

Return type:

*Self*

int()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1349)

Casts this storage to int type.

*property*is_cuda

*property*is_hpu

is_pinned(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1167)

Determine whether the CPU TypedStorage is already pinned on device.

Parameters:

**device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*torch.device*](tensor_attributes.html#torch.device)) - The device to pin memory on (default: `'cuda'`).
This argument is discouraged and subject to deprecated.

Returns:

A boolean variable.

is_shared()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1454)

is_sparse*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

long()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1344)

Casts this storage to long type.

nbytes()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1036)

pickle_storage_type()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1236)

pin_memory(*device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1180)

Copy the CPU TypedStorage to pinned memory, if it's not already pinned.

Parameters:

**device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*torch.device*](tensor_attributes.html#torch.device)) - The device to pin memory on (default: `'cuda'`).
This argument is discouraged and subject to deprecated.

Returns:

A pinned CPU storage.

resizable()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1260)

resize_(*size*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1264)

share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1195)

See `torch.UntypedStorage.share_memory_()`

short()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1354)

Casts this storage to short type.

size()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1226)

to(***, *device*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1087)

Returns a copy of this object in device memory.

If this object is already on the correct device, then no copy is performed
and the original object is returned.

Parameters:

- **device** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The destination device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host. Otherwise,
the argument has no effect.

Return type:

Self

tolist()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1157)

Return a list containing the elements of this storage.

type(*dtype=None*, *non_blocking=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L1044)

Returns the type if dtype is not provided, else casts this object to
the specified type.

If this is already of the correct type, no copy is performed and the
original object is returned.

Parameters:

- **dtype** ([*type*](https://docs.python.org/3/library/functions.html#type)*or**string*) - The desired type
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, and the source is in pinned memory
and destination is on the GPU or vice versa, the copy is performed
asynchronously with respect to the host. Otherwise, the argument
has no effect.
- ****kwargs** - For compatibility, may contain the key `async` in place of
the `non_blocking` argument. The `async` arg is deprecated.

Return type:

*_StorageBase* | *TypedStorage* | [str](https://docs.python.org/3/library/stdtypes.html#str)

untyped()[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/storage.py#L890)

Return the internal `torch.UntypedStorage`.

*class*torch.DoubleStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1950)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.float64*

*class*torch.FloatStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1961)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.float32*

*class*torch.HalfStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1972)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.float16*

*class*torch.LongStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1983)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.int64*

*class*torch.IntStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1994)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.int32*

*class*torch.ShortStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2005)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.int16*

*class*torch.CharStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2016)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.int8*

*class*torch.ByteStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L1939)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.uint8*

*class*torch.BoolStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2027)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.bool*

*class*torch.BFloat16Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2038)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.bfloat16*

*class*torch.ComplexDoubleStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2049)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.complex128*

*class*torch.ComplexFloatStorage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2060)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.complex64*

*class*torch.QUInt8Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2071)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.quint8*

*class*torch.QInt8Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2082)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.qint8*

*class*torch.QInt32Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2093)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.qint32*

*class*torch.QUInt4x2Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2104)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.quint4x2*

*class*torch.QUInt2x4Storage(**args*, *wrap_storage=None*, *dtype=None*, *device=None*, *_internal=False*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/__init__.py#L2115)

dtype*: [torch.dtype](tensor_attributes.html#torch.dtype)**= torch.quint2x4*