# torch.nn.functional.triplet_margin_loss

torch.nn.functional.triplet_margin_loss(*anchor*, *positive*, *negative*, *margin=1.0*, *p=2*, *eps=1e-06*, *swap=False*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/nn/functional.py#L5989)

Compute the triplet loss between given input tensors and a margin greater than 0.

See [`TripletMarginLoss`](torch.nn.TripletMarginLoss.html#torch.nn.TripletMarginLoss) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)