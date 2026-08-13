# torch.fx.experimental.graph_gradual_typechecker.conv2d_inference_rule

torch.fx.experimental.graph_gradual_typechecker.conv2d_inference_rule(*n*, *module_instance*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/graph_gradual_typechecker.py#L427)

Given a Conv2D instance and a node check the following conditions:
- the input type can be expanded to a size 4 tensor: t = (x_1, x_2, H, W)
- the current node type can be expanded to a size 4 tensor: t' = (x_1', x_2', x_3', x_4')
- x_2 is consistent with the module's in_channels
- let o = (x_1, out_channels, H_out, W_out)
then the output is the greatest upper bound of o and the existing node type t'.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)