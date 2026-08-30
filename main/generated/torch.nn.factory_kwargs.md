# torch.nn.factory_kwargs

torch.nn.factory_kwargs(*kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/nn/__init__.py#L21)

Return a canonicalized dict of factory kwargs.

Given kwargs, returns a canonicalized dict of factory kwargs that can be directly passed
to factory functions like torch.empty, or errors if unrecognized kwargs are present.

This function makes it simple to write code like this:

```
class MyModule(nn.Module):
 def __init__(self, **kwargs):
 factory_kwargs = torch.nn.factory_kwargs(kwargs)
 self.weight = Parameter(torch.empty(10, **factory_kwargs))
```

Why should you use this function instead of just passing kwargs along directly?

1. This function does error validation, so if there are unexpected kwargs we will
immediately report an error, instead of deferring it to the factory call
2. This function supports a special factory_kwargs argument, which can be used to
explicitly specify a kwarg to be used for factory functions, in the event one of the
factory kwargs conflicts with an already existing argument in the signature (e.g.
in the signature `def f(dtype, **kwargs)`, you can specify `dtype` for factory
functions, as distinct from the dtype argument, by saying
`f(dtype1, factory_kwargs={"dtype": dtype2})`)