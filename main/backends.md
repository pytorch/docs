# torch.backends

`torch.backends` controls the behavior of various backends that PyTorch supports.

These backends include:

- `torch.backends.cpu`
- `torch.backends.cuda`
- `torch.backends.cudnn`
- `torch.backends.cusparselt`
- `torch.backends.mha`
- `torch.backends.mps`
- `torch.backends.mkl`
- `torch.backends.mkldnn`
- `torch.backends.nnpack`
- `torch.backends.openmp`
- `torch.backends.opt_einsum`
- `torch.backends.python_native`
- `torch.backends.xeon`

## torch.backends.cpu

torch.backends.cpu.get_cpu_capability()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cpu/__init__.py#L9)

Return cpu capability as a string value.

Possible values:
- "DEFAULT"
- "VSX"
- "Z VECTOR"
- "NO AVX"
- "AVX2"
- "AVX512"
- "SVE256"

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

## torch.backends.cuda

torch.backends.cuda.is_built()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L43)

Return whether PyTorch is built with CUDA support.

Note that this doesn't necessarily mean CUDA is available; just that if this PyTorch
binary were run on a machine with working CUDA drivers and devices, we would be able to use it.

torch.backends.cuda.matmul.allow_tf32

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether TensorFloat-32 tensor cores may be used in matrix
multiplications on Ampere or newer GPUs. allow_tf32 is going to be deprecated. See [TensorFloat-32 (TF32) on Ampere (and later) devices](notes/cuda.html#tf32-on-ampere).

torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether reduced precision reductions (e.g.,
with fp16 accumulation type) are allowed with fp16 GEMMs.
For tuple assignment and split-k behavior, see
[Reduced Precision Reduction in FP16 GEMMs](notes/cuda.html#fp16reducedprecision).

torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction_split_k

A readonly [`bool`](https://docs.python.org/3/library/functions.html#bool) that reports whether split-K heuristics may be used
for fp16 GEMMs when dispatching to cuBLASLt. For how this value is
controlled, see
[Reduced Precision Reduction in FP16 GEMMs](notes/cuda.html#fp16reducedprecision).

torch.backends.cuda.matmul.prefer_cublaslt_grouped_gemm

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether supported grouped GEMMs prefer the
cuBLASLt backend.

torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether reduced precision reductions are
allowed with bf16 GEMMs.
For tuple assignment and split-k behavior, see
[Reduced Precision Reduction in BF16 GEMMs](notes/cuda.html#bf16reducedprecision).

torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction_split_k

A readonly [`bool`](https://docs.python.org/3/library/functions.html#bool) that reports whether split-K heuristics may be used
for bf16 GEMMs when dispatching to cuBLASLt. For how this value is
controlled, see
[Reduced Precision Reduction in BF16 GEMMs](notes/cuda.html#bf16reducedprecision).

torch.backends.cuda.cufft_plan_cache

`cufft_plan_cache` contains the cuFFT plan caches for each CUDA device.
Query a specific device i's cache via torch.backends.cuda.cufft_plan_cache[i].

torch.backends.cuda.cufft_plan_cache.size

A readonly [`int`](https://docs.python.org/3/library/functions.html#int) that shows the number of plans currently in a cuFFT plan cache.

torch.backends.cuda.cufft_plan_cache.max_size

A [`int`](https://docs.python.org/3/library/functions.html#int) that controls the capacity of a cuFFT plan cache.

torch.backends.cuda.cufft_plan_cache.clear()

Clears a cuFFT plan cache.

torch.backends.cuda.preferred_blas_library(*backend=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L296)

Override the library PyTorch uses for BLAS operations. Choose between cuBLAS, cuBLASLt, and CK [ROCm-only].

Warning

This flag is experimental and subject to change.

When PyTorch runs a CUDA BLAS operation it defaults to cuBLAS even if both cuBLAS and cuBLASLt are available.
For PyTorch built for ROCm, hipBLAS, hipBLASLt, and CK may offer different performance.
This flag (a [`str`](https://docs.python.org/3/library/stdtypes.html#str)) allows overriding which BLAS library to use.

- If "cublas" is set then cuBLAS will be used wherever possible.
- If "cublaslt" is set then cuBLASLt will be used wherever possible.
- If "ck" is set then CK will be used wherever possible.
- If "default" (the default) is set then heuristics will be used to pick between the other options.
- When no input is given, this function returns the currently preferred library.
- User may use the environment variable TORCH_BLAS_PREFER_CUBLASLT=1 to set the preferred library to cuBLASLt
globally.
This flag only sets the initial value of the preferred library and the preferred library
may still be overridden by this function call later in your script.

Note: When a library is preferred other libraries may still be used if the preferred library
doesn't implement the operation(s) called.
This flag may achieve better performance if PyTorch's library selection is incorrect
for your application's inputs.

Return type:

*_BlasBackend*

torch.backends.cuda.cublas_workspace_size(*size=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L340)

Query or set the cuBLAS workspace size in bytes.

When called with no arguments, returns the current workspace size.
When called with a size argument, sets the workspace size and returns the new value.
Setting the workspace size will take precedence over the CUBLAS_WORKSPACE_CONFIG environment variable.
Changes take effect lazily: only handles used after the change get new workspaces.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - workspace size in bytes. Must be non-negative.

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.backends.cuda.cublaslt_workspace_size(*size=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L359)

Query or set the cuBLASLt workspace size in bytes.

When called with no arguments, returns the current workspace size.
When called with a size argument, sets the workspace size and returns the new value.
Setting the workspace size will take precedence over the CUBLASLT_WORKSPACE_SIZE environment variable.
Changes take effect lazily: only handles used after the change get new workspaces.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - workspace size in bytes. Must be non-negative.

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.backends.cuda.blas_workspace_size(*size=None*, *backend=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L378)

Query or set the BLAS workspace size for a given backend.

Convenience wrapper that dispatches to `cublas_workspace_size()` or
`cublaslt_workspace_size()` depending on the backend.

When *backend* is `None` the current `preferred_blas_library()` is
used. `Default` is resolved to the platform's default backend (cuBLAS
on NVIDIA, potentially hipBLASLt on supported ROCm architectures).

Note

When `TORCH_CUBLASLT_UNIFIED_WORKSPACE` is enabled (the default on
open-source CUDA builds), the cuBLASLt workspace is capped at the
cuBLAS workspace size and physically reuses the same allocation.
Setting a large cuBLASLt workspace via this function will therefore
*not* increase memory beyond the cuBLAS workspace size.

Note

Setting the workspace size for the cublas backend will take precedence
over the CUBLAS_WORKSPACE_CONFIG environment variable, and setting the
workspace size for the cublaslt backend will take precedence over the
CUBLASLT_WORKSPACE_SIZE environment variable.

Parameters:

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - workspace size in bytes. Must be non-negative.
When omitted the current size is returned without modification.
- **backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**torch._C._BlasBackend**,**optional*) - which backend's
workspace to query/set. Accepts the same strings as
`preferred_blas_library()` (e.g. `"cublas"`, `"cublaslt"`).

Returns:

the current (or newly set) workspace size in bytes.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if the resolved backend is CK (no workspace concept).

torch.backends.cuda.preferred_rocm_fa_library(*backend=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L454)

[ROCm-only]
Override the backend PyTorch uses in ROCm environments for Flash Attention. Choose between AOTriton and CK

Warning

This flag is experimental and subject to change.

When Flash Attention is enabled and desired, PyTorch defaults to using AOTriton as the backend.
This flag (a [`str`](https://docs.python.org/3/library/stdtypes.html#str)) allows users to override this backend to use composable_kernel

- If "default" is set then the default backend will be used wherever possible. Currently AOTriton.
- If "aotriton" is set then AOTriton will be used wherever possible.
- If "ck" is set then CK will be used wherever possible.
- When no input is given, this function returns the currently preferred library.
- User may use the environment variable TORCH_ROCM_FA_PREFER_CK=1 to set the preferred library to CK
globally.

Note: When a library is preferred other libraries may still be used if the preferred library
doesn't implement the operation(s) called.
This flag may achieve better performance if PyTorch's library selection is incorrect
for your application's inputs.

Return type:

*_ROCmFABackend*

torch.backends.cuda.is_ck_sdpa_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L499)

Warning

This flag is beta and subject to change.

Returns whether composable_kernel may be used as the backend for
scaled-dot-product-attention.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.cuda.preferred_linalg_library(*backend=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L225)

Override the heuristic PyTorch uses to choose between cuSOLVER and MAGMA for CUDA linear algebra operations.

Warning

This flag is experimental and subject to change.

When PyTorch runs a CUDA linear algebra operation it often uses the cuSOLVER or MAGMA libraries,
and if both are available it decides which to use with a heuristic.
This flag (a [`str`](https://docs.python.org/3/library/stdtypes.html#str)) allows overriding those heuristics.

- If "cusolver" is set then cuSOLVER will be used wherever possible.
- If "magma" is set then MAGMA will be used wherever possible.
- If "default" (the default) is set then heuristics will be used to pick between
cuSOLVER and MAGMA if both are available.
- When no input is given, this function returns the currently preferred library.
- User may use the environment variable TORCH_LINALG_PREFER_CUSOLVER=1 to set the preferred library to cuSOLVER
globally.
This flag only sets the initial value of the preferred library and the preferred library
may still be overridden by this function call later in your script.

Note: When a library is preferred other libraries may still be used if the preferred library
doesn't implement the operation(s) called.
This flag may achieve better performance if PyTorch's heuristic library selection is incorrect
for your application's inputs.

Currently supported linalg operators:

- [`torch.linalg.inv()`](generated/torch.linalg.inv.html#torch.linalg.inv)
- [`torch.linalg.inv_ex()`](generated/torch.linalg.inv_ex.html#torch.linalg.inv_ex)
- [`torch.linalg.cholesky()`](generated/torch.linalg.cholesky.html#torch.linalg.cholesky)
- [`torch.linalg.cholesky_ex()`](generated/torch.linalg.cholesky_ex.html#torch.linalg.cholesky_ex)
- [`torch.cholesky_solve()`](generated/torch.cholesky_solve.html#torch.cholesky_solve)
- [`torch.cholesky_inverse()`](generated/torch.cholesky_inverse.html#torch.cholesky_inverse)
- [`torch.linalg.lu_factor()`](generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor)
- [`torch.linalg.lu()`](generated/torch.linalg.lu.html#torch.linalg.lu)
- [`torch.linalg.lu_solve()`](generated/torch.linalg.lu_solve.html#torch.linalg.lu_solve)
- [`torch.linalg.qr()`](generated/torch.linalg.qr.html#torch.linalg.qr)
- [`torch.linalg.eigh()`](generated/torch.linalg.eigh.html#torch.linalg.eigh)
- [`torch.linalg.eigvals()`](generated/torch.linalg.eigvals.html#torch.linalg.eigvals)
- [`torch.linalg.svd()`](generated/torch.linalg.svd.html#torch.linalg.svd)
- [`torch.linalg.svdvals()`](generated/torch.linalg.svdvals.html#torch.linalg.svdvals)

Return type:

*_LinalgBackend*

*class*torch.backends.cuda.SDPAParams

torch.backends.cuda.flash_sdp_enabled()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L510)

Warning

This flag is beta and subject to change.

Returns whether flash scaled dot product attention is enabled or not.

torch.backends.cuda.enable_mem_efficient_sdp(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L537)

Warning

This flag is beta and subject to change.

Enables or disables memory efficient scaled dot product attention.

torch.backends.cuda.mem_efficient_sdp_enabled()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L528)

Warning

This flag is beta and subject to change.

Returns whether memory efficient scaled dot product attention is enabled or not.

torch.backends.cuda.enable_flash_sdp(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L519)

Warning

This flag is beta and subject to change.

Enables or disables flash scaled dot product attention.

torch.backends.cuda.math_sdp_enabled()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L546)

Warning

This flag is beta and subject to change.

Returns whether math scaled dot product attention is enabled or not.

torch.backends.cuda.enable_math_sdp(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L555)

Warning

This flag is beta and subject to change.

Enables or disables math scaled dot product attention.

torch.backends.cuda.fp16_bf16_reduction_math_sdp_allowed()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L573)

Warning

This flag is beta and subject to change.

Returns whether fp16/bf16 reduction in math scaled dot product attention is enabled or not.

torch.backends.cuda.allow_fp16_bf16_reduction_math_sdp(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L564)

Warning

This flag is beta and subject to change.

Enables or disables fp16/bf16 reduction in math scaled dot product attention.

torch.backends.cuda.cudnn_sdp_enabled()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L655)

Warning

This flag is beta and subject to change.

Returns whether cuDNN scaled dot product attention is enabled or not.

torch.backends.cuda.enable_cudnn_sdp(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L664)

Warning

This flag is beta and subject to change.

Enables or disables cuDNN scaled dot product attention.

torch.backends.cuda.is_flash_attention_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L582)

Check if PyTorch was built with FlashAttention for scaled_dot_product_attention.

Returns:

True if FlashAttention is built and available; otherwise, False.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False
in non-CUDA environments.

torch.backends.cuda.can_use_flash_attention(*params*, *debug=False*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L595)

Check if FlashAttention can be utilized in scaled_dot_product_attention.

Parameters:

- **params** (*_SDPAParams*) - An instance of SDPAParams containing the tensors for query,
key, value, an optional attention mask, dropout rate, and
a flag indicating if the attention is causal.
- **debug** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to logging.warn debug information as to why FlashAttention could not be run.
Defaults to False.

Returns:

True if FlashAttention can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False
in non-CUDA environments.

torch.backends.cuda.can_use_efficient_attention(*params*, *debug=False*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L615)

Check if efficient_attention can be utilized in scaled_dot_product_attention.

Parameters:

- **params** (*_SDPAParams*) - An instance of SDPAParams containing the tensors for query,
key, value, an optional attention mask, dropout rate, and
a flag indicating if the attention is causal.
- **debug** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to logging.warn with information as to why efficient_attention could not be run.
Defaults to False.

Returns:

True if efficient_attention can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False
in non-CUDA environments.

torch.backends.cuda.can_use_cudnn_attention(*params*, *debug=False*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L635)

Check if cudnn_attention can be utilized in scaled_dot_product_attention.

Parameters:

- **params** (*_SDPAParams*) - An instance of SDPAParams containing the tensors for query,
key, value, an optional attention mask, dropout rate, and
a flag indicating if the attention is causal.
- **debug** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to logging.warn with information as to why cuDNN attention could not be run.
Defaults to False.

Returns:

True if cuDNN can be used with the given parameters; otherwise, False.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Note

This function is dependent on a CUDA-enabled build of PyTorch. It will return False
in non-CUDA environments.

torch.backends.cuda.sdp_kernel(*enable_flash=True*, *enable_math=True*, *enable_mem_efficient=True*, *enable_cudnn=True*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cuda/__init__.py#L673)

Warning

This flag is beta and subject to change.

This context manager can be used to temporarily enable or disable any of the three backends for scaled dot product attention.
Upon exiting the context manager, the previous state of the flags will be restored.

## torch.backends.cudnn

torch.backends.cudnn.version()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cudnn/__init__.py#L110)

Return the version of cuDNN.

torch.backends.cudnn.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cudnn/__init__.py#L124)

Return a bool indicating if CUDNN is currently available.

torch.backends.cudnn.enabled

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether cuDNN is enabled.

torch.backends.cudnn.allow_tf32

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls where TensorFloat-32 tensor cores may be used in cuDNN
convolutions on Ampere or newer GPUs. allow_tf32 is going to be deprecated. See [TensorFloat-32 (TF32) on Ampere (and later) devices](notes/cuda.html#tf32-on-ampere).

torch.backends.cudnn.deterministic

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that, if True, causes cuDNN to only use deterministic convolution algorithms.
See also [`torch.are_deterministic_algorithms_enabled()`](generated/torch.are_deterministic_algorithms_enabled.html#torch.are_deterministic_algorithms_enabled) and
[`torch.use_deterministic_algorithms()`](generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms).

torch.backends.cudnn.benchmark

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that, if True, causes cuDNN to benchmark multiple convolution algorithms
and select the fastest.

torch.backends.cudnn.benchmark_limit

A [`int`](https://docs.python.org/3/library/functions.html#int) that specifies the maximum number of cuDNN convolution algorithms to try when
torch.backends.cudnn.benchmark is True. Set benchmark_limit to zero to try every
available algorithm. Note that this setting only affects convolutions dispatched via the
cuDNN v8 API.

## torch.backends.cusparselt

torch.backends.cusparselt.version()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cusparselt/__init__.py#L42)

Return the version of cuSPARSELt

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | None

torch.backends.cusparselt.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cusparselt/__init__.py#L49)

Return a bool indicating if cuSPARSELt is currently available.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.cusparselt.get_max_alg_id()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/cusparselt/__init__.py#L54)

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | None

## torch.backends.mha

torch.backends.mha.get_fastpath_enabled()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mha/__init__.py#L9)

Returns whether fast path for TransformerEncoder and MultiHeadAttention
is enabled, or `True` if jit is scripting.

Note

The fastpath might not be run even if `get_fastpath_enabled` returns
`True` unless all conditions on inputs are met.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.mha.set_fastpath_enabled(*value*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mha/__init__.py#L22)

Sets whether fast path is enabled

## torch.backends.miopen

torch.backends.miopen.immediate

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that, if True, causes MIOpen to use Immediate Mode
([https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html](https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html)).

## torch.backends.mps

torch.backends.mps.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L28)

Return a bool indicating if MPS is currently available.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.mps.is_built()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L18)

Return whether PyTorch is built with MPS support.

Note that this doesn't necessarily mean MPS is available; just that
if this PyTorch binary were run on a machine with working MPS drivers
and devices, we would be able to use it.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.mps.get_core_count()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L52)

Return GPU core count.

According to the documentation, one core is comprised of 16 Execution Units.
One execution Unit has 8 ALUs.
And one ALU can run 24 threads, i.e. one core is capable of executing 3072 threads concurrently.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

torch.backends.mps.get_name()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L46)

Return Metal device name

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

torch.backends.mps.is_macos13_or_newer(*minor=0*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L40)

Return a bool indicating whether MPS is running on MacOS 13 or newer.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.mps.is_macos_or_newer(*major*, *minor*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mps/__init__.py#L34)

Return a bool indicating whether MPS is running on given MacOS or newer.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

## torch.backends.mkl

torch.backends.mkl.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mkl/__init__.py#L5)

Return whether PyTorch is built with MKL support.

*class*torch.backends.mkl.verbose(*enable*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mkl/__init__.py#L14)

On-demand oneMKL verbosing functionality.

To make it easier to debug performance issues, oneMKL can dump verbose
messages containing execution information like duration while executing
the kernel. The verbosing functionality can be invoked via an environment
variable named MKL_VERBOSE. However, this methodology dumps messages in
all steps. Those are a large amount of verbose messages. Moreover, for
investigating the performance issues, generally taking verbose messages
for one single iteration is enough. This on-demand verbosing functionality
makes it possible to control scope for verbose message dumping. In the
following example, verbose messages will be dumped out for the second
inference only.

```
import torch

model(data)
with torch.backends.mkl.verbose(torch.backends.mkl.VERBOSE_ON):
 model(data)
```

Parameters:

**level** - Verbose level
- `VERBOSE_OFF`: Disable verbosing
- `VERBOSE_ON`: Enable verbosing

## torch.backends.mkldnn

torch.backends.mkldnn.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mkldnn/__init__.py#L114)

*class*torch.backends.mkldnn.verbose(*level*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/mkldnn/__init__.py#L33)

On-demand oneDNN (former MKL-DNN) verbosing functionality.

To make it easier to debug performance issues, oneDNN can dump verbose
messages containing information like kernel size, input data size and
execution duration while executing the kernel. The verbosing functionality
can be invoked via an environment variable named DNNL_VERBOSE. However,
this methodology dumps messages in all steps. Those are a large amount of
verbose messages. Moreover, for investigating the performance issues,
generally taking verbose messages for one single iteration is enough.
This on-demand verbosing functionality makes it possible to control scope
for verbose message dumping. In the following example, verbose messages
will be dumped out for the second inference only.

```
import torch

model(data)
with torch.backends.mkldnn.verbose(torch.backends.mkldnn.VERBOSE_ON):
 model(data)
```

Parameters:

**level** - Verbose level
- `VERBOSE_OFF`: Disable verbosing
- `VERBOSE_ON`: Enable verbosing
- `VERBOSE_ON_CREATION`: Enable verbosing, including oneDNN kernel creation

## torch.backends.nnpack

torch.backends.nnpack.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/nnpack/__init__.py#L11)

Return whether PyTorch is built with NNPACK support.

torch.backends.nnpack.flags(*enabled=False*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/nnpack/__init__.py#L23)

Context manager for setting if nnpack is enabled globally

torch.backends.nnpack.set_flags(*_enabled*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/nnpack/__init__.py#L16)

Set if nnpack is enabled globally

## torch.backends.openmp

torch.backends.openmp.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/openmp/__init__.py#L5)

Return whether PyTorch is built with OpenMP support.

torch.backends.kleidiai.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/kleidiai/__init__.py#L5)

Return whether PyTorch is built with KleidiAI support.

## torch.backends.opt_einsum

torch.backends.opt_einsum.is_available()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/opt_einsum/__init__.py#L17)

Return a bool indicating if opt_einsum is currently available.

You must install opt-einsum in order for torch to automatically optimize einsum. To
make opt-einsum available, you can install it along with torch: `pip install torch[opt-einsum]`
or by itself: `pip install opt-einsum`. If the package is installed, torch will import
it automatically and use it accordingly. Use this function to check whether opt-einsum
was installed and properly imported by torch.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

torch.backends.opt_einsum.get_opt_einsum()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/opt_einsum/__init__.py#L30)

Return the opt_einsum package if opt_einsum is currently available, else None.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

torch.backends.opt_einsum.enabled

A [`bool`](https://docs.python.org/3/library/functions.html#bool) that controls whether opt_einsum is enabled (`True` by default). If so,
torch.einsum will use opt_einsum ([https://optimized-einsum.readthedocs.io/en/stable/path_finding.html](https://optimized-einsum.readthedocs.io/en/stable/path_finding.html))
if available to calculate an optimal path of contraction for faster performance.

If opt_einsum is not available, torch.einsum will fall back to the default contraction path
of left to right.

torch.backends.opt_einsum.strategy

A [`str`](https://docs.python.org/3/library/stdtypes.html#str) that specifies which strategies to try when `torch.backends.opt_einsum.enabled`
is `True`. By default, torch.einsum will try the "auto" strategy, but the "greedy" and "optimal"
strategies are also supported. Note that the "optimal" strategy is factorial on the number of
inputs as it tries all possible paths. See more details in opt_einsum's docs
([https://optimized-einsum.readthedocs.io/en/stable/path_finding.html](https://optimized-einsum.readthedocs.io/en/stable/path_finding.html)).

## torch.backends.python_native

The `torch.backends.python_native` module provides user control over native operators implemented in python
via. DSLs (Domain Specific Languages) that are defined in `torch._native`. This allows users to selectively
enable or disable high-performance implementations from various DSLs like Triton and CuteDSL.

### Module-level Functions

torch.backends.python_native.get_dsl_operations(*dsl_name*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L206)

Get list of operations registered by a specific DSL.

Parameters:

**dsl_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the DSL to query (e.g., 'triton', 'cutedsl').

Returns:

Sorted list of operation names registered by the DSL.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

Example:

```
ops = torch.backends.python_native.get_dsl_operations("triton")
print(ops) # ['triton_to_mxfp8_dim0', ...]
```

torch.backends.python_native.disable_operations(**op_symbols*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L224)

Disable specific operations across all DSLs.

Parameters:

***op_symbols** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Names of operations to disable.

Example:

```
# Disable scaled matrix multiply across all DSLs
torch.backends.python_native.disable_operations("scaled_mm")

# Disable multiple operations
torch.backends.python_native.disable_operations(
 "scaled_mm", "flash_attention"
)
```

torch.backends.python_native.enable_operations(**op_symbols*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L243)

Re-enable specific operations across all DSLs.

Parameters:

***op_symbols** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Names of operations to re-enable.

Example:

```
# Re-enable previously disabled operations
torch.backends.python_native.enable_operations(
 "scaled_mm", "flash_attention"
)
```

torch.backends.python_native.disable_dispatch_keys(**dispatch_keys*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L259)

Disable operations at specific dispatch keys.

Parameters:

***dispatch_keys** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Dispatch keys to disable (e.g., 'CUDA', 'CPU').

Example:

```
# Disable all native operations on CUDA
torch.backends.python_native.disable_dispatch_keys("CUDA")
```

torch.backends.python_native.enable_dispatch_keys(**dispatch_keys*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L273)

Re-enable operations at specific dispatch keys.

Parameters:

***dispatch_keys** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Dispatch keys to re-enable (e.g., 'CUDA', 'CPU').

Example:

```
# Re-enable native operations on CUDA
torch.backends.python_native.enable_dispatch_keys("CUDA")
```

torch.backends.python_native.operations_disabled(**op_symbols*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/python_native/__init__.py#L287)

Context manager to temporarily disable operations.

Parameters:

***op_symbols** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Names of operations to temporarily disable.

Example:

```
with torch.backends.python_native.operations_disabled("scaled_mm"):
 # scaled_mm is disabled across all DSLs
 result = model(input)
# scaled_mm is automatically re-enabled here
```

### Module-level Properties

torch.backends.python_native.available_dsls

A [`list`](https://docs.python.org/3/library/stdtypes.html#list) of [`str`](https://docs.python.org/3/library/stdtypes.html#str) containing the names of DSLs that are available at runtime.
This is a subset of `all_dsls` that have their runtime dependencies satisfied.

torch.backends.python_native.all_dsls

A [`list`](https://docs.python.org/3/library/stdtypes.html#list) of [`str`](https://docs.python.org/3/library/stdtypes.html#str) containing the names of all registered DSLs, whether
available at runtime or not.

### DSL Controllers

For each registered DSL (e.g., `triton`, `cutedsl`), auto-populated controller modules are available:

#### DSL Properties

Each DSL controller (e.g., `torch.backends.python_native.triton`) provides the following properties:

| Property | Type | Description |
| --- | --- | --- |
| `name` | `str` | The name of the DSL |
| `available` | `bool` | Whether the DSL's runtime dependencies are available |
| `enabled` | `bool` | Controls whether all operations from this DSL are enabled. Setting to `False` disables all operations from the DSL, while `True` re-enables them |
| `version` | `Version` or `None` | The version of the DSL runtime, if available. Returns `None` if the DSL is not available |

#### DSL Methods

Each DSL controller provides the following methods:

**disable()**
Disable all operations from this DSL.

**enable()**
Re-enable all operations from this DSL.

**disabled()**
Context manager that temporarily disables all operations from this DSL.
Operations are automatically re-enabled when exiting the context.

```
Example::

 with torch.backends.python_native.triton.disabled():
 # Triton operations are disabled here
 result = model(input)
 # Triton operations restored here
```

### Usage Examples

```
import torch.backends.python_native as pn

# Query available DSLs
print(pn.available_dsls) # ['triton', 'cutedsl']

# Disable all Triton operations
pn.triton.enabled = False

# Temporarily disable CuteDSL operations
with pn.cutedsl.disabled():
 result = model(input) # CuteDSL ops disabled

# Disable specific operations across all DSLs
pn.disable_operations('scaled_mm', '_flash_attention_forward')

# Query operations for a specific DSL
triton_ops = pn.get_dsl_operations('triton')
```

## torch.backends.xeon

torch.backends.xeon.run_cpu.create_args(*parser=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/backends/xeon/run_cpu.py#L842)

Parse the command line options.

@retval ArgumentParser