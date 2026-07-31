# torch.fx.passes.graph_manipulation.replace_target_nodes_with

torch.fx.passes.graph_manipulation.replace_target_nodes_with(*fx_module*, *old_op*, *old_target*, *new_op*, *new_target*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/fx/passes/graph_manipulation.py#L20)

Modifies all nodes in fx_module.graph.nodes which match the specified op code
and target, and updates them to match the new op code and target.

Warning

This API is experimental and is *NOT* backward-compatible.