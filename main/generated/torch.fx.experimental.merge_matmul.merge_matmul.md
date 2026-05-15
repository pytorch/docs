# torch.fx.experimental.merge_matmul.merge_matmul

torch.fx.experimental.merge_matmul.merge_matmul(*in_mod*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/fx/experimental/merge_matmul.py#L90)

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