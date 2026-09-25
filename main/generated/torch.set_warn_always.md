# torch.set_warn_always

torch.set_warn_always(*b*, */*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/__init__.py#L2061)

When this flag is False (default) then some PyTorch warnings may only
appear once per process. This helps avoid excessive warning information.
Setting it to True causes these warnings to always appear, which may be
helpful when debugging.

Parameters:

**b** ([`bool`](https://docs.python.org/3/builtins/functions.html#bool)) - If True, force warnings to always be emitted
If False, set to the default behaviour