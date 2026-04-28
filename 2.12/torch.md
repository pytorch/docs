# torch

The torch package contains data structures for multi-dimensional
tensors and defines mathematical operations over these tensors.
Additionally, it provides many utilities for efficient serialization of
Tensors and arbitrary types, and other useful utilities.

It has a CUDA counterpart, that enables you to run your tensor computations
on an NVIDIA GPU with compute capability >= 3.0.

## Tensors

| [`is_tensor`](generated/torch.is_tensor.html#torch.is_tensor) | Returns True if obj is a PyTorch tensor. |
| --- | --- |
| [`is_storage`](generated/torch.is_storage.html#torch.is_storage) | Returns True if obj is a PyTorch storage object. |
| [`is_complex`](generated/torch.is_complex.html#torch.is_complex) | Returns True if the data type of `input` is a complex data type i.e., one of `torch.complex64`, and `torch.complex128`. |
| [`is_conj`](generated/torch.is_conj.html#torch.is_conj) | Returns True if the `input` is a conjugated tensor, i.e. its conjugate bit is set to True. |
| [`is_floating_point`](generated/torch.is_floating_point.html#torch.is_floating_point) | Returns True if the data type of `input` is a floating point data type i.e., one of `torch.float64`, `torch.float32`, `torch.float16`, and `torch.bfloat16`. |
| [`is_nonzero`](generated/torch.is_nonzero.html#torch.is_nonzero) | Returns True if the `input` is a single element tensor which is not equal to zero after type conversions. |
| [`set_default_dtype`](generated/torch.set_default_dtype.html#torch.set_default_dtype) | Sets the default floating point dtype to `d`. |
| [`get_default_dtype`](generated/torch.get_default_dtype.html#torch.get_default_dtype) | Get the current default floating point [`torch.dtype`](tensor_attributes.html#torch.dtype). |
| [`set_default_device`](generated/torch.set_default_device.html#torch.set_default_device) | Sets the default `torch.Tensor` to be allocated on `device`. |
| [`get_default_device`](generated/torch.get_default_device.html#torch.get_default_device) | Gets the default `torch.Tensor` to be allocated on `device` |
| [`set_default_tensor_type`](generated/torch.set_default_tensor_type.html#torch.set_default_tensor_type) | |
| [`numel`](generated/torch.numel.html#torch.numel) | Returns the total number of elements in the `input` tensor. |
| [`set_printoptions`](generated/torch.set_printoptions.html#torch.set_printoptions) | Set options for printing. |
| [`set_flush_denormal`](generated/torch.set_flush_denormal.html#torch.set_flush_denormal) | Disables denormal floating numbers on CPU. |

### Creation Ops

Note

Random sampling creation ops are listed under Random sampling and
include:
[`torch.rand()`](generated/torch.rand.html#torch.rand)
[`torch.rand_like()`](generated/torch.rand_like.html#torch.rand_like)
[`torch.randn()`](generated/torch.randn.html#torch.randn)
[`torch.randn_like()`](generated/torch.randn_like.html#torch.randn_like)
[`torch.randint()`](generated/torch.randint.html#torch.randint)
[`torch.randint_like()`](generated/torch.randint_like.html#torch.randint_like)
[`torch.randperm()`](generated/torch.randperm.html#torch.randperm)
You may also use [`torch.empty()`](generated/torch.empty.html#torch.empty) with the In-place random sampling
methods to create [`torch.Tensor`](tensors.html#torch.Tensor) s with values sampled from a broader
range of distributions.

| [`tensor`](generated/torch.tensor.html#torch.tensor) | Constructs a tensor with no autograd history (also known as a "leaf tensor", see [Autograd mechanics](notes/autograd.html)) by copying `data`. |
| --- | --- |
| [`sparse_coo_tensor`](generated/torch.sparse_coo_tensor.html#torch.sparse_coo_tensor) | Constructs a [sparse tensor in COO(rdinate) format](sparse.html#sparse-coo-docs) with specified values at the given `indices`. |
| [`sparse_csr_tensor`](generated/torch.sparse_csr_tensor.html#torch.sparse_csr_tensor) | Constructs a [sparse tensor in CSR (Compressed Sparse Row)](sparse.html#sparse-csr-docs) with specified values at the given `crow_indices` and `col_indices`. |
| [`sparse_csc_tensor`](generated/torch.sparse_csc_tensor.html#torch.sparse_csc_tensor) | Constructs a [sparse tensor in CSC (Compressed Sparse Column)](sparse.html#sparse-csc-docs) with specified values at the given `ccol_indices` and `row_indices`. |
| [`sparse_bsr_tensor`](generated/torch.sparse_bsr_tensor.html#torch.sparse_bsr_tensor) | Constructs a [sparse tensor in BSR (Block Compressed Sparse Row))](sparse.html#sparse-bsr-docs) with specified 2-dimensional blocks at the given `crow_indices` and `col_indices`. |
| [`sparse_bsc_tensor`](generated/torch.sparse_bsc_tensor.html#torch.sparse_bsc_tensor) | Constructs a [sparse tensor in BSC (Block Compressed Sparse Column))](sparse.html#sparse-bsc-docs) with specified 2-dimensional blocks at the given `ccol_indices` and `row_indices`. |
| [`asarray`](generated/torch.asarray.html#torch.asarray) | Converts `obj` to a tensor. |
| [`as_tensor`](generated/torch.as_tensor.html#torch.as_tensor) | Converts `data` into a tensor, sharing data and preserving autograd history if possible. |
| [`as_strided`](generated/torch.as_strided.html#torch.as_strided) | Create a view of an existing torch.Tensor `input` with specified `size`, `stride` and `storage_offset`. |
| [`from_file`](generated/torch.from_file.html#torch.from_file) | Creates a CPU tensor with a storage backed by a memory-mapped file. |
| [`from_numpy`](generated/torch.from_numpy.html#torch.from_numpy) | Creates a [`Tensor`](tensors.html#torch.Tensor) from a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray). |
| [`from_dlpack`](generated/torch.from_dlpack.html#torch.from_dlpack) | Converts a tensor from an external library into a `torch.Tensor`. |
| [`frombuffer`](generated/torch.frombuffer.html#torch.frombuffer) | Creates a 1-dimensional [`Tensor`](tensors.html#torch.Tensor) from an object that implements the Python buffer protocol. |
| [`zeros`](generated/torch.zeros.html#torch.zeros) | Returns a tensor filled with the scalar value 0, with the shape defined by the variable argument `size`. |
| [`zeros_like`](generated/torch.zeros_like.html#torch.zeros_like) | Returns a tensor filled with the scalar value 0, with the same size as `input`. |
| [`ones`](generated/torch.ones.html#torch.ones) | Returns a tensor filled with the scalar value 1, with the shape defined by the variable argument `size`. |
| [`ones_like`](generated/torch.ones_like.html#torch.ones_like) | Returns a tensor filled with the scalar value 1, with the same size as `input`. |
| [`arange`](generated/torch.arange.html#torch.arange) | Returns a 1-D tensor of size ⌈end−startstep⌉\left\lceil \frac{\text{end} - \text{start}}{\text{step}} \right\rceil⌈stepend−start​⌉ with values from the interval `[start, end)` taken with common difference `step` beginning from start. |
| [`range`](generated/torch.range.html#torch.range) | Returns a 1-D tensor of size ⌊end−startstep⌋+1\left\lfloor \frac{\text{end} - \text{start}}{\text{step}} \right\rfloor + 1⌊stepend−start​⌋+1 with values from `start` to `end` with step `step`. |
| [`linspace`](generated/torch.linspace.html#torch.linspace) | Creates a one-dimensional tensor of size `steps` whose values are evenly spaced from `start` to `end`, inclusive. |
| [`logspace`](generated/torch.logspace.html#torch.logspace) | Creates a one-dimensional tensor of size `steps` whose values are evenly spaced from basestart{{\text{{base}}}}^{{\text{{start}}}}basestart to baseend{{\text{{base}}}}^{{\text{{end}}}}baseend, inclusive, on a logarithmic scale with base `base`. |
| [`eye`](generated/torch.eye.html#torch.eye) | Returns a 2-D tensor with ones on the diagonal and zeros elsewhere. |
| [`empty`](generated/torch.empty.html#torch.empty) | Returns a tensor filled with uninitialized data. |
| [`empty_like`](generated/torch.empty_like.html#torch.empty_like) | Returns an uninitialized tensor with the same size as `input`. |
| [`empty_strided`](generated/torch.empty_strided.html#torch.empty_strided) | Creates a tensor with the specified `size` and `stride` and filled with undefined data. |
| [`full`](generated/torch.full.html#torch.full) | Creates a tensor of size `size` filled with `fill_value`. |
| [`full_like`](generated/torch.full_like.html#torch.full_like) | Returns a tensor with the same size as `input` filled with `fill_value`. |
| [`quantize_per_tensor`](generated/torch.quantize_per_tensor.html#torch.quantize_per_tensor) | Converts a float tensor to a quantized tensor with given scale and zero point. |
| [`quantize_per_channel`](generated/torch.quantize_per_channel.html#torch.quantize_per_channel) | Converts a float tensor to a per-channel quantized tensor with given scales and zero points. |
| [`dequantize`](generated/torch.dequantize.html#torch.dequantize) | Returns an fp32 Tensor by dequantizing a quantized Tensor |
| [`complex`](generated/torch.complex.html#torch.complex) | Constructs a complex tensor with its real part equal to [`real`](generated/torch.real.html#torch.real) and its imaginary part equal to [`imag`](generated/torch.imag.html#torch.imag). |
| [`polar`](generated/torch.polar.html#torch.polar) | Constructs a complex tensor whose elements are Cartesian coordinates corresponding to the polar coordinates with absolute value [`abs`](generated/torch.abs.html#torch.abs) and angle [`angle`](generated/torch.angle.html#torch.angle). |
| [`heaviside`](generated/torch.heaviside.html#torch.heaviside) | Computes the Heaviside step function for each element in `input`. |

### Indexing, Slicing, Joining, Mutating Ops

| [`adjoint`](generated/torch.adjoint.html#torch.adjoint) | Returns a view of the tensor conjugated and with the last two dimensions transposed. |
| --- | --- |
| [`argwhere`](generated/torch.argwhere.html#torch.argwhere) | Returns a tensor containing the indices of all non-zero elements of `input`. |
| [`cat`](generated/torch.cat.html#torch.cat) | Concatenates the given sequence of tensors in `tensors` in the given dimension. |
| [`concat`](generated/torch.concat.html#torch.concat) | Alias of [`torch.cat()`](generated/torch.cat.html#torch.cat). |
| [`concatenate`](generated/torch.concatenate.html#torch.concatenate) | Alias of [`torch.cat()`](generated/torch.cat.html#torch.cat). |
| [`conj`](generated/torch.conj.html#torch.conj) | Returns a view of `input` with a flipped conjugate bit. |
| [`chunk`](generated/torch.chunk.html#torch.chunk) | Attempts to split a tensor into the specified number of chunks. |
| [`dsplit`](generated/torch.dsplit.html#torch.dsplit) | Splits `input`, a tensor with three or more dimensions, into multiple tensors depthwise according to `indices_or_sections`. |
| [`column_stack`](generated/torch.column_stack.html#torch.column_stack) | Creates a new tensor by horizontally stacking the tensors in `tensors`. |
| [`dstack`](generated/torch.dstack.html#torch.dstack) | Stack tensors in sequence depthwise (along third axis). |
| [`gather`](generated/torch.gather.html#torch.gather) | Gathers values along an axis specified by dim. |
| [`hsplit`](generated/torch.hsplit.html#torch.hsplit) | Splits `input`, a tensor with one or more dimensions, into multiple tensors horizontally according to `indices_or_sections`. |
| [`hstack`](generated/torch.hstack.html#torch.hstack) | Stack tensors in sequence horizontally (column wise). |
| [`index_add`](generated/torch.index_add.html#torch.index_add) | See [`index_add_()`](generated/torch.Tensor.index_add_.html#torch.Tensor.index_add_) for function description. |
| [`index_copy`](generated/torch.index_copy.html#torch.index_copy) | See [`index_copy_()`](generated/torch.Tensor.index_copy_.html#torch.Tensor.index_copy_) for function description. |
| [`index_reduce`](generated/torch.index_reduce.html#torch.index_reduce) | See [`index_reduce_()`](generated/torch.Tensor.index_reduce_.html#torch.Tensor.index_reduce_) for function description. |
| [`index_select`](generated/torch.index_select.html#torch.index_select) | Returns a new tensor which indexes the `input` tensor along dimension `dim` using the entries in `index`. |
| [`masked_select`](generated/torch.masked_select.html#torch.masked_select) | Returns a new 1-D tensor which indexes the `input` tensor according to the boolean mask `mask` which is a BoolTensor. |
| [`movedim`](generated/torch.movedim.html#torch.movedim) | Moves the dimension(s) of `input` at the position(s) in `source` to the position(s) in `destination`. |
| [`moveaxis`](generated/torch.moveaxis.html#torch.moveaxis) | Alias for [`torch.movedim()`](generated/torch.movedim.html#torch.movedim). |
| [`narrow`](generated/torch.narrow.html#torch.narrow) | Returns a new tensor that is a narrowed version of `input` tensor. |
| [`narrow_copy`](generated/torch.narrow_copy.html#torch.narrow_copy) | Same as [`Tensor.narrow()`](generated/torch.Tensor.narrow.html#torch.Tensor.narrow) except this returns a copy rather than shared storage. |
| [`nonzero`](generated/torch.nonzero.html#torch.nonzero) | |
| [`permute`](generated/torch.permute.html#torch.permute) | Returns a view of the original tensor `input` with its dimensions permuted. |
| [`reshape`](generated/torch.reshape.html#torch.reshape) | Returns a tensor with the same data and number of elements as `input`, but with the specified shape. |
| [`row_stack`](generated/torch.row_stack.html#torch.row_stack) | Alias of [`torch.vstack()`](generated/torch.vstack.html#torch.vstack). |
| [`select`](generated/torch.select.html#torch.select) | Slices the `input` tensor along the selected dimension at the given index. |
| [`scatter`](generated/torch.scatter.html#torch.scatter) | Out-of-place version of [`torch.Tensor.scatter_()`](generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_) |
| [`diagonal_scatter`](generated/torch.diagonal_scatter.html#torch.diagonal_scatter) | Embeds the values of the `src` tensor into `input` along the diagonal elements of `input`, with respect to `dim1` and `dim2`. |
| [`select_scatter`](generated/torch.select_scatter.html#torch.select_scatter) | Embeds the values of the `src` tensor into `input` at the given index. |
| [`slice_scatter`](generated/torch.slice_scatter.html#torch.slice_scatter) | Embeds the values of the `src` tensor into `input` at the given dimension. |
| [`scatter_add`](generated/torch.scatter_add.html#torch.scatter_add) | Out-of-place version of [`torch.Tensor.scatter_add_()`](generated/torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_) |
| [`scatter_reduce`](generated/torch.scatter_reduce.html#torch.scatter_reduce) | Out-of-place version of [`torch.Tensor.scatter_reduce_()`](generated/torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_) |
| [`segment_reduce`](generated/torch.segment_reduce.html#torch.segment_reduce) | Perform a segment reduction operation on the input tensor along the specified axis. |
| [`split`](generated/torch.split.html#torch.split) | Splits the tensor into chunks. |
| [`squeeze`](generated/torch.squeeze.html#torch.squeeze) | Returns a tensor with all specified dimensions of `input` of size 1 removed. |
| [`stack`](generated/torch.stack.html#torch.stack) | Concatenates a sequence of tensors along a new dimension. |
| [`swapaxes`](generated/torch.swapaxes.html#torch.swapaxes) | Alias for [`torch.transpose()`](generated/torch.transpose.html#torch.transpose). |
| [`swapdims`](generated/torch.swapdims.html#torch.swapdims) | Alias for [`torch.transpose()`](generated/torch.transpose.html#torch.transpose). |
| [`t`](generated/torch.t.html#torch.t) | Expects `input` to be <= 2-D tensor and transposes dimensions 0 and 1. |
| [`take`](generated/torch.take.html#torch.take) | Returns a new tensor with the elements of `input` at the given indices. |
| [`take_along_dim`](generated/torch.take_along_dim.html#torch.take_along_dim) | Selects values from `input` at the 1-dimensional indices from `indices` along the given `dim`. |
| [`tensor_split`](generated/torch.tensor_split.html#torch.tensor_split) | Splits a tensor into multiple sub-tensors, all of which are views of `input`, along dimension `dim` according to the indices or number of sections specified by `indices_or_sections`. |
| [`tile`](generated/torch.tile.html#torch.tile) | Constructs a tensor by repeating the elements of `input`. |
| [`transpose`](generated/torch.transpose.html#torch.transpose) | Returns a tensor that is a transposed version of `input`. |
| [`unbind`](generated/torch.unbind.html#torch.unbind) | Removes a tensor dimension. |
| [`unravel_index`](generated/torch.unravel_index.html#torch.unravel_index) | Converts a tensor of flat indices into a tuple of coordinate tensors that index into an arbitrary tensor of the specified shape. |
| [`unsqueeze`](generated/torch.unsqueeze.html#torch.unsqueeze) | Returns a new tensor with a dimension of size one inserted at the specified position. |
| [`vsplit`](generated/torch.vsplit.html#torch.vsplit) | Splits `input`, a tensor with two or more dimensions, into multiple tensors vertically according to `indices_or_sections`. |
| [`vstack`](generated/torch.vstack.html#torch.vstack) | Stack tensors in sequence vertically (row wise). |
| [`where`](generated/torch.where.html#torch.where) | Return a tensor of elements selected from either `input` or `other`, depending on `condition`. |

## Accelerators

Within the PyTorch repo, we define an "Accelerator" as a [`torch.device`](tensor_attributes.html#torch.device) that is being used
alongside a CPU to speed up computation. These devices use an asynchronous execution scheme,
using [`torch.Stream`](generated/torch.Stream.html#torch.Stream) and [`torch.Event`](generated/torch.Event.html#torch.Event) as their main way to perform synchronization.
We also assume that only one such accelerator can be available at once on a given host. This allows
us to use the current accelerator as the default device for relevant concepts such as pinned memory,
Stream device_type, FSDP, etc.

As of today, accelerator devices are (in no particular order) ["CUDA"](cuda.html), ["MTIA"](mtia.html),
["XPU"](xpu.html), ["MPS"](mps.html), "HPU", and PrivateUse1 (many device not in the PyTorch repo itself).

Many tools in the PyTorch Ecosystem use fork to create subprocesses (for example dataloading
or intra-op parallelism), it is thus important to delay as much as possible any
operation that would prevent further forks. This is especially important here as most accelerator's initialization has such effect.
In practice, you should keep in mind that checking [`torch.accelerator.current_accelerator()`](generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator)
is a compile-time check by default, it is thus always fork-safe.
On the contrary, passing the `check_available=True` flag to this function or calling
[`torch.accelerator.is_available()`](generated/torch.accelerator.is_available.html#torch.accelerator.is_available) will usually prevent later fork.

Some backends provide an experimental opt-in option to make the runtime availability
check fork-safe. When using the CUDA device `PYTORCH_NVML_BASED_CUDA_CHECK=1` can be
used for example.

| [`Stream`](generated/torch.Stream.html#torch.Stream) | An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order. |
| --- | --- |
| [`Event`](generated/torch.Event.html#torch.Event) | Query and record Stream status to identify or control dependencies across Stream and measure timing. |

## Generators

| [`Generator`](generated/torch.Generator.html#torch.Generator) | Creates and returns a generator object that manages the state of the algorithm which produces pseudo random numbers. |
| --- | --- |

## Random sampling

| [`seed`](generated/torch.seed.html#torch.seed) | Sets the seed for generating random numbers to a non-deterministic random number on all devices. |
| --- | --- |
| [`manual_seed`](generated/torch.manual_seed.html#torch.manual_seed) | Sets the seed for generating random numbers on all devices. |
| [`initial_seed`](generated/torch.initial_seed.html#torch.initial_seed) | Returns the initial seed for generating random numbers as a Python long. |
| [`get_rng_state`](generated/torch.get_rng_state.html#torch.get_rng_state) | Returns the random number generator state as a torch.ByteTensor. |
| [`set_rng_state`](generated/torch.set_rng_state.html#torch.set_rng_state) | Sets the random number generator state. |

torch.default_generator*Returns the default CPU torch.Generator*

| [`bernoulli`](generated/torch.bernoulli.html#torch.bernoulli) | Draws binary random numbers (0 or 1) from a Bernoulli distribution. |
| --- | --- |
| [`multinomial`](generated/torch.multinomial.html#torch.multinomial) | Returns a tensor where each row contains `num_samples` indices sampled from the multinomial (a stricter definition would be multivariate, refer to [`torch.distributions.multinomial.Multinomial`](distributions.html#torch.distributions.multinomial.Multinomial) for more details) probability distribution located in the corresponding row of tensor `input`. |
| [`normal`](generated/torch.normal.html#torch.normal) | Returns a tensor of random numbers drawn from separate normal distributions whose mean and standard deviation are given. |
| [`poisson`](generated/torch.poisson.html#torch.poisson) | Returns a tensor of the same size as `input` with each element sampled from a Poisson distribution with rate parameter given by the corresponding element in `input` i.e., |
| [`rand`](generated/torch.rand.html#torch.rand) | Returns a tensor filled with random numbers from a uniform distribution on the interval [0,1)[0, 1)[0,1) |
| [`rand_like`](generated/torch.rand_like.html#torch.rand_like) | Returns a tensor with the same size as `input` that is filled with random numbers from a uniform distribution on the interval [0,1)[0, 1)[0,1). |
| [`randint`](generated/torch.randint.html#torch.randint) | Returns a tensor filled with random integers generated uniformly between `low` (inclusive) and `high` (exclusive). |
| [`randint_like`](generated/torch.randint_like.html#torch.randint_like) | Returns a tensor with the same shape as Tensor `input` filled with random integers generated uniformly between `low` (inclusive) and `high` (exclusive). |
| [`randn`](generated/torch.randn.html#torch.randn) | Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 (also called the standard normal distribution). |
| [`randn_like`](generated/torch.randn_like.html#torch.randn_like) | Returns a tensor with the same size as `input` that is filled with random numbers from a normal distribution with mean 0 and variance 1. |
| [`randperm`](generated/torch.randperm.html#torch.randperm) | Returns a random permutation of integers from `0` to `n - 1`. |

### In-place random sampling

There are a few more in-place random sampling functions defined on Tensors as well. Click through to refer to their documentation:

- [`torch.Tensor.bernoulli_()`](generated/torch.Tensor.bernoulli_.html#torch.Tensor.bernoulli_) - in-place version of [`torch.bernoulli()`](generated/torch.bernoulli.html#torch.bernoulli)
- [`torch.Tensor.cauchy_()`](generated/torch.Tensor.cauchy_.html#torch.Tensor.cauchy_) - numbers drawn from the Cauchy distribution
- [`torch.Tensor.exponential_()`](generated/torch.Tensor.exponential_.html#torch.Tensor.exponential_) - numbers drawn from the exponential distribution
- [`torch.Tensor.geometric_()`](generated/torch.Tensor.geometric_.html#torch.Tensor.geometric_) - elements drawn from the geometric distribution
- [`torch.Tensor.log_normal_()`](generated/torch.Tensor.log_normal_.html#torch.Tensor.log_normal_) - samples from the log-normal distribution
- [`torch.Tensor.normal_()`](generated/torch.Tensor.normal_.html#torch.Tensor.normal_) - in-place version of [`torch.normal()`](generated/torch.normal.html#torch.normal)
- [`torch.Tensor.random_()`](generated/torch.Tensor.random_.html#torch.Tensor.random_) - numbers sampled from the discrete uniform distribution
- [`torch.Tensor.uniform_()`](generated/torch.Tensor.uniform_.html#torch.Tensor.uniform_) - numbers sampled from the continuous uniform distribution

### Quasi-random sampling

| [`quasirandom.SobolEngine`](generated/torch.quasirandom.SobolEngine.html#torch.quasirandom.SobolEngine) | The [`torch.quasirandom.SobolEngine`](generated/torch.quasirandom.SobolEngine.html#torch.quasirandom.SobolEngine) is an engine for generating (scrambled) Sobol sequences. |
| --- | --- |

## Serialization

| [`save`](generated/torch.save.html#torch.save) | Saves an object to a disk file. |
| --- | --- |
| [`load`](generated/torch.load.html#torch.load) | Loads an object saved with [`torch.save()`](generated/torch.save.html#torch.save) from a file. |

torch.serialization.check_module_version_greater_or_equal(*module*, *req_version_tuple*, *error_if_malformed=True*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/serialization.py#L489)

Check if a module's version satisfies requirements

Usually, a module's version string will be like 'x.y.z', which would be represented
as a tuple (x, y, z), but sometimes it could be an unexpected format. If the version
string does not match the given tuple's format up to the length of the tuple, then
error and exit or emit a warning.

Parameters:

- **module** - the module to check the version of
- **req_version_tuple** - tuple (usually of ints) representing the required version
- **error_if_malformed** - whether we should exit if module version string is malformed

Returns:

bool

Return type:

requirement_is_met

torch.serialization.default_restore_location(*storage*, *location*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/serialization.py#L713)

Restores storage using a deserializer function registered for the location.

This function looks in the registry for deserializer functions that match the location.
If found, it attempts to use them, in priority order, to restore storage until one
returns a not None result. If no deserializer can be found in the registry, or all found fail
to bear a result, it raises a RuntimeError.

Parameters:

- **storage** (*STORAGE*) - the storage object to restore
- **location** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the location tag associated with the storage object

Returns:

Optional[STORAGE]

Return type:

storage

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If no deserializer matching location is found in the registry or if
 all matching ones return None.

## Parallelism

| [`get_num_threads`](generated/torch.get_num_threads.html#torch.get_num_threads) | Returns the number of threads used for parallelizing CPU operations |
| --- | --- |
| [`set_num_threads`](generated/torch.set_num_threads.html#torch.set_num_threads) | Sets the number of threads used for intraop parallelism on CPU. |
| [`get_num_interop_threads`](generated/torch.get_num_interop_threads.html#torch.get_num_interop_threads) | Returns the number of threads used for inter-op parallelism on CPU (e.g. in JIT interpreter). |
| [`set_num_interop_threads`](generated/torch.set_num_interop_threads.html#torch.set_num_interop_threads) | Sets the number of threads used for interop parallelism (e.g. in JIT interpreter) on CPU. |

## Locally disabling gradient computation

The context managers [`torch.no_grad()`](generated/torch.no_grad.html#torch.no_grad), [`torch.enable_grad()`](generated/torch.enable_grad.html#torch.enable_grad), and
`torch.set_grad_enabled()` are helpful for locally disabling and enabling
gradient computation. See [Locally disabling gradient computation](autograd.html#locally-disable-grad) for more details on
their usage. These context managers are thread local, so they won't
work if you send work to another thread using the `threading` module, etc.

Examples:

```
>>> x = torch.zeros(1, requires_grad=True)
>>> with torch.no_grad():
... y = x * 2
>>> y.requires_grad
False

>>> is_train = False
>>> with torch.set_grad_enabled(is_train):
... y = x * 2
>>> y.requires_grad
False

>>> torch.set_grad_enabled(True) # this can also be used as a function
>>> y = x * 2
>>> y.requires_grad
True

>>> torch.set_grad_enabled(False)
>>> y = x * 2
>>> y.requires_grad
False
```

| [`no_grad`](generated/torch.no_grad.html#torch.no_grad) | Context-manager that disables gradient calculation. |
| --- | --- |
| [`enable_grad`](generated/torch.enable_grad.html#torch.enable_grad) | Context-manager that enables gradient calculation. |
| [`autograd.grad_mode.set_grad_enabled`](generated/torch.autograd.grad_mode.set_grad_enabled.html#torch.autograd.grad_mode.set_grad_enabled) | Context-manager that sets gradient calculation on or off. |
| [`is_grad_enabled`](generated/torch.is_grad_enabled.html#torch.is_grad_enabled) | Returns True if grad mode is currently enabled. |
| [`autograd.grad_mode.inference_mode`](generated/torch.autograd.grad_mode.inference_mode.html#torch.autograd.grad_mode.inference_mode) | Context manager that enables or disables inference mode. |
| [`is_inference_mode_enabled`](generated/torch.is_inference_mode_enabled.html#torch.is_inference_mode_enabled) | Returns True if inference mode is currently enabled. |

## Math operations

### Constants

| `e` | Euler's number, the base of natural logarithms (~2.7183). Alias for `math.e`. |
| --- | --- |
| `inf` | A floating-point positive infinity. Alias for `math.inf`. |
| `nan` | A floating-point "not a number" value. This value is not a legal number. Alias for `math.nan`. |
| `pi` | The ratio of a circle's circumference to its diameter (~3.1416). Alias for `math.pi`. |

### Pointwise Ops

| [`abs`](generated/torch.abs.html#torch.abs) | Computes the absolute value of each element in `input`. |
| --- | --- |
| [`absolute`](generated/torch.absolute.html#torch.absolute) | Alias for [`torch.abs()`](generated/torch.abs.html#torch.abs) |
| [`acos`](generated/torch.acos.html#torch.acos) | Returns a new tensor with the arccosine (in radians) of each element in `input`. |
| [`arccos`](generated/torch.arccos.html#torch.arccos) | Alias for [`torch.acos()`](generated/torch.acos.html#torch.acos). |
| [`acosh`](generated/torch.acosh.html#torch.acosh) | Returns a new tensor with the inverse hyperbolic cosine of the elements of `input`. |
| [`arccosh`](generated/torch.arccosh.html#torch.arccosh) | Alias for [`torch.acosh()`](generated/torch.acosh.html#torch.acosh). |
| [`add`](generated/torch.add.html#torch.add) | Adds `other`, scaled by `alpha`, to `input`. |
| [`addcdiv`](generated/torch.addcdiv.html#torch.addcdiv) | Performs the element-wise division of `tensor1` by `tensor2`, multiplies the result by the scalar `value` and adds it to `input`. |
| [`addcmul`](generated/torch.addcmul.html#torch.addcmul) | Performs the element-wise multiplication of `tensor1` by `tensor2`, multiplies the result by the scalar `value` and adds it to `input`. |
| [`angle`](generated/torch.angle.html#torch.angle) | Computes the element-wise angle (in radians) of the given `input` tensor. |
| [`asin`](generated/torch.asin.html#torch.asin) | Returns a new tensor with the arcsine of the elements (in radians) in the `input` tensor. |
| [`arcsin`](generated/torch.arcsin.html#torch.arcsin) | Alias for [`torch.asin()`](generated/torch.asin.html#torch.asin). |
| [`asinh`](generated/torch.asinh.html#torch.asinh) | Returns a new tensor with the inverse hyperbolic sine of the elements of `input`. |
| [`arcsinh`](generated/torch.arcsinh.html#torch.arcsinh) | Alias for [`torch.asinh()`](generated/torch.asinh.html#torch.asinh). |
| [`atan`](generated/torch.atan.html#torch.atan) | Returns a new tensor with the arctangent of the elements (in radians) in the `input` tensor. |
| [`arctan`](generated/torch.arctan.html#torch.arctan) | Alias for [`torch.atan()`](generated/torch.atan.html#torch.atan). |
| [`atanh`](generated/torch.atanh.html#torch.atanh) | Returns a new tensor with the inverse hyperbolic tangent of the elements of `input`. |
| [`arctanh`](generated/torch.arctanh.html#torch.arctanh) | Alias for [`torch.atanh()`](generated/torch.atanh.html#torch.atanh). |
| [`atan2`](generated/torch.atan2.html#torch.atan2) | Element-wise arctangent of inputi/otheri\text{input}_{i} / \text{other}_{i}inputi​/otheri​ with consideration of the quadrant. |
| [`arctan2`](generated/torch.arctan2.html#torch.arctan2) | Alias for [`torch.atan2()`](generated/torch.atan2.html#torch.atan2). |
| [`bitwise_not`](generated/torch.bitwise_not.html#torch.bitwise_not) | Computes the bitwise NOT of the given input tensor. |
| [`bitwise_and`](generated/torch.bitwise_and.html#torch.bitwise_and) | Computes the bitwise AND of `input` and `other`. |
| [`bitwise_or`](generated/torch.bitwise_or.html#torch.bitwise_or) | Computes the bitwise OR of `input` and `other`. |
| [`bitwise_xor`](generated/torch.bitwise_xor.html#torch.bitwise_xor) | Computes the bitwise XOR of `input` and `other`. |
| [`bitwise_left_shift`](generated/torch.bitwise_left_shift.html#torch.bitwise_left_shift) | Computes the left arithmetic shift of `input` by `other` bits. |
| [`bitwise_right_shift`](generated/torch.bitwise_right_shift.html#torch.bitwise_right_shift) | Computes the right arithmetic shift of `input` by `other` bits. |
| [`ceil`](generated/torch.ceil.html#torch.ceil) | Returns a new tensor with the ceil of the elements of `input`, the smallest integer greater than or equal to each element. |
| [`clamp`](generated/torch.clamp.html#torch.clamp) | Clamps all elements in `input` into the range [ [`min`](generated/torch.min.html#torch.min), [`max`](generated/torch.max.html#torch.max) ]. |
| [`clip`](generated/torch.clip.html#torch.clip) | Alias for [`torch.clamp()`](generated/torch.clamp.html#torch.clamp). |
| [`conj_physical`](generated/torch.conj_physical.html#torch.conj_physical) | Computes the element-wise conjugate of the given `input` tensor. |
| [`copysign`](generated/torch.copysign.html#torch.copysign) | Create a new floating-point tensor with the magnitude of `input` and the sign of `other`, elementwise. |
| [`cos`](generated/torch.cos.html#torch.cos) | Returns a new tensor with the cosine of the elements of `input` given in radians. |
| [`cosh`](generated/torch.cosh.html#torch.cosh) | Returns a new tensor with the hyperbolic cosine of the elements of `input`. |
| [`deg2rad`](generated/torch.deg2rad.html#torch.deg2rad) | Returns a new tensor with each of the elements of `input` converted from angles in degrees to radians. |
| [`div`](generated/torch.div.html#torch.div) | Divides each element of the input `input` by the corresponding element of `other`. |
| [`divide`](generated/torch.divide.html#torch.divide) | Alias for [`torch.div()`](generated/torch.div.html#torch.div). |
| [`digamma`](generated/torch.digamma.html#torch.digamma) | Alias for [`torch.special.digamma()`](special.html#torch.special.digamma). |
| [`erf`](generated/torch.erf.html#torch.erf) | Alias for [`torch.special.erf()`](special.html#torch.special.erf). |
| [`erfc`](generated/torch.erfc.html#torch.erfc) | Alias for [`torch.special.erfc()`](special.html#torch.special.erfc). |
| [`erfinv`](generated/torch.erfinv.html#torch.erfinv) | Alias for [`torch.special.erfinv()`](special.html#torch.special.erfinv). |
| [`exp`](generated/torch.exp.html#torch.exp) | Returns a new tensor with the exponential of the elements of the input tensor `input`. |
| [`exp2`](generated/torch.exp2.html#torch.exp2) | Alias for [`torch.special.exp2()`](special.html#torch.special.exp2). |
| [`expm1`](generated/torch.expm1.html#torch.expm1) | Alias for [`torch.special.expm1()`](special.html#torch.special.expm1). |
| [`fake_quantize_per_channel_affine`](generated/torch.fake_quantize_per_channel_affine.html#torch.fake_quantize_per_channel_affine) | Returns a new tensor with the data in `input` fake quantized per channel using `scale`, `zero_point`, `quant_min` and `quant_max`, across the channel specified by `axis`. |
| [`fake_quantize_per_tensor_affine`](generated/torch.fake_quantize_per_tensor_affine.html#torch.fake_quantize_per_tensor_affine) | Returns a new tensor with the data in `input` fake quantized using `scale`, `zero_point`, `quant_min` and `quant_max`. |
| [`fix`](generated/torch.fix.html#torch.fix) | Alias for [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) |
| [`float_power`](generated/torch.float_power.html#torch.float_power) | Raises `input` to the power of `exponent`, elementwise, in double precision. |
| [`floor`](generated/torch.floor.html#torch.floor) | Returns a new tensor with the floor of the elements of `input`, the largest integer less than or equal to each element. |
| [`floor_divide`](generated/torch.floor_divide.html#torch.floor_divide) | |
| [`fmod`](generated/torch.fmod.html#torch.fmod) | Applies C++'s [std::fmod](https://en.cppreference.com/w/cpp/numeric/math/fmod) entrywise. |
| [`frac`](generated/torch.frac.html#torch.frac) | Computes the fractional portion of each element in `input`. |
| [`frexp`](generated/torch.frexp.html#torch.frexp) | Decomposes `input` into mantissa and exponent tensors such that input=mantissa×2exponent\text{input} = \text{mantissa} \times 2^{\text{exponent}}input=mantissa×2exponent. |
| [`gradient`](generated/torch.gradient.html#torch.gradient) | Estimates the gradient of a function g:Rn→Rg : \mathbb{R}^n \rightarrow \mathbb{R}g:Rn→R in one or more dimensions using the [second-order accurate central differences method](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf) and either first or second order estimates at the boundaries. |
| [`imag`](generated/torch.imag.html#torch.imag) | Returns a new tensor containing imaginary values of the `self` tensor. |
| [`ldexp`](generated/torch.ldexp.html#torch.ldexp) | Multiplies `input` by 2 ** `other`. |
| [`lerp`](generated/torch.lerp.html#torch.lerp) | Does a linear interpolation of two tensors `start` (given by `input`) and `end` based on a scalar or tensor `weight` and returns the resulting `out` tensor. |
| [`lgamma`](generated/torch.lgamma.html#torch.lgamma) | Computes the natural logarithm of the absolute value of the gamma function on `input`. |
| [`log`](generated/torch.log.html#torch.log) | Returns a new tensor with the natural logarithm of the elements of `input`. |
| [`log10`](generated/torch.log10.html#torch.log10) | Returns a new tensor with the logarithm to the base 10 of the elements of `input`. |
| [`log1p`](generated/torch.log1p.html#torch.log1p) | Returns a new tensor with the natural logarithm of (1 + `input`). |
| [`log2`](generated/torch.log2.html#torch.log2) | Returns a new tensor with the logarithm to the base 2 of the elements of `input`. |
| [`logaddexp`](generated/torch.logaddexp.html#torch.logaddexp) | Logarithm of the sum of exponentiations of the inputs. |
| [`logaddexp2`](generated/torch.logaddexp2.html#torch.logaddexp2) | Logarithm of the sum of exponentiations of the inputs in base-2. |
| [`logical_and`](generated/torch.logical_and.html#torch.logical_and) | Computes the element-wise logical AND of the given input tensors. |
| [`logical_not`](generated/torch.logical_not.html#torch.logical_not) | Computes the element-wise logical NOT of the given input tensor. |
| [`logical_or`](generated/torch.logical_or.html#torch.logical_or) | Computes the element-wise logical OR of the given input tensors. |
| [`logical_xor`](generated/torch.logical_xor.html#torch.logical_xor) | Computes the element-wise logical XOR of the given input tensors. |
| [`logit`](generated/torch.logit.html#torch.logit) | Alias for [`torch.special.logit()`](special.html#torch.special.logit). |
| [`hypot`](generated/torch.hypot.html#torch.hypot) | Given the legs of a right triangle, return its hypotenuse. |
| [`i0`](generated/torch.i0.html#torch.i0) | Alias for [`torch.special.i0()`](special.html#torch.special.i0). |
| [`igamma`](generated/torch.igamma.html#torch.igamma) | Alias for [`torch.special.gammainc()`](special.html#torch.special.gammainc). |
| [`igammac`](generated/torch.igammac.html#torch.igammac) | Alias for [`torch.special.gammaincc()`](special.html#torch.special.gammaincc). |
| [`mul`](generated/torch.mul.html#torch.mul) | Multiplies `input` by `other`. |
| [`multiply`](generated/torch.multiply.html#torch.multiply) | Alias for [`torch.mul()`](generated/torch.mul.html#torch.mul). |
| [`mvlgamma`](generated/torch.mvlgamma.html#torch.mvlgamma) | Alias for [`torch.special.multigammaln()`](special.html#torch.special.multigammaln). |
| [`nan_to_num`](generated/torch.nan_to_num.html#torch.nan_to_num) | Replaces `NaN`, positive infinity, and negative infinity values in `input` with the values specified by `nan`, `posinf`, and `neginf`, respectively. |
| [`neg`](generated/torch.neg.html#torch.neg) | Returns a new tensor with the negative of the elements of `input`. |
| [`negative`](generated/torch.negative.html#torch.negative) | Alias for [`torch.neg()`](generated/torch.neg.html#torch.neg) |
| [`nextafter`](generated/torch.nextafter.html#torch.nextafter) | Return the next floating-point value after `input` towards `other`, elementwise. |
| [`polygamma`](generated/torch.polygamma.html#torch.polygamma) | Alias for [`torch.special.polygamma()`](special.html#torch.special.polygamma). |
| [`positive`](generated/torch.positive.html#torch.positive) | Returns `input`. |
| [`pow`](generated/torch.pow.html#torch.pow) | Takes the power of each element in `input` with `exponent` and returns a tensor with the result. |
| [`quantized_batch_norm`](generated/torch.quantized_batch_norm.html#torch.quantized_batch_norm) | Applies batch normalization on a 4D (NCHW) quantized tensor. |
| [`quantized_max_pool1d`](generated/torch.quantized_max_pool1d.html#torch.quantized_max_pool1d) | Applies a 1D max pooling over an input quantized tensor composed of several input planes. |
| [`quantized_max_pool2d`](generated/torch.quantized_max_pool2d.html#torch.quantized_max_pool2d) | Applies a 2D max pooling over an input quantized tensor composed of several input planes. |
| [`rad2deg`](generated/torch.rad2deg.html#torch.rad2deg) | Returns a new tensor with each of the elements of `input` converted from angles in radians to degrees. |
| [`real`](generated/torch.real.html#torch.real) | Returns a new tensor containing real values of the `self` tensor. |
| [`reciprocal`](generated/torch.reciprocal.html#torch.reciprocal) | Returns a new tensor with the reciprocal of the elements of `input` |
| [`remainder`](generated/torch.remainder.html#torch.remainder) | Computes [Python's modulus operation](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) entrywise. |
| [`round`](generated/torch.round.html#torch.round) | Rounds elements of `input` to the nearest integer. |
| [`rsqrt`](generated/torch.rsqrt.html#torch.rsqrt) | Returns a new tensor with the reciprocal of the square-root of each of the elements of `input`. |
| [`sigmoid`](generated/torch.sigmoid.html#torch.sigmoid) | Alias for [`torch.special.expit()`](special.html#torch.special.expit). |
| [`sign`](generated/torch.sign.html#torch.sign) | Returns a new tensor with the signs of the elements of `input`. |
| [`sgn`](generated/torch.sgn.html#torch.sgn) | This function is an extension of torch.sign() to complex tensors. |
| [`signbit`](generated/torch.signbit.html#torch.signbit) | Tests if each element of `input` has its sign bit set or not. |
| [`sin`](generated/torch.sin.html#torch.sin) | Returns a new tensor with the sine of the elements in the `input` tensor, where each value in this input tensor is in radians. |
| [`sinc`](generated/torch.sinc.html#torch.sinc) | Alias for [`torch.special.sinc()`](special.html#torch.special.sinc). |
| [`sinh`](generated/torch.sinh.html#torch.sinh) | Returns a new tensor with the hyperbolic sine of the elements of `input`. |
| [`softmax`](generated/torch.softmax.html#torch.softmax) | Alias for [`torch.nn.functional.softmax()`](generated/torch.nn.functional.softmax.html#torch.nn.functional.softmax). |
| [`sqrt`](generated/torch.sqrt.html#torch.sqrt) | Returns a new tensor with the square-root of the elements of `input`. |
| [`square`](generated/torch.square.html#torch.square) | Returns a new tensor with the square of the elements of `input`. |
| [`sub`](generated/torch.sub.html#torch.sub) | Subtracts `other`, scaled by `alpha`, from `input`. |
| [`subtract`](generated/torch.subtract.html#torch.subtract) | Alias for [`torch.sub()`](generated/torch.sub.html#torch.sub). |
| [`tan`](generated/torch.tan.html#torch.tan) | Returns a new tensor with the tangent of the elements in the `input` tensor, where each value in this input tensor is in radians. |
| [`tanh`](generated/torch.tanh.html#torch.tanh) | Returns a new tensor with the hyperbolic tangent of the elements of `input`. |
| [`true_divide`](generated/torch.true_divide.html#torch.true_divide) | Alias for [`torch.div()`](generated/torch.div.html#torch.div) with `rounding_mode=None`. |
| [`trunc`](generated/torch.trunc.html#torch.trunc) | Returns a new tensor with the truncated integer values of the elements of `input`. |
| [`xlogy`](generated/torch.xlogy.html#torch.xlogy) | Alias for [`torch.special.xlogy()`](special.html#torch.special.xlogy). |

### Reduction Ops

| [`argmax`](generated/torch.argmax.html#torch.argmax) | Returns the indices of the maximum value of all elements in the `input` tensor. |
| --- | --- |
| [`argmin`](generated/torch.argmin.html#torch.argmin) | Returns the indices of the minimum value(s) of the flattened tensor or along a dimension |
| [`amax`](generated/torch.amax.html#torch.amax) | Returns the maximum value of each slice of the `input` tensor in the given dimension(s) `dim`. |
| [`amin`](generated/torch.amin.html#torch.amin) | Returns the minimum value of each slice of the `input` tensor in the given dimension(s) `dim`. |
| [`aminmax`](generated/torch.aminmax.html#torch.aminmax) | Computes the minimum and maximum values of the `input` tensor. |
| [`all`](generated/torch.all.html#torch.all) | Tests if all elements in `input` evaluate to True. |
| [`any`](generated/torch.any.html#torch.any) | Tests if any element in `input` evaluates to True. |
| [`max`](generated/torch.max.html#torch.max) | Returns the maximum value of all elements in the `input` tensor. |
| [`min`](generated/torch.min.html#torch.min) | Returns the minimum value of all elements in the `input` tensor. |
| [`dist`](generated/torch.dist.html#torch.dist) | Returns the p-norm of (`input` - `other`) |
| [`logsumexp`](generated/torch.logsumexp.html#torch.logsumexp) | Returns the log of summed exponentials of each row of the `input` tensor in the given dimension `dim`. |
| [`mean`](generated/torch.mean.html#torch.mean) | |
| [`nanmean`](generated/torch.nanmean.html#torch.nanmean) | Computes the mean of all non-NaN elements along the specified dimensions. |
| [`median`](generated/torch.median.html#torch.median) | Returns the median of the values in `input`. |
| [`nanmedian`](generated/torch.nanmedian.html#torch.nanmedian) | Returns the median of the values in `input`, ignoring `NaN` values. |
| [`mode`](generated/torch.mode.html#torch.mode) | Returns a namedtuple `(values, indices)` where `values` is the mode value of each row of the `input` tensor in the given dimension `dim`, i.e. a value which appears most often in that row, and `indices` is the index location of each mode value found. |
| [`norm`](generated/torch.norm.html#torch.norm) | Returns the matrix norm or vector norm of a given tensor. |
| [`nansum`](generated/torch.nansum.html#torch.nansum) | Returns the sum of all elements, treating Not a Numbers (NaNs) as zero. |
| [`prod`](generated/torch.prod.html#torch.prod) | Returns the product of all elements in the `input` tensor. |
| [`quantile`](generated/torch.quantile.html#torch.quantile) | Computes the q-th quantiles of each row of the `input` tensor along the dimension `dim`. |
| [`nanquantile`](generated/torch.nanquantile.html#torch.nanquantile) | This is a variant of [`torch.quantile()`](generated/torch.quantile.html#torch.quantile) that "ignores" `NaN` values, computing the quantiles `q` as if `NaN` values in `input` did not exist. |
| [`std`](generated/torch.std.html#torch.std) | Calculates the standard deviation over the dimensions specified by `dim`. |
| [`std_mean`](generated/torch.std_mean.html#torch.std_mean) | Calculates the standard deviation and mean over the dimensions specified by `dim`. |
| [`sum`](generated/torch.sum.html#torch.sum) | Returns the sum of all elements in the `input` tensor. |
| [`unique`](generated/torch.unique.html#torch.unique) | Returns the unique elements of the input tensor. |
| [`unique_consecutive`](generated/torch.unique_consecutive.html#torch.unique_consecutive) | Eliminates all but the first element from every consecutive group of equivalent elements. |
| [`var`](generated/torch.var.html#torch.var) | Calculates the variance over the dimensions specified by `dim`. |
| [`var_mean`](generated/torch.var_mean.html#torch.var_mean) | Calculates the variance and mean over the dimensions specified by `dim`. |
| [`count_nonzero`](generated/torch.count_nonzero.html#torch.count_nonzero) | Counts the number of non-zero values in the tensor `input` along the given `dim`. |
| [`hash_tensor`](generated/torch.hash_tensor.html#torch.hash_tensor) | Returns a hash of all elements in the `input` tensor. |

### Comparison Ops

| [`allclose`](generated/torch.allclose.html#torch.allclose) | This function checks if `input` and `other` satisfy the condition: |
| --- | --- |
| [`argsort`](generated/torch.argsort.html#torch.argsort) | Returns the indices that sort a tensor along a given dimension in ascending order by value. |
| [`eq`](generated/torch.eq.html#torch.eq) | Computes element-wise equality |
| [`equal`](generated/torch.equal.html#torch.equal) | `True` if two tensors have the same size and elements, `False` otherwise. |
| [`ge`](generated/torch.ge.html#torch.ge) | Computes input≥other\text{input} \geq \text{other}input≥other element-wise. |
| [`greater_equal`](generated/torch.greater_equal.html#torch.greater_equal) | Alias for [`torch.ge()`](generated/torch.ge.html#torch.ge). |
| [`gt`](generated/torch.gt.html#torch.gt) | Computes input>other\text{input} > \text{other}input>other element-wise. |
| [`greater`](generated/torch.greater.html#torch.greater) | Alias for [`torch.gt()`](generated/torch.gt.html#torch.gt). |
| [`isclose`](generated/torch.isclose.html#torch.isclose) | Returns a new tensor with boolean elements representing if each element of `input` is "close" to the corresponding element of `other`. |
| [`isfinite`](generated/torch.isfinite.html#torch.isfinite) | Returns a new tensor with boolean elements representing if each element is finite or not. |
| [`isin`](generated/torch.isin.html#torch.isin) | Tests if each element of `elements` is in `test_elements`. |
| [`isinf`](generated/torch.isinf.html#torch.isinf) | Tests if each element of `input` is infinite (positive or negative infinity) or not. |
| [`isposinf`](generated/torch.isposinf.html#torch.isposinf) | Tests if each element of `input` is positive infinity or not. |
| [`isneginf`](generated/torch.isneginf.html#torch.isneginf) | Tests if each element of `input` is negative infinity or not. |
| [`isnan`](generated/torch.isnan.html#torch.isnan) | Returns a new tensor with boolean elements representing if each element of `input` is NaN or not. |
| [`isreal`](generated/torch.isreal.html#torch.isreal) | Returns a new tensor with boolean elements representing if each element of `input` is real-valued or not. |
| [`kthvalue`](generated/torch.kthvalue.html#torch.kthvalue) | Returns a namedtuple `(values, indices)` where `values` is the `k` th smallest element of each row of the `input` tensor in the given dimension `dim`. |
| [`le`](generated/torch.le.html#torch.le) | Computes input≤other\text{input} \leq \text{other}input≤other element-wise. |
| [`less_equal`](generated/torch.less_equal.html#torch.less_equal) | Alias for [`torch.le()`](generated/torch.le.html#torch.le). |
| [`lt`](generated/torch.lt.html#torch.lt) | Computes input<other\text{input} < \text{other}input<other element-wise. |
| [`less`](generated/torch.less.html#torch.less) | Alias for [`torch.lt()`](generated/torch.lt.html#torch.lt). |
| [`maximum`](generated/torch.maximum.html#torch.maximum) | Computes the element-wise maximum of `input` and `other`. |
| [`minimum`](generated/torch.minimum.html#torch.minimum) | Computes the element-wise minimum of `input` and `other`. |
| [`fmax`](generated/torch.fmax.html#torch.fmax) | Computes the element-wise maximum of `input` and `other`. |
| [`fmin`](generated/torch.fmin.html#torch.fmin) | Computes the element-wise minimum of `input` and `other`. |
| [`ne`](generated/torch.ne.html#torch.ne) | Computes input≠other\text{input} \neq \text{other}input=other element-wise. |
| [`not_equal`](generated/torch.not_equal.html#torch.not_equal) | Alias for [`torch.ne()`](generated/torch.ne.html#torch.ne). |
| [`sort`](generated/torch.sort.html#torch.sort) | Sorts the elements of the `input` tensor along a given dimension in ascending order by value. |
| [`topk`](generated/torch.topk.html#torch.topk) | Returns the `k` largest elements of the given `input` tensor along a given dimension. |
| [`msort`](generated/torch.msort.html#torch.msort) | Sorts the elements of the `input` tensor along its first dimension in ascending order by value. |

### Spectral Ops

| [`stft`](generated/torch.stft.html#torch.stft) | Short-time Fourier transform (STFT). |
| --- | --- |
| [`istft`](generated/torch.istft.html#torch.istft) | Inverse short time Fourier Transform. |
| [`bartlett_window`](generated/torch.bartlett_window.html#torch.bartlett_window) | Bartlett window function. |
| [`blackman_window`](generated/torch.blackman_window.html#torch.blackman_window) | Blackman window function. |
| [`hamming_window`](generated/torch.hamming_window.html#torch.hamming_window) | Hamming window function. |
| [`hann_window`](generated/torch.hann_window.html#torch.hann_window) | Hann window function. |
| [`kaiser_window`](generated/torch.kaiser_window.html#torch.kaiser_window) | Computes the Kaiser window with window length `window_length` and shape parameter `beta`. |

### Other Operations

| [`atleast_1d`](generated/torch.atleast_1d.html#torch.atleast_1d) | Returns a 1-dimensional view of each input tensor with zero dimensions. |
| --- | --- |
| [`atleast_2d`](generated/torch.atleast_2d.html#torch.atleast_2d) | Returns a 2-dimensional view of each input tensor with zero dimensions. |
| [`atleast_3d`](generated/torch.atleast_3d.html#torch.atleast_3d) | Returns a 3-dimensional view of each input tensor with zero dimensions. |
| [`bincount`](generated/torch.bincount.html#torch.bincount) | Count the frequency of each value in an array of non-negative ints. |
| [`block_diag`](generated/torch.block_diag.html#torch.block_diag) | Create a block diagonal matrix from provided tensors. |
| [`broadcast_tensors`](generated/torch.broadcast_tensors.html#torch.broadcast_tensors) | Broadcasts the given tensors according to [Broadcasting semantics](notes/broadcasting.html#broadcasting-semantics). |
| [`broadcast_to`](generated/torch.broadcast_to.html#torch.broadcast_to) | Broadcasts `input` to the shape `shape`. |
| [`broadcast_shapes`](generated/torch.broadcast_shapes.html#torch.broadcast_shapes) | Similar to [`broadcast_tensors()`](generated/torch.broadcast_tensors.html#torch.broadcast_tensors) but for shapes. |
| [`bucketize`](generated/torch.bucketize.html#torch.bucketize) | Returns the indices of the buckets to which each value in the `input` belongs, where the boundaries of the buckets are set by `boundaries`. |
| [`cartesian_prod`](generated/torch.cartesian_prod.html#torch.cartesian_prod) | Do cartesian product of the given sequence of tensors. |
| [`cdist`](generated/torch.cdist.html#torch.cdist) | Computes batched the p-norm distance between each pair of the two collections of row vectors. |
| [`clone`](generated/torch.clone.html#torch.clone) | Returns a copy of `input`. |
| [`combinations`](generated/torch.combinations.html#torch.combinations) | Compute combinations of length rrr of the given tensor. |
| [`corrcoef`](generated/torch.corrcoef.html#torch.corrcoef) | Estimates the Pearson product-moment correlation coefficient matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations. |
| [`cov`](generated/torch.cov.html#torch.cov) | Estimates the covariance matrix of the variables given by the `input` matrix, where rows are the variables and columns are the observations. |
| [`cross`](generated/torch.cross.html#torch.cross) | Returns the cross product of vectors in dimension `dim` of `input` and `other`. |
| [`cummax`](generated/torch.cummax.html#torch.cummax) | Returns a namedtuple `(values, indices)` where `values` is the cumulative maximum of elements of `input` in the dimension `dim`. |
| [`cummin`](generated/torch.cummin.html#torch.cummin) | Returns a namedtuple `(values, indices)` where `values` is the cumulative minimum of elements of `input` in the dimension `dim`. |
| [`cumprod`](generated/torch.cumprod.html#torch.cumprod) | Returns the cumulative product of elements of `input` in the dimension `dim`. |
| [`cumsum`](generated/torch.cumsum.html#torch.cumsum) | Returns the cumulative sum of elements of `input` in the dimension `dim`. |
| [`diag`](generated/torch.diag.html#torch.diag) | - If `input` is a vector (1-D tensor), then returns a 2-D square tensor |
| [`diag_embed`](generated/torch.diag_embed.html#torch.diag_embed) | Creates a tensor whose diagonals of certain 2D planes (specified by `dim1` and `dim2`) are filled by `input`. |
| [`diagflat`](generated/torch.diagflat.html#torch.diagflat) | - If `input` is a vector (1-D tensor), then returns a 2-D square tensor |
| [`diagonal`](generated/torch.diagonal.html#torch.diagonal) | Returns a partial view of `input` with the its diagonal elements with respect to `dim1` and `dim2` appended as a dimension at the end of the shape. |
| [`diff`](generated/torch.diff.html#torch.diff) | Computes the n-th forward difference along the given dimension. |
| [`einsum`](generated/torch.einsum.html#torch.einsum) | Sums the product of the elements of the input `operands` along dimensions specified using a notation based on the Einstein summation convention. |
| [`flatten`](generated/torch.flatten.html#torch.flatten) | Flattens `input` by reshaping it into a one-dimensional tensor. |
| [`flip`](generated/torch.flip.html#torch.flip) | Reverse the order of an n-D tensor along given axis in dims. |
| [`fliplr`](generated/torch.fliplr.html#torch.fliplr) | Flip tensor in the left/right direction, returning a new tensor. |
| [`flipud`](generated/torch.flipud.html#torch.flipud) | Flip tensor in the up/down direction, returning a new tensor. |
| [`kron`](generated/torch.kron.html#torch.kron) | Computes the Kronecker product, denoted by ⊗\otimes⊗, of `input` and `other`. |
| [`rot90`](generated/torch.rot90.html#torch.rot90) | Rotate an n-D tensor by 90 degrees in the plane specified by dims axis. |
| [`gcd`](generated/torch.gcd.html#torch.gcd) | Computes the element-wise greatest common divisor (GCD) of `input` and `other`. |
| [`histc`](generated/torch.histc.html#torch.histc) | Computes the histogram of a tensor. |
| [`histogram`](generated/torch.histogram.html#torch.histogram) | Computes a histogram of the values in a tensor. |
| [`histogramdd`](generated/torch.histogramdd.html#torch.histogramdd) | Computes a multi-dimensional histogram of the values in a tensor. |
| [`meshgrid`](generated/torch.meshgrid.html#torch.meshgrid) | Creates grids of coordinates specified by the 1D inputs in attr:tensors. |
| [`lcm`](generated/torch.lcm.html#torch.lcm) | Computes the element-wise least common multiple (LCM) of `input` and `other`. |
| [`logcumsumexp`](generated/torch.logcumsumexp.html#torch.logcumsumexp) | Returns the logarithm of the cumulative summation of the exponentiation of elements of `input` in the dimension `dim`. |
| [`ravel`](generated/torch.ravel.html#torch.ravel) | Return a contiguous flattened tensor. |
| [`renorm`](generated/torch.renorm.html#torch.renorm) | Returns a tensor where each sub-tensor of `input` along dimension `dim` is normalized such that the p-norm of the sub-tensor is lower than the value `maxnorm` |
| [`repeat_interleave`](generated/torch.repeat_interleave.html#torch.repeat_interleave) | Repeat elements of a tensor. |
| [`roll`](generated/torch.roll.html#torch.roll) | Roll the tensor `input` along the given dimension(s). |
| [`searchsorted`](generated/torch.searchsorted.html#torch.searchsorted) | Find the indices from the *innermost* dimension of `sorted_sequence` such that, if the corresponding values in `values` were inserted before the indices, when sorted, the order of the corresponding *innermost* dimension within `sorted_sequence` would be preserved. |
| [`tensordot`](generated/torch.tensordot.html#torch.tensordot) | Returns a contraction of a and b over multiple dimensions. |
| [`trace`](generated/torch.trace.html#torch.trace) | Returns the sum of the elements of the diagonal of the input 2-D matrix. |
| [`tril`](generated/torch.tril.html#torch.tril) | Returns the lower triangular part of the matrix (2-D tensor) or batch of matrices `input`, the other elements of the result tensor `out` are set to 0. |
| [`tril_indices`](generated/torch.tril_indices.html#torch.tril_indices) | Returns the indices of the lower triangular part of a `row`-by- `col` matrix in a 2-by-N Tensor, where the first row contains row coordinates of all indices and the second row contains column coordinates. |
| [`triu`](generated/torch.triu.html#torch.triu) | Returns the upper triangular part of a matrix (2-D tensor) or batch of matrices `input`, the other elements of the result tensor `out` are set to 0. |
| [`triu_indices`](generated/torch.triu_indices.html#torch.triu_indices) | Returns the indices of the upper triangular part of a `row` by `col` matrix in a 2-by-N Tensor, where the first row contains row coordinates of all indices and the second row contains column coordinates. |
| [`unflatten`](generated/torch.unflatten.html#torch.unflatten) | Expands a dimension of the input tensor over multiple dimensions. |
| [`vander`](generated/torch.vander.html#torch.vander) | Generates a Vandermonde matrix. |
| [`view_as_real`](generated/torch.view_as_real.html#torch.view_as_real) | Returns a view of `input` as a real tensor. |
| [`view_as_complex`](generated/torch.view_as_complex.html#torch.view_as_complex) | Returns a view of `input` as a complex tensor. |
| [`resolve_conj`](generated/torch.resolve_conj.html#torch.resolve_conj) | Returns a new tensor with materialized conjugation if `input`'s conjugate bit is set to True, else returns `input`. |
| [`resolve_neg`](generated/torch.resolve_neg.html#torch.resolve_neg) | Returns a new tensor with materialized negation if `input`'s negative bit is set to True, else returns `input`. |

### BLAS and LAPACK Operations

| [`addbmm`](generated/torch.addbmm.html#torch.addbmm) | Performs a batch matrix-matrix product of matrices stored in `batch1` and `batch2`, with a reduced add step (all matrix multiplications get accumulated along the first dimension). |
| --- | --- |
| [`addmm`](generated/torch.addmm.html#torch.addmm) | Performs a matrix multiplication of the matrices `mat1` and `mat2`. |
| [`addmv`](generated/torch.addmv.html#torch.addmv) | Performs a matrix-vector product of the matrix `mat` and the vector `vec`. |
| [`addr`](generated/torch.addr.html#torch.addr) | Performs the outer-product of vectors `vec1` and `vec2` and adds it to the matrix `input`. |
| [`baddbmm`](generated/torch.baddbmm.html#torch.baddbmm) | Performs a batch matrix-matrix product of matrices in `batch1` and `batch2`. |
| [`bmm`](generated/torch.bmm.html#torch.bmm) | Performs a batch matrix-matrix product of matrices stored in `input` and `mat2`. |
| [`chain_matmul`](generated/torch.chain_matmul.html#torch.chain_matmul) | Returns the matrix product of the NNN 2-D tensors. |
| [`cholesky`](generated/torch.cholesky.html#torch.cholesky) | Computes the Cholesky decomposition of a symmetric positive-definite matrix AAA or for batches of symmetric positive-definite matrices. |
| [`cholesky_inverse`](generated/torch.cholesky_inverse.html#torch.cholesky_inverse) | Computes the inverse of a complex Hermitian or real symmetric positive-definite matrix given its Cholesky decomposition. |
| [`cholesky_solve`](generated/torch.cholesky_solve.html#torch.cholesky_solve) | Computes the solution of a system of linear equations with complex Hermitian or real symmetric positive-definite lhs given its Cholesky decomposition. |
| [`dot`](generated/torch.dot.html#torch.dot) | Computes the dot product of two 1D tensors. |
| [`geqrf`](generated/torch.geqrf.html#torch.geqrf) | This is a low-level function for calling LAPACK's geqrf directly. |
| [`ger`](generated/torch.ger.html#torch.ger) | Alias of [`torch.outer()`](generated/torch.outer.html#torch.outer). |
| [`inner`](generated/torch.inner.html#torch.inner) | Computes the dot product for 1D tensors. |
| [`inverse`](generated/torch.inverse.html#torch.inverse) | Alias for [`torch.linalg.inv()`](generated/torch.linalg.inv.html#torch.linalg.inv) |
| [`det`](generated/torch.det.html#torch.det) | Alias for [`torch.linalg.det()`](generated/torch.linalg.det.html#torch.linalg.det) |
| [`logdet`](generated/torch.logdet.html#torch.logdet) | Calculates log determinant of a square matrix or batches of square matrices. |
| [`slogdet`](generated/torch.slogdet.html#torch.slogdet) | Alias for [`torch.linalg.slogdet()`](generated/torch.linalg.slogdet.html#torch.linalg.slogdet) |
| [`lu`](generated/torch.lu.html#torch.lu) | Computes the LU factorization of a matrix or batches of matrices `A`. |
| [`lu_solve`](generated/torch.lu_solve.html#torch.lu_solve) | Returns the LU solve of the linear system Ax=bAx = bAx=b using the partially pivoted LU factorization of A from [`lu_factor()`](generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor). |
| [`lu_unpack`](generated/torch.lu_unpack.html#torch.lu_unpack) | Unpacks the LU decomposition returned by [`lu_factor()`](generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor) into the P, L, U matrices. |
| [`matmul`](generated/torch.matmul.html#torch.matmul) | Matrix product of two tensors. |
| [`matrix_power`](generated/torch.matrix_power.html#torch.matrix_power) | Alias for [`torch.linalg.matrix_power()`](generated/torch.linalg.matrix_power.html#torch.linalg.matrix_power) |
| [`matrix_exp`](generated/torch.matrix_exp.html#torch.matrix_exp) | Alias for [`torch.linalg.matrix_exp()`](generated/torch.linalg.matrix_exp.html#torch.linalg.matrix_exp). |
| [`mm`](generated/torch.mm.html#torch.mm) | Performs a matrix multiplication of the matrices `input` and `mat2`. |
| [`mv`](generated/torch.mv.html#torch.mv) | Performs a matrix-vector product of the matrix `input` and the vector `vec`. |
| [`orgqr`](generated/torch.orgqr.html#torch.orgqr) | Alias for [`torch.linalg.householder_product()`](generated/torch.linalg.householder_product.html#torch.linalg.householder_product). |
| [`ormqr`](generated/torch.ormqr.html#torch.ormqr) | Computes the matrix-matrix multiplication of a product of Householder matrices with a general matrix. |
| [`outer`](generated/torch.outer.html#torch.outer) | Outer product of `input` and `vec2`. |
| [`pinverse`](generated/torch.pinverse.html#torch.pinverse) | Alias for [`torch.linalg.pinv()`](generated/torch.linalg.pinv.html#torch.linalg.pinv) |
| [`qr`](generated/torch.qr.html#torch.qr) | Computes the QR decomposition of a matrix or a batch of matrices `input`, and returns a namedtuple (Q, R) of tensors such that input=QR\text{input} = Q Rinput=QR with QQQ being an orthogonal matrix or batch of orthogonal matrices and RRR being an upper triangular matrix or batch of upper triangular matrices. |
| [`svd`](generated/torch.svd.html#torch.svd) | Computes the singular value decomposition of either a matrix or batch of matrices `input`. |
| [`svd_lowrank`](generated/torch.svd_lowrank.html#torch.svd_lowrank) | Return the singular value decomposition `(U, S, V)` of a matrix, batches of matrices, or a sparse matrix AAA such that A≈Udiag⁡(S)VHA \approx U \operatorname{diag}(S) V^{\text{H}}A≈Udiag(S)VH. |
| [`pca_lowrank`](generated/torch.pca_lowrank.html#torch.pca_lowrank) | Performs linear Principal Component Analysis (PCA) on a low-rank matrix, batches of such matrices, or sparse matrix. |
| [`lobpcg`](generated/torch.lobpcg.html#torch.lobpcg) | Find the k largest (or smallest) eigenvalues and the corresponding eigenvectors of a symmetric positive definite generalized eigenvalue problem using matrix-free LOBPCG methods. |
| [`trapz`](generated/torch.trapz.html#torch.trapz) | Alias for [`torch.trapezoid()`](generated/torch.trapezoid.html#torch.trapezoid). |
| [`trapezoid`](generated/torch.trapezoid.html#torch.trapezoid) | Computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) along `dim`. |
| [`cumulative_trapezoid`](generated/torch.cumulative_trapezoid.html#torch.cumulative_trapezoid) | Cumulatively computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) along `dim`. |
| [`triangular_solve`](generated/torch.triangular_solve.html#torch.triangular_solve) | Solves a system of equations with a square upper or lower triangular invertible matrix AAA and multiple right-hand sides bbb. |
| [`vdot`](generated/torch.vdot.html#torch.vdot) | Computes the dot product of two 1D vectors along a dimension. |

### Foreach Operations

Warning

This API is in beta and subject to future changes.
Forward-mode AD is not supported.

| [`_foreach_abs`](generated/torch._foreach_abs.html#torch._foreach_abs) | Apply [`torch.abs()`](generated/torch.abs.html#torch.abs) to each Tensor of the input list. |
| --- | --- |
| [`_foreach_abs_`](generated/torch._foreach_abs_.html#torch._foreach_abs_) | Apply [`torch.abs()`](generated/torch.abs.html#torch.abs) to each Tensor of the input list. |
| [`_foreach_acos`](generated/torch._foreach_acos.html#torch._foreach_acos) | Apply [`torch.acos()`](generated/torch.acos.html#torch.acos) to each Tensor of the input list. |
| [`_foreach_acos_`](generated/torch._foreach_acos_.html#torch._foreach_acos_) | Apply [`torch.acos()`](generated/torch.acos.html#torch.acos) to each Tensor of the input list. |
| [`_foreach_asin`](generated/torch._foreach_asin.html#torch._foreach_asin) | Apply [`torch.asin()`](generated/torch.asin.html#torch.asin) to each Tensor of the input list. |
| [`_foreach_asin_`](generated/torch._foreach_asin_.html#torch._foreach_asin_) | Apply [`torch.asin()`](generated/torch.asin.html#torch.asin) to each Tensor of the input list. |
| [`_foreach_atan`](generated/torch._foreach_atan.html#torch._foreach_atan) | Apply [`torch.atan()`](generated/torch.atan.html#torch.atan) to each Tensor of the input list. |
| [`_foreach_atan_`](generated/torch._foreach_atan_.html#torch._foreach_atan_) | Apply [`torch.atan()`](generated/torch.atan.html#torch.atan) to each Tensor of the input list. |
| [`_foreach_ceil`](generated/torch._foreach_ceil.html#torch._foreach_ceil) | Apply [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) to each Tensor of the input list. |
| [`_foreach_ceil_`](generated/torch._foreach_ceil_.html#torch._foreach_ceil_) | Apply [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) to each Tensor of the input list. |
| [`_foreach_clone`](generated/torch._foreach_clone.html#torch._foreach_clone) | |
| [`_foreach_cos`](generated/torch._foreach_cos.html#torch._foreach_cos) | Apply [`torch.cos()`](generated/torch.cos.html#torch.cos) to each Tensor of the input list. |
| [`_foreach_cos_`](generated/torch._foreach_cos_.html#torch._foreach_cos_) | Apply [`torch.cos()`](generated/torch.cos.html#torch.cos) to each Tensor of the input list. |
| [`_foreach_cosh`](generated/torch._foreach_cosh.html#torch._foreach_cosh) | Apply [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) to each Tensor of the input list. |
| [`_foreach_cosh_`](generated/torch._foreach_cosh_.html#torch._foreach_cosh_) | Apply [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) to each Tensor of the input list. |
| [`_foreach_erf`](generated/torch._foreach_erf.html#torch._foreach_erf) | Apply [`torch.erf()`](generated/torch.erf.html#torch.erf) to each Tensor of the input list. |
| [`_foreach_erf_`](generated/torch._foreach_erf_.html#torch._foreach_erf_) | Apply [`torch.erf()`](generated/torch.erf.html#torch.erf) to each Tensor of the input list. |
| [`_foreach_erfc`](generated/torch._foreach_erfc.html#torch._foreach_erfc) | Apply [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) to each Tensor of the input list. |
| [`_foreach_erfc_`](generated/torch._foreach_erfc_.html#torch._foreach_erfc_) | Apply [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) to each Tensor of the input list. |
| [`_foreach_exp`](generated/torch._foreach_exp.html#torch._foreach_exp) | Apply [`torch.exp()`](generated/torch.exp.html#torch.exp) to each Tensor of the input list. |
| [`_foreach_exp_`](generated/torch._foreach_exp_.html#torch._foreach_exp_) | Apply [`torch.exp()`](generated/torch.exp.html#torch.exp) to each Tensor of the input list. |
| [`_foreach_expm1`](generated/torch._foreach_expm1.html#torch._foreach_expm1) | Apply [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) to each Tensor of the input list. |
| [`_foreach_expm1_`](generated/torch._foreach_expm1_.html#torch._foreach_expm1_) | Apply [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) to each Tensor of the input list. |
| [`_foreach_floor`](generated/torch._foreach_floor.html#torch._foreach_floor) | Apply [`torch.floor()`](generated/torch.floor.html#torch.floor) to each Tensor of the input list. |
| [`_foreach_floor_`](generated/torch._foreach_floor_.html#torch._foreach_floor_) | Apply [`torch.floor()`](generated/torch.floor.html#torch.floor) to each Tensor of the input list. |
| [`_foreach_log`](generated/torch._foreach_log.html#torch._foreach_log) | Apply [`torch.log()`](generated/torch.log.html#torch.log) to each Tensor of the input list. |
| [`_foreach_log_`](generated/torch._foreach_log_.html#torch._foreach_log_) | Apply [`torch.log()`](generated/torch.log.html#torch.log) to each Tensor of the input list. |
| [`_foreach_log10`](generated/torch._foreach_log10.html#torch._foreach_log10) | Apply [`torch.log10()`](generated/torch.log10.html#torch.log10) to each Tensor of the input list. |
| [`_foreach_log10_`](generated/torch._foreach_log10_.html#torch._foreach_log10_) | Apply [`torch.log10()`](generated/torch.log10.html#torch.log10) to each Tensor of the input list. |
| [`_foreach_log1p`](generated/torch._foreach_log1p.html#torch._foreach_log1p) | Apply [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) to each Tensor of the input list. |
| [`_foreach_log1p_`](generated/torch._foreach_log1p_.html#torch._foreach_log1p_) | Apply [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) to each Tensor of the input list. |
| [`_foreach_log2`](generated/torch._foreach_log2.html#torch._foreach_log2) | Apply [`torch.log2()`](generated/torch.log2.html#torch.log2) to each Tensor of the input list. |
| [`_foreach_log2_`](generated/torch._foreach_log2_.html#torch._foreach_log2_) | Apply [`torch.log2()`](generated/torch.log2.html#torch.log2) to each Tensor of the input list. |
| [`_foreach_neg`](generated/torch._foreach_neg.html#torch._foreach_neg) | Apply [`torch.neg()`](generated/torch.neg.html#torch.neg) to each Tensor of the input list. |
| [`_foreach_neg_`](generated/torch._foreach_neg_.html#torch._foreach_neg_) | Apply [`torch.neg()`](generated/torch.neg.html#torch.neg) to each Tensor of the input list. |
| [`_foreach_tan`](generated/torch._foreach_tan.html#torch._foreach_tan) | Apply [`torch.tan()`](generated/torch.tan.html#torch.tan) to each Tensor of the input list. |
| [`_foreach_tan_`](generated/torch._foreach_tan_.html#torch._foreach_tan_) | Apply [`torch.tan()`](generated/torch.tan.html#torch.tan) to each Tensor of the input list. |
| [`_foreach_sin`](generated/torch._foreach_sin.html#torch._foreach_sin) | Apply [`torch.sin()`](generated/torch.sin.html#torch.sin) to each Tensor of the input list. |
| [`_foreach_sin_`](generated/torch._foreach_sin_.html#torch._foreach_sin_) | Apply [`torch.sin()`](generated/torch.sin.html#torch.sin) to each Tensor of the input list. |
| [`_foreach_sinh`](generated/torch._foreach_sinh.html#torch._foreach_sinh) | Apply [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) to each Tensor of the input list. |
| [`_foreach_sinh_`](generated/torch._foreach_sinh_.html#torch._foreach_sinh_) | Apply [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) to each Tensor of the input list. |
| [`_foreach_round`](generated/torch._foreach_round.html#torch._foreach_round) | Apply [`torch.round()`](generated/torch.round.html#torch.round) to each Tensor of the input list. |
| [`_foreach_round_`](generated/torch._foreach_round_.html#torch._foreach_round_) | Apply [`torch.round()`](generated/torch.round.html#torch.round) to each Tensor of the input list. |
| [`_foreach_sqrt`](generated/torch._foreach_sqrt.html#torch._foreach_sqrt) | Apply [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) to each Tensor of the input list. |
| [`_foreach_sqrt_`](generated/torch._foreach_sqrt_.html#torch._foreach_sqrt_) | Apply [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) to each Tensor of the input list. |
| [`_foreach_lgamma`](generated/torch._foreach_lgamma.html#torch._foreach_lgamma) | Apply [`torch.lgamma()`](generated/torch.lgamma.html#torch.lgamma) to each Tensor of the input list. |
| [`_foreach_lgamma_`](generated/torch._foreach_lgamma_.html#torch._foreach_lgamma_) | Apply [`torch.lgamma()`](generated/torch.lgamma.html#torch.lgamma) to each Tensor of the input list. |
| [`_foreach_frac`](generated/torch._foreach_frac.html#torch._foreach_frac) | Apply [`torch.frac()`](generated/torch.frac.html#torch.frac) to each Tensor of the input list. |
| [`_foreach_frac_`](generated/torch._foreach_frac_.html#torch._foreach_frac_) | Apply [`torch.frac()`](generated/torch.frac.html#torch.frac) to each Tensor of the input list. |
| [`_foreach_reciprocal`](generated/torch._foreach_reciprocal.html#torch._foreach_reciprocal) | Apply [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) to each Tensor of the input list. |
| [`_foreach_reciprocal_`](generated/torch._foreach_reciprocal_.html#torch._foreach_reciprocal_) | Apply [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) to each Tensor of the input list. |
| [`_foreach_sigmoid`](generated/torch._foreach_sigmoid.html#torch._foreach_sigmoid) | Apply [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) to each Tensor of the input list. |
| [`_foreach_sigmoid_`](generated/torch._foreach_sigmoid_.html#torch._foreach_sigmoid_) | Apply [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) to each Tensor of the input list. |
| [`_foreach_trunc`](generated/torch._foreach_trunc.html#torch._foreach_trunc) | Apply [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) to each Tensor of the input list. |
| [`_foreach_trunc_`](generated/torch._foreach_trunc_.html#torch._foreach_trunc_) | Apply [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) to each Tensor of the input list. |
| [`_foreach_zero_`](generated/torch._foreach_zero_.html#torch._foreach_zero_) | Apply `torch.zero()` to each Tensor of the input list. |

## Utilities

| [`compiled_with_cxx11_abi`](generated/torch.compiled_with_cxx11_abi.html#torch.compiled_with_cxx11_abi) | Returns whether PyTorch was built with _GLIBCXX_USE_CXX11_ABI=1 |
| --- | --- |
| [`result_type`](generated/torch.result_type.html#torch.result_type) | Returns the [`torch.dtype`](tensor_attributes.html#torch.dtype) that would result from performing an arithmetic operation on the provided input tensors. |
| [`can_cast`](generated/torch.can_cast.html#torch.can_cast) | Determines if a type conversion is allowed under PyTorch casting rules described in the type promotion [documentation](tensor_attributes.html#type-promotion-doc). |
| [`promote_types`](generated/torch.promote_types.html#torch.promote_types) | Returns the [`torch.dtype`](tensor_attributes.html#torch.dtype) with the smallest size and scalar kind that is not smaller nor of lower kind than either type1 or type2. |
| [`use_deterministic_algorithms`](generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) | Sets whether PyTorch operations must use "deterministic" algorithms. |
| [`are_deterministic_algorithms_enabled`](generated/torch.are_deterministic_algorithms_enabled.html#torch.are_deterministic_algorithms_enabled) | Returns True if the global deterministic flag is turned on. |
| [`is_deterministic_algorithms_warn_only_enabled`](generated/torch.is_deterministic_algorithms_warn_only_enabled.html#torch.is_deterministic_algorithms_warn_only_enabled) | Returns True if the global deterministic flag is set to warn only. |
| [`set_deterministic_debug_mode`](generated/torch.set_deterministic_debug_mode.html#torch.set_deterministic_debug_mode) | Sets the debug mode for deterministic operations. |
| [`get_deterministic_debug_mode`](generated/torch.get_deterministic_debug_mode.html#torch.get_deterministic_debug_mode) | Returns the current value of the debug mode for deterministic operations. |
| [`set_float32_matmul_precision`](generated/torch.set_float32_matmul_precision.html#torch.set_float32_matmul_precision) | Sets the internal precision of float32 matrix multiplications. |
| [`get_float32_matmul_precision`](generated/torch.get_float32_matmul_precision.html#torch.get_float32_matmul_precision) | Returns the current value of float32 matrix multiplication precision. |
| [`set_warn_always`](generated/torch.set_warn_always.html#torch.set_warn_always) | When this flag is False (default) then some PyTorch warnings may only appear once per process. |
| [`get_device_module`](generated/torch.get_device_module.html#torch.get_device_module) | Returns the module associated with a given device(e.g., torch.device('cuda'), "mtia:0", "xpu", ...). |
| [`is_warn_always_enabled`](generated/torch.is_warn_always_enabled.html#torch.is_warn_always_enabled) | Returns True if the global warn_always flag is turned on. |
| [`vmap`](generated/torch.vmap.html#torch.vmap) | vmap is the vectorizing map; `vmap(func)` returns a new function that maps `func` over some dimension of the inputs. |
| [`_assert`](generated/torch._assert.html#torch._assert) | A wrapper around Python's assert which is symbolically traceable. |
| [`typename`](generated/torch.typename.html#torch.typename) | String representation of the type of an object. |

## Symbolic Numbers

*class*torch.SymInt(*node*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L447)

Like an int (including magic methods), but redirects all operations on the
wrapped node. This is used in particular to symbolically record operations
in the symbolic shape workflow.

as_integer_ratio()[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L629)

Represent this int as an exact integer ratio

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[SymInt, [int](https://docs.python.org/3/library/functions.html#int)]

*class*torch.SymFloat(*node*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L644)

Like a float (including magic methods), but redirects all operations on the
wrapped node. This is used in particular to symbolically record operations
in the symbolic shape workflow.

as_integer_ratio()[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L744)

Represent this float as an exact integer ratio

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]

conjugate()[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L757)

Returns the complex conjugate of the float.

Return type:

*SymFloat*

hex()[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L761)

Returns the hexadecimal representation of the float.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

is_integer()[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L740)

Return True if the float is an integer.

*class*torch.SymBool(*node*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/__init__.py#L766)

Like a bool (including magic methods), but redirects all operations on the
wrapped node. This is used in particular to symbolically record operations
in the symbolic shape workflow.

Unlike regular bools, regular boolean operators will force extra guards instead
of symbolically evaluate. Use the bitwise operators instead to handle this.

| [`sym_float`](generated/torch.sym_float.html#torch.sym_float) | SymInt-aware utility for float casting. |
| --- | --- |
| [`sym_fresh_size`](generated/torch.sym_fresh_size.html#torch.sym_fresh_size) | |
| [`sym_int`](generated/torch.sym_int.html#torch.sym_int) | SymInt-aware utility for int casting. |
| [`sym_max`](generated/torch.sym_max.html#torch.sym_max) | SymInt-aware utility for max which avoids branching on a < b. |
| [`sym_min`](generated/torch.sym_min.html#torch.sym_min) | SymInt-aware utility for min(). |
| [`sym_not`](generated/torch.sym_not.html#torch.sym_not) | SymInt-aware utility for logical negation. |
| [`sym_ite`](generated/torch.sym_ite.html#torch.sym_ite) | SymInt-aware utility for ternary operator (`t if b else f`.) |
| [`sym_sqrt`](generated/torch.sym_sqrt.html#torch.sym_sqrt) | |
| [`sym_sum`](generated/torch.sym_sum.html#torch.sym_sum) | N-ary add which is faster to compute for long lists than iterated binary addition. |

## Export Path

Warning

This feature is a prototype and may have compatibility breaking changes in the future.

export
generated/exportdb/index

## Control Flow

Warning

This feature is a prototype and may have compatibility breaking changes in the future.

| [`cond`](generated/torch.cond.html#torch.cond) | Conditionally applies true_fn or false_fn. |
| --- | --- |

## Optimizations

| [`compile`](generated/torch.compile.html#torch.compile) | Optimizes given model/function using TorchDynamo and specified backend. |
| --- | --- |

[torch.compile documentation](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler.html)

## Operator Tags

*class*torch.Tag

Members:

core

cudagraph_unsafe

data_dependent_output

dynamic_output_shape

flexible_layout

generated

inplace_view

maybe_aliasing_or_mutating

needs_contiguous_strides

needs_exact_strides

needs_fixed_stride_order

nondeterministic_bitwise

nondeterministic_seeded

out_variant

pointwise

pt2_compliant_tag

reduction

view_copy

*property*name