# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/symbolic_shapes.py#L2396)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.