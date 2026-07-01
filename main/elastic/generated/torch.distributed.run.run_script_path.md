# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/distributed/run.py#L972)

Run the provided training_script from within this interpreter.

Usage: script_as_function("/abs/path/to/script.py", "-arg1", "val1")