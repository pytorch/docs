# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/distributed/run.py#L1094)

Run the provided training_script from within this interpreter.

Usage: script_as_function("/abs/path/to/script.py", "-arg1", "val1")