# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/fx/experimental/symbolic_shapes.py#L2395)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.