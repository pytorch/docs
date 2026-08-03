# torch.distributions.utils.broadcast_all

torch.distributions.utils.broadcast_all(**values*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/distributions/utils.py#L27)

Given a list of values (possibly containing numbers), returns a list where each
value is broadcasted based on the following rules:

- torch.*Tensor instances are broadcasted as per [Broadcasting semantics](../notes/broadcasting.html#broadcasting-semantics).
- Number instances (scalars) are upcast to tensors having
the same size and type as the first tensor passed to values. If all the
values are scalars, then they are upcasted to scalar Tensors.

Parameters:

**values** (list of Number, torch.*Tensor or objects implementing __torch_function__) -

Raises:

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) - if any of the values is not a Number instance,
 a torch.*Tensor instance, or an instance implementing __torch_function__

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), ...]