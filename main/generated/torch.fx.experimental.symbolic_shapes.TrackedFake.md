# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/fx/experimental/symbolic_shapes.py#L2368)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.