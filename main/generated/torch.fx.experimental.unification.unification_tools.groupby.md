# torch.fx.experimental.unification.unification_tools.groupby

torch.fx.experimental.unification.unification_tools.groupby(*key*, *seq*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/unification/unification_tools.py#L420)

Group a collection by a key function

```
>>> names = ["Alice", "Bob", "Charlie", "Dan", "Edith", "Frank"]
>>> groupby(len, names) 
{3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}
```

```
>>> iseven = lambda x: x % 2 == 0
>>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8]) 
{False: [1, 3, 5, 7], True: [2, 4, 6, 8]}
```

Non-callable keys imply grouping on a member.

```
>>> groupby(
... "gender",
... [
... {"name": "Alice", "gender": "F"},
... {"name": "Bob", "gender": "M"},
... {"name": "Charlie", "gender": "M"},
... ],
... ) 
{'F': [{'gender': 'F', 'name': 'Alice'}],
 'M': [{'gender': 'M', 'name': 'Bob'},
 {'gender': 'M', 'name': 'Charlie'}]}
```

Not to be confused with `itertools.groupby`

See also

countby

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[object](https://docs.python.org/3/library/functions.html#object), [list](https://docs.python.org/3/library/stdtypes.html#list)[[object](https://docs.python.org/3/library/functions.html#object)]]