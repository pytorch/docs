# Debugging Environment Variables

| Variable | Description |
| --- | --- |
| `TORCH_SHOW_CPP_STACKTRACES` | If set to `1`, makes PyTorch print out a stack trace when it detects a C++ error. |
| `TORCH_CPP_LOG_LEVEL` | Set the log level of c10 logging facility (supports both GLOG and c10 loggers). Valid values are `INFO`, `WARNING`, `ERROR`, and `FATAL` or their numerical equivalents `0`, `1`, `2`, and `3`. |
| `TORCH_LOGS` | For a more in depth explanation of this environment variable, see [torch._logging](logging.html). |