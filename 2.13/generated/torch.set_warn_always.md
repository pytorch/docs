# torch.set_warn_always

torch.set_warn_always(*b*, */*)[[source]](https://github.com/pytorch/pytorch/blob/v2.13.0/torch/__init__.py#L1685)

When this flag is False (default) then some PyTorch warnings may only
appear once per process. This helps avoid excessive warning information.
Setting it to True causes these warnings to always appear, which may be
helpful when debugging.

Parameters:

**b** ([`bool`](https://docs.python.org/3/library/functions.html#bool)) - If True, force warnings to always be emitted
If False, set to the default behaviour