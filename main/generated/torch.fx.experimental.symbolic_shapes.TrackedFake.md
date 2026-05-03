# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/fx/experimental/symbolic_shapes.py#L2350)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.