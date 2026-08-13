# torch.fx.experimental.optimization.modules_to_mkldnn

torch.fx.experimental.optimization.modules_to_mkldnn(*nodes*, *modules*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/optimization.py#L182)

For each node, if it's a module that can be preconverted into MKLDNN,
then we do so and create a mapping to allow us to convert from the MKLDNN
version of the module to the original.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[*Module*](torch.nn.Module.html#torch.nn.Module), [*Module*](torch.nn.Module.html#torch.nn.Module)]