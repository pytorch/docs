# torch.nn.utils.parametrize.cached

torch.nn.utils.parametrize.cached()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/utils/parametrize.py#L33)

Context manager that enables the caching system within parametrizations registered with [`register_parametrization()`](torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization).

The value of the parametrized objects is computed and cached the first time
they are required when this context manager is active. The cached values are
discarded when leaving the context manager.

This is useful when using a parametrized parameter more than once in the forward pass.
An example of this is when parametrizing the recurrent kernel of an RNN or when
sharing weights.

The simplest way to activate the cache is by wrapping the forward pass of the neural network

```
import torch.nn.utils.parametrize as P

...
with P.cached():
 output = model(inputs)
```

in training and evaluation. One may also wrap the parts of the modules that use
several times the parametrized tensors. For example, the loop of an RNN with a
parametrized recurrent kernel:

```
with P.cached():
 for x in xs:
 out_rnn = self.rnn_cell(x, out_rnn)
```