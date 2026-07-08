# Generator

*class*torch.Generator

clone_state() → torch.Generator

Clones the current state of the generator and returns a new generator pointing to this cloned state.
This method is beneficial for preserving a particular state of a generator to restore at a later point.

Returns:

A Generator pointing to the newly cloned state.

Return type:

torch.Generator

Example

```
>>> g_cuda = torch.Generator(device='cuda')
>>> cloned_state = g_cuda.clone_state()
```

device

Generator.device -> device

Gets the current device of the generator.

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu.device
device(type='cpu')
```

get_state() → [Tensor](../tensors.html#torch.Tensor)

Returns the Generator state as a `torch.ByteTensor`.

Returns:

A `torch.ByteTensor` which contains all the necessary bits
to restore a Generator to a specific point in time.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu.get_state()
```

graphsafe_get_state() → torch.Generator

Retrieves the current state of the generator in a manner that is safe for graph capture.
This method is crucial for ensuring that the generator's state can be captured in the CUDA graph.

Returns:

A Generator point to the current state of the generator

Return type:

torch.Generator

Example

```
>>> g_cuda = torch.Generator(device='cuda')
>>> current_state = g_cuda.graphsafe_get_state()
```

graphsafe_set_state(*state*) → [None](https://docs.python.org/3/library/constants.html#None)

Sets the state of the generator to the specified state in a manner that is safe for use in graph capture.
This method is crucial for ensuring that the generator's state can be captured in the CUDA graph.

Parameters:

**state** (*torch.Generator*) - A Generator point to the new state for the generator, typically obtained from graphsafe_get_state.

Example

```
>>> g_cuda = torch.Generator(device='cuda')
>>> g_cuda_other = torch.Generator(device='cuda')
>>> current_state = g_cuda_other.graphsafe_get_state()
>>> g_cuda.graphsafe_set_state(current_state)
```

initial_seed() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the initial seed for generating random numbers.

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu.initial_seed()
2147483647
```

manual_seed(*seed*) → Generator

Sets the seed for generating random numbers. Returns a torch.Generator object. Any 32-bit integer is a valid seed.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed. Value must be within the inclusive range
[-0x8000_0000_0000_0000, 0xffff_ffff_ffff_ffff]. Otherwise, a RuntimeError
is raised. Negative inputs are remapped to positive values with the formula
0xffff_ffff_ffff_ffff + seed.

Returns:

An torch.Generator object.

Return type:

Generator

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu.manual_seed(2147483647)
```

seed() → [int](https://docs.python.org/3/library/functions.html#int)

Gets a non-deterministic random number from std::random_device or the current
time and uses it to seed a Generator.

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu.seed()
1516516984916
```

set_state(*new_state*) → void

Sets the Generator state.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state.

Example:

```
>>> g_cpu = torch.Generator()
>>> g_cpu_other = torch.Generator()
>>> g_cpu.set_state(g_cpu_other.get_state())
```