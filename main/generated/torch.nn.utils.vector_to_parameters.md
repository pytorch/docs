# torch.nn.utils.vector_to_parameters

torch.nn.utils.vector_to_parameters(*vec*, *parameters*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/nn/utils/convert_parameters.py#L28)

Copy slices of a vector into an iterable of parameters.

Parameters:

- **vec** ([*Tensor*](../tensors.html#torch.Tensor)) - a single vector representing the parameters of a model.
- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of Tensors that are the
parameters of a model.