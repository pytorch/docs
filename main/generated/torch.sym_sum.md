# torch.sym_sum

torch.sym_sum(**args*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/__init__.py#L958)

N-ary add which is faster to compute for long lists than iterated binary
addition. Only does something special for integers.

Accepts both `sym_sum([a, b, c])` and `sym_sum(a, b, c)`.