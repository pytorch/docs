# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/fx/experimental/optimization.py#L138)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)