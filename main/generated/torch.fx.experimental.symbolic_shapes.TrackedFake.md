# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/fx/experimental/symbolic_shapes.py#L2350)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.