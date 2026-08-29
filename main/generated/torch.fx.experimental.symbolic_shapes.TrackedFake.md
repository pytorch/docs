# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/fx/experimental/symbolic_shapes.py#L2395)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.