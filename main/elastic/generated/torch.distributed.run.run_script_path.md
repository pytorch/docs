# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/run.py#L1094)

Run the provided training_script from within this interpreter.

Usage: script_as_function("/abs/path/to/script.py", "-arg1", "val1")