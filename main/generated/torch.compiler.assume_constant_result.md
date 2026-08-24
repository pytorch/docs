# torch.compiler.assume_constant_result

torch.compiler.assume_constant_result(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/compiler/__init__.py#L322)

This function is used to mark a function fn as having a constant result.
This allows the compiler to optimize away your function.
Returns The same function fn

Parameters:

**fn** - The function to be marked as having a constant result.

Warning

assume_constant_result can, if invalid, cause safety and soundness issues, [`torch.compile()`](torch.compile.html#torch.compile)
will not attempt to validate whether the constant assumption is true or not