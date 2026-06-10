# torch.set_num_interop_threads

torch.set_num_interop_threads(*int*)

Sets the number of threads used for interop parallelism
(e.g. in JIT interpreter) on CPU.

Warning

Can only be called once and before any inter-op parallel work
is started (e.g. JIT execution).