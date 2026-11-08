# torch.func.debug_unwrap

torch.func.debug_unwrap(*tensor*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/_functorch/eager_transforms.py#L1947)

Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor.

This function should only be used in a debug setting (e.g. trying to print the
value of a Tensor in a debugger). Otherwise, using the result of function
inside of a function being transformed will lead to undefined behavior.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)