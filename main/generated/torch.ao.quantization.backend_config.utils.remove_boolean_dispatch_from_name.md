# remove_boolean_dispatch_from_name

*class*torch.ao.quantization.backend_config.utils.remove_boolean_dispatch_from_name(*p*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/quantization/backend_config/utils.py#L149)

Some ops have a default string representation such as
'<function boolean_dispatch.<locals>.fn at 0x7ff1106bf280>',
this function replaces them with the hardcoded function names.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)