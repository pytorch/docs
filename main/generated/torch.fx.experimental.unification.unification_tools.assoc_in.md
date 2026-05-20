# torch.fx.experimental.unification.unification_tools.assoc_in

torch.fx.experimental.unification.unification_tools.assoc_in(*d*, *keys*, *value*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/fx/experimental/unification/unification_tools.py#L272)

Return a new dict with new, potentially nested, key value pair

```
>>> purchase = {
... "name": "Alice",
... "order": {"items": ["Apple", "Orange"], "costs": [0.50, 1.25]},
... "credit card": "5555-1234-1234-1234",
... }
>>> assoc_in(purchase, ["order", "costs"], [0.25, 1.00]) 
{'credit card': '5555-1234-1234-1234',
 'name': 'Alice',
 'order': {'costs': [0.25, 1.00], 'items': ['Apple', 'Orange']}}
```

Return type:

[object](https://docs.python.org/3/library/functions.html#object)