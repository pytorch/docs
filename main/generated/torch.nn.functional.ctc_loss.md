# torch.nn.functional.ctc_loss

torch.nn.functional.ctc_loss(*log_probs*, *targets*, *input_lengths*, *target_lengths*, *blank=0*, *reduction='mean'*, *zero_infinity=False*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/nn/functional.py#L3052)

Compute the Connectionist Temporal Classification loss.

See [`CTCLoss`](torch.nn.CTCLoss.html#torch.nn.CTCLoss) for details.

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](../notes/randomness.html) for more information.

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Parameters:

- **log_probs** ([*Tensor*](../tensors.html#torch.Tensor)) - (T,N,C)(T, N, C)(T,N,C) or (T,C)(T, C)(T,C) where C = number of characters in alphabet including blank,
T = input length, and N = batch size.
The logarithmized probabilities of the outputs
(e.g. obtained with [`torch.nn.functional.log_softmax()`](torch.nn.functional.log_softmax.html#torch.nn.functional.log_softmax)).
- **targets** ([*Tensor*](../tensors.html#torch.Tensor)) - (N,S)(N, S)(N,S) or (sum(target_lengths)).
May be an empty tensor if all entries in target_lengths are zero.
In the second form, the targets are assumed to be concatenated.
- **input_lengths** ([*Tensor*](../tensors.html#torch.Tensor)) - (N)(N)(N) or ()()().
Lengths of the inputs (must each be ≤T\leq T≤T)
- **target_lengths** ([*Tensor*](../tensors.html#torch.Tensor)) - (N)(N)(N) or ()()().
Lengths of the targets
- **blank** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Blank label. Default 000.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the output losses will be divided by the target lengths and
then the mean over the batch is taken, `'sum'`: the output will be
summed. Default: `'mean'`
- **zero_infinity** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to zero infinite losses and the associated gradients.
Default: `False`
Infinite losses mainly occur when the inputs are too short
to be aligned to the targets.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> log_probs = torch.randn(50, 16, 20).log_softmax(2).detach().requires_grad_()
>>> targets = torch.randint(1, 20, (16, 30), dtype=torch.long)
>>> input_lengths = torch.full((16,), 50, dtype=torch.long)
>>> target_lengths = torch.randint(10, 30, (16,), dtype=torch.long)
>>> loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)
>>> loss.backward()
```