# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/optimization.py#L138)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)