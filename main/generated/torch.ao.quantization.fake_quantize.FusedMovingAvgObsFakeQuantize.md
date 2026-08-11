# FusedMovingAvgObsFakeQuantize

*class*torch.ao.quantization.fake_quantize.FusedMovingAvgObsFakeQuantize(*observer=<class 'torch.ao.quantization.observer.MovingAverageMinMaxObserver'>*, *quant_min=0*, *quant_max=255*, ***observer_kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/quantization/fake_quantize.py#L371)

Define a fused module to observe the tensor.

Fused module that is used to observe the input tensor (compute min/max), compute
scale/zero_point and fake_quantize the tensor.
This module uses calculation similar MovingAverageMinMaxObserver for the inputs,
to compute the min/max values in order to compute the scale/zero_point.
The qscheme input in the observer is used to differentiate between symmetric/affine
quantization scheme.

The output of this module is given by
x_out = (clamp(round(x/scale + zero_point), quant_min, quant_max)-zero_point)*scale

Similar to `FakeQuantize`, and accepts the same attributes as the
base class.