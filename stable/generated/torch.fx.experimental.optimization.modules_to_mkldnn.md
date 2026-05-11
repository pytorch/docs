# torch.fx.experimental.optimization.modules_to_mkldnn

torch.fx.experimental.optimization.modules_to_mkldnn(*nodes*, *modules*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/experimental/optimization.py#L186)

For each node, if it's a module that can be preconverted into MKLDNN,
then we do so and create a mapping to allow us to convert from the MKLDNN
version of the module to the original.