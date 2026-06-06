# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/fx/experimental/symbolic_shapes.py#L2369)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.