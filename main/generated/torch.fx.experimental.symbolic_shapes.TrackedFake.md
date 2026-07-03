# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/symbolic_shapes.py#L2383)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.