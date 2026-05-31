# torch.nn.functional.triplet_margin_with_distance_loss

torch.nn.functional.triplet_margin_with_distance_loss(*anchor*, *positive*, *negative*, ***, *distance_function=None*, *margin=1.0*, *swap=False*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/nn/functional.py#L5791)

Compute the triplet margin loss for input tensors using a custom distance function.

See [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)