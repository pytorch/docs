# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/experimental/symbolic_shapes.py#L2395)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.