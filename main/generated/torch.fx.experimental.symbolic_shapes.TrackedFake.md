# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/fx/experimental/symbolic_shapes.py#L2389)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.