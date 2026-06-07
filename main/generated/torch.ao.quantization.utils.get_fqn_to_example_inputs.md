# get_fqn_to_example_inputs

*class*torch.ao.quantization.utils.get_fqn_to_example_inputs(*model*, *example_inputs*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/ao/quantization/utils.py#L734)

Given a model and its example inputs, return a dictionary from
fully qualified name of submodules to example_inputs for that submodule,
e.g. `{"linear1": (tensor1,), "linear2": (tensor2,), "sub": (tensor3,),
"sub.linear1": (tensor4,), ...}`

Used to make quantizing submodules easier now that FX Graph Mode Quantization requires
example inputs.

Also works for keyword arguments with default values, we would flatten keyword
arguments as positional arguments and fill in the missing keyword args with default
values, e.g. if we have a forward function:

```
def forward(self, x, key1=3, key2=3): ...
```

and we call it with `self.submodule(x, key2=6)`
we'll get `example_inputs: (x, 3, 6)`

user can also override `key1` with positional arguments as well:
for `self.submodule(x, 5, key2=6)`
we'll get: `(x, 5, 6)`

variable positional arguments and variable positional keyword arguments in forward
function are not supported currently, so please make sure no submodules is using
them.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), ...]]