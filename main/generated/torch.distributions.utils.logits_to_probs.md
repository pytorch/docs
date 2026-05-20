# torch.distributions.utils.logits_to_probs

torch.distributions.utils.logits_to_probs(*logits*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/distributions/utils.py#L90)

Converts a tensor of logits into probabilities. Note that for the
binary case, each value denotes log odds, whereas for the
multi-dimensional case, the values along the last dimension denote
the log probabilities (possibly unnormalized) of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)