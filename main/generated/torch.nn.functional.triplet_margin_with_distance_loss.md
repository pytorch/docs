# torch.nn.functional.triplet_margin_with_distance_loss

torch.nn.functional.triplet_margin_with_distance_loss(*anchor*, *positive*, *negative*, ***, *distance_function=None*, *margin=1.0*, *swap=False*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/nn/functional.py#L5638)

Compute the triplet margin loss for input tensors using a custom distance function.

See [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)