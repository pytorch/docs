# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/6e3cf2e4280672104341718ea51a55799bb3aca4/torch/fx/experimental/symbolic_shapes.py#L2368)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.