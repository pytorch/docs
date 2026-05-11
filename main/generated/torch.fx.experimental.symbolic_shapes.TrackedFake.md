# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/experimental/symbolic_shapes.py#L2368)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.