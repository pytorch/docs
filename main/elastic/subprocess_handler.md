# Subprocess Handling

## Retrieve SubprocessHandler

torch.distributed.elastic.multiprocessing.subprocess_handler.handlers.get_subprocess_handler(*entrypoint*, *args*, *env*, *stdout*, *stderr*, *local_rank_id*, *numa_options=None*)[[source]](https://github.com/pytorch/pytorch/blob/2700915a75e05f161593ddd3bb8f6c01c29b8777/torch/distributed/elastic/multiprocessing/subprocess_handler/handlers.py#L16)

Return type:

*SubprocessHandler*

## SubprocessHandler

*class*torch.distributed.elastic.multiprocessing.subprocess_handler.subprocess_handler.SubprocessHandler(*entrypoint*, *args*, *env*, *stdout*, *stderr*, *local_rank_id*, *numa_options*)[[source]](https://github.com/pytorch/pytorch/blob/2700915a75e05f161593ddd3bb8f6c01c29b8777/torch/distributed/elastic/multiprocessing/subprocess_handler/subprocess_handler.py#L30)

Convenience wrapper around python's `subprocess.Popen`. Keeps track of
meta-objects associated to the process (e.g. stdout and stderr redirect fds).