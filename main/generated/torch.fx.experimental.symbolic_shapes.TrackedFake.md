# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/fx/experimental/symbolic_shapes.py#L2350)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.