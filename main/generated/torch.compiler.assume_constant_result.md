# torch.compiler.assume_constant_result

torch.compiler.assume_constant_result(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/compiler/__init__.py#L323)

This function is used to mark a function fn as having a constant result.
This allows the compiler to optimize away your function.
Returns The same function fn

Parameters:

**fn** - The function to be marked as having a constant result.

Warning

assume_constant_result can, if invalid, cause safety and soundness issues, [`torch.compile()`](torch.compile.html#torch.compile)
will not attempt to validate whether the constant assumption is true or not