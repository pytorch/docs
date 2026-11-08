# default_eval_fn

*class*torch.ao.quantization.default_eval_fn(*model*, *calib_data*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/__init__.py#L156)

Define the default evaluation function.

Default evaluation function takes a torch.utils.data.Dataset or a list of
input Tensors and run the model on the dataset