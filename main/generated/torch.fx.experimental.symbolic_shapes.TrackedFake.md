# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/6ced8259c1c883abd806189dbf32b9707f69adeb/torch/fx/experimental/symbolic_shapes.py#L2388)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.