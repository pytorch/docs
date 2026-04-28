# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/fx/experimental/optimization.py#L138)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)