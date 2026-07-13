# set_multithreading_enabled

*class*torch.autograd.grad_mode.set_multithreading_enabled(*mode*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/autograd/grad_mode.py#L314)

Context-manager that enables or disables multithreaded backward.

Ordinarily, when [accelerator](../torch.html#accelerators) devices are in use,
the backward pass runs on device-specific worker threads. The engine
creates these threads based on the number of available devices and
reuses them across iterations.

When `mode=False`, the backward pass runs on the calling thread
instead. `mode=True` restores the default behavior.

This can be used as a context-manager or as a function. It is
thread-local and will not affect computation in other threads.

Parameters:

**mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to enable multithreaded backward (`True`,
default) or disable (`False`).

Note

This API does not apply to [forward-mode AD](../autograd.html#forward-mode-ad),
which never uses multithreading.

clone()[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/autograd/grad_mode.py#L349)

Create a copy of this class

Return type:

*set_multithreading_enabled*