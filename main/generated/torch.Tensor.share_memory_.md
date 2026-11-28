# torch.Tensor.share_memory_

Tensor.share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/_tensor.py#L867)

Moves the underlying storage to shared memory.

This is a no-op if the underlying storage is already in shared memory
and for CUDA tensors. Tensors in shared memory cannot be resized.

See [`torch.UntypedStorage.share_memory_()`](../storage.html#torch.UntypedStorage.share_memory_) for more details.