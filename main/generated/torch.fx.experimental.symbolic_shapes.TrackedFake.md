# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/6728ae647ab077842210f24d515b54df7709e144/torch/fx/experimental/symbolic_shapes.py#L2396)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.