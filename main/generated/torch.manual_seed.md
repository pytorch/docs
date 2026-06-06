# torch.manual_seed

torch.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/random.py#L49)

Sets the seed for generating random numbers on all devices. Returns a
torch.Generator object.

Parameters:

**seed** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The desired seed. Value must be within the inclusive range
[-0x8000_0000_0000_0000, 0xffff_ffff_ffff_ffff]. Otherwise, a RuntimeError
is raised. Negative inputs are remapped to positive values with the formula
0xffff_ffff_ffff_ffff + seed.

Return type:

[*Generator*](torch.Generator.html#torch.Generator)