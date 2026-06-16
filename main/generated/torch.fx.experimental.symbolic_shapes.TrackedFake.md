# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/fx/experimental/symbolic_shapes.py#L2375)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.