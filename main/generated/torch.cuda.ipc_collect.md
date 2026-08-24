# torch.cuda.ipc_collect

torch.cuda.ipc_collect()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/__init__.py#L1296)

Force collects GPU memory after it has been released by CUDA IPC.

Note

Checks if any sent CUDA tensors could be cleaned from the memory. Force
closes shared memory file used for reference counting if there is no
active counters. Useful when the producer process stopped actively sending
tensors and want to release unused memory.