# torch.Tensor.q_per_channel_scales

Tensor.q_per_channel_scales() → [Tensor](../tensors.html#torch.Tensor)

Given a Tensor quantized by linear (affine) per-channel quantization,
returns a Tensor of scales of the underlying quantizer. It has the number of
elements that matches the corresponding dimensions (from q_per_channel_axis) of
the tensor.