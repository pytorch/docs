# CodeGen

*class*torch.fx.graph.CodeGen[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L366)

Warning

This API is experimental and is *NOT* backward-compatible.

additional_globals()[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L493)

If your codegen uses extra global values, add tuples of (identifier,reference to the value) here.
For example, return ['List', typing.List] if you need `List` in the global context.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]]

gen_fn_def(*free_vars*, *maybe_return_annotation*, ***, *expanded_def=False*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L430)

Given the free variables and a return annotation, generates the beginning of the FX function.
By default, gen_fn_def(['a', 'b'], '') == 'def {self._func_name}(a, b):'

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

generate_output(*output_args*, ***, *descs=None*, *repr_fn=None*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L454)

Given the output arguments, generates the return statement of the FX function.
Note: The returned statement should not be indented.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

process_inputs(**args*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L474)

Transforms the inputs so that the graph can take them as arguments, as
non-default codegen may result in the inputs to the function being
different from the inputs to the graph.

If the graph was directly runnable, this invariant should hold true
f.graph.process_outputs(f.graph(*f.graph.process_inputs(*inputs))) == f(*inputs)

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

process_outputs(*outputs*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/fx/graph.py#L485)

Transforms the outputs of the graph to be identical to the codegen.

See `process_inputs` for more details.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)