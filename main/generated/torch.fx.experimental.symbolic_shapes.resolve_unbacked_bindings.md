# torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings

torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings(*shape_env*, *bindings*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/fx/experimental/symbolic_shapes.py#L581)

When we do fake tensor prop, we oftentimes will allocate new unbacked symints.
We then run proxy tensor mode, which populates node.meta["unbacked_bindings"]
with these new symints. To ensure consistency we use PropagateUnbackedSymInts
to rename unbacked bindings to their old ones. But all of the node metas are
still using the old bindings from before the renaming. This function helps to
post facto apply any renamings discovered in the PropagateUnbackedSymInts pass.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*Symbol*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*KeyEntry*, ...]] | None