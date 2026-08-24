# torch.distributions.utils.logits_to_probs

torch.distributions.utils.logits_to_probs(*logits*, *is_binary=False*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/distributions/utils.py#L90)

Converts a tensor of logits into probabilities. Note that for the
binary case, each value denotes log odds, whereas for the
multi-dimensional case, the values along the last dimension denote
the log probabilities (possibly unnormalized) of the events.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)