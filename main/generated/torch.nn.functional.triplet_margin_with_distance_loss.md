# torch.nn.functional.triplet_margin_with_distance_loss

torch.nn.functional.triplet_margin_with_distance_loss(*anchor*, *positive*, *negative*, ***, *distance_function=None*, *margin=1.0*, *swap=False*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/nn/functional.py#L6031)

Compute the triplet margin loss for input tensors using a custom distance function.

See [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)