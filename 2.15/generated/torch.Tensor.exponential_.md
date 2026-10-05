# torch.Tensor.exponential_

Tensor.exponential_(*lambd=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with elements drawn from the PDF (probability density function):

f(x)=λe−λx,x>0f(x) = \lambda e^{-\lambda x}, x > 0f(x)=λe−λx,x>0

Note

In probability theory, exponential distribution is supported on interval [0, inf⁡\infinf) (i.e., x>=0x >= 0x>=0)
implying that zero can be sampled from the exponential distribution.
However, `torch.Tensor.exponential_()` does not sample zero,
which means that its actual support is the interval (0, inf⁡\infinf).

Note that [`torch.distributions.exponential.Exponential()`](../distributions.html#torch.distributions.exponential.Exponential) is supported on the interval [0, inf⁡\infinf) and can sample zero.