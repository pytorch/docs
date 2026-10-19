# torch.distributions.utils.probs_to_logits

torch.distributions.utils.probs_to_logits(*probs*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/distributions/utils.py#L128)

Converts a tensor of probabilities into logits. For the binary case,
this denotes the probability of occurrence of the event indexed by 1.
For the multi-dimensional case, the values along the last dimension
denote the probabilities of occurrence of each of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)