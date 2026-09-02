# torch.fx.experimental.merge_matmul.merge_matmul

torch.fx.experimental.merge_matmul.merge_matmul(*in_mod*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/experimental/merge_matmul.py#L90)

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