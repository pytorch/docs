# torch.fx.experimental.unification.unification_tools.get_in

torch.fx.experimental.unification.unification_tools.get_in(*keys*, *coll*, *default=None*, *no_default=False*)[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/fx/experimental/unification/unification_tools.py#L358)

Returns coll[i0][i1]...[iX] where [i0, i1, ..., iX]==keys.

If coll[i0][i1]...[iX] cannot be found, returns `default`, unless
`no_default` is specified, then it raises KeyError or IndexError.

`get_in` is a generalization of `operator.getitem` for nested data
structures such as dictionaries and lists.

```
>>> transaction = {
... "name": "Alice",
... "purchase": {"items": ["Apple", "Orange"], "costs": [0.50, 1.25]},
... "credit card": "5555-1234-1234-1234",
... }
>>> get_in(["purchase", "items", 0], transaction)
'Apple'
>>> get_in(["name"], transaction)
'Alice'
>>> get_in(["purchase", "total"], transaction)
>>> get_in(["purchase", "items", "apple"], transaction)
>>> get_in(["purchase", "items", 10], transaction)
>>> get_in(["purchase", "total"], transaction, 0)
0
>>> get_in(["y"], {}, no_default=True)
Traceback (most recent call last):
 ...
KeyError: 'y'
```

See also

itertoolz.get
operator.getitem

Return type:

[object](https://docs.python.org/3/library/functions.html#object)