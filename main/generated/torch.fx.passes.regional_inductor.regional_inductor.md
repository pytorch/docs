# torch.fx.passes.regional_inductor.regional_inductor

torch.fx.passes.regional_inductor.regional_inductor(*gm*, **example_args*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/fx/passes/regional_inductor.py#L269)

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