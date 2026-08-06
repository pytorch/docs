# torch.distributions.utils.probs_to_logits

torch.distributions.utils.probs_to_logits(*probs*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/distributions/utils.py#L128)

Converts a tensor of probabilities into logits. For the binary case,
this denotes the probability of occurrence of the event indexed by 1.
For the multi-dimensional case, the values along the last dimension
denote the probabilities of occurrence of each of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)