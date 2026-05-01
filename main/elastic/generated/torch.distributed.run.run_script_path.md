# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/distributed/run.py#L960)

Run the provided training_script from within this interpreter.

Usage: script_as_function("/abs/path/to/script.py", "-arg1", "val1")