# torch.sym_sum

torch.sym_sum(**args*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/__init__.py#L1320)

N-ary add which is faster to compute for long lists than iterated binary
addition. Only does something special for integers.

Accepts both `sym_sum([a, b, c])` and `sym_sum(a, b, c)`.

Return type:

IntLikeType