# torch.sym_sum

torch.sym_sum(**args*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/__init__.py#L1328)

N-ary add which is faster to compute for long lists than iterated binary
addition. Only does something special for integers.

Accepts both `sym_sum([a, b, c])` and `sym_sum(a, b, c)`.

Return type:

IntLikeType