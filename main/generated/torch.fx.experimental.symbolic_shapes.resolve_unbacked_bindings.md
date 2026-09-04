# torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings

torch.fx.experimental.symbolic_shapes.resolve_unbacked_bindings(*shape_env*, *bindings*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/symbolic_shapes.py#L582)

When we do fake tensor prop, we oftentimes will allocate new unbacked symints.
We then run proxy tensor mode, which populates node.meta["unbacked_bindings"]
with these new symints. To ensure consistency we use PropagateUnbackedSymInts
to rename unbacked bindings to their old ones. But all of the node metas are
still using the old bindings from before the renaming. This function helps to
post facto apply any renamings discovered in the PropagateUnbackedSymInts pass.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*Symbol*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*KeyEntry*, ...]] | None