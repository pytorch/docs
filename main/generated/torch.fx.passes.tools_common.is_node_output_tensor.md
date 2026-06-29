# torch.fx.passes.tools_common.is_node_output_tensor

torch.fx.passes.tools_common.is_node_output_tensor(*node*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/fx/passes/tools_common.py#L88)

Checks if the node output produces a Tensor or not.

> NOTE: This requires to run ShapeProp on the containing fx graph before
> calling this function. This is because it works by checking the type
> metadata on the node. This metadata is produced by the ShapeProp.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)