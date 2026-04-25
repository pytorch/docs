# torch.Tensor.int_repr

Tensor.int_repr() → [Tensor](../tensors.html#torch.Tensor)

Given a quantized Tensor,
`self.int_repr()` returns a CPU Tensor with uint8_t as data type that stores the
underlying uint8_t values of the given Tensor.