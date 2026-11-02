# torch.distributed.run.run_script_path

torch.distributed.run.run_script_path(*training_script*, **training_script_args*)[[source]](https://github.com/pytorch/pytorch/blob/0f53a707a91af21a7b8f519b354bcf06268a941a/torch/distributed/run.py#L1083)

Run the provided training_script from within this interpreter.

Usage: `run_script_path("/abs/path/to/script.py", "--arg1", "val1")`