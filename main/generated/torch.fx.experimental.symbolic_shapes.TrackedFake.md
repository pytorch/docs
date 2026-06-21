# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/fx/experimental/symbolic_shapes.py#L2383)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.