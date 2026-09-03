# CodeGen

*class*torch.fx.graph.CodeGen[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L368)

Warning

This API is experimental and is *NOT* backward-compatible.

additional_globals()[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L495)

If your codegen uses extra global values, add tuples of (identifier,reference to the value) here.
For example, return ['List', typing.List] if you need `List` in the global context.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]]

gen_fn_def(*free_vars*, *maybe_return_annotation*, ***, *expanded_def=False*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L432)

Given the free variables and a return annotation, generates the beginning of the FX function.
By default, gen_fn_def(['a', 'b'], '') == 'def {self._func_name}(a, b):'

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

generate_output(*output_args*, ***, *descs=None*, *repr_fn=None*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L456)

Given the output arguments, generates the return statement of the FX function.
Note: The returned statement should not be indented.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

process_inputs(**args*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L476)

Transforms the inputs so that the graph can take them as arguments, as
non-default codegen may result in the inputs to the function being
different from the inputs to the graph.

If the graph was directly runnable, this invariant should hold true
f.graph.process_outputs(f.graph(*f.graph.process_inputs(*inputs))) == f(*inputs)

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Unpack*]

process_outputs(*outputs*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/graph.py#L487)

Transforms the outputs of the graph to be identical to the codegen.

See `process_inputs` for more details.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)