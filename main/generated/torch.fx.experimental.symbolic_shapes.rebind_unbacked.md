# torch.fx.experimental.symbolic_shapes.rebind_unbacked

torch.fx.experimental.symbolic_shapes.rebind_unbacked(*shape_env*, *n*, *result*)[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/fx/experimental/symbolic_shapes.py#L603)

Suppose we are retracing a pre-existing FX graph that previously had
fake tensor propagation (and therefore unbacked SymInts). When we retrace,
we re-propagate fake tensors, which results in new unbacked SymInts.
When this happens, we need to tell the shape environment about the equivalence
of the old and new unbacked SymInts. Pass us the old torch.fx.Node (which
has the old binding information) and the new result (which we can extract the
new unbacked SymInts out from).