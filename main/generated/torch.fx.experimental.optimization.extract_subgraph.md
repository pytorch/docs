# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/27b52de22e4e5fa572c07a4065423083a41b8756/torch/fx/experimental/optimization.py#L138)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)