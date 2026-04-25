# torch.func.debug_unwrap

torch.func.debug_unwrap(*tensor*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/_functorch/eager_transforms.py#L1940)

Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor.

This function should only be used in a debug setting (e.g. trying to print the
value of a Tensor in a debugger). Otherwise, using the result of function
inside of a function being transformed will lead to undefined behavior.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)