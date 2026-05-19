# torch.autograd.backward

torch.autograd.backward(*tensors*, *grad_tensors=None*, *retain_graph=None*, *create_graph=False*, *grad_variables=None*, *inputs=None*)[[source]](https://github.com/pytorch/pytorch/blob/2700915a75e05f161593ddd3bb8f6c01c29b8777/torch/autograd/__init__.py#L255)

Compute the sum of gradients of given tensors with respect to graph leaves.

The graph is differentiated using the chain rule. If any of `tensors`
are non-scalar (i.e. their data has more than one element) and require
gradient, then the Jacobian-vector product would be computed, in this
case the function additionally requires specifying `grad_tensors`.
It should be a sequence of matching length, that contains the "vector"
in the Jacobian-vector product, usually the gradient of the differentiated
function w.r.t. corresponding tensors (`None` is an acceptable value for
all tensors that don't need gradient tensors).

This function accumulates gradients in the leaves - you might need to zero
`.grad` attributes or set them to `None` before calling it.
See [Default gradient layouts](../autograd.html#default-grad-layouts)
for details on the memory layout of accumulated gradients.

Note

Using this method with `create_graph=True` will create a reference cycle
between the parameter and its gradient which can cause a memory leak.
We recommend using `autograd.grad` when creating the graph to avoid this.
If you have to use this function, make sure to reset the `.grad` fields of your
parameters to `None` after use to break the cycle and avoid the leak.

Note

If you run any forward ops, create `grad_tensors`, and/or call `backward`
in a user-specified CUDA stream context, see
[Stream semantics of backward passes](../notes/cuda.html#bwd-cuda-stream-semantics).

Note

When `inputs` are provided and a given input is not a leaf,
the current implementation will call its grad_fn (even though it is not strictly needed to get these gradients).
It is an implementation detail on which the user should not rely.
See [pytorch/pytorch#60521](https://github.com/pytorch/pytorch/pull/60521#issuecomment-867061780) for more details.

Parameters:

- **tensors** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)*or**Sequence**[*[*GradientEdge*](../autograd.html#torch.autograd.graph.GradientEdge)*] or*[*GradientEdge*](../autograd.html#torch.autograd.graph.GradientEdge)) - Tensors of which
the derivative will be computed.
- **grad_tensors** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*or**None**] or*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The "vector" in
the Jacobian-vector product, usually gradients w.r.t. each element of
corresponding tensors. None values can be specified for scalar Tensors or
ones that don't require grad. If a None value would be acceptable for all
grad_tensors, then this argument is optional.
- **retain_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `False`, the graph used to compute the grad
will be freed. Note that in nearly all cases setting this option to `True`
is not needed and often can be worked around in a much more efficient
way. Defaults to the value of `create_graph`.
- **create_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, graph of the derivative will
be constructed, allowing to compute higher order derivative products.
Defaults to `False`.
- **inputs** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)*or**Sequence**[*[*GradientEdge*](../autograd.html#torch.autograd.graph.GradientEdge)*] or*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Tensor*](../tensors.html#torch.Tensor)*]**,**optional*) - Inputs w.r.t. which the gradient will be accumulated into `.grad`.
All other Tensors will be ignored. If not provided, the gradient is
accumulated into all the leaf Tensors that were used to compute the
`tensors`. A dict of tensors (e.g.
`dict(model.named_parameters())`) is also accepted, in which case
the values are used as the input tensors.