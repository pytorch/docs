# Subprocess Handling

## Retrieve SubprocessHandler

torch.distributed.elastic.multiprocessing.subprocess_handler.handlers.get_subprocess_handler(*entrypoint*, *args*, *env*, *stdout*, *stderr*, *local_rank_id*, *numa_options=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/distributed/elastic/multiprocessing/subprocess_handler/handlers.py#L16)

Return type:

*SubprocessHandler*

## SubprocessHandler

*class*torch.distributed.elastic.multiprocessing.subprocess_handler.subprocess_handler.SubprocessHandler(*entrypoint*, *args*, *env*, *stdout*, *stderr*, *local_rank_id*, *numa_options*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/distributed/elastic/multiprocessing/subprocess_handler/subprocess_handler.py#L30)

Convenience wrapper around python's `subprocess.Popen`. Keeps track of
meta-objects associated to the process (e.g. stdout and stderr redirect fds).