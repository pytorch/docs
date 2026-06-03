# LinearCrossEntropyOptions

*class*torch.nn.LinearCrossEntropyOptions(*allow_retain_graph=False*, *batch_chunk_size=None*, *chunking_method='auto'*, *acc_policy='auto'*, *acc_dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/modules/linear_cross_entropy_options.py#L28)

Configuration for the chunked implementation of
`linear_cross_entropy()`.

The chunked implementation processes the batch dimension in pieces, so
the full `(num_batches, num_classes)` logits tensor is never
materialized - useful when `num_classes` is much larger than
`in_features` (e.g. LLM vocabulary heads). Pass `options=None` to
use the reference path; pass an instance of this class to opt in.

Zero-argument `LinearCrossEntropyOptions()` leaves
`acc_policy` and `chunking_method` set to `"auto"`,
resolved at call time from `_AUTO_DEFAULTS` (per-(device, dtype)
picks measured on A100 / x86 CPU); unlisted pairs fall back to
`("compact", "aspect_ratio:2")`.

Supports a subset of `linear_cross_entropy()`; unsupported
configurations fall through to the reference path with a warning.

Chunking is a win when `num_batches >= in_features` and
`num_classes > in_features`; below that, the reference path is
cheaper.

acc_dtype*: [dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/library/constants.html#None)*

Dtype for internal accumulation. `None` resolves at call time
to `torch.float32` under `acc_policy="auto"` with fp16/bf16
input on hardware with mixed-precision mm (CUDA SM 7.0+ for fp16,
SM 8.0+ for bf16, and CPU); otherwise to the input dtype.
Mixed-precision currently requires fp16/bf16 input with
`acc_dtype=torch.float32`.

acc_policy*: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['accurate', 'balanced', 'compact', 'auto']*

Precision/memory trade-off for the chunked path. Controls which
intermediates are kept in `acc_dtype` vs. the input dtype, and
whether the per-chunk weight-gradient scratch buffer is materialized.

- `"auto"` (default) - per-(device, dtype) pick from
`_AUTO_DEFAULTS`; unlisted pairs fall back to `"compact"`.
The fallback assumes a CUDA-like backend with hardware-native
low-precision matmul; pass `"accurate"` explicitly on backends
that emulate fp16/bf16 GEMMs via fp32 upcast.
- `"accurate"` - broadest use of `acc_dtype`; noticeably
better input-grad accuracy when chunk size is large relative to
`num_classes`. Highest peak memory and slowest of the chunked
policies on CUDA. Only chunked policy whose weight-grad matmul
runs in fp32 on CPU (other policies hit CPU's emulated
low-precision path, ~20-50x slower).
- `"balanced"` - `acc_dtype` only where needed for gradient
correctness; keeps a `(num_classes, in_features)`
`acc_dtype` scratch for cross-chunk weight-grad accumulation.
Same precision as `"accurate"` in bf16, slightly looser in fp16,
faster than `"accurate"` in both.
- `"compact"` - like `"balanced"` but drops the weight-grad
scratch and accumulates per-chunk directly via `addmm_` (cuBLAS
uses an fp32 internal accumulator, so bulk precision matches
`"balanced"`). Saves `num_classes * in_features *
sizeof(acc_dtype)` - typically several hundred MB for an LLM
head. On non-CUDA mixed-precision falls back to `"balanced"`.

Policy effects (`"balanced"` vs `"accurate"`) are visible only
when `acc_dtype` differs from the input dtype; `"compact"`
saves memory in both regimes.

allow_retain_graph*: [bool](https://docs.python.org/3/library/functions.html#bool)*

Allow `retain_graph=True` on backward.

When `False` (default), backward consumes pre-computed gradient
buffers in place; a second `.backward()` raises `RuntimeError`.

When `True`, the buffers are preserved at the cost of one extra
gradient-sized allocation per call.

Higher-order autograd (gradgrad, forward-mode AD) is unsupported.

Under [`torch.compile()`](torch.compile.html#torch.compile) this field is auto-promoted to `True`
because the default-mode second-backward guard relies on a ctx
mutation Dynamo doesn't preserve; the wrapper warns on the promotion.

batch_chunk_size*: [int](https://docs.python.org/3/library/functions.html#int) | [None](https://docs.python.org/3/library/constants.html#None)*

Batch rows per chunk. The op loops over
`ceil(num_batches / batch_chunk_size)` chunks; smaller values cut
peak memory but launch more kernels. Default `None` means a single
chunk. Cannot be combined with `chunking_method` - if both are
set and disagree, `ValueError` is raised.

chunking_method*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

Heuristic for picking `batch_chunk_size`.

- `"auto"` (default) - resolves to a per-(device, dtype) pick from
`_AUTO_DEFAULTS` at call time; falls back to
`"aspect_ratio:2"` for unlisted pairs.
- `"aspect_ratio"` - sizes each chunk so its
`(batch_chunk_size, num_classes)` logits buffer matches the
`(num_batches, in_features)` input in memory:
`next_pow2(ceil(num_batches / ceil(num_classes / in_features)))`.
Best when `num_classes >> in_features` (LLM vocab heads).
- `"aspect_ratio:N"` (`N >= 1`) - same, divided by `N`.
~N times less peak memory at the cost of N times more chunks.
- `None` - disables the heuristic; uses `batch_chunk_size`.