# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/distributed/run.py#L1082)

Run the provided training_script from within this interpreter.

Usage: script_as_function("/abs/path/to/script.py", "-arg1", "val1")