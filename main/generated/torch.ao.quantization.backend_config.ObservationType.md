# ObservationType

*class*torch.ao.quantization.backend_config.ObservationType(*value*)[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/ao/quantization/backend_config/backend_config.py#L55)

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