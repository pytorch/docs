# Utilities

torch.distributed.elastic.utils.api.get_env_variable_or_raise(*env_name*)[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/distributed/elastic/utils/api.py#L15)

Tries to retrieve environment variable. Raises `ValueError`
if no environment variable found.

Parameters:

**env_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - Name of the env variable

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

torch.distributed.elastic.utils.distributed.get_free_port()[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/distributed/elastic/utils/distributed.py#L124)

Returns a port that is unused on all local addresses.

This function finds an unused port by binding a socket to the wildcard
address and then closing it.

Returns:

a port that is unused on all local addresses

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Example

```
>>> get_free_port()
63976
```

Note

The port returned by `get_free_port()` is not reserved and may be
taken by another process after this function returns.

torch.distributed.elastic.utils.log_level.get_log_level()[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/distributed/elastic/utils/log_level.py#L10)

Return default log level for pytorch.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

torch.distributed.elastic.utils.logging.get_logger(*name=None*)[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/distributed/elastic/utils/logging.py#L17)

Util function to set up a simple logger that writes
into stderr. The loglevel is fetched from the LOGLEVEL
env. variable or WARNING as default. The function will use the
module name of the caller if no name is provided.

Parameters:

**name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*|**None*) - Name of the logger. If no name provided, the name will
be derived from the call stack.

Return type:

[*Logger*](https://docs.python.org/3/library/logging.html#logging.Logger)