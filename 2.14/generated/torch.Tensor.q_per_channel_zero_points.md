# torch.Tensor.q_per_channel_zero_points

Tensor.q_per_channel_zero_points() → [Tensor](../tensors.html#torch.Tensor)

Given a Tensor quantized by linear (affine) per-channel quantization,
returns a tensor of zero_points of the underlying quantizer. It has the number of
elements that matches the corresponding dimensions (from q_per_channel_axis) of
the tensor.