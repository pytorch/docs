# remove_boolean_dispatch_from_name

*class*torch.ao.quantization.backend_config.utils.remove_boolean_dispatch_from_name(*p*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/ao/quantization/backend_config/utils.py#L149)

Some ops have a default string representation such as
'<function boolean_dispatch.<locals>.fn at 0x7ff1106bf280>',
this function replaces them with the hardcoded function names.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)