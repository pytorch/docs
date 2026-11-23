# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/fx/experimental/symbolic_shapes.py#L2417)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.