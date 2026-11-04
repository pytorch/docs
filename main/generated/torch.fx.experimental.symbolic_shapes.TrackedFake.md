# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/e5fed85d1847df3bfad77cb48791e6b5d4957cee/torch/fx/experimental/symbolic_shapes.py#L2396)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.