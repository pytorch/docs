# torch.manual_seed

torch.manual_seed(*seed*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/random.py#L49)

Sets the seed for generating random numbers on all devices. Returns a
torch.Generator object.

Parameters:

**seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired seed. Value must be within the inclusive range
[-0x8000_0000_0000_0000, 0xffff_ffff_ffff_ffff]. Otherwise, a RuntimeError
is raised. Negative inputs are remapped to positive values with the formula
0xffff_ffff_ffff_ffff + seed.

Return type:

[*Generator*](torch.Generator.html#torch.Generator)