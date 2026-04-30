# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/fx/experimental/symbolic_shapes.py#L2350)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.