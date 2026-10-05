# torch.Tensor.type_as

Tensor.type_as(*tensor*) → [Tensor](../tensors.html#torch.Tensor)

Returns this tensor cast to the type of the given tensor.

This is a no-op if the tensor is already of the correct type. This is
equivalent to `self.type(tensor.type())`

Parameters:

**tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor which has the desired type