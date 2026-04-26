# torch.fx.passes.regional_inductor.regional_inductor

torch.fx.passes.regional_inductor.regional_inductor(*gm*, **example_args*)[[source]](https://github.com/pytorch/pytorch/blob/dff44973f3eba04a92de8499c17cd237997140f2/torch/fx/passes/regional_inductor.py#L267)

Scoops out inductor marked regions and compiles them with inductor.

Inductor options should be provided via the annotation API:

```
with fx_traceback.annotate(
 {
 "compile_with_inductor": {
 "inductor_configs": {
 "max_autotune": True,
 "triton.cudagraphs": False,
 }
 }
 }
):
 ...
```

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)