# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/fx/experimental/symbolic_shapes.py#L2390)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.