# torch.nn.functional.triplet_margin_with_distance_loss

torch.nn.functional.triplet_margin_with_distance_loss(*anchor*, *positive*, *negative*, ***, *distance_function=None*, *margin=1.0*, *swap=False*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/nn/functional.py#L6031)

Compute the triplet margin loss for input tensors using a custom distance function.

See [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)