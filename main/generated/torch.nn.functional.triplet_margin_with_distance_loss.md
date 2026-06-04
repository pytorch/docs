# torch.nn.functional.triplet_margin_with_distance_loss

torch.nn.functional.triplet_margin_with_distance_loss(*anchor*, *positive*, *negative*, ***, *distance_function=None*, *margin=1.0*, *swap=False*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/40a42e9b743c053cc9e6d11c0502026a8f5d7d57/torch/nn/functional.py#L5932)

Compute the triplet margin loss for input tensors using a custom distance function.

See [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)