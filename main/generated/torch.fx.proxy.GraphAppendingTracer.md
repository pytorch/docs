# GraphAppendingTracer

*class*torch.fx.proxy.GraphAppendingTracer(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L578)

Note

Backwards-compatibility for this API is guaranteed.

create_arg(*a*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L410)

A method that lowers the objects seen as arguments during symbolic evaluation
into Argument types that can be stored in IR.

Can be override to support more trace-specific types.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[Argument, ...] | [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[Argument] | [*Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), Argument] | [slice](https://docs.python.org/3/library/functions.html#slice) | [range](https://docs.python.org/3/library/stdtypes.html#range) | [*Node*](../fx.html#torch.fx.Node) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool) | [complex](https://docs.python.org/3/library/functions.html#complex) | [*dtype*](../tensor_attributes.html#torch.dtype) | [*Tensor*](../tensors.html#torch.Tensor) | [*device*](../tensor_attributes.html#torch.device) | [*memory_format*](../tensor_attributes.html#torch.memory_format) | [*layout*](../tensor_attributes.html#torch.layout) | *OpOverload* | [*SymInt*](../torch.html#torch.SymInt) | [*SymBool*](../torch.html#torch.SymBool) | [*SymFloat*](../torch.html#torch.SymFloat) | None

create_node(*kind*, *target*, *args*, *kwargs*, *name=None*, *type_expr=None*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L214)

Inserts a graph node given target, args, kwargs, and name.

This method can be overridden to do extra checking, validation, or
modification of values used in node creation. For example, one might
want to disallow in-place operations from being recorded.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Node*](../fx.html#torch.fx.Node)

create_proxy(*kind*, *target*, *args*, *kwargs*, *name=None*, *type_expr=None*, *proxy_factory_fn=None*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L339)

Create a Node from the given arguments, then return the Node
wrapped in a Proxy object.

If kind = 'placeholder', then we're creating a Node that
represents the parameter of a function. If we need to encode
a default parameter, we use the `args` tuple. `args` is
otherwise empty for `placeholder` Nodes.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Proxy*](../fx.html#torch.fx.Proxy)

iter(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L496)

Called when a proxy object is being iterated over, such as

when used in control flow. Normally we don't know what to do because
we don't know the value of the proxy, but a custom tracer can attach more
information to the graph node using create_node and can choose to return an iterator.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Iterator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)

keys(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L514)

Called when a proxy object is has the keys() method called.

This is what happens when ** is called on a proxy. This should return an
iterator it ** is suppose to work in your custom tracer.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Proxy*](../fx.html#torch.fx.Proxy)

proxy(*node*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L335)

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[*Proxy*](../fx.html#torch.fx.Proxy)

to_bool(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/proxy.py#L485)

Called when a proxy object is being converted to a boolean, such as

when used in control flow. Normally we don't know what to do because
we don't know the value of the proxy, but a custom tracer can attach more
information to the graph node using create_node and can choose to return a value.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)