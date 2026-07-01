# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/fx/experimental/symbolic_shapes.py#L2383)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.