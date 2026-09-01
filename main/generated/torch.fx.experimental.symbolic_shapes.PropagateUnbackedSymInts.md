# PropagateUnbackedSymInts

*class*torch.fx.experimental.symbolic_shapes.PropagateUnbackedSymInts(*module*, *garbage_collect_values=True*, *graph=None*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/experimental/symbolic_shapes.py#L9230)

boxed_run(*args_list*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L239)

Run module via interpretation and return the result. This uses the "boxed"
calling convention, where you pass a list of arguments, which will be cleared
by the interpreter. This ensures that input tensors are promptly deallocated.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

call_function(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L356)

Execute a `call_function` node and return the result.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Return

Any: The value returned by the function invocation

Note

Backwards-compatibility for this API is guaranteed.

call_method(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L379)

Execute a `call_method` node and return the result.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Return

Any: The value returned by the method invocation

Note

Backwards-compatibility for this API is guaranteed.

call_module(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L404)

Execute a `call_module` node and return the result.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Return

Any: The value returned by the module invocation

Note

Backwards-compatibility for this API is guaranteed.

fetch_args_kwargs_from_env(*n*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L472)

Fetch the concrete values of `args` and `kwargs` of node `n`
from the current execution environment.

Parameters:

**n** ([*Node*](../fx.html#torch.fx.Node)) - The node for which `args` and `kwargs` should be fetched.

Returns:

`args` and `kwargs` with concrete values for `n`.

Return type:

Tuple[Tuple, Dict]

Note

Backwards-compatibility for this API is guaranteed.

fetch_attr(*target*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L451)

Fetch an attribute from the `Module` hierarchy of `self.module`.

Parameters:

**target** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The fully-qualified name of the attribute to fetch

Returns:

The value of the attribute.

Return type:

Any

Note

Backwards-compatibility for this API is guaranteed.

get_attr(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L334)

Execute a `get_attr` node. Will retrieve an attribute
value from the `Module` hierarchy of `self.module`.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Returns:

The value of the attribute that was retrieved

Return type:

Any

Note

Backwards-compatibility for this API is guaranteed.

map_nodes_to_values(*args*, *n*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L494)

Recursively descend through `args` and look up the concrete value
for each `Node` in the current execution environment.

Parameters:

- **args** (*Argument*) - Data structure within which to look up concrete values
- **n** ([*Node*](../fx.html#torch.fx.Node)) - Node to which `args` belongs. This is only used for error reporting.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[Argument, ...] | [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[Argument] | [*Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), Argument] | [slice](https://docs.python.org/3/library/functions.html#slice) | [range](https://docs.python.org/3/library/stdtypes.html#range) | [*Node*](../fx.html#torch.fx.Node) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [complex](https://docs.python.org/3/library/functions.html#complex) | [*dtype*](../tensor_attributes.html#torch.dtype) | [*Tensor*](../tensors.html#torch.Tensor) | [*device*](../tensor_attributes.html#torch.device) | [*memory_format*](../tensor_attributes.html#torch.memory_format) | [*layout*](../tensor_attributes.html#torch.layout) | *OpOverload* | [*SymInt*](../torch.html#torch.SymInt) | [*SymBool*](../torch.html#torch.SymBool) | [*SymFloat*](../torch.html#torch.SymFloat) | None

Note

Backwards-compatibility for this API is guaranteed.

output(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L430)

Execute an `output` node. This really just retrieves
the value referenced by the `output` node and returns it.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Returns:

The return value referenced by the output node

Return type:

Any

Note

Backwards-compatibility for this API is guaranteed.

placeholder(*target*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L297)

Execute a `placeholder` node. Note that this is stateful:
`Interpreter` maintains an internal iterator over
arguments passed to `run` and this method returns
next() on that iterator.

Parameters:

- **target** (*Target*) - The call target for this node. See
[Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node) for
details on semantics
- **args** (*Tuple*) - Tuple of positional args for this invocation
- **kwargs** (*Dict*) - Dict of keyword arguments for this invocation

Returns:

The argument value that was retrieved.

Return type:

Any

Note

Backwards-compatibility for this API is guaranteed.

run(**args*, *initial_env=None*, *enable_io_processing=True*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/interpreter.py#L147)

Run module via interpretation and return the result.

Parameters:

- ***args** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) - The arguments to the Module to run, in positional order
- **initial_env** (*Optional**[**Dict**[*[*Node*](../fx.html#torch.fx.Node)*,**Any**]**]*) - An optional starting environment for execution.
This is a dict mapping Node to any value. This can be used, for example, to
pre-populate results for certain Nodes so as to do only partial evaluation within
the interpreter.
- **enable_io_processing** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If true, we process the inputs and outputs with graph's process_inputs and
process_outputs function first before using them.

Returns:

The value returned from executing the Module

Return type:

Any

Note

Backwards-compatibility for this API is guaranteed.

run_node(*n*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/experimental/symbolic_shapes.py#L9231)

Run an FX node, propagating unbacked Symbol bindings to the new fake tensor

Return type:

[*Tensor*](../tensors.html#torch.Tensor) | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), ...]