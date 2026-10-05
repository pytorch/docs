# torch.Tensor.pin_memory

Tensor.pin_memory() → [Tensor](../tensors.html#torch.Tensor)

Copies the tensor to pinned memory, if it's not already pinned.
By default, the device pinned memory on will be the current [accelerator](../torch.html#accelerators).