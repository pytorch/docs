# Serialization semantics

This note describes how you can save and load PyTorch tensors and module states
in Python, and how to serialize Python modules so they can be loaded in C++.

## Saving and loading tensors

[`torch.save()`](../generated/torch.save.html#torch.save) and [`torch.load()`](../generated/torch.load.html#torch.load) let you easily save and load tensors:

```
>>> t = torch.tensor([1., 2.])
>>> torch.save(t, 'tensor.pt')
>>> torch.load('tensor.pt')
tensor([1., 2.])
```

By convention, PyTorch files are typically written with a '.pt' or '.pth' extension.

[`torch.save()`](../generated/torch.save.html#torch.save) and [`torch.load()`](../generated/torch.load.html#torch.load) use Python's pickle by default,
so you can also save multiple tensors as part of Python objects like tuples,
lists, and dicts:

```
>>> d = {'a': torch.tensor([1., 2.]), 'b': torch.tensor([3., 4.])}
>>> torch.save(d, 'tensor_dict.pt')
>>> torch.load('tensor_dict.pt')
{'a': tensor([1., 2.]), 'b': tensor([3., 4.])}
```

Custom data structures that include PyTorch tensors can also be saved if the
data structure is pickle-able.

## Saving and loading tensors preserves views

Saving tensors preserves their view relationships:

```
>>> numbers = torch.arange(1, 10)
>>> evens = numbers[1::2]
>>> torch.save([numbers, evens], 'tensors.pt')
>>> loaded_numbers, loaded_evens = torch.load('tensors.pt')
>>> loaded_evens *= 2
>>> loaded_numbers
tensor([ 1, 4, 3, 8, 5, 12, 7, 16, 9])
```

Behind the scenes, these tensors share the same "storage." See
[Tensor Views](https://pytorch.org/docs/main/tensor_view.html) for more
on views and storage.

When PyTorch saves tensors it saves their storage objects and tensor
metadata separately. This is an implementation detail that may change in the
future, but it typically saves space and lets PyTorch easily
reconstruct the view relationships between the loaded tensors. In the above
snippet, for example, only a single storage is written to 'tensors.pt'.

In some cases, however, saving the current storage objects may be unnecessary
and create prohibitively large files. In the following snippet a storage much
larger than the saved tensor is written to a file:

```
>>> large = torch.arange(1, 1000)
>>> small = large[0:5]
>>> torch.save(small, 'small.pt')
>>> loaded_small = torch.load('small.pt')
>>> loaded_small.storage().size()
999
```

Instead of saving only the five values in the small tensor to 'small.pt,'
the 999 values in the storage it shares with large were saved and loaded.

When saving tensors with fewer elements than their storage objects, the size of
the saved file can be reduced by first cloning the tensors. Cloning a tensor
produces a new tensor with a new storage object containing only the values
in the tensor:

```
>>> large = torch.arange(1, 1000)
>>> small = large[0:5]
>>> torch.save(small.clone(), 'small.pt') # saves a clone of small
>>> loaded_small = torch.load('small.pt')
>>> loaded_small.storage().size()
5
```

Since the cloned tensors are independent of each other, however, they have
none of the view relationships the original tensors did. If both file size and
view relationships are important when saving tensors smaller than their
storage objects, then care must be taken to construct new tensors that minimize
the size of their storage objects but still have the desired view relationships
before saving.

## Saving and loading torch.nn.Modules

See also: [Tutorial: Saving and loading modules](https://pytorch.org/tutorials/beginner/saving_loading_models.html)

In PyTorch, a module's state is frequently serialized using a 'state dict.'
A module's state dict contains all of its parameters and persistent buffers:

```
>>> bn = torch.nn.BatchNorm1d(3, track_running_stats=True)
>>> list(bn.named_parameters())
[('weight', Parameter containing: tensor([1., 1., 1.], requires_grad=True)),
 ('bias', Parameter containing: tensor([0., 0., 0.], requires_grad=True))]

>>> list(bn.named_buffers())
[('running_mean', tensor([0., 0., 0.])),
 ('running_var', tensor([1., 1., 1.])),
 ('num_batches_tracked', tensor(0))]

>>> bn.state_dict()
OrderedDict([('weight', tensor([1., 1., 1.])),
 ('bias', tensor([0., 0., 0.])),
 ('running_mean', tensor([0., 0., 0.])),
 ('running_var', tensor([1., 1., 1.])),
 ('num_batches_tracked', tensor(0))])
```

Instead of saving a module directly, for compatibility reasons it is recommended
to instead save only its state dict. Python modules even have a function,
[`load_state_dict()`](../generated/torch.nn.Module.html#torch.nn.Module.load_state_dict), to restore their states from a state dict:

```
>>> torch.save(bn.state_dict(), 'bn.pt')
>>> bn_state_dict = torch.load('bn.pt')
>>> new_bn = torch.nn.BatchNorm1d(3, track_running_stats=True)
>>> new_bn.load_state_dict(bn_state_dict)
<All keys matched successfully>
```

Note that the state dict is first loaded from its file with [`torch.load()`](../generated/torch.load.html#torch.load)
and the state then restored with [`load_state_dict()`](../generated/torch.nn.Module.html#torch.nn.Module.load_state_dict).

Even custom modules and modules containing other modules have state dicts and
can use this pattern:

```
# A module with two linear layers
>>> class MyModule(torch.nn.Module):
 def __init__(self):
 super().__init__()
 self.l0 = torch.nn.Linear(4, 2)
 self.l1 = torch.nn.Linear(2, 1)

 def forward(self, input):
 out0 = self.l0(input)
 out0_relu = torch.nn.functional.relu(out0)
 return self.l1(out0_relu)

>>> m = MyModule()
>>> m.state_dict()
OrderedDict([('l0.weight', tensor([[ 0.1400, 0.4563, -0.0271, -0.4406],
 [-0.3289, 0.2827, 0.4588, 0.2031]])),
 ('l0.bias', tensor([ 0.0300, -0.1316])),
 ('l1.weight', tensor([[0.6533, 0.3413]])),
 ('l1.bias', tensor([-0.1112]))])

>>> torch.save(m.state_dict(), 'mymodule.pt')
>>> m_state_dict = torch.load('mymodule.pt')
>>> new_m = MyModule()
>>> new_m.load_state_dict(m_state_dict)
<All keys matched successfully>
```

## Serialized file format for `torch.save`

Since PyTorch 1.6.0, `torch.save` defaults to returning an uncompressed ZIP64
archive unless the user sets `_use_new_zipfile_serialization=False`.

In this archive, the files are ordered as such

```
checkpoint.pth
├── data.pkl
├── byteorder # added in PyTorch 2.1.0
├── data/
│ ├── 0
│ ├── 1
│ ├── 2
│ └── ...
└── version
```

The entries are as follows:

- `data.pkl` is the result of pickling the object passed to `torch.save`
excluding `torch.Storage` objects that it contains
- `byteorder` contains a string with the `sys.byteorder` when saving ("little" or "big")
- `data/` contains all the storages in the object, where each storage is a separate file
- `version` contains a version number at save time that can be used at load time

When saving, PyTorch will ensure that the local file header of each file is padded
to an offset that is a multiple of 64 bytes, ensuring that the offset of each file
is 64-byte aligned.

Note

Tensors on certain devices such as XLA are serialized as pickled numpy arrays. As
such, their storages are not serialized. In these cases `data/` might not exist
in the checkpoint.

## Layout Control

The `mmap` argument in [`torch.load()`](../generated/torch.load.html#torch.load) allows for lazy loading of tensor storages.

In addition, there are some advanced features that allow for more fine-grained
control and manipulation of a `torch.save` checkpoint.

The `torch.serialization.skip_data` context manager enables

- Saving a checkpoint with `torch.save` that includes empty space for data bytes
to be written later.
- Loading a checkpoint with `torch.load` and filling in the data bytes of tensors later.

To inspect tensor metadata in a `torch.save` checkpoint without allocating memory for storage
data, use `torch.load` within the `FakeTensorMode` context manager. On top of skipping loading
storage data similar to `skip_data` above, it additionally tags storages with their offset within
the checkpoint, enabling direct checkpoint manipulation.

```
import torch.nn as nn
from torch._subclasses.fake_tensor import FakeTensorMode

m = nn.Linear(10, 10)
torch.save(m.state_dict(), "checkpoint.pt")

with FakeTensorMode() as mode:
 fake_sd = torch.load("checkpoint.pt")

for k, v in fake_sd.items():
 print(f"key={k}, dtype={v.dtype}, shape={v.shape}, stride={v.stride()}, storage_offset={v.storage_offset()}")
 # offset of the storage in the checkpoint
 print(f"key={k}, checkpoint_offset={v.untyped_storage()._checkpoint_offset}")
```

For more information, [this tutorial](https://docs.pytorch.org/tutorials/prototype/gpu_direct_storage.html)
offers a comprehensive example of using these features to manipulate a checkpoint.

## `torch.load` with `weights_only=True`

Starting in version 2.6, `torch.load` will use `weights_only=True` if the `pickle_module`
argument is not passed.

### weights_only security

As discussed in the documentation for [`torch.load()`](../generated/torch.load.html#torch.load), `weights_only=True` restricts
the unpickler used in `torch.load` to only executing functions/building classes required for
`state_dicts` of plain `torch.Tensors` as well as some other primitive types. Further,
unlike the default `Unpickler` provided by the `pickle` module, the `weights_only` Unpickler
is not allowed to dynamically import anything during unpickling.

`weights_only=True` narrows the surface of remote code execution attacks but has the following limitations:

1. `weights_only=True` does not guard against denial of service attacks.
2. We try to prevent memory corruptions during `torch.load(weights_only=True)` but they might still be possible.

Note that even if memory corruption does not occur during `torch.load` itself, loading CAN create
unexpected objects for the downstream code that can also lead to memory corruption (e.g. a Tensor of
indices and values made to a sparse Tensor in user code might write/read out of bounds).

### weights_only allowlist

As mentioned above, saving a module's `state_dict` is a best practice when using `torch.save`. If loading an old
checkpoint that contains an `nn.Module`, we recommend `weights_only=False`. When loading a checkpoint that contains
tensor subclasses, there will likely be functions/classes that need to be allowlisted, see below for further details.

If the `weights_only` Unpickler encounters a function or class that is not allowlisted
by default within the pickle file, you should see an actionable error like such

```
_pickle.UnpicklingError: Weights only load failed. This file can still be loaded,
to do so you have two options, do those steps only if you trust the source of the checkpoint.
 1. Re-running `torch.load` with `weights_only` set to `False` will likely succeed,
 but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
 2. Alternatively, to load with `weights_only=True` please check the recommended
 steps in the following error message.
 WeightsUnpickler error: Unsupported global: GLOBAL {__module__}.{__name__} was not an allowed global by
 default. Please use `torch.serialization.add_safe_globals([{__name__}])` or the
 `torch.serialization.safe_globals([{__name__}])` context manager to allowlist this global
 if you trust this class/function.
```

Please follow the steps in the error message and allowlist the functions or classes only if you trust them.

To get all GLOBALs (functions/classes) in the checkpoint that are not yet allowlisted you can use
`torch.serialization.get_unsafe_globals_in_checkpoint()` which will return a list of strings of the form
`{__module__}.{__name__}`. If you trust these functions/classes, you can import them and allowlist them per
the error message either via `torch.serialization.add_safe_globals()` or the context manager
`torch.serialization.safe_globals`.

To access the list of user-allowlisted functions/classes you can use `torch.serialization.get_safe_globals()` and
to clear the current list see `torch.serialization.clear_safe_globals()`.

### Troubleshooting `weights_only`

#### Getting unsafe globals

A caveat is that `torch.serialization.get_unsafe_globals_in_checkpoint()` analyzes the checkpoint statically,
some types might be built dynamically during the unpickling process and hence will not be reported by
`torch.serialization.get_unsafe_globals_in_checkpoint()`. One such example is `dtypes` in numpy. In
`numpy < 1.25` after allowlisting all the functions/classes reported by
`torch.serialization.get_unsafe_globals_in_checkpoint()` you might see an error like

```
WeightsUnpickler error: Can only build Tensor, Parameter, OrderedDict or types allowlisted via `add_safe_globals`,
but got <class 'numpy.dtype[float32]'>
```

This can be allowlisted via `{add_}safe_globals([type(np.dtype(np.float32))])`.

In `numpy >=1.25` you would see

```
WeightsUnpickler error: Can only build Tensor, Parameter, OrderedDict or types allowlisted via `add_safe_globals`,
but got <class 'numpy.dtypes.Float32DType'>
```

This can be allowlisted via `{add_}safe_globals([np.dtypes.Float32DType])`.

#### Environment Variables

There are two environment variables that will influence the behavior of `torch.load`. These can be helpful
if one does not have access to the `torch.load` callsites.

- `TORCH_FORCE_WEIGHTS_ONLY_LOAD=1` will override all `torch.load` callsites to use `weights_only=True`.
- `TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD=1` will make `torch.load` callsites use `weights_only=False` **only**
if `weights_only` was not passed as an argument.

## Utility functions

The following utility functions are related to serialization:

torch.serialization.register_package(*priority*, *tagger*, *deserializer*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L444)

Registers callables for tagging and deserializing storage objects with an associated priority.
Tagging associates a device with a storage object at save time while deserializing moves a
storage object to an appropriate device at load time. `tagger` and `deserializer`
are run in the order given by their `priority` until a tagger/deserializer returns a
value that is not None.

To override the deserialization behavior for a device in the global registry, one can register a
tagger with a higher priority than the existing tagger.

This function can also be used to register a tagger and deserializer for new devices.

Parameters:

- **priority** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Indicates the priority associated with the tagger and deserializer, where a lower
value indicates higher priority.
- **tagger** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**Storage**|*[*TypedStorage*](../storage.html#torch.TypedStorage)*|*[*UntypedStorage*](../storage.html#torch.UntypedStorage)*]**,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None**]*) - Callable that takes in a storage object and returns its tagged device as a string
or None.
- **deserializer** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**Storage**|*[*TypedStorage*](../storage.html#torch.TypedStorage)*|*[*UntypedStorage*](../storage.html#torch.UntypedStorage)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**,**Storage**|*[*TypedStorage*](../storage.html#torch.TypedStorage)*|*[*UntypedStorage*](../storage.html#torch.UntypedStorage)*|**None**]*) - Callable that takes in storage object and a device string and returns a storage
object on the appropriate device or None.

Returns:

None

Example

```
>>> def ipu_tag(obj):
>>> if obj.device.type == 'ipu':
>>> return 'ipu'
>>> def ipu_deserialize(obj, location):
>>> if location.startswith('ipu'):
>>> ipu = getattr(torch, "ipu", None)
>>> assert ipu is not None, "IPU device module is not loaded"
>>> assert torch.ipu.is_available(), "ipu is not available"
>>> return obj.ipu(location)
>>> torch.serialization.register_package(11, ipu_tag, ipu_deserialize)
```

torch.serialization.get_crc32_options()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L172)

Get whether [`torch.save()`](../generated/torch.save.html#torch.save) computes and writes crc32 for each record.

Defaults to `True`.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.serialization.set_crc32_options(*compute_crc32*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L183)

Set whether [`torch.save()`](../generated/torch.save.html#torch.save) computes and writes crc32 for each record.

Note

Setting this to `False` may make unzipping of the `torch.save` output
fail or warn due to corrupted CRC32. However `torch.load` will be
able to load the file.

Parameters:

**compute_crc32** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - set crc32 computation flag

torch.serialization.get_default_load_endianness()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L138)

Get fallback byte order for loading files

If byteorder mark is not present in saved checkpoint,
this byte order is used as fallback.
By default, it's "native" byte order.

Returns:

Optional[LoadEndianness]

Return type:

default_load_endian

torch.serialization.set_default_load_endianness(*endianness*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L154)

Set fallback byte order for loading files

If byteorder mark is not present in saved checkpoint,
this byte order is used as fallback.
By default, it's "native" byte order.

Parameters:

**endianness** - the new fallback byte order

torch.serialization.get_default_mmap_options()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L200)

Get default mmap options for [`torch.load()`](../generated/torch.load.html#torch.load) with `mmap=True`.

Defaults to `mmap.MAP_PRIVATE`.

Returns:

int

Return type:

default_mmap_options

torch.serialization.set_default_mmap_options(*flags*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L229)

Context manager or function to set default mmap options for [`torch.load()`](../generated/torch.load.html#torch.load) with `mmap=True` to flags.

For now, only either `mmap.MAP_PRIVATE` or `mmap.MAP_SHARED` are supported.
Please open an issue if you need any other option to be added here.

Note

This feature is currently not supported for Windows.

Parameters:

**flags** ([*int*](https://docs.python.org/3/library/functions.html#int)) - `mmap.MAP_PRIVATE` or `mmap.MAP_SHARED`

torch.serialization.add_safe_globals(*safe_globals*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L282)

Marks the given globals as safe for `weights_only` load. For example, functions
added to this list can be called during unpickling, classes could be instantiated
and have state set.

Each item in the list can either be a function/class or a tuple of the form
(function/class, string) where string is the full path of the function/class.

Within the serialized format, each function is identified with its full
path as `{__module__}.{__qualname__}`. When calling this API, you can provide this
full path that should match the one in the checkpoint otherwise the default
`{fn.__module__}.{fn.__qualname__}` will be used.

Parameters:

**safe_globals** (*List**[**Union**[**Callable**,**Tuple**[**Callable**,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]**]*) - list of globals to mark as safe

Example

```
>>> import tempfile
>>> class MyTensor(torch.Tensor):
... pass
>>> t = MyTensor(torch.randn(2, 3))
>>> with tempfile.NamedTemporaryFile() as f:
... torch.save(t, f.name)
# Running `torch.load(f.name, weights_only=True)` will fail with
# Unsupported global: GLOBAL __main__.MyTensor was not an allowed global by default.
# Check the code and make sure MyTensor is safe to be used when loaded from an arbitrary checkpoint.
... torch.serialization.add_safe_globals([MyTensor])
... torch.load(f.name, weights_only=True)
# MyTensor([[-0.5024, -1.8152, -0.5455],
# [-0.8234, 2.0500, -0.3657]])
```

torch.serialization.clear_safe_globals()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L268)

Clears the list of globals that are safe for `weights_only` load.

torch.serialization.get_safe_globals()[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L275)

Returns the list of user-added globals that are safe for `weights_only` load.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable) | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable), [str](https://docs.python.org/3/library/stdtypes.html#str)]]

torch.serialization.get_unsafe_globals_in_checkpoint(*f*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L343)

Returns a list of strings of functions/classes in a `torch.save` object that are not safe for `weights_only`.

For a given function or class `f`, the corresponding string will be of the form
`{f.__module__}.{f.__name__}`.

This function will return any GLOBALs in the checkpoint that are not in the set marked safe
for `weights_only` (either via `add_safe_globals()` or `safe_globals` context or
allowlisted by `torch` by default).

Note

This function will statically disassemble the pickle file in the checkpoint.
The implication is any classes dynamically pushed onto the stack during unpickling
will not be included in the output.

Parameters:

**f** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|*[*IO*](https://docs.python.org/3/library/typing.html#typing.IO)*[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)*]*) - File-like object or string containing the checkpoint object saved via `torch.save`

Returns:

A list of strings of pickle GLOBALs in the checkpoint that are not allowlisted for `weights_only`.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

*class*torch.serialization.safe_globals(*safe_globals*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L318)

Context-manager that adds certain globals as safe for `weights_only` load.

Parameters:

**safe_globals** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) - List of globals for weights_only load.

Example

```
>>> import tempfile
>>> class MyTensor(torch.Tensor):
... pass
>>> t = MyTensor(torch.randn(2, 3))
>>> with tempfile.NamedTemporaryFile() as f:
... torch.save(t, f.name)
# Running `torch.load(f.name, weights_only=True)` will fail with
# Unsupported global: GLOBAL __main__.MyTensor was not an allowed global by default.
# Check the code and make sure MyTensor is safe to be used when loaded from an arbitrary checkpoint.
... with torch.serialization.safe_globals([MyTensor]):
... torch.load(f.name, weights_only=True)
# MyTensor([[-0.5024, -1.8152, -0.5455],
# [-0.8234, 2.0500, -0.3657]])
>>> assert torch.serialization.get_safe_globals() == []
```

*class*torch.serialization.skip_data(*materialize_fake_tensors=False*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/serialization.py#L385)

Context-manager that skips writing/reading storage bytes for `torch.save` / `torch.load` calls.

For the save path, storages will still be saved, but the space that their bytes would usually be written to
will be empty space. The storage bytes can then be populated in a separate pass.

For the load path, tensors will be loaded per the checkpoint but their storages will not be populated with data.

Warning

The `skip_data` context manager is an early prototype and is subject to change.

Parameters:

**materialize_fake_tensors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to materialize FakeTensors during save. This is a no-op for the load path.

Example

```
>>> import tempfile
>>> t = torch.randn(2, 3)
>>> with tempfile.NamedTemporaryFile() as f:
... with torch.serialization.skip_data():
... torch.save(t, f.name)
... torch.load(f.name, weights_only=True)
tensor([[0., 0., 0.],
 [0., 0., 0.]])
```

## Config

`torch.utils.serialization.config` provides a global config that can control the behavior of
`torch.save` and `torch.load`.

`torch.utils.serialization.config.save` contains options that control the behavior of `torch.save`.

> - `compute_crc32`: whether to compute and write the zip file checksum (Default : `True`).
> See `set_crc32_options()`.
> - `use_pinned_memory_for_d2h`: for storages that are on an accelerator when passed to `torch.save`, whether to
> move storage to pinned memory or pageable memory on CPU within `torch.save`. (Default: `False` (i.e. pageable))
> - `storage_alignment`: alignment of storages in the checkpoint during `torch.save` in bytes. (Default `64`)

`torch.utils.serialization.config.load` contains options that control the behavior of `torch.load`.

> - `mmap`: See the documentation for `mmap` argument in [`torch.load()`](../generated/torch.load.html#torch.load).
> This config will set the behavior of `mmap` for `torch.load` if it is not
> already explicitly passed to the `torch.load` call (Default : `False`).
> - `endianness`: See `set_default_load_endianness()`.
> (Default : `torch.serialization.LoadEndianness.NATIVE`)
> - `mmap_flags`: See `set_default_mmap_options`.
> (Default : `MAP_PRIVATE`)
> - `calculate_storage_offsets`: If this config is set to `True`, offsets for storages will be
> calculated rather than read via random reads when using `torch.load(mmap=True)`. This minimizes
> random reads, which can be helpful when the file is being loaded over a network. (Default : `False`)