# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/experimental/symbolic_shapes.py#L2417)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.