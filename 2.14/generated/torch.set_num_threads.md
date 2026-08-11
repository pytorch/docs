# torch.set_num_threads

torch.set_num_threads(*int*)

Sets the number of threads used for intraop parallelism on CPU.

Warning

To ensure that the correct number of threads is used, set_num_threads
must be called before running eager, JIT or autograd code.