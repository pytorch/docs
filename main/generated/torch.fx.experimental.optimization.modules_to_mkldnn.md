# torch.fx.experimental.optimization.modules_to_mkldnn

torch.fx.experimental.optimization.modules_to_mkldnn(*nodes*, *modules*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/fx/experimental/optimization.py#L182)

For each node, if it's a module that can be preconverted into MKLDNN,
then we do so and create a mapping to allow us to convert from the MKLDNN
version of the module to the original.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[*Module*](torch.nn.Module.html#torch.nn.Module), [*Module*](torch.nn.Module.html#torch.nn.Module)]