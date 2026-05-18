# torch.nn.functional.glu

torch.nn.functional.glu(*input*, *dim=-1*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/6e3cf2e4280672104341718ea51a55799bb3aca4/torch/nn/functional.py#L1743)

The gated linear unit. Computes:

GLU(a,b)=a⊗σ(b)\text{GLU}(a, b) = a \otimes \sigma(b)

GLU(a,b)=a⊗σ(b)

where input is split in half along dim to form a and b, σ\sigmaσ
is the sigmoid function and ⊗\otimes⊗ is the element-wise product between matrices.

See [Language Modeling with Gated Convolutional Networks](https://arxiv.org/abs/1612.08083).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input tensor
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension on which to split the input. Default: -1

Return type:

[*Tensor*](../tensors.html#torch.Tensor)