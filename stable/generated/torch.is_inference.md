# torch.is_inference

torch.is_inference(*input*)

Returns True if `input` is an inference tensor.

A non-view tensor is an inference tensor if and only if it was
allocated during inference mode. A view tensor is an inference
tensor if and only if the tensor it is a view of is an inference tensor.

For details on inference mode please see
[Inference Mode](https://pytorch.org/cppdocs/notes/inference_mode.html).

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.