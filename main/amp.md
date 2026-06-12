# Automatic Mixed Precision package - torch.amp

`torch.amp` provides convenience methods for mixed precision,
where some operations use the `torch.float32` (`float`) datatype and other operations
use lower precision floating point datatype (`lower_precision_fp`): `torch.float16` (`half`) or `torch.bfloat16`. Some ops, like linear layers and convolutions,
are much faster in `lower_precision_fp`. Other ops, like reductions, often require the dynamic
range of `float32`. Mixed precision tries to match each op to its appropriate datatype.

Ordinarily, "automatic mixed precision training" with datatype of `torch.float16` uses `torch.autocast` and
`torch.amp.GradScaler` together, as shown in the [Automatic Mixed Precision examples](notes/amp_examples.html#amp-examples)
and [Automatic Mixed Precision recipe](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html).
However, `torch.autocast` and `torch.GradScaler` are modular, and may be used separately if desired.
As shown in the CPU example section of `torch.autocast`, "automatic mixed precision training/inference" on CPU with
datatype of `torch.bfloat16` only uses `torch.autocast`.

Warning

`torch.cuda.amp.autocast(args...)` and `torch.cpu.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast("cuda", args...)` or `torch.amp.autocast("cpu", args...)` instead.
`torch.cuda.amp.GradScaler(args...)` and `torch.cpu.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler("cuda", args...)` or `torch.amp.GradScaler("cpu", args...)` instead.

Warning

When combining AMP with `torch.compile`, note that the default
`torch._functorch.config.backward_pass_autocast` setting is
`"same_as_forward"`. This assumes the compiled backward runs under the same
autocast context as the compiled forward. If you follow AMP's recommended
training pattern and run backward outside autocast, set
`torch._functorch.config.backward_pass_autocast` to `"off"` for the
compiled region. See [torch.compile has different autograd semantics](user_guide/torch_compiler/torch.compiler_backward.html#compiler-backward) for details.

`torch.autocast` and `torch.cpu.amp.autocast` are new in version `1.10`.

## Autocasting

torch.amp.autocast_mode.is_autocast_available(*device_type*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/amp/autocast_mode.py#L28)

Return a bool indicating if autocast is available on `device_type`.

Parameters:

**device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type to use. Possible values are: 'cuda', 'cpu', 'mtia', 'maia', 'xpu', and so on.
The type is the same as the type attribute of a [`torch.device`](tensor_attributes.html#torch.device).
Thus, you may obtain the device type of a tensor using Tensor.device.type.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*class*torch.autocast(*device_type*, *dtype=None*, *enabled=True*, *cache_enabled=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/amp/autocast_mode.py#L52)

Instances of `autocast` serve as context managers or decorators that
allow regions of your script to run in mixed precision.

In these regions, ops run in an op-specific dtype chosen by autocast
to improve performance while maintaining accuracy.
See the Autocast Op Reference for details.

When entering an autocast-enabled region, Tensors may be any type.
You should not call `half()` or `bfloat16()` on your model(s) or inputs when using autocasting.

`autocast` should wrap only the forward pass(es) of your network, including the loss
computation(s). Backward passes under autocast are not recommended.
Backward ops run in the same type that autocast used for corresponding forward ops.

Example for CUDA Devices:

```
# Creates model and optimizer in default precision
model = Net().cuda()
optimizer = optim.SGD(model.parameters(), ...)

for input, target in data:
 optimizer.zero_grad()

 # Enables autocasting for the forward pass (model + loss)
 with torch.autocast(device_type="cuda"):
 output = model(input)
 loss = loss_fn(output, target)

 # Exits the context manager before backward()
 loss.backward()
 optimizer.step()
```

See the [Automatic Mixed Precision examples](notes/amp_examples.html#amp-examples) for usage (along with gradient scaling)
in more complex scenarios (e.g., gradient penalty, multiple models/losses, custom autograd functions).

`autocast` can also be used as a decorator, e.g., on the `forward` method of your model:

```
class AutocastModel(nn.Module):
 ...

 @torch.autocast(device_type="cuda")
 def forward(self, input): ...
```

Floating-point Tensors produced in an autocast-enabled region may be `float16`.
After returning to an autocast-disabled region, using them with floating-point
Tensors of different dtypes may cause type mismatch errors. If so, cast the Tensor(s)
produced in the autocast region back to `float32` (or other dtype if desired).
If a Tensor from the autocast region is already `float32`, the cast is a no-op,
and incurs no additional overhead.
CUDA Example:

```
# Creates some tensors in default dtype (here assumed to be float32)
a_float32 = torch.rand((8, 8), device="cuda")
b_float32 = torch.rand((8, 8), device="cuda")
c_float32 = torch.rand((8, 8), device="cuda")
d_float32 = torch.rand((8, 8), device="cuda")

with torch.autocast(device_type="cuda"):
 # torch.mm is on autocast's list of ops that should run in float16.
 # Inputs are float32, but the op runs in float16 and produces float16 output.
 # No manual casts are required.
 e_float16 = torch.mm(a_float32, b_float32)
 # Also handles mixed input types
 f_float16 = torch.mm(d_float32, e_float16)

# After exiting autocast, calls f_float16.float() to use with d_float32
g_float32 = torch.mm(d_float32, f_float16.float())
```

CPU Training Example:

```
# Creates model and optimizer in default precision
model = Net()
optimizer = optim.SGD(model.parameters(), ...)

for epoch in epochs:
 for input, target in data:
 optimizer.zero_grad()

 # Runs the forward pass with autocasting.
 with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
 output = model(input)
 loss = loss_fn(output, target)

 loss.backward()
 optimizer.step()
```

CPU Inference Example:

```
# Creates model in default precision
model = Net().eval()

with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
 for input in data:
 # Runs the forward pass with autocasting.
 output = model(input)
```

CPU Inference Example with Jit Trace:

```
class TestModel(nn.Module):
 def __init__(self, input_size, num_classes):
 super().__init__()
 self.fc1 = nn.Linear(input_size, num_classes)

 def forward(self, x):
 return self.fc1(x)

input_size = 2
num_classes = 2
model = TestModel(input_size, num_classes).eval()

# For now, we suggest to disable the Jit Autocast Pass,
# As the issue: https://github.com/pytorch/pytorch/issues/75956
torch._C._jit_set_autocast_mode(False)

with torch.cpu.amp.autocast(cache_enabled=False):
 model = torch.jit.trace(model, torch.randn(1, input_size))
model = torch.jit.freeze(model)
# Models Run
for _ in range(3):
 model(torch.randn(1, input_size))
```

Type mismatch errors *in* an autocast-enabled region are a bug; if this is what you observe,
please file an issue.

`autocast(enabled=False)` subregions can be nested in autocast-enabled regions.
Locally disabling autocast can be useful, for example, if you want to force a subregion
to run in a particular `dtype`. Disabling autocast gives you explicit control over
the execution type. In the subregion, inputs from the surrounding region
should be cast to `dtype` before use:

```
# Creates some tensors in default dtype (here assumed to be float32)
a_float32 = torch.rand((8, 8), device="cuda")
b_float32 = torch.rand((8, 8), device="cuda")
c_float32 = torch.rand((8, 8), device="cuda")
d_float32 = torch.rand((8, 8), device="cuda")

with torch.autocast(device_type="cuda"):
 e_float16 = torch.mm(a_float32, b_float32)
 with torch.autocast(device_type="cuda", enabled=False):
 # Calls e_float16.float() to ensure float32 execution
 # (necessary because e_float16 was created in an autocasted region)
 f_float32 = torch.mm(c_float32, e_float16.float())

 # No manual casts are required when re-entering the autocast-enabled region.
 # torch.mm again runs in float16 and produces float16 output, regardless of input types.
 g_float16 = torch.mm(d_float32, f_float32)
```

The autocast state is thread-local. If you want it enabled in a new thread, the context manager or decorator
must be invoked in that thread. This affects [`torch.nn.DataParallel`](generated/torch.nn.DataParallel.html#torch.nn.DataParallel) and
[`torch.nn.parallel.DistributedDataParallel`](generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel) when used with more than one GPU per process
(see [Working with Multiple GPUs](notes/amp_examples.html#amp-multigpu)).

Parameters:

- **device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**required*) - Device type to use. Possible values are: 'cuda', 'cpu', 'mtia', 'maia', 'xpu', and 'hpu'.
The type is the same as the type attribute of a [`torch.device`](tensor_attributes.html#torch.device).
Thus, you may obtain the device type of a tensor using Tensor.device.type.
- **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether autocasting should be enabled in the region.
Default: `True`
- **dtype** (*torch_dtype**,**optional*) - Data type for ops run in autocast. It uses the default value
(`torch.float16` for CUDA and `torch.bfloat16` for CPU), given by
[`get_autocast_dtype()`](generated/torch.get_autocast_dtype.html#torch.get_autocast_dtype), if [`dtype`](tensor_attributes.html#torch.dtype) is `None`.
Default: `None`
- **cache_enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether the weight cache inside autocast should be enabled.
Default: `True`

torch.amp.custom_fwd(*fwd=None*, ***, *device_type*, *cast_inputs=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/amp/autocast_mode.py#L441)

Create a helper decorator for `forward` methods of custom autograd functions.

Autograd functions are subclasses of [`torch.autograd.Function`](autograd.html#torch.autograd.Function).
See the [example page](notes/amp_examples.html#amp-custom-examples) for more detail.

Parameters:

- **device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type to use. 'cuda', 'cpu', 'mtia', 'maia', 'xpu' and so on.
The type is the same as the type attribute of a [`torch.device`](tensor_attributes.html#torch.device).
Thus, you may obtain the device type of a tensor using Tensor.device.type.
- **cast_inputs** ([`torch.dtype`](tensor_attributes.html#torch.dtype) or None, optional, default=None) - If not `None`,
when `forward` runs in an autocast-enabled region, casts incoming
floating-point Tensors to the target dtype (non-floating-point Tensors are not affected),
then executes `forward` with autocast disabled.
If `None`, `forward`'s internal ops execute with the current autocast state.

Note

If the decorated `forward` is called outside an autocast-enabled region,
`custom_fwd` is a no-op and `cast_inputs` has no effect.

torch.amp.custom_bwd(*bwd=None*, ***, *device_type*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/amp/autocast_mode.py#L500)

Create a helper decorator for backward methods of custom autograd functions.

Autograd functions are subclasses of [`torch.autograd.Function`](autograd.html#torch.autograd.Function).
Ensures that `backward` executes with the same autocast state as `forward`.
See the [example page](notes/amp_examples.html#amp-custom-examples) for more detail.

Parameters:

**device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Device type to use. 'cuda', 'cpu', 'mtia', 'maia', 'xpu' and so on.
The type is the same as the type attribute of a [`torch.device`](tensor_attributes.html#torch.device).
Thus, you may obtain the device type of a tensor using Tensor.device.type.

*class*torch.cuda.amp.autocast(*enabled=True*, *dtype=torch.float16*, *cache_enabled=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cuda/amp/autocast_mode.py#L13)

See `torch.autocast`.

`torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast("cuda", args...)` instead.

torch.cuda.amp.custom_fwd(*fwd=None*, ***, *cast_inputs=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cuda/amp/autocast_mode.py#L85)

`torch.cuda.amp.custom_fwd(args...)` is deprecated. Please use
`torch.amp.custom_fwd(args..., device_type='cuda')` instead.

torch.cuda.amp.custom_bwd(*bwd*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cuda/amp/autocast_mode.py#L100)

`torch.cuda.amp.custom_bwd(args...)` is deprecated. Please use
`torch.amp.custom_bwd(args..., device_type='cuda')` instead.

*class*torch.cpu.amp.autocast(*enabled=True*, *dtype=torch.bfloat16*, *cache_enabled=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cpu/amp/autocast_mode.py#L12)

See `torch.autocast`.
`torch.cpu.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast("cpu", args...)` instead.

## Gradient Scaling

If the forward pass for a particular op has `float16` inputs, the backward pass for
that op will produce `float16` gradients.
Gradient values with small magnitudes may not be representable in `float16`.
These values will flush to zero ("underflow"), so the update for the corresponding parameters will be lost.

To prevent underflow, "gradient scaling" multiplies the network's loss(es) by a scale factor and
invokes a backward pass on the scaled loss(es). Gradients flowing backward through the network are
then scaled by the same factor. In other words, gradient values have a larger magnitude,
so they don't flush to zero.

Each parameter's gradient (`.grad` attribute) should be unscaled before the optimizer
updates the parameters, so the scale factor does not interfere with the learning rate.

Note

AMP/fp16 may not work for every model! For example, most bf16-pretrained models cannot operate in
the fp16 numerical range of max 65504 and will cause gradients to overflow instead of underflow. In
this case, the scale factor may decrease under 1 as an attempt to bring gradients to a number
representable in the fp16 dynamic range. While one may expect the scale to always be above 1, our
GradScaler does NOT make this guarantee to maintain performance. If you encounter NaNs in your loss
or gradients when running with AMP/fp16, verify your model is compatible.

*class*torch.cuda.amp.GradScaler(*init_scale=65536.0*, *growth_factor=2.0*, *backoff_factor=0.5*, *growth_interval=2000*, *enabled=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cuda/amp/grad_scaler.py#L12)

See `torch.amp.GradScaler`.
`torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler("cuda", args...)` instead.

*class*torch.cpu.amp.GradScaler(*init_scale=65536.0*, *growth_factor=2.0*, *backoff_factor=0.5*, *growth_interval=2000*, *enabled=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cpu/amp/grad_scaler.py#L9)

See `torch.amp.GradScaler`.
`torch.cpu.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler("cpu", args...)` instead.

## Autocast Op Reference

### Op Eligibility

Ops that run in `float64` or non-floating-point dtypes are not eligible, and will
run in these types whether or not autocast is enabled.

Only out-of-place ops and Tensor methods are eligible.
In-place variants and calls that explicitly supply an `out=...` Tensor
are allowed in autocast-enabled regions, but won't go through autocasting.
For example, in an autocast-enabled region `a.addmm(b, c)` can autocast,
but `a.addmm_(b, c)` and `a.addmm(b, c, out=d)` cannot.
For best performance and stability, prefer out-of-place ops in autocast-enabled
regions.

Ops called with an explicit `dtype=...` argument are not eligible,
and will produce output that respects the `dtype` argument.

### CUDA Op-Specific Behavior

The following lists describe the behavior of eligible ops in autocast-enabled regions.
These ops always go through autocasting whether they are invoked as part of a [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module),
as a function, or as a [`torch.Tensor`](tensors.html#torch.Tensor) method. If functions are exposed in multiple namespaces,
they go through autocasting regardless of the namespace.

Ops not listed below do not go through autocasting. They run in the type
defined by their inputs. However, autocasting may still change the type
in which unlisted ops run if they're downstream from autocasted ops.

If an op is unlisted, we assume it's numerically stable in `float16`.
If you believe an unlisted op is numerically unstable in `float16`,
please file an issue.

#### CUDA Ops that can autocast to `float16`

`__matmul__`,
`addbmm`,
`addmm`,
`addmv`,
`addr`,
`baddbmm`,
`bmm`,
`chain_matmul`,
`multi_dot`,
`conv1d`,
`conv2d`,
`conv3d`,
`conv_transpose1d`,
`conv_transpose2d`,
`conv_transpose3d`,
`GRUCell`,
`linear`,
`LSTMCell`,
`matmul`,
`mm`,
`mv`,
`prelu`,
`RNNCell`

#### CUDA Ops that can autocast to `float32`

`__pow__`,
`__rdiv__`,
`__rpow__`,
`__rtruediv__`,
`acos`,
`asin`,
`binary_cross_entropy_with_logits`,
`cosh`,
`cosine_embedding_loss`,
`cdist`,
`cosine_similarity`,
`cross_entropy`,
`cumprod`,
`cumsum`,
`dist`,
`erfinv`,
`exp`,
`expm1`,
`group_norm`,
`hinge_embedding_loss`,
`kl_div`,
`l1_loss`,
`layer_norm`,
`log`,
`log_softmax`,
`log10`,
`log1p`,
`log2`,
`margin_ranking_loss`,
`mse_loss`,
`multilabel_margin_loss`,
`multi_margin_loss`,
`nll_loss`,
`norm`,
`normalize`,
`pdist`,
`poisson_nll_loss`,
`pow`,
`prod`,
`reciprocal`,
`rsqrt`,
`sinh`,
`smooth_l1_loss`,
`soft_margin_loss`,
`softmax`,
`softmin`,
`softplus`,
`sum`,
`renorm`,
`tan`,
`triplet_margin_loss`

#### CUDA Ops that promote to the widest input type

These ops don't require a particular dtype for stability, but take multiple inputs
and require that the inputs' dtypes match. If all of the inputs are
`float16`, the op runs in `float16`. If any of the inputs is `float32`,
autocast casts all inputs to `float32` and runs the op in `float32`.

`addcdiv`,
`addcmul`,
`atan2`,
`bilinear`,
`cross`,
`dot`,
`grid_sample`,
`index_put`,
`scatter_add`,
`tensordot`

Some ops not listed here (e.g., binary ops like `add`) natively promote
inputs without autocasting's intervention. If inputs are a mixture of `float16`
and `float32`, these ops run in `float32` and produce `float32` output,
regardless of whether autocast is enabled.

#### Prefer `binary_cross_entropy_with_logits` over `binary_cross_entropy`

The backward passes of [`torch.nn.functional.binary_cross_entropy()`](generated/torch.nn.functional.binary_cross_entropy.html#torch.nn.functional.binary_cross_entropy) (and [`torch.nn.BCELoss`](generated/torch.nn.BCELoss.html#torch.nn.BCELoss), which wraps it)
can produce gradients that aren't representable in `float16`. In autocast-enabled regions, the forward input
may be `float16`, which means the backward gradient must be representable in `float16` (autocasting `float16`
forward inputs to `float32` doesn't help, because that cast must be reversed in backward).
Therefore, `binary_cross_entropy` and `BCELoss` raise an error in autocast-enabled regions.

Many models use a sigmoid layer right before the binary cross entropy layer.
In this case, combine the two layers using [`torch.nn.functional.binary_cross_entropy_with_logits()`](generated/torch.nn.functional.binary_cross_entropy_with_logits.html#torch.nn.functional.binary_cross_entropy_with_logits)
or [`torch.nn.BCEWithLogitsLoss`](generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss). `binary_cross_entropy_with_logits` and `BCEWithLogits`
are safe to autocast.

### XPU Op-Specific Behavior (Experimental)

The following lists describe the behavior of eligible ops in autocast-enabled regions.
These ops always go through autocasting whether they are invoked as part of a [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module),
as a function, or as a [`torch.Tensor`](tensors.html#torch.Tensor) method. If functions are exposed in multiple namespaces,
they go through autocasting regardless of the namespace.

Ops not listed below do not go through autocasting. They run in the type
defined by their inputs. However, autocasting may still change the type
in which unlisted ops run if they're downstream from autocasted ops.

If an op is unlisted, we assume it's numerically stable in `float16`.
If you believe an unlisted op is numerically unstable in `float16`,
please file an issue.

#### XPU Ops that can autocast to `float16`

`addbmm`,
`addmm`,
`addmv`,
`addr`,
`baddbmm`,
`bmm`,
`chain_matmul`,
`multi_dot`,
`conv1d`,
`conv2d`,
`conv3d`,
`conv_transpose1d`,
`conv_transpose2d`,
`conv_transpose3d`,
`GRUCell`,
`linear`,
`LSTMCell`,
`matmul`,
`mm`,
`mv`,
`RNNCell`

#### XPU Ops that can autocast to `float32`

`__pow__`,
`__rdiv__`,
`__rpow__`,
`__rtruediv__`,
`binary_cross_entropy_with_logits`,
`cosine_embedding_loss`,
`cosine_similarity`,
`cumsum`,
`dist`,
`exp`,
`group_norm`,
`hinge_embedding_loss`,
`kl_div`,
`l1_loss`,
`layer_norm`,
`log`,
`log_softmax`,
`margin_ranking_loss`,
`nll_loss`,
`normalize`,
`poisson_nll_loss`,
`pow`,
`reciprocal`,
`rsqrt`,
`soft_margin_loss`,
`softmax`,
`softmin`,
`sum`,
`triplet_margin_loss`

#### XPU Ops that promote to the widest input type

These ops don't require a particular dtype for stability, but take multiple inputs
and require that the inputs' dtypes match. If all of the inputs are
`float16`, the op runs in `float16`. If any of the inputs is `float32`,
autocast casts all inputs to `float32` and runs the op in `float32`.

`bilinear`,
`cross`,
`grid_sample`,
`index_put`,
`scatter_add`,
`tensordot`

Some ops not listed here (e.g., binary ops like `add`) natively promote
inputs without autocasting's intervention. If inputs are a mixture of `float16`
and `float32`, these ops run in `float32` and produce `float32` output,
regardless of whether autocast is enabled.

### CPU Op-Specific Behavior

The following lists describe the behavior of eligible ops in autocast-enabled regions.
These ops always go through autocasting whether they are invoked as part of a [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module),
as a function, or as a [`torch.Tensor`](tensors.html#torch.Tensor) method. If functions are exposed in multiple namespaces,
they go through autocasting regardless of the namespace.

Ops not listed below do not go through autocasting. They run in the type
defined by their inputs. However, autocasting may still change the type
in which unlisted ops run if they're downstream from autocasted ops.

If an op is unlisted, we assume it's numerically stable in `bfloat16`.
If you believe an unlisted op is numerically unstable in `bfloat16`,
please file an issue. `float16` shares the lists of `bfloat16`.

#### CPU Ops that can autocast to `bfloat16`

`conv1d`,
`conv2d`,
`conv3d`,
`bmm`,
`mm`,
`linalg_vecdot`,
`baddbmm`,
`addmm`,
`addbmm`,
`linear`,
`matmul`,
`_convolution`,
`conv_tbc`,
`mkldnn_rnn_layer`,
`conv_transpose1d`,
`conv_transpose2d`,
`conv_transpose3d`,
`prelu`,
`scaled_dot_product_attention`,
`_native_multi_head_attention`

#### CPU Ops that can autocast to `float32`

`avg_pool3d`,
`binary_cross_entropy`,
`grid_sampler`,
`grid_sampler_2d`,
`_grid_sampler_2d_cpu_fallback`,
`grid_sampler_3d`,
`polar`,
`prod`,
`quantile`,
`nanquantile`,
`stft`,
`cdist`,
`trace`,
`view_as_complex`,
`cholesky_inverse`,
`cholesky_solve`,
`inverse`,
`lu_solve`,
`orgqr`,
`inverse`,
`ormqr`,
`pinverse`,
`max_pool3d`,
`max_unpool2d`,
`max_unpool3d`,
`adaptive_avg_pool3d`,
`reflection_pad1d`,
`reflection_pad2d`,
`replication_pad1d`,
`replication_pad2d`,
`replication_pad3d`,
`mse_loss`,
`cosine_embedding_loss`,
`nll_loss`,
`nll_loss2d`,
`hinge_embedding_loss`,
`poisson_nll_loss`,
`cross_entropy_loss`,
`l1_loss`,
`huber_loss`,
`margin_ranking_loss`,
`soft_margin_loss`,
`triplet_margin_loss`,
`multi_margin_loss`,
`ctc_loss`,
`kl_div`,
`multilabel_margin_loss`,
`binary_cross_entropy_with_logits`,
`fft_fft`,
`fft_ifft`,
`fft_fft2`,
`fft_ifft2`,
`fft_fftn`,
`fft_ifftn`,
`fft_rfft`,
`fft_irfft`,
`fft_rfft2`,
`fft_irfft2`,
`fft_rfftn`,
`fft_irfftn`,
`fft_hfft`,
`fft_ihfft`,
`linalg_cond`,
`linalg_matrix_rank`,
`linalg_solve`,
`linalg_cholesky`,
`linalg_svdvals`,
`linalg_eigvals`,
`linalg_eigvalsh`,
`linalg_inv`,
`linalg_householder_product`,
`linalg_tensorinv`,
`linalg_tensorsolve`,
`fake_quantize_per_tensor_affine`,
`geqrf`,
`_lu_with_info`,
`qr`,
`svd`,
`triangular_solve`,
`fractional_max_pool2d`,
`fractional_max_pool3d`,
`adaptive_max_pool3d`,
`multilabel_margin_loss_forward`,
`linalg_qr`,
`linalg_cholesky_ex`,
`linalg_svd`,
`linalg_eig`,
`linalg_eigh`,
`linalg_lstsq`,
`linalg_inv_ex`

#### CPU Ops that promote to the widest input type

These ops don't require a particular dtype for stability, but take multiple inputs
and require that the inputs' dtypes match. If all of the inputs are
`bfloat16`, the op runs in `bfloat16`. If any of the inputs is `float32`,
autocast casts all inputs to `float32` and runs the op in `float32`.

`cat`,
`stack`,
`index_copy`

Some ops not listed here (e.g., binary ops like `add`) natively promote
inputs without autocasting's intervention. If inputs are a mixture of `bfloat16`
and `float32`, these ops run in `float32` and produce `float32` output,
regardless of whether autocast is enabled.