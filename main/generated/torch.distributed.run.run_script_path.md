# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/distributed/run.py#L1083)

Run the provided training_script from within this interpreter.

Usage: `run_script_path("/abs/path/to/script.py", "--arg1", "val1")`