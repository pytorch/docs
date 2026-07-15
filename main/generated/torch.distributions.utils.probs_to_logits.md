# torch.distributions.utils.probs_to_logits

torch.distributions.utils.probs_to_logits(*probs*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/distributions/utils.py#L128)

Converts a tensor of probabilities into logits. For the binary case,
this denotes the probability of occurrence of the event indexed by 1.
For the multi-dimensional case, the values along the last dimension
denote the probabilities of occurrence of each of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)