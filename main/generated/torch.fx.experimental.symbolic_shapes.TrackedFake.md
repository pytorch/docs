# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/fx/experimental/symbolic_shapes.py#L2369)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.