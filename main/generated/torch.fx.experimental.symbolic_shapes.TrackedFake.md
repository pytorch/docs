# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/45fe85941b3ecb8add365f049f7fbf455c5107ff/torch/fx/experimental/symbolic_shapes.py#L2388)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.