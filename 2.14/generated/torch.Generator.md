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

philox_state(*increment*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)]

Reserves `increment` values from this generator's Philox4x32-10 stream and
returns the reserved position as `(seed, offset, intragraph_offset)`, three
1-element `int64` tensors. This is the same reservation protocol the
built-in CUDA random kernels use (`PhiloxCudaState` in C++), so kernels
built on it draw from the same stream as, and compose with, the built-in
random operations. Only Philox-based generators (currently CUDA) support this
method.

**What the reservation grants.** With `effective_offset =
(uint64(offset) + uint64(intragraph_offset)) % 2**64` (both operands
reinterpreted back from int64 to uint64 first; see below), the caller owns
the Philox counter values `effective_offset / 4` through
`effective_offset / 4 + ceil(increment / 4) - 1` (the counter advances once
per 4 generated values), at the fixed `seed`, for **every** subsequence.
Following the built-in kernels' convention of one subsequence per thread
(`curand_init(seed, subsequence, effective_offset, ...)`, where the counter
occupies `counter.x/y` and the subsequence `counter.z/w`), a thread may
generate up to `increment` values rounded up to a multiple of 4. The
generator's offset advances by that rounded amount, so `increment` must be
at least the number of 32-bit values any single thread of the consuming
kernel generates.

**int64 reinterpretation.** Seed and offset are unsigned 64-bit quantities
returned bit-exactly in `int64` tensors (PyTorch tensors have no uint64
arithmetic support); values at or above `2**63` appear negative. Kernels
should reinterpret the bits back to uint64 (e.g. load as int64 and bitcast);
for host-side inspection use `.item() & (2**64 - 1)`. The offset wraps
modulo `2**64` on advancement.

**Graph capture.** The two return modes mirror the C++ `PhiloxCudaState`
protocol. Outside capture (`HostState`), `seed` and `offset` are CPU
tensors holding the current values; `.item()` is cheap and does not
synchronize, so callers pass the values as scalar kernel arguments. During
capture (`DevState`, under [`torch.accelerator.Graph`](torch.accelerator.Graph.html#torch.accelerator.Graph) or
[`torch.cuda.CUDAGraph`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph)), `seed` and `offset` are CUDA tensors
aliasing generator state that each replay refills with the values current at
replay time, so kernels must load them from device memory at run time.
`intragraph_offset` is always a CPU tensor: 0 outside capture, and this
reservation's position within the graph during capture. Callers branch on
capture state (e.g. [`torch.cuda.is_current_stream_capturing()`](torch.cuda.is_current_stream_capturing.html#torch.cuda.is_current_stream_capturing), or the
device of the returned tensors), exactly like the built-in kernels branch on
`PhiloxCudaState` via `at::cuda::philox::unpack`.

Warning

Tensors returned during capture alias the capture's state: their contents
are undefined until the first replay and they must not be used after the
graph is destroyed.

Parameters:

**increment** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of Philox outputs to reserve. Must be
non-negative and at most `2**64 - 1`; the offset it advances
wraps modulo `2**64` (under graph capture, where the intragraph
offset starts at 0, the total reserved within one graph must stay
below `2**64`).

Returns:

`(seed, offset, intragraph_offset)`,
each a 1-element `int64` tensor. `seed` and `offset` hold the
generator's seed and the reserved stream position as uint64 bits (CPU
tensors outside capture, CUDA tensors aliasing generator state during
capture); `intragraph_offset` is always a CPU tensor holding this
reservation's position within the capturing graph (0 outside capture).

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)]

Example

```
>>> g_cuda = torch.Generator(device='cuda')
>>> seed, offset, intragraph = g_cuda.philox_state(4)
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