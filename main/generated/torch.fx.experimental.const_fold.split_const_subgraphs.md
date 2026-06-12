# torch.fx.experimental.const_fold.split_const_subgraphs

torch.fx.experimental.const_fold.split_const_subgraphs(*module*, *skip_folding_node_fn=None*, *device_for_folded_attrs='cpu'*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/fx/experimental/const_fold.py#L194)

Looks through module for any nodes that have all constant attribute inputs
and separates them out into their own constant subgraph, and returns a
FoldedGraphModule which runs that constant subgraph on the first run to set
attributes on the module prior to running the non-constant portion of the
graph.

Return type:

*FoldedGraphModule*