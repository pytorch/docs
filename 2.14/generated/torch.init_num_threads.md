# torch.init_num_threads

torch.init_num_threads() → [None](https://docs.python.org/3/library/constants.html#None)

init_num_threads()

Initializes the number of parallel threads used on the current thread.

Call this whenever a new thread is created in order to propagate values from
[`torch.set_num_threads()`](torch.set_num_threads.html#torch.set_num_threads) onto the new thread.