# torch.sym_sum

torch.sym_sum(**args*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/__init__.py#L1409)

N-ary add which is faster to compute for long lists than iterated binary
addition. Only does something special for integers.

Accepts both `sym_sum([a, b, c])` and `sym_sum(a, b, c)`.

Return type:

IntLikeType