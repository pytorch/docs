# torch.special

The torch.special module, modeled after SciPy's [special](https://docs.scipy.org/doc/scipy/reference/special.html) module.

## Functions

torch.special.airy_ai(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L982)

Airy function Ai(input)\text{Ai}\left(\text{input}\right)Ai(input).

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.bessel_j0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L999)

Bessel function of the first kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.bessel_j1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1016)

Bessel function of the first kind of order 111.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.bessel_y0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1033)

Bessel function of the second kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.bessel_y1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1050)

Bessel function of the second kind of order 111.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.chebyshev_polynomial_t(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1067)

Chebyshev polynomial of the first kind Tn(input)T_{n}(\text{input})Tn​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1, input\text{input}input
is returned. If n<6n < 6n<6 or ∣input∣>1|\text{input}| > 1∣input∣>1 the recursion:

Tn+1(input)=2×input×Tn(input)−Tn−1(input)T_{n + 1}(\text{input}) = 2 \times \text{input} \times T_{n}(\text{input}) - T_{n - 1}(\text{input})

Tn+1​(input)=2×input×Tn​(input)−Tn−1​(input)

is evaluated. Otherwise, the explicit trigonometric formula:

Tn(input)=cos(n×arccos(x))T_{n}(\text{input}) = \text{cos}(n \times \text{arccos}(x))

Tn​(input)=cos(n×arccos(x))

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.chebyshev_polynomial_u(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1098)

Chebyshev polynomial of the second kind Un(input)U_{n}(\text{input})Un​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1,
2×input2 \times \text{input}2×input is returned. If n<6n < 6n<6 or
∣input∣>1|\text{input}| > 1∣input∣>1, the recursion:

Un+1(input)=2×input×Un(input)−Un−1(input)U_{n + 1}(\text{input}) = 2 \times \text{input} \times U_{n}(\text{input}) - U_{n - 1}(\text{input})

Un+1​(input)=2×input×Un​(input)−Un−1​(input)

is evaluated. Otherwise, the explicit trigonometric formula:

sin((n+1)×arccos(input))sin(arccos(input))\frac{\text{sin}((n + 1) \times \text{arccos}(\text{input}))}{\text{sin}(\text{arccos}(\text{input}))}

sin(arccos(input))sin((n+1)×arccos(input))​

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.chebyshev_polynomial_v(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1130)

Chebyshev polynomial of the third kind Vn∗(input)V_{n}^{\ast}(\text{input})Vn∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.chebyshev_polynomial_w(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1148)

Chebyshev polynomial of the fourth kind Wn∗(input)W_{n}^{\ast}(\text{input})Wn∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.digamma(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L109)

Computes the logarithmic derivative of the gamma function on input.

ϝ(x)=ddxln⁡(Γ(x))=Γ′(x)Γ(x)\digamma(x) = \frac{d}{dx} \ln\left(\Gamma\left(x\right)\right) = \frac{\Gamma'(x)}{\Gamma(x)}

ϝ(x)=dxd​ln(Γ(x))=Γ(x)Γ′(x)​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the tensor to compute the digamma function on

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Note

This function is similar to SciPy's scipy.special.digamma.

Note

From PyTorch 1.8 onwards, the digamma function returns -Inf for 0.
Previously it returned NaN for 0.

Example:

```
>>> a = torch.tensor([1, 0.5])
>>> torch.special.digamma(a)
tensor([-0.5772, -1.9635])
```

torch.special.entr(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L67)

Computes the entropy on `input` (as defined below), elementwise.

entr(x)={−x∗ln⁡(x)x>00x=0.0−∞x<0\begin{align}
\text{entr(x)} = \begin{cases}
 -x * \ln(x) & x > 0 \\
 0 & x = 0.0 \\
 -\infty & x < 0
\end{cases}
\end{align}

entr(x)=⎩⎨⎧​−x∗ln(x)0−∞​x>0x=0.0x<0​​​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.arange(-0.5, 1, 0.5)
>>> a
tensor([-0.5000, 0.0000, 0.5000])
>>> torch.special.entr(a)
tensor([ -inf, 0.0000, 0.3466])
```

torch.special.erf(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L202)

Computes the error function of `input`. The error function is defined as follows:

erf(x)=2π∫0xe−t2dt\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} dt

erf(x)=π​2​∫0x​e−t2dt
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.erf(torch.tensor([0, -1., 10.]))
tensor([ 0.0000, -0.8427, 1.0000])
```

torch.special.erfc(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L226)

Computes the complementary error function of `input`.
The complementary error function is defined as follows:

erfc(x)=1−2π∫0xe−t2dt\mathrm{erfc}(x) = 1 - \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} dt

erfc(x)=1−π​2​∫0x​e−t2dt
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.erfc(torch.tensor([0, -1., 10.]))
tensor([ 1.0000, 1.8427, 0.0000])
```

torch.special.erfcx(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L251)

Computes the scaled complementary error function for each element of `input`.
The scaled complementary error function is defined as follows:

erfcx(x)=ex2erfc(x)\mathrm{erfcx}(x) = e^{x^2} \mathrm{erfc}(x)

erfcx(x)=ex2erfc(x)
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.erfcx(torch.tensor([0, -1., 10.]))
tensor([ 1.0000, 5.0090, 0.0561])
```

torch.special.erfinv(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L279)

Computes the inverse error function of `input`.
The inverse error function is defined in the range (−1,1)(-1, 1)(−1,1) as:

erfinv(erf(x))=x\mathrm{erfinv}(\mathrm{erf}(x)) = x

erfinv(erf(x))=x
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.erfinv(torch.tensor([0, 0.5, -1.]))
tensor([ 0.0000, 0.4769, -inf])
```

torch.special.exp2(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L379)

Computes the base two exponential function of `input`.

yi=2xiy_{i} = 2^{x_{i}}

yi​=2xi​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.exp2(torch.tensor([0, math.log2(2.), 3, 4]))
tensor([ 1., 2., 8., 16.])
```

torch.special.expit(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L352)

Computes the expit (also known as the logistic sigmoid function) of the elements of `input`.

outi=11+e−inputi\text{out}_{i} = \frac{1}{1 + e^{-\text{input}_{i}}}

outi​=1+e−inputi​1​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.randn(4)
>>> t
tensor([ 0.9213, 1.0887, -0.8858, -1.7683])
>>> torch.special.expit(t)
tensor([ 0.7153, 0.7481, 0.2920, 0.1458])
```

torch.special.expm1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L404)

Computes the exponential of the elements minus 1
of `input`.

yi=exi−1y_{i} = e^{x_{i}} - 1

yi​=exi​−1

Note

This function provides greater precision than exp(x) - 1 for small values of x.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.expm1(torch.tensor([0, math.log(2.)]))
tensor([ 0., 1.])
```

torch.special.gammainc(*input*, *other*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L885)

Computes the regularized lower incomplete gamma function:

outi=1Γ(inputi)∫0otheritinputi−1e−tdt\text{out}_{i} = \frac{1}{\Gamma(\text{input}_i)} \int_0^{\text{other}_i} t^{\text{input}_i-1} e^{-t} dt

outi​=Γ(inputi​)1​∫0otheri​​tinputi​−1e−tdt

where both inputi\text{input}_iinputi​ and otheri\text{other}_iotheri​ are weakly positive
and at least one is strictly positive.
If both are zero or either is negative then outi=nan\text{out}_i=\text{nan}outi​=nan.
Γ(⋅)\Gamma(\cdot)Γ(⋅) in the equation above is the gamma function,

Γ(inputi)=∫0∞t(inputi−1)e−tdt.\Gamma(\text{input}_i) = \int_0^\infty t^{(\text{input}_i-1)} e^{-t} dt.

Γ(inputi​)=∫0∞​t(inputi​−1)e−tdt.

See `torch.special.gammaincc()` and `torch.special.gammaln()` for related functions.

Supports [broadcasting to a common shape](notes/broadcasting.html#broadcasting-semantics)
and float inputs.

Note

The backward pass with respect to `input` is not yet supported.
Please open an issue on PyTorch's Github to request it.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the first non-negative input tensor
- **other** ([*Tensor*](tensors.html#torch.Tensor)) - the second non-negative input tensor

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a1 = torch.tensor([4.0])
>>> a2 = torch.tensor([3.0, 4.0, 5.0])
>>> a = torch.special.gammaincc(a1, a2)
tensor([0.3528, 0.5665, 0.7350])
tensor([0.3528, 0.5665, 0.7350])
>>> b = torch.special.gammainc(a1, a2) + torch.special.gammaincc(a1, a2)
tensor([1., 1., 1.])
```

torch.special.gammaincc(*input*, *other*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L934)

Computes the regularized upper incomplete gamma function:

outi=1Γ(inputi)∫otheri∞tinputi−1e−tdt\text{out}_{i} = \frac{1}{\Gamma(\text{input}_i)} \int_{\text{other}_i}^{\infty} t^{\text{input}_i-1} e^{-t} dt

outi​=Γ(inputi​)1​∫otheri​∞​tinputi​−1e−tdt

where both inputi\text{input}_iinputi​ and otheri\text{other}_iotheri​ are weakly positive
and at least one is strictly positive.
If both are zero or either is negative then outi=nan\text{out}_i=\text{nan}outi​=nan.
Γ(⋅)\Gamma(\cdot)Γ(⋅) in the equation above is the gamma function,

Γ(inputi)=∫0∞t(inputi−1)e−tdt.\Gamma(\text{input}_i) = \int_0^\infty t^{(\text{input}_i-1)} e^{-t} dt.

Γ(inputi​)=∫0∞​t(inputi​−1)e−tdt.

See `torch.special.gammainc()` and `torch.special.gammaln()` for related functions.

Supports [broadcasting to a common shape](notes/broadcasting.html#broadcasting-semantics)
and float inputs.

Note

The backward pass with respect to `input` is not yet supported.
Please open an issue on PyTorch's Github to request it.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the first non-negative input tensor
- **other** ([*Tensor*](tensors.html#torch.Tensor)) - the second non-negative input tensor

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a1 = torch.tensor([4.0])
>>> a2 = torch.tensor([3.0, 4.0, 5.0])
>>> a = torch.special.gammaincc(a1, a2)
tensor([0.6472, 0.4335, 0.2650])
>>> b = torch.special.gammainc(a1, a2) + torch.special.gammaincc(a1, a2)
tensor([1., 1., 1.])
```

torch.special.gammaln(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L140)

Computes the natural logarithm of the absolute value of the gamma function on `input`.

outi=ln⁡Γ(∣inputi∣)\text{out}_{i} = \ln \Gamma(|\text{input}_{i}|)

outi​=lnΓ(∣inputi​∣)
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.arange(0.5, 2, 0.5)
>>> torch.special.gammaln(a)
tensor([ 0.5724, 0.0000, -0.1208])
```

torch.special.hermite_polynomial_h(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1166)

Physicist's Hermite polynomial Hn(input)H_{n}(\text{input})Hn​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1, input\text{input}input
is returned. Otherwise, the recursion:

Hn+1(input)=2×input×Hn(input)−Hn−1(input)H_{n + 1}(\text{input}) = 2 \times \text{input} \times H_{n}(\text{input}) - H_{n - 1}(\text{input})

Hn+1​(input)=2×input×Hn​(input)−Hn−1​(input)

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.hermite_polynomial_he(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1192)

Probabilist's Hermite polynomial Hen(input)He_{n}(\text{input})Hen​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1, input\text{input}input
is returned. Otherwise, the recursion:

Hen+1(input)=2×input×Hen(input)−Hen−1(input)He_{n + 1}(\text{input}) = 2 \times \text{input} \times He_{n}(\text{input}) - He_{n - 1}(\text{input})

Hen+1​(input)=2×input×Hen​(input)−Hen−1​(input)

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.i0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L522)

Computes the zeroth order modified Bessel function of the first kind for each element of `input`.

outi=I0(inputi)=∑k=0∞(inputi2/4)k(k!)2\text{out}_{i} = I_0(\text{input}_{i}) = \sum_{k=0}^{\infty} \frac{(\text{input}_{i}^2/4)^k}{(k!)^2}

outi​=I0​(inputi​)=k=0∑∞​(k!)2(inputi2​/4)k​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.i0(torch.arange(5, dtype=torch.float32))
tensor([ 1.0000, 1.2661, 2.2796, 4.8808, 11.3019])
```

torch.special.i0e(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L548)

Computes the exponentially scaled zeroth order modified Bessel function of the first kind (as defined below)
for each element of `input`.

outi=exp⁡(−∣x∣)∗i0(x)=exp⁡(−∣x∣)∗∑k=0∞(inputi2/4)k(k!)2\text{out}_{i} = \exp(-|x|) * i0(x) = \exp(-|x|) * \sum_{k=0}^{\infty} \frac{(\text{input}_{i}^2/4)^k}{(k!)^2}

outi​=exp(−∣x∣)∗i0(x)=exp(−∣x∣)∗k=0∑∞​(k!)2(inputi2​/4)k​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.i0e(torch.arange(5, dtype=torch.float32))
tensor([1.0000, 0.4658, 0.3085, 0.2430, 0.2070])
```

torch.special.i1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L573)

Computes the first order modified Bessel function of the first kind (as defined below)
for each element of `input`.

outi=(inputi)2∗∑k=0∞(inputi2/4)k(k!)∗(k+1)!\text{out}_{i} = \frac{(\text{input}_{i})}{2} * \sum_{k=0}^{\infty} \frac{(\text{input}_{i}^2/4)^k}{(k!) * (k+1)!}

outi​=2(inputi​)​∗k=0∑∞​(k!)∗(k+1)!(inputi2​/4)k​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.i1(torch.arange(5, dtype=torch.float32))
tensor([0.0000, 0.5652, 1.5906, 3.9534, 9.7595])
```

torch.special.i1e(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L598)

Computes the exponentially scaled first order modified Bessel function of the first kind (as defined below)
for each element of `input`.

outi=exp⁡(−∣x∣)∗i1(x)=exp⁡(−∣x∣)∗(inputi)2∗∑k=0∞(inputi2/4)k(k!)∗(k+1)!\text{out}_{i} = \exp(-|x|) * i1(x) =
 \exp(-|x|) * \frac{(\text{input}_{i})}{2} * \sum_{k=0}^{\infty} \frac{(\text{input}_{i}^2/4)^k}{(k!) * (k+1)!}

outi​=exp(−∣x∣)∗i1(x)=exp(−∣x∣)∗2(inputi​)​∗k=0∑∞​(k!)∗(k+1)!(inputi2​/4)k​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.i1e(torch.arange(5, dtype=torch.float32))
tensor([0.0000, 0.2079, 0.2153, 0.1968, 0.1788])
```

torch.special.laguerre_polynomial_l(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1218)

Laguerre polynomial Ln(input)L_{n}(\text{input})Ln​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1, input\text{input}input
is returned. Otherwise, the recursion:

Ln+1(input)=2×input×Ln(input)−Ln−1(input)L_{n + 1}(\text{input}) = 2 \times \text{input} \times L_{n}(\text{input}) - L_{n - 1}(\text{input})

Ln+1​(input)=2×input×Ln​(input)−Ln−1​(input)

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.legendre_polynomial_p(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1244)

Legendre polynomial Pn(input)P_{n}(\text{input})Pn​(input).

If n=0n = 0n=0, 111 is returned. If n=1n = 1n=1, input\text{input}input
is returned. Otherwise, the recursion:

Pn+1(input)=2×input×Pn(input)−Pn−1(input)P_{n + 1}(\text{input}) = 2 \times \text{input} \times P_{n}(\text{input}) - P_{n - 1}(\text{input})

Pn+1​(input)=2×input×Pn​(input)−Pn−1​(input)

is evaluated.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.log1p(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L702)

Alias for [`torch.log1p()`](generated/torch.log1p.html#torch.log1p).

torch.special.log_ndtr(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L677)

Computes the log of the area under the standard Gaussian probability density function,
integrated from minus infinity to `input`, elementwise.

log_ndtr(x)=log⁡(12π∫−∞xe−12t2dt)\text{log\_ndtr}(x) = \log\left(\frac{1}{\sqrt{2 \pi}}\int_{-\infty}^{x} e^{-\frac{1}{2}t^2} dt \right)

log_ndtr(x)=log(2π​1​∫−∞x​e−21​t2dt)
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.log_ndtr(torch.tensor([-3., -2, -1, 0, 1, 2, 3]))
tensor([-6.6077 -3.7832 -1.841 -0.6931 -0.1728 -0.023 -0.0014])
```

torch.special.log_softmax(*input*, *dim*, ***, *dtype=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L782)

Computes softmax followed by a logarithm.

While mathematically equivalent to log(softmax(x)), doing these two
operations separately is slower and numerically unstable. This function
is computed as:

log_softmax(xi)=log⁡(exp⁡(xi)∑jexp⁡(xj))\text{log\_softmax}(x_{i}) = \log\left(\frac{\exp(x_i) }{ \sum_j \exp(x_j)} \right)

log_softmax(xi​)=log(∑j​exp(xj​)exp(xi​)​)
Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which log_softmax will be computed.
- **dtype** ([`torch.dtype`](tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is cast to `dtype` before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> t = torch.ones(2, 2)
>>> torch.special.log_softmax(t, 0)
tensor([[-0.6931, -0.6931],
 [-0.6931, -0.6931]])
```

torch.special.logit(*input*, *eps=None*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L305)

Returns a new tensor with the logit of the elements of `input`.
`input` is clamped to [eps, 1 - eps] when eps is not None.
When eps is None and `input` < 0 or `input` > 1, the function will yield NaN.

yi=ln⁡(zi1−zi)zi={xiif eps is Noneepsif xi<epsxiif eps≤xi≤1−eps1−epsif xi>1−eps\begin{align}
y_{i} &= \ln(\frac{z_{i}}{1 - z_{i}}) \\
z_{i} &= \begin{cases}
 x_{i} & \text{if eps is None} \\
 \text{eps} & \text{if } x_{i} < \text{eps} \\
 x_{i} & \text{if } \text{eps} \leq x_{i} \leq 1 - \text{eps} \\
 1 - \text{eps} & \text{if } x_{i} > 1 - \text{eps}
\end{cases}
\end{align}

yi​zi​​=ln(1−zi​zi​​)=⎩⎨⎧​xi​epsxi​1−eps​if eps is Noneif xi​<epsif eps≤xi​≤1−epsif xi​>1−eps​​​
Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the epsilon for input clamp bound. Default: `None`

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.rand(5)
>>> a
tensor([0.2796, 0.9331, 0.6486, 0.1523, 0.6516])
>>> torch.special.logit(a, eps=1e-6)
tensor([-0.9466, 2.6352, 0.6131, -1.7169, 0.6261])
```

torch.special.logsumexp(*input*, *dim*, *keepdim=False*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L343)

Alias for [`torch.logsumexp()`](generated/torch.logsumexp.html#torch.logsumexp).

torch.special.modified_bessel_i0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1270)

Modified Bessel function of the first kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.modified_bessel_i1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1287)

Modified Bessel function of the first kind of order 111.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.modified_bessel_k0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1304)

Modified Bessel function of the second kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.modified_bessel_k1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1321)

Modified Bessel function of the second kind of order 111.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.multigammaln(*input*, *p*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L848)

Computes the [multivariate log-gamma function](https://en.wikipedia.org/wiki/Multivariate_gamma_function) with dimension
ppp element-wise, given by

log⁡(Γp(a))=C+∑i=1plog⁡(Γ(a−i−12))\log(\Gamma_{p}(a)) = C + \displaystyle \sum_{i=1}^{p} \log\left(\Gamma\left(a - \frac{i - 1}{2}\right)\right)

log(Γp​(a))=C+i=1∑p​log(Γ(a−2i−1​))

where C=log⁡(π)⋅p(p−1)4C = \log(\pi) \cdot \frac{p (p - 1)}{4}C=log(π)⋅4p(p−1)​ and Γ(−)\Gamma(-)Γ(−) is the Gamma function.

All elements must be greater than p−12\frac{p - 1}{2}2p−1​, otherwise the behavior is undefined.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the tensor to compute the multivariate log-gamma function
- **p** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of dimensions

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.empty(2, 3).uniform_(1, 2)
>>> a
tensor([[1.6835, 1.8474, 1.1929],
 [1.0475, 1.7162, 1.4180]])
>>> torch.special.multigammaln(a, 2)
tensor([[0.3928, 0.4007, 0.7586],
 [1.0311, 0.3901, 0.5049]])
```

torch.special.ndtr(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L624)

Computes the area under the standard Gaussian probability density function,
integrated from minus infinity to `input`, elementwise.

ndtr(x)=12π∫−∞xe−12t2dt\text{ndtr}(x) = \frac{1}{\sqrt{2 \pi}}\int_{-\infty}^{x} e^{-\frac{1}{2}t^2} dt

ndtr(x)=2π​1​∫−∞x​e−21​t2dt
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.ndtr(torch.tensor([-3., -2, -1, 0, 1, 2, 3]))
tensor([0.0013, 0.0228, 0.1587, 0.5000, 0.8413, 0.9772, 0.9987])
```

torch.special.ndtri(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L649)

Computes the argument, x, for which the area under the Gaussian probability density function
(integrated from minus infinity to x) is equal to `input`, elementwise.

ndtri(p)=2erf−1(2p−1)\text{ndtri}(p) = \sqrt{2}\text{erf}^{-1}(2p - 1)

ndtri(p)=2​erf−1(2p−1)

Note

Also known as quantile function for Normal Distribution.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.special.ndtri(torch.tensor([0, 0.25, 0.5, 0.75, 1]))
tensor([ -inf, -0.6745, 0.0000, 0.6745, inf])
```

torch.special.polygamma(*n*, *input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L166)

Computes the nthn^{th}nth derivative of the digamma function on `input`.
n≥0n \geq 0n≥0 is called the order of the polygamma function.

ψ(n)(x)=d(n)dx(n)ψ(x)\psi^{(n)}(x) = \frac{d^{(n)}}{dx^{(n)}} \psi(x)

ψ(n)(x)=dx(n)d(n)​ψ(x)

Note

This function is implemented only for nonnegative integers n≥0n \geq 0n≥0.

Parameters:

- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the order of the polygamma function
- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([1, 0.5])
>>> torch.special.polygamma(1, a)
tensor([1.64493, 4.9348])
>>> torch.special.polygamma(2, a)
tensor([ -2.4041, -16.8288])
>>> torch.special.polygamma(3, a)
tensor([ 6.4939, 97.4091])
>>> torch.special.polygamma(4, a)
tensor([ -24.8863, -771.4742])
```

torch.special.psi(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L100)

Alias for `torch.special.digamma()`.

torch.special.round(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L743)

Alias for [`torch.round()`](generated/torch.round.html#torch.round).

torch.special.scaled_modified_bessel_k0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1338)

Scaled modified Bessel function of the second kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.scaled_modified_bessel_k1(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1355)

Scaled modified Bessel function of the second kind of order 111.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.shifted_chebyshev_polynomial_t(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1372)

Chebyshev polynomial of the first kind Tn∗(input)T_{n}^{\ast}(\text{input})Tn∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.shifted_chebyshev_polynomial_u(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1390)

Chebyshev polynomial of the second kind Un∗(input)U_{n}^{\ast}(\text{input})Un∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.shifted_chebyshev_polynomial_v(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1408)

Chebyshev polynomial of the third kind Vn∗(input)V_{n}^{\ast}(\text{input})Vn∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.shifted_chebyshev_polynomial_w(*input*, *n*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1426)

Chebyshev polynomial of the fourth kind Wn∗(input)W_{n}^{\ast}(\text{input})Wn∗​(input).

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.
- **n** ([*Tensor*](tensors.html#torch.Tensor)) - Degree of the polynomial.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.sinc(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L711)

Computes the normalized sinc of `input.`

outi={1,if inputi=0sin⁡(πinputi)/(πinputi),otherwise\text{out}_{i} =
\begin{cases}
 1, & \text{if}\ \text{input}_{i}=0 \\
 \sin(\pi \text{input}_{i}) / (\pi \text{input}_{i}), & \text{otherwise}
\end{cases}

outi​={1,sin(πinputi​)/(πinputi​),​if inputi​=0otherwise​
Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.randn(4)
>>> t
tensor([ 0.2252, -0.2948, 1.0267, -1.1566])
>>> torch.special.sinc(t)
tensor([ 0.9186, 0.8631, -0.0259, -0.1300])
```

torch.special.softmax(*input*, *dim*, ***, *dtype=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L752)

Computes the softmax function.

Softmax is defined as:

Softmax(xi)=exp⁡(xi)∑jexp⁡(xj)\text{Softmax}(x_{i}) = \frac{\exp(x_i)}{\sum_j \exp(x_j)}Softmax(xi​)=∑j​exp(xj​)exp(xi​)​

It is applied to all slices along dim, and will re-scale them so that the elements
lie in the range [0, 1] and sum to 1.

Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmax will be computed.
- **dtype** ([`torch.dtype`](tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is cast to `dtype` before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Examples::

```
>>> t = torch.ones(2, 2)
>>> torch.special.softmax(t, 0)
tensor([[0.5000, 0.5000],
 [0.5000, 0.5000]])
```

torch.special.spherical_bessel_j0(*input*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L1444)

Spherical Bessel function of the first kind of order 000.

Parameters:

**input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

torch.special.xlog1py(*input*, *other*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L432)

Computes `input * log1p(other)` with the following cases.

outi={NaNif otheri=NaN0if inputi=0.0 and otheri!=NaNinputi∗log1p(otheri)otherwise\text{out}_{i} = \begin{cases}
 \text{NaN} & \text{if } \text{other}_{i} = \text{NaN} \\
 0 & \text{if } \text{input}_{i} = 0.0 \text{ and } \text{other}_{i} != \text{NaN} \\
 \text{input}_{i} * \text{log1p}(\text{other}_{i})& \text{otherwise}
\end{cases}

outi​=⎩⎨⎧​NaN0inputi​∗log1p(otheri​)​if otheri​=NaNif inputi​=0.0 and otheri​!=NaNotherwise​

Similar to SciPy's scipy.special.xlog1py.

Parameters:

- **input** (*Number**or*[*Tensor*](tensors.html#torch.Tensor)) - Multiplier
- **other** (*Number**or*[*Tensor*](tensors.html#torch.Tensor)) - Argument

Note

At least one of `input` or `other` must be a tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.zeros(5,)
>>> y = torch.tensor([-1, 0, 1, float('inf'), float('nan')])
>>> torch.special.xlog1py(x, y)
tensor([0., 0., 0., 0., nan])
>>> x = torch.tensor([1, 2, 3])
>>> y = torch.tensor([3, 2, 1])
>>> torch.special.xlog1py(x, y)
tensor([1.3863, 2.1972, 2.0794])
>>> torch.special.xlog1py(x, 4)
tensor([1.6094, 3.2189, 4.8283])
>>> torch.special.xlog1py(2, y)
tensor([2.7726, 2.1972, 1.3863])
```

torch.special.xlogy(*input*, *other*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L477)

Computes `input * log(other)` with the following cases.

outi={NaNif otheri=NaN0if inputi=0.0inputi∗log⁡(otheri)otherwise\text{out}_{i} = \begin{cases}
 \text{NaN} & \text{if } \text{other}_{i} = \text{NaN} \\
 0 & \text{if } \text{input}_{i} = 0.0 \\
 \text{input}_{i} * \log{(\text{other}_{i})} & \text{otherwise}
\end{cases}

outi​=⎩⎨⎧​NaN0inputi​∗log(otheri​)​if otheri​=NaNif inputi​=0.0otherwise​

Similar to SciPy's scipy.special.xlogy.

Parameters:

- **input** (*Number**or*[*Tensor*](tensors.html#torch.Tensor)) - Multiplier
- **other** (*Number**or*[*Tensor*](tensors.html#torch.Tensor)) - Argument

Note

At least one of `input` or `other` must be a tensor.

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.zeros(5,)
>>> y = torch.tensor([-1, 0, 1, float('inf'), float('nan')])
>>> torch.special.xlogy(x, y)
tensor([0., 0., 0., 0., nan])
>>> x = torch.tensor([1, 2, 3])
>>> y = torch.tensor([3, 2, 1])
>>> torch.special.xlogy(x, y)
tensor([1.0986, 1.3863, 0.0000])
>>> torch.special.xlogy(x, 4)
tensor([1.3863, 2.7726, 4.1589])
>>> torch.special.xlogy(2, y)
tensor([2.1972, 1.3863, 0.0000])
```

torch.special.zeta(*input*, *other*, ***, *out=None*) → [Tensor](tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/special/__init__.py#L814)

Computes the Hurwitz zeta function, elementwise.

ζ(x,q)=∑k=0∞1(k+q)x\zeta(x, q) = \sum_{k=0}^{\infty} \frac{1}{(k + q)^x}

ζ(x,q)=k=0∑∞​(k+q)x1​
Parameters:

- **input** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor corresponding to x.
- **other** ([*Tensor*](tensors.html#torch.Tensor)) - the input tensor corresponding to q.

Note

The Riemann zeta function corresponds to the case when q = 1

Keyword Arguments:

**out** ([*Tensor*](tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.tensor([2., 4.])
>>> torch.special.zeta(x, 1)
tensor([1.6449, 1.0823])
>>> torch.special.zeta(x, torch.tensor([1., 2.]))
tensor([1.6449, 0.0823])
>>> torch.special.zeta(2, torch.tensor([1., 2.]))
tensor([1.6449, 0.6449])
```