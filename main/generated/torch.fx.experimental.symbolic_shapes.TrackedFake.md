# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/fx/experimental/symbolic_shapes.py#L2383)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.