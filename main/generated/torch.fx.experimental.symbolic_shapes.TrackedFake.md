# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/fx/experimental/symbolic_shapes.py#L2383)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.