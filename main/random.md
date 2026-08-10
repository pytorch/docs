# torch.random

torch.random.fork_rng(*devices=None*, *enabled=True*, *_caller='fork_rng'*, *_devices_kw='devices'*, *device_type=None*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L156)

Forks the RNG, so that when you return, the RNG is reset
to the state that it was previously in.

Parameters:

- **devices** (*iterable**of**Device IDs*) - devices for which to fork
the RNG. CPU RNG state is always forked. By default, `fork_rng()` operates
on all devices, but will emit a warning if your machine has a lot
of devices, since this function will run very slowly in that case.
If you explicitly specify devices, this warning will be suppressed
- **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `False`, the RNG is not forked. This is a convenience
argument for easily disabling the context manager without having
to delete it and unindent your Python code under it.
- **device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - device type str, default is `None`, in which case the type
is taken from [`torch.accelerator.current_accelerator()`](generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator), falling back
to `"cuda"` when the type cannot be determined. As for supported devices,
see details in [accelerator](torch.html#accelerators)

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)

torch.random.get_rng_state()[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L39)

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: `torch.random.fork_rng()`.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

torch.random.initial_seed()[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L144)

Returns the initial seed for generating random numbers as a
Python long.

Note

The returned seed is for the default generator on CPU only.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.random.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L49)

Sets the seed for generating random numbers on all devices. Returns a
torch.Generator object.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed. Value must be within the inclusive range
[-0x8000_0000_0000_0000, 0xffff_ffff_ffff_ffff]. Otherwise, a RuntimeError
is raised. Negative inputs are remapped to positive values with the formula
0xffff_ffff_ffff_ffff + seed.

Return type:
[*Generator*](generated/torch.Generator.html#torch.Generator)

torch.random.seed()[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L89)

Sets the seed for generating random numbers to a non-deterministic
random number on all devices. Returns a 64 bit number used to seed the RNG.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.random.set_rng_state(*new_state*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L27)

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use
[`torch.manual_seed()`](generated/torch.manual_seed.html#torch.manual_seed), which works for both CPU and CUDA.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state

torch.random.thread_safe_generator()[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/random.py#L242)

Returns a thread-safe random number generator for use in DataLoader workers.
This function provides a convenient way for transforms and user code to use
thread-safe random number generation without manually checking worker context.
When called in a DataLoader thread worker, returns the worker's thread-local
[`torch.Generator`](generated/torch.Generator.html#torch.Generator). When called in the main process or process workers,
returns `None` (which causes PyTorch functions to use the default global RNG).
:returns: Thread-local generator in thread workers, None otherwise.
:rtype: Optional[torch.Generator]

Example::

```
>>> from torch.random import thread_safe_generator
>>> generator = thread_safe_generator()
>>> torch.randint(0, 10, (5,), generator=generator)
```

Example with transforms::

```
>>> from torch.random import thread_safe_generator
>>> class MyRandomTransform:
... def __call__(self, img):
... generator = thread_safe_generator()
... offset = torch.randint(0, 10, (2,), generator=generator)
... return img[..., offset[0]:, offset[1]:]
```

Return type:

[*Generator*](generated/torch.Generator.html#torch.Generator) | None