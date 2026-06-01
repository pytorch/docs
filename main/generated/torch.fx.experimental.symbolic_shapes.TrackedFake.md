# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/symbolic_shapes.py#L2369)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.