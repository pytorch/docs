# torch.fx.experimental.unification.multipledispatch.utils.groupby

torch.fx.experimental.unification.multipledispatch.utils.groupby(*func*, *seq*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/unification/multipledispatch/utils.py#L103)

Group a collection by a key function
>>> names = ["Alice", "Bob", "Charlie", "Dan", "Edith", "Frank"]
>>> groupby(len, names) # doctest: +SKIP
{3: ['Bob', 'Dan'], 5: ['Alice', 'Edith', 'Frank'], 7: ['Charlie']}
>>> iseven = lambda x: x % 2 == 0
>>> groupby(iseven, [1, 2, 3, 4, 5, 6, 7, 8]) # doctest: +SKIP
{False: [1, 3, 5, 7], True: [2, 4, 6, 8]}
.. seealso:: `countby`

Return type:

OrderedDict[[object](https://docs.python.org/3/builtins/functions.html#object), [list](https://docs.python.org/3/builtins/stdtypes.html#list)[_T]]