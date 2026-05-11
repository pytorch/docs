# default_eval_fn

*class*torch.ao.quantization.default_eval_fn(*model*, *calib_data*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/ao/quantization/__init__.py#L166)

Define the default evaluation function.

Default evaluation function takes a torch.utils.data.Dataset or a list of
input Tensors and run the model on the dataset