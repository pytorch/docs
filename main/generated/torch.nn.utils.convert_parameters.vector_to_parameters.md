# torch.nn.utils.convert_parameters.vector_to_parameters

torch.nn.utils.convert_parameters.vector_to_parameters(*vec*, *parameters*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/nn/utils/convert_parameters.py#L28)

Copy slices of a vector into an iterable of parameters.

Parameters:

- **vec** ([*Tensor*](../tensors.html#torch.Tensor)) - a single vector representing the parameters of a model.
- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of Tensors that are the
parameters of a model.