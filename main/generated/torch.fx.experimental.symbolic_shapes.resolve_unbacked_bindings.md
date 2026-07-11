# torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings

torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings(*shape_env*, *bindings*)[[source]](https://github.com/pytorch/pytorch/blob/e708521bdf92712674ed3a0d332b56c356502328/torch/fx/experimental/symbolic_shapes.py#L580)

When we do fake tensor prop, we oftentimes will allocate new unbacked symints.
We then run proxy tensor mode, which populates node.meta["unbacked_bindings"]
with these new symints. To ensure consistency we use PropagateUnbackedSymInts
to rename unbacked bindings to their old ones. But all of the node metas are
still using the old bindings from before the renaming. This function helps to
post facto apply any renamings discovered in the PropagateUnbackedSymInts pass.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*Symbol*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*KeyEntry*, ...]] | None