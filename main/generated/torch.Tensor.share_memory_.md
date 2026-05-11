# torch.Tensor.share_memory_

Tensor.share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/_tensor.py#L846)

Moves the underlying storage to shared memory.

This is a no-op if the underlying storage is already in shared memory
and for CUDA tensors. Tensors in shared memory cannot be resized.

See [`torch.UntypedStorage.share_memory_()`](../storage.html#torch.UntypedStorage.share_memory_) for more details.