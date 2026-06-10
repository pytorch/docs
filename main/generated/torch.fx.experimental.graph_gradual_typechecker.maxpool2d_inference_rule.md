# torch.fx.experimental.graph_gradual_typechecker.maxpool2d_inference_rule

torch.fx.experimental.graph_gradual_typechecker.maxpool2d_inference_rule(*n*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/experimental/graph_gradual_typechecker.py#L497)

Given a MaxPool2D instance and a node check the following conditions:

- Input size matches size 3 or 4
- Current node type is consistent with the output type we will calculate
- Input size matches output size and the last two dimensions of the output
are w_out and h_out. The remaining dimensions are the same as the input
- Our final result is the greatest upper bound of the output we calculate
and the current node type.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)