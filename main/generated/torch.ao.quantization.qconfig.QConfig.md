# QConfig

*class*torch.ao.quantization.qconfig.QConfig(*activation*, *weight*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/quantization/qconfig.py#L86)

Describes how to quantize a layer or a part of the network by providing
settings (observer classes) for activations and weights respectively.

Note that QConfig needs to contain observer **classes** (like MinMaxObserver) or a callable that returns
instances on invocation, not the concrete observer instances themselves.
Quantization preparation function will instantiate observers multiple times for each of the layers.

Observer classes have usually reasonable default arguments, but they can be overwritten with with_args
method (that behaves like functools.partial):

```
my_qconfig = QConfig(
 activation=MinMaxObserver.with_args(dtype=torch.qint8),
 weight=default_observer.with_args(dtype=torch.qint8),
)
```