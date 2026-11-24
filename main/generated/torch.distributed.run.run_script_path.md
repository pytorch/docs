# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/distributed/run.py#L1083)

Run the provided training_script from within this interpreter.

Usage: `run_script_path("/abs/path/to/script.py", "--arg1", "val1")`