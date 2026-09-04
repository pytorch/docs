# torch.func.debug_unwrap

torch.func.debug_unwrap(*tensor*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/_functorch/eager_transforms.py#L1947)

Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor.

This function should only be used in a debug setting (e.g. trying to print the
value of a Tensor in a debugger). Otherwise, using the result of function
inside of a function being transformed will lead to undefined behavior.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)