# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/fx/experimental/symbolic_shapes.py#L2350)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.