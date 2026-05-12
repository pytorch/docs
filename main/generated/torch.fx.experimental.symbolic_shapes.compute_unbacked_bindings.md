# torch.fx.experimental.symbolic_shapes.compute_unbacked_bindings

torch.fx.experimental.symbolic_shapes.compute_unbacked_bindings(*shape_env*, *example_value*, *old_example_value=None*, *peek=False*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/fx/experimental/symbolic_shapes.py#L1419)

After having run fake tensor propagation and producing example_value
result, traverse example_value looking for freshly bound unbacked
symbols and record their paths for later. It is an error if
we have allocated an unbacked SymInt but it cannot be found in
example_value. (NB: this means if you have a multi-output
function, you must call this on the tuple of tensor output, you
cannot wait!)

The peek parameter lets you check out what the bindings are without
changing the affected list. This is primarily useful for ensuring
real_tensor_prop_unbacked_vals is promptly populated when propagate_real_tensors is on.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*Symbol*, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*KeyEntry*, ...]] | None