# torch.compiler.disable

torch.compiler.disable(*fn=None*, *recursive=True*, ***, *reason=None*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/compiler/__init__.py#L342)

This function provides a decorator to disable compilation on a function.
It also provides the option of recursively disabling called functions.

Parameters:

- **fn** (*optional*) - The function to disable
- **recursive** (*optional*) - A boolean value indicating whether the disabling should be recursive.
- **reason** (*optional*) - A string value indicating the reason for disabling the function.