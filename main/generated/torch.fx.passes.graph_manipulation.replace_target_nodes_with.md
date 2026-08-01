# torch.fx.passes.graph_manipulation.replace_target_nodes_with

torch.fx.passes.graph_manipulation.replace_target_nodes_with(*fx_module*, *old_op*, *old_target*, *new_op*, *new_target*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/fx/passes/graph_manipulation.py#L20)

Modifies all nodes in fx_module.graph.nodes which match the specified op code
and target, and updates them to match the new op code and target.

Warning

This API is experimental and is *NOT* backward-compatible.