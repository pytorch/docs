# torch.fx.passes.pass_manager.loop_pass

torch.fx.passes.pass_manager.loop_pass(*base_pass*, *n_iter=None*, *predicate=None*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/fx/passes/pass_manager.py#L86)

Convenience wrapper for passes which need to be applied multiple times.

Exactly one of n_iter`or `predicate must be specified.

Parameters:

- **base_pass** (*Callable**[**Object**,**Object**]*) - pass to be applied in loop
- **n_iter** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - number of times to loop pass
- **predicate** (*Callable**[**Object**,*[*bool*](https://docs.python.org/3/library/functions.html#bool)*]**,**optional*) -

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[*_T*], *_T*]