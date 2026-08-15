# torch.fx.experimental.const_fold.split_const_subgraphs

torch.fx.experimental.const_fold.split_const_subgraphs(*module*, *skip_folding_node_fn=None*, *device_for_folded_attrs='cpu'*, *is_impure_node=None*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/fx/experimental/const_fold.py#L198)

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

is_impure_node, if provided, is forwarded to eliminate_dead_code so DCE
preserves nodes the caller considers impure beyond the default
Node.is_impure() check (e.g. out-variant ops that write a pre-allocated
buffer via an out= kwarg not declared mutable in their schema).

Return type:

*FoldedGraphModule*