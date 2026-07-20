# torch.fx.experimental.const_fold.split_const_subgraphs

torch.fx.experimental.const_fold.split_const_subgraphs(*module*, *skip_folding_node_fn=None*, *device_for_folded_attrs='cpu'*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/fx/experimental/const_fold.py#L194)

Looks through module for any nodes that have all constant attribute inputs
and separates them out into their own constant subgraph, and returns a
FoldedGraphModule which runs that constant subgraph on the first run to set
attributes on the module prior to running the non-constant portion of the
graph.

skip_folding_node_fn, if provided, may be invoked on nodes owned by nested
call_module subgraphs, not just top-level nodes: a call_module node is
folded atomically, so it is skipped if any node inside its subgraph is
skipped. Predicates must therefore be node-local; one that needs to resolve a
node's target to a submodule must use node.graph.owning_module rather than
a captured top-level module.

Return type:

*FoldedGraphModule*