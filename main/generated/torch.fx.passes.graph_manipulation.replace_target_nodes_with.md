# torch.fx.passes.graph_manipulation.replace_target_nodes_with

torch.fx.passes.graph_manipulation.replace_target_nodes_with(*fx_module*, *old_op*, *old_target*, *new_op*, *new_target*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/fx/passes/graph_manipulation.py#L20)

Modifies all nodes in fx_module.graph.nodes which match the specified op code
and target, and updates them to match the new op code and target.

Warning

This API is experimental and is *NOT* backward-compatible.