# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/fx/experimental/symbolic_shapes.py#L2417)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.