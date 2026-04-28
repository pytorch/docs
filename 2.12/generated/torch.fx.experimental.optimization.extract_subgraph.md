# torch.fx.experimental.optimization.extract_subgraph

torch.fx.experimental.optimization.extract_subgraph(*orig_module*, *nodes*, *inputs*, *outputs*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/fx/experimental/optimization.py#L137)

Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.