# torch.Tensor.share_memory_

Tensor.share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/_tensor.py#L836)

Moves the underlying storage to shared memory.

This is a no-op if the underlying storage is already in shared memory
and for CUDA tensors. Tensors in shared memory cannot be resized.

See [`torch.UntypedStorage.share_memory_()`](../storage.html#torch.UntypedStorage.share_memory_) for more details.