# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/symbolic_shapes.py#L2390)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.