# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/fx/experimental/symbolic_shapes.py#L2368)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.