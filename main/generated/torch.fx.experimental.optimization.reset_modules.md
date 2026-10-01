# torch.fx.experimental.optimization.reset_modules

torch.fx.experimental.optimization.reset_modules(*nodes*, *modules*, *old_modules*)[[source]](https://github.com/pytorch/pytorch/blob/38cca96300da024842405ecefa081e4761254922/torch/fx/experimental/optimization.py#L213)

Maps each module that's been changed with modules_to_mkldnn back to its
original.