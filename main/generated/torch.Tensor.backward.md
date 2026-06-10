# torch.Tensor.backward

Tensor.backward(*gradient=None*, *retain_graph=None*, *create_graph=False*, *inputs=None*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/_tensor.py#L566)

Computes the gradient of current tensor wrt graph leaves.

The graph is differentiated using the chain rule. If the tensor is
non-scalar (i.e. its data has more than one element) and requires
gradient, the function additionally requires specifying a `gradient`.
It should be a tensor of matching type and shape, that represents
the gradient of the differentiated function w.r.t. `self`.

This function accumulates gradients in the leaves - you might need to zero
`.grad` attributes or set them to `None` before calling it.
See [Default gradient layouts](../autograd.html#default-grad-layouts)
for details on the memory layout of accumulated gradients.

Note

If you run any forward ops, create `gradient`, and/or call `backward`
in a user-specified CUDA stream context, see
[Stream semantics of backward passes](../notes/cuda.html#bwd-cuda-stream-semantics).

Note

When `inputs` are provided and a given input is not a leaf,
the current implementation will call its grad_fn (though it is not strictly needed to get this gradients).
It is an implementation detail on which the user should not rely.
See [pytorch/pytorch#60521](https://github.com/pytorch/pytorch/pull/60521#issuecomment-867061780) for more details.

Parameters:

- **gradient** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The gradient of the function
being differentiated w.r.t. `self`.
This argument can be omitted if `self` is a scalar. Defaults to `None`.
- **retain_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `False`, the graph used to compute the grads will be freed;
If `True`, it will be retained. The default is `None`, in which case the value is inferred from `create_graph`
(i.e., the graph is retained only when higher-order derivative tracking is requested). Note that in nearly all cases
setting this option to True is not needed and often can be worked around in a much more efficient way.
- **create_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, graph of the derivative will
be constructed, allowing to compute higher order derivative
products. Defaults to `False`.
- **inputs** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Tensor*](../tensors.html#torch.Tensor)*]**,**optional*) - Inputs w.r.t. which
the gradient will be accumulated into `.grad`. All other tensors will be
ignored. If not provided, the gradient is accumulated into all the leaf
Tensors that were used to compute the `tensors`. A dict of tensors
(e.g. `dict(model.named_parameters())`) is also accepted.
Defaults to `None`.