# torch.compiler.assume_constant_result

torch.compiler.assume_constant_result(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/compiler/__init__.py#L322)

This function is used to mark a function fn as having a constant result.
This allows the compiler to optimize away your function.
Returns The same function fn

Parameters:

**fn** - The function to be marked as having a constant result.

Warning

assume_constant_result can, if invalid, cause safety and soundness issues, [`torch.compile()`](torch.compile.html#torch.compile)
will not attempt to validate whether the constant assumption is true or not