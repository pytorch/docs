# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/a4a15a72064ca010a723eae7c73835fe206f8de6/torch/fx/experimental/symbolic_shapes.py#L2417)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.