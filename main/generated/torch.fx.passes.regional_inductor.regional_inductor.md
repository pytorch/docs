# torch.fx.passes.regional_inductor.regional_inductor

torch.fx.passes.regional_inductor.regional_inductor(*gm*, **example_args*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/passes/regional_inductor.py#L269)

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