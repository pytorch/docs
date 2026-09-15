# torch.fx.passes.pass_manager.loop_pass

torch.fx.passes.pass_manager.loop_pass(*base_pass*, *n_iter=None*, *predicate=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/passes/pass_manager.py#L86)

Convenience wrapper for passes which need to be applied multiple times.

Exactly one of n_iter`or `predicate must be specified.

Parameters:

- **base_pass** (*Callable**[**Object**,**Object**]*) - pass to be applied in loop
- **n_iter** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - number of times to loop pass
- **predicate** (*Callable**[**Object**,*[*bool*](https://docs.python.org/3/builtins/functions.html#bool)*]**,**optional*) -

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[*_T*], *_T*]