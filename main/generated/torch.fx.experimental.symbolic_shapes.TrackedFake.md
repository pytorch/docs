# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/fx/experimental/symbolic_shapes.py#L2431)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.