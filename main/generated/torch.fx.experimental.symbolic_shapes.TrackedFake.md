# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/fx/experimental/symbolic_shapes.py#L2389)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.