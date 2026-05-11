# torch.Tensor.log_normal_

Tensor.log_normal_(*mean=1*, *std=2*, ***, *generator=None*)

Fills `self` tensor with numbers samples from the log-normal distribution
parameterized by the given mean μ\muμ and standard deviation
σ\sigmaσ. Note that [`mean`](torch.mean.html#torch.mean) and [`std`](torch.std.html#torch.std) are the mean and
standard deviation of the underlying normal distribution, and not of the
returned distribution:

f(x)=1xσ2π e−(ln⁡x−μ)22σ2f(x) = \dfrac{1}{x \sigma \sqrt{2\pi}}\ e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}f(x)=xσ2π​1​ e−2σ2(lnx−μ)2​