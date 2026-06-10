# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/fx/experimental/optimization.py#L138)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)