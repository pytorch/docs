# default_eval_fn

*class*torch.ao.quantization.default_eval_fn(*model*, *calib_data*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/ao/quantization/__init__.py#L156)

Define the default evaluation function.

Default evaluation function takes a torch.utils.data.Dataset or a list of
input Tensors and run the model on the dataset