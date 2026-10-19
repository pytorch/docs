# torch.func.debug_unwrap

torch.func.debug_unwrap(*tensor*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/_functorch/eager_transforms.py#L1947)

Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor.

This function should only be used in a debug setting (e.g. trying to print the
value of a Tensor in a debugger). Otherwise, using the result of function
inside of a function being transformed will lead to undefined behavior.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)