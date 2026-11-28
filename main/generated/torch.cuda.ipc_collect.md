# torch.cuda.ipc_collect

torch.cuda.ipc_collect()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/__init__.py#L1388)

Force collects GPU memory after it has been released by CUDA IPC.

Note

Checks if any sent CUDA tensors could be cleaned from the memory. Force
closes shared memory file used for reference counting if there is no
active counters. Useful when the producer process stopped actively sending
tensors and want to release unused memory.