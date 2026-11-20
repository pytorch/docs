# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/fx/experimental/symbolic_shapes.py#L2417)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.