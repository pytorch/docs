# torch.Tensor.share_memory_

Tensor.share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/_tensor.py#L836)

Moves the underlying storage to shared memory.

This is a no-op if the underlying storage is already in shared memory
and for CUDA tensors. Tensors in shared memory cannot be resized.

See [`torch.UntypedStorage.share_memory_()`](../storage.html#torch.UntypedStorage.share_memory_) for more details.