# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/fx/experimental/symbolic_shapes.py#L2390)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.