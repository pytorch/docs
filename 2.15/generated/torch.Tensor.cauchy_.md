# torch.Tensor.cauchy_

Tensor.cauchy_(*median=0*, *sigma=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills the tensor with numbers drawn from the Cauchy distribution:

f(x)=1πσ(x−median)2+σ2f(x) = \dfrac{1}{\pi} \dfrac{\sigma}{(x - \text{median})^2 + \sigma^2}f(x)=π1​(x−median)2+σ2σ​

Note

Sigma (σ\sigmaσ) is used to denote the scale parameter in Cauchy distribution.