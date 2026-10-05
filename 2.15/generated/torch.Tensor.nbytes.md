# torch.Tensor.nbytes

Tensor.nbytes

Returns the number of bytes consumed by the "view" of elements of the Tensor
if the Tensor does not use sparse storage layout.
Defined to be [`numel()`](torch.Tensor.numel.html#torch.Tensor.numel) * [`element_size()`](torch.Tensor.element_size.html#torch.Tensor.element_size)