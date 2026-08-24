# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/fx/experimental/symbolic_shapes.py#L2390)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.