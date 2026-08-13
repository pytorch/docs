# torch.compiler.assume_constant_result

torch.compiler.assume_constant_result(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/compiler/__init__.py#L323)

This function is used to mark a function fn as having a constant result.
This allows the compiler to optimize away your function.
Returns The same function fn

Parameters:

**fn** - The function to be marked as having a constant result.

Warning

assume_constant_result can, if invalid, cause safety and soundness issues, [`torch.compile()`](torch.compile.html#torch.compile)
will not attempt to validate whether the constant assumption is true or not