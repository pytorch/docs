# FakeQuantize

*class*torch.ao.quantization.fake_quantize.FakeQuantize(*observer=<class 'torch.ao.quantization.observer.MovingAverageMinMaxObserver'>*, *quant_min=None*, *quant_max=None*, *is_dynamic=False*, ***observer_kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/ao/quantization/fake_quantize.py#L128)

Simulate the quantize and dequantize operations in training time.

The output of this module is given by:

```
x_out = (
 clamp(round(x / scale + zero_point), quant_min, quant_max) - zero_point
) * scale
```

- `is_dynamic` indicates whether the fake quantie is a placeholder for dynamic quantization
operators (choose_qparams -> q -> dq) or static quantization operators (q -> dq)
- `scale` defines the scale factor used for quantization.
- `zero_point` specifies the quantized value to which 0 in floating point maps to
- `fake_quant_enabled` controls the application of fake quantization on tensors, note that
statistics can still be updated.
- `observer_enabled` controls statistics collection on tensors
- `dtype` specifies the quantized dtype that is being emulated with fake-quantization,

allowable values are torch.qint8 and torch.quint8.

Parameters:

- **observer** (*module*) - Module for observing statistics on input tensors and calculating scale
and zero-point.
- **observer_kwargs** (*optional*) - Arguments for the observer module

Variables:

**activation_post_process** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - User provided module that collects statistics on the input tensor and
provides a method to calculate scale and zero-point.