# torch.nn.utils.vector_to_parameters

torch.nn.utils.vector_to_parameters(*vec*, *parameters*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/nn/utils/convert_parameters.py#L28)

Copy slices of a vector into an iterable of parameters.

Parameters:

- **vec** ([*Tensor*](../tensors.html#torch.Tensor)) - a single vector representing the parameters of a model.
- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of Tensors that are the
parameters of a model.