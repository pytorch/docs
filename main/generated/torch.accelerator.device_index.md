# device_index

*class*torch.accelerator.device_index(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/accelerator/__init__.py#L275)

Context manager to set the current device index for the current [accelerator](../torch.html#accelerators).
Temporarily changes the current device index to the specified value for the duration
of the context, and automatically restores the previous device index when exiting
the context.

Parameters:

**device** (*Optional**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - a given device index to temporarily set. If None,
no device index switching occurs.

Examples

```
>>> # Set device 0 as the current device temporarily
>>> with torch.accelerator.device_index(0):
... # Code here runs with device 0 as the current device
... pass
>>> # Original device is now restored
>>> # No-op when None is passed
>>> with torch.accelerator.device_index(None):
... # No device switching occurs
... pass
```