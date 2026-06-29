# torch.utils.get_cpp_backtrace

torch.utils.get_cpp_backtrace(*frames_to_skip=0*, *maximum_number_of_frames=64*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/utils/cpp_backtrace.py#L4)

Return a string containing the C++ stack trace of the current thread.

Parameters:

- **frames_to_skip** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of frames to skip from the top of the stack
- **maximum_number_of_frames** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the maximum number of frames to return

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)