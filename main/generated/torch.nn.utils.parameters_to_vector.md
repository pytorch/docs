# torch.nn.utils.parameters_to_vector

torch.nn.utils.parameters_to_vector(*parameters*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/utils/convert_parameters.py#L6)

Flatten an iterable of parameters into a single vector.

Parameters:

**parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - an iterable of Tensors that are the
parameters of a model.

Returns:

The parameters represented by a single vector

Return type:

[*Tensor*](../tensors.html#torch.Tensor)