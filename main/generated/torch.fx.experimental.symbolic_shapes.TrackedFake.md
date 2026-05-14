# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/fx/experimental/symbolic_shapes.py#L2368)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.