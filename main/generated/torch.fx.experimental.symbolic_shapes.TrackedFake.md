# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/fx/experimental/symbolic_shapes.py#L2390)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.