# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/fx/experimental/symbolic_shapes.py#L2395)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.