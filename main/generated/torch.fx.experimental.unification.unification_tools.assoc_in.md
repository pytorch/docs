# torch.fx.experimental.unification.unification_tools.assoc_in

torch.fx.experimental.unification.unification_tools.assoc_in(*d*, *keys*, *value*, *factory=<class 'dict'>*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/fx/experimental/unification/unification_tools.py#L272)

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

[object](https://docs.python.org/3/builtins/functions.html#object)