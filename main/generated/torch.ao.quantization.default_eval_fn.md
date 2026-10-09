# default_eval_fn

*class*torch.ao.quantization.default_eval_fn(*model*, *calib_data*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/ao/quantization/__init__.py#L166)

Define the default evaluation function.

Default evaluation function takes a torch.utils.data.Dataset or a list of
input Tensors and run the model on the dataset