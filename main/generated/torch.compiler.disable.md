# torch.compiler.disable

torch.compiler.disable(*fn=None*, *recursive=True*, ***, *reason=None*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/compiler/__init__.py#L341)

This function provides a decorator to disable compilation on a function.
It also provides the option of recursively disabling called functions.

Parameters:

- **fn** (*optional*) - The function to disable
- **recursive** (*optional*) - A boolean value indicating whether the disabling should be recursive.
- **reason** (*optional*) - A string value indicating the reason for disabling the function.