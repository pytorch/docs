# torch.fx.experimental.optimization.modules_to_mkldnn

torch.fx.experimental.optimization.modules_to_mkldnn(*nodes*, *modules*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/fx/experimental/optimization.py#L182)

For each node, if it's a module that can be preconverted into MKLDNN,
then we do so and create a mapping to allow us to convert from the MKLDNN
version of the module to the original.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[*Module*](torch.nn.Module.html#torch.nn.Module), [*Module*](torch.nn.Module.html#torch.nn.Module)]