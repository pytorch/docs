# TrackedFake

*class*torch.fx.experimental.symbolic_shapes.TrackedFake(*fake*, *source*, *symbolic_context*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/experimental/symbolic_shapes.py#L2369)

Tracks the sources of all fake tensors we wrap in Dynamo.
Used by shape guard computation.