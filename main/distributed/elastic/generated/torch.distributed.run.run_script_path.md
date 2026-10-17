# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/distributed/run.py#L1083)

Run the provided training_script from within this interpreter.

Usage: `run_script_path("/abs/path/to/script.py", "--arg1", "val1")`