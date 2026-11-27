# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/fx/experimental/symbolic_shapes.py#L2431)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.