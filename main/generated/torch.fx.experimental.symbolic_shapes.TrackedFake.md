# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/symbolic_shapes.py#L2395)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.