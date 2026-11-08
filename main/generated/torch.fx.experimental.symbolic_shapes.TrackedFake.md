# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/symbolic_shapes.py#L2396)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.