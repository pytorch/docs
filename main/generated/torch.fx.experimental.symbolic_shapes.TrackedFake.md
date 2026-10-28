# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/fx/experimental/symbolic_shapes.py#L2396)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.