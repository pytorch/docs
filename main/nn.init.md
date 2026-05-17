# torch.nn.init

Warning

All the functions in this module are intended to be used to initialize neural
network parameters, so they all run in [`torch.no_grad()`](generated/torch.no_grad.html#torch.no_grad) mode and will not
be taken into account by autograd.

torch.nn.init.calculate_gain(*nonlinearity*, *param=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L173)

Return the recommended gain value for the given nonlinearity function.

The values are as follows:

| nonlinearity | gain |
| --- | --- |
| Linear / Identity | 111 |
| Conv{1,2,3}D | 111 |
| Sigmoid | 111 |
| Tanh | 53\frac{5}{3}35​ |
| ReLU | 2\sqrt{2}2​ |
| Leaky Relu | 21+negative_slope2\sqrt{\frac{2}{1 + \text{negative\_slope}^2}}1+negative_slope22​​ |
| SELU | 34\frac{3}{4}43​ |

Warning

In order to implement [Self-Normalizing Neural Networks](https://papers.nips.cc/paper/2017/hash/5d44ee6f2c3f71b73125876103c8f6c4-Abstract.html),
you should use `nonlinearity='linear'` instead of `nonlinearity='selu'`.
This gives the initial weights a variance of `1 / N`,
which is necessary to induce a stable fixed point in the forward pass.
In contrast, the default gain for `SELU` sacrifices the normalization
effect for more stable gradient flow in rectangular layers.

Parameters:

- **nonlinearity** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'linear'**,**'conv1d'**,**'conv2d'**,**'conv3d'**,**'conv_transpose1d'**,**'conv_transpose2d'**,**'conv_transpose3d'**,**'sigmoid'**,**'tanh'**,**'relu'**,**'leaky_relu'**,**'selu'**]*) - the non-linear function (nn.functional name)
- **param** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - optional parameter for the non-linear function

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

Examples

```
>>> gain = nn.init.calculate_gain(
... "leaky_relu", 0.2
... ) # leaky_relu with negative_slope=0.2
```

torch.nn.init.uniform_(*tensor*, *a=0.0*, *b=1.0*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L247)

Fill the input Tensor with values drawn from the uniform distribution.

U(a,b)\mathcal{U}(a, b)U(a,b).

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **a** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the lower bound of the uniform distribution
- **b** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the upper bound of the uniform distribution
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.uniform_(w)
```

torch.nn.init.normal_(*tensor*, *mean=0.0*, *std=1.0*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L274)

Fill the input Tensor with values drawn from the normal distribution.

N(mean,std2)\mathcal{N}(\text{mean}, \text{std}^2)N(mean,std2).

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the mean of the normal distribution
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the standard deviation of the normal distribution
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.normal_(w)
```

torch.nn.init.constant_(*tensor*, *val*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L337)

Fill the input Tensor with the value val\text{val}val.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **val** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the value to fill the tensor with

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.constant_(w, 0.3)
```

torch.nn.init.ones_(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L355)

Fill the input Tensor with the scalar value 1.

Parameters:

**tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.ones_(w)
```

torch.nn.init.zeros_(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L368)

Fill the input Tensor with the scalar value 0.

Parameters:

**tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.zeros_(w)
```

torch.nn.init.eye_(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L381)

Fill the 2-dimensional input Tensor with the identity matrix.

Preserves the identity of the inputs in Linear layers, where as
many inputs are preserved as possible.

Parameters:

**tensor** ([*Tensor*](tensors.html#torch.Tensor)) - a 2-dimensional torch.Tensor

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.eye_(w)
```

torch.nn.init.dirac_(*tensor*, *groups=1*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L402)

Fill the {3, 4, 5}-dimensional input Tensor with the Dirac delta function.

Preserves the identity of the inputs in Convolutional
layers, where as many input channels are preserved as possible. In case
of groups>1, each group of channels preserves identity

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - a {3, 4, 5}-dimensional torch.Tensor
- **groups** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - number of groups in the conv layer (default: 1)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 16, 5, 5)
>>> nn.init.dirac_(w)
>>> w = torch.empty(3, 24, 5, 5)
>>> nn.init.dirac_(w, 3)
```

torch.nn.init.xavier_uniform_(*tensor*, *gain=1.0*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L479)

Fill the input Tensor with values using a Xavier uniform distribution.

The method is described in Understanding the difficulty of training
deep feedforward neural networks - Glorot, X. & Bengio, Y. (2010).
The resulting tensor will have values sampled from
U(−a,a)\mathcal{U}(-a, a)U(−a,a) where

a=gain×6fan_in+fan_outa = \text{gain} \times \sqrt{\frac{6}{\text{fan\_in} + \text{fan\_out}}}

a=gain×fan_in+fan_out6​​

Also known as Glorot initialization.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **gain** ([*float*](https://docs.python.org/3/library/functions.html#float)) - an optional scaling factor
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.xavier_uniform_(w, gain=nn.init.calculate_gain("relu"))
```

torch.nn.init.xavier_normal_(*tensor*, *gain=1.0*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L512)

Fill the input Tensor with values using a Xavier normal distribution.

The method is described in Understanding the difficulty of training deep feedforward
neural networks - Glorot, X. & Bengio, Y. (2010). The resulting tensor
will have values sampled from N(0,std2)\mathcal{N}(0, \text{std}^2)N(0,std2) where

std=gain×2fan_in+fan_out\text{std} = \text{gain} \times \sqrt{\frac{2}{\text{fan\_in} + \text{fan\_out}}}

std=gain×fan_in+fan_out2​​

Also known as Glorot initialization.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **gain** ([*float*](https://docs.python.org/3/library/functions.html#float)) - an optional scaling factor
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.xavier_normal_(w)
```

torch.nn.init.kaiming_uniform_(*tensor*, *a=0*, *mode='fan_in'*, *nonlinearity='leaky_relu'*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L554)

Fill the input Tensor with values using a Kaiming uniform distribution.

The method is described in Delving deep into rectifiers: Surpassing
human-level performance on ImageNet classification - He, K. et al. (2015).
The resulting tensor will have values sampled from
U(−bound,bound)\mathcal{U}(-\text{bound}, \text{bound})U(−bound,bound) where

bound=gain×3fan_mode\text{bound} = \text{gain} \times \sqrt{\frac{3}{\text{fan\_mode}}}

bound=gain×fan_mode3​​

Also known as He initialization.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **a** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the negative slope of the rectifier used after this layer (only
used with `'leaky_relu'`)
- **mode** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'fan_in'**,**'fan_out'**]*) - either `'fan_in'` (default) or `'fan_out'`. Choosing `'fan_in'`
preserves the magnitude of the variance of the weights in the
forward pass. Choosing `'fan_out'` preserves the magnitudes in the
backwards pass.
- **nonlinearity** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'linear'**,**'conv1d'**,**'conv2d'**,**'conv3d'**,**'conv_transpose1d'**,**'conv_transpose2d'**,**'conv_transpose3d'**,**'sigmoid'**,**'tanh'**,**'relu'**,**'leaky_relu'**,**'selu'**]*) - the non-linear function (nn.functional name),
recommended to use only with `'relu'` or `'leaky_relu'` (default).
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.kaiming_uniform_(w, mode="fan_in", nonlinearity="relu")
```

Note

Be aware that `fan_in` and `fan_out` are calculated assuming
that the weight matrix is used in a transposed manner,
(i.e., `x @ w.T` in `Linear` layers, where `w.shape = [fan_out, fan_in]`).
This is important for correct initialization.
If you plan to use `x @ w`, where `w.shape = [fan_in, fan_out]`,
pass in a transposed weight matrix, i.e. `nn.init.kaiming_uniform_(w.T, ...)`.

torch.nn.init.kaiming_normal_(*tensor*, *a=0*, *mode='fan_in'*, *nonlinearity='leaky_relu'*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L619)

Fill the input Tensor with values using a Kaiming normal distribution.

The method is described in Delving deep into rectifiers: Surpassing
human-level performance on ImageNet classification - He, K. et al. (2015).
The resulting tensor will have values sampled from
N(0,std2)\mathcal{N}(0, \text{std}^2)N(0,std2) where

std=gainfan_mode\text{std} = \frac{\text{gain}}{\sqrt{\text{fan\_mode}}}

std=fan_mode​gain​

Also known as He initialization.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **a** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the negative slope of the rectifier used after this layer (only
used with `'leaky_relu'`)
- **mode** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'fan_in'**,**'fan_out'**]*) - either `'fan_in'` (default) or `'fan_out'`. Choosing `'fan_in'`
preserves the magnitude of the variance of the weights in the
forward pass. Choosing `'fan_out'` preserves the magnitudes in the
backwards pass.
- **nonlinearity** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'linear'**,**'conv1d'**,**'conv2d'**,**'conv3d'**,**'conv_transpose1d'**,**'conv_transpose2d'**,**'conv_transpose3d'**,**'sigmoid'**,**'tanh'**,**'relu'**,**'leaky_relu'**,**'selu'**]*) - the non-linear function (nn.functional name),
recommended to use only with `'relu'` or `'leaky_relu'` (default).
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.kaiming_normal_(w, mode="fan_out", nonlinearity="relu")
```

Note

Be aware that `fan_in` and `fan_out` are calculated assuming
that the weight matrix is used in a transposed manner,
(i.e., `x @ w.T` in `Linear` layers, where `w.shape = [fan_out, fan_in]`).
This is important for correct initialization.
If you plan to use `x @ w`, where `w.shape = [fan_in, fan_out]`,
pass in a transposed weight matrix, i.e. `nn.init.kaiming_normal_(w.T, ...)`.

torch.nn.init.trunc_normal_(*tensor*, *mean=0.0*, *std=1.0*, *a=-2.0*, *b=2.0*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L301)

Fill the input Tensor with values drawn from a truncated normal distribution.

The values are effectively drawn from the
normal distribution N(mean,std2)\mathcal{N}(\text{mean}, \text{std}^2)N(mean,std2)
with values outside [a,b][a, b][a,b] redrawn until they are within
the bounds. The method used for generating the random values works
best when a≤mean≤ba \leq \text{mean} \leq ba≤mean≤b.

For reduced-precision types (`torch.float16` and `torch.bfloat16`),
sampling quality depends on the underlying `normal_()` and `uniform_()`
implementations which operate at higher internal precision to avoid
quantization artifacts.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **mean** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the mean of the normal distribution
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the standard deviation of the normal distribution
- **a** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the minimum cutoff value
- **b** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the maximum cutoff value
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.trunc_normal_(w)
```

torch.nn.init.orthogonal_(*tensor*, *gain=1*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L672)

Fill the input Tensor with a (semi) orthogonal matrix.

Described in Exact solutions to the nonlinear dynamics of learning in deep
linear neural networks - Saxe, A. et al. (2013). The input tensor must have
at least 2 dimensions, and for tensors with more than 2 dimensions the
trailing dimensions are flattened.

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor, where n≥2n \geq 2n≥2
- **gain** ([*float*](https://docs.python.org/3/library/functions.html#float)) - optional scaling factor
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.orthogonal_(w)
```

torch.nn.init.sparse_(*tensor*, *sparsity*, *std=0.01*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/init.py#L723)

Fill the 2D input Tensor as a sparse matrix.

The non-zero elements will be drawn from the normal distribution
N(0,0.01)\mathcal{N}(0, 0.01)N(0,0.01), as described in Deep learning via
Hessian-free optimization - Martens, J. (2010).

Parameters:

- **tensor** ([*Tensor*](tensors.html#torch.Tensor)) - an n-dimensional torch.Tensor
- **sparsity** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The fraction of elements in each column to be set to zero
- **std** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the standard deviation of the normal distribution used to generate
the non-zero values
- **generator** ([*Generator*](generated/torch.Generator.html#torch.Generator)*|**None*) - the torch Generator to sample from (default: None)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

Examples

```
>>> w = torch.empty(3, 5)
>>> nn.init.sparse_(w, sparsity=0.1)
```