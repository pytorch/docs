# ObservationType

*class*torch.ao.quantization.backend_config.ObservationType(*value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/ao/quantization/backend_config/backend_config.py#L55)

An enum that represents different ways of how an operator/operator pattern
should be observed

INPUT_OUTPUT_NOT_OBSERVED*= 2*

this means the input and output are never observed
example: x.shape, x.size

OUTPUT_SHARE_OBSERVER_WITH_INPUT*= 1*

this means the output will use the same observer instance as input, based
on qconfig.activation
example: torch.cat, maxpool

OUTPUT_USE_DIFFERENT_OBSERVER_AS_INPUT*= 0*

this means input and output are observed with different observers, based
on qconfig.activation
example: conv, linear, softmax