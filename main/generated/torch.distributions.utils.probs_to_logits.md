# torch.distributions.utils.probs_to_logits

torch.distributions.utils.probs_to_logits(*probs*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/distributions/utils.py#L128)

Converts a tensor of probabilities into logits. For the binary case,
this denotes the probability of occurrence of the event indexed by 1.
For the multi-dimensional case, the values along the last dimension
denote the probabilities of occurrence of each of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)