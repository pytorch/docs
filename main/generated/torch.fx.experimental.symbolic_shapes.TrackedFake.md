# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/fx/experimental/symbolic_shapes.py#L2369)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.