# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/experimental/symbolic_shapes.py#L2405)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.