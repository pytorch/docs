# Torch Environment Variables

PyTorch leverages environment variables for adjusting various settings that influence its runtime behavior.
These variables offer control over key functionalities, such as displaying the C++ stack trace upon encountering errors, synchronizing the execution of CUDA kernels,
specifying the number of threads for parallel processing tasks and many more.

Moreover, PyTorch leverages several high-performance libraries, such as MKL and cuDNN,
which also utilize environment variables to modify their functionality.
This interplay of settings allows for a highly customizable development environment that can be
optimized for efficiency, debugging, and computational resource management.

Please note that while this documentation covers a broad spectrum of environment variables relevant to PyTorch and its associated libraries, it is not exhaustive.
If you find anything in this documentation that is missing, incorrect, or could be improved, please let us know by filing an issue or opening a pull request.

- [Threading Environment Variables](threading_environment_variables.html)
- [CUDA Environment Variables](cuda_environment_variables.html)
- [MPS Environment Variables](mps_environment_variables.html)
- [Debugging Environment Variables](debugging_environment_variables.html)
- [Miscellaneous Environment Variables](miscellaneous_environment_variables.html)
- [torch._logging](logging.html)
- [PYTORCH ProcessGroupNCCL Environment Variables](torch_nccl_environment_variables.html)