# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/symbolic_shapes.py#L2389)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.