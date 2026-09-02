# torch.compiler.disable

torch.compiler.disable(*fn=None*, *recursive=True*, ***, *reason=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L341)

This function provides a decorator to disable compilation on a function.
It also provides the option of recursively disabling called functions.

Parameters:

- **fn** (*optional*) - The function to disable
- **recursive** (*optional*) - A boolean value indicating whether the disabling should be recursive.
- **reason** (*optional*) - A string value indicating the reason for disabling the function.