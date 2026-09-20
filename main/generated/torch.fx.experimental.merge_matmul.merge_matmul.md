# torch.fx.experimental.merge_matmul.merge_matmul

torch.fx.experimental.merge_matmul.merge_matmul(*in_mod*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/fx/experimental/merge_matmul.py#L90)

A graph transformation that merges matrix multiplication operations that share the same right-hand
side operand into one large matrix multiplication.

```
____ _________ _________
 ---- | | | | M| A * C |
M| A | T| B | * K| C | = |---------|
 ---- , | | | | T| B * C |
 K ---- --------- ---------
 K R R
```

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)