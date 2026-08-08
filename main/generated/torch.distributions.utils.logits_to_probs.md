# torch.distributions.utils.logits_to_probs

torch.distributions.utils.logits_to_probs(*logits*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/distributions/utils.py#L90)

Converts a tensor of logits into probabilities. Note that for the
binary case, each value denotes log odds, whereas for the
multi-dimensional case, the values along the last dimension denote
the log probabilities (possibly unnormalized) of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)