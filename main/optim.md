# torch.optim

`torch.optim` is a package implementing various optimization algorithms.

Most commonly used methods are already supported, and the interface is general
enough, so that more sophisticated ones can also be easily integrated in the
future.

## How to use an optimizer

To use `torch.optim` you have to construct an optimizer object that will hold
the current state and will update the parameters based on the computed gradients.

### Constructing it

To construct an `Optimizer` you have to give it an iterable containing the
parameters (all should be `Parameter` s) or named parameters
(tuples of (str, `Parameter`)) to optimize. Then,
you can specify optimizer-specific options such as the learning rate, weight decay, etc.

Example:

```
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
optimizer = optim.Adam([var1, var2], lr=0.0001)
```

Named parameters example:

```
optimizer = optim.SGD(model.named_parameters(), lr=0.01, momentum=0.9)
optimizer = optim.Adam([('layer0', var1), ('layer1', var2)], lr=0.0001)
```

### Per-parameter options

`Optimizer` s also support specifying per-parameter options. To do this, instead
of passing an iterable of `Variable` s, pass in an iterable of
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict) s. Each of them will define a separate parameter group, and should contain
a `params` key, containing a list of parameters belonging to it. Other keys
should match the keyword arguments accepted by the optimizers, and will be used
as optimization options for this group.

For example, this is very useful when one wants to specify per-layer learning rates:

```
optim.SGD([
 {'params': model.base.parameters(), 'lr': 1e-2},
 {'params': model.classifier.parameters()}
], lr=1e-3, momentum=0.9)

optim.SGD([
 {'params': model.base.named_parameters(), 'lr': 1e-2},
 {'params': model.classifier.named_parameters()}
], lr=1e-3, momentum=0.9)
```

This means that `model.base`'s parameters will use a learning rate of `1e-2`, whereas
`model.classifier`'s parameters will stick to the default learning rate of `1e-3`.
Finally a momentum of `0.9` will be used for all parameters.

Note

You can still pass options as keyword arguments. They will be used as
defaults, in the groups that didn't override them. This is useful when you
only want to vary a single option, while keeping all others consistent
between parameter groups.

Also consider the following example related to the distinct penalization of parameters.
Remember that [`parameters()`](generated/torch.nn.Module.html#torch.nn.Module.parameters) returns an iterable that
contains all learnable parameters, including biases and other
parameters that may prefer distinct penalization. To address this, one can specify
individual penalization weights for each parameter group:

```
bias_params = [p for name, p in self.named_parameters() if 'bias' in name]
others = [p for name, p in self.named_parameters() if 'bias' not in name]

optim.SGD([
 {'params': others},
 {'params': bias_params, 'weight_decay': 0}
], weight_decay=1e-2, lr=1e-2)
```

In this manner, bias terms are isolated from non-bias terms, and a `weight_decay`
of `0` is set specifically for the bias terms, as to avoid any penalization for
this group.

### Taking an optimization step

All optimizers implement a [`step()`](generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step) method, that updates the
parameters. It can be used in two ways:

#### `optimizer.step()`

This is a simplified version supported by most optimizers. The function can be
called once the gradients are computed using e.g.
`backward()`.

Example:

```
for input, target in dataset:
 optimizer.zero_grad()
 output = model(input)
 loss = loss_fn(output, target)
 loss.backward()
 optimizer.step()
```

#### `optimizer.step(closure)`

Some optimization algorithms such as Conjugate Gradient and LBFGS need to
reevaluate the function multiple times, so you have to pass in a closure that
allows them to recompute your model. The closure should clear the gradients,
compute the loss, and return it.

Example:

```
for input, target in dataset:
 def closure():
 optimizer.zero_grad()
 output = model(input)
 loss = loss_fn(output, target)
 loss.backward()
 return loss
 optimizer.step(closure)
```

## Base class

*class*torch.optim.Optimizer(*params*, *defaults*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/optimizer.py#L339)

Base class for all optimizers.

Warning

Parameters need to be specified as collections that have a deterministic
ordering that is consistent between runs. Examples of objects that don't
satisfy those properties are sets and iterators over values of dictionaries.

Parameters:

- **params** (*iterable*) - an iterable of [`torch.Tensor`](tensors.html#torch.Tensor) s or
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict) s. Specifies what Tensors should be optimized.
- **defaults** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) - (dict): a dict containing default values of optimization
options (used when a parameter group doesn't specify them).

| [`Optimizer.add_param_group`](generated/torch.optim.Optimizer.add_param_group.html#torch.optim.Optimizer.add_param_group) | Add a param group to the `Optimizer` s param_groups. |
| --- | --- |
| [`Optimizer.load_state_dict`](generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) | Load the optimizer state. |
| [`Optimizer.register_load_state_dict_pre_hook`](generated/torch.optim.Optimizer.register_load_state_dict_pre_hook.html#torch.optim.Optimizer.register_load_state_dict_pre_hook) | Register a load_state_dict pre-hook which will be called before [`load_state_dict()`](generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) is called. It should have the following signature::. |
| [`Optimizer.register_load_state_dict_post_hook`](generated/torch.optim.Optimizer.register_load_state_dict_post_hook.html#torch.optim.Optimizer.register_load_state_dict_post_hook) | Register a load_state_dict post-hook which will be called after [`load_state_dict()`](generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) is called. It should have the following signature::. |
| [`Optimizer.state_dict`](generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict) | Return the state of the optimizer as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict). |
| [`Optimizer.register_state_dict_pre_hook`](generated/torch.optim.Optimizer.register_state_dict_pre_hook.html#torch.optim.Optimizer.register_state_dict_pre_hook) | Register a state dict pre-hook which will be called before [`state_dict()`](generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict) is called. |
| [`Optimizer.register_state_dict_post_hook`](generated/torch.optim.Optimizer.register_state_dict_post_hook.html#torch.optim.Optimizer.register_state_dict_post_hook) | Register a state dict post-hook which will be called after [`state_dict()`](generated/torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict) is called. |
| [`Optimizer.step`](generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step) | Perform a single optimization step to update parameter. |
| [`Optimizer.register_step_pre_hook`](generated/torch.optim.Optimizer.register_step_pre_hook.html#torch.optim.Optimizer.register_step_pre_hook) | Register an optimizer step pre hook which will be called before optimizer step. |
| [`Optimizer.register_step_post_hook`](generated/torch.optim.Optimizer.register_step_post_hook.html#torch.optim.Optimizer.register_step_post_hook) | Register an optimizer step post hook which will be called after optimizer step. |
| [`Optimizer.zero_grad`](generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad) | Reset the gradients of all optimized [`torch.Tensor`](tensors.html#torch.Tensor) s. |

## Module-level hooks

torch.optim.optimizer.register_optimizer_step_post_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/optimizer.py#L309)

Register a post hook common to all optimizers.

The hook should have the following signature:

```
hook(optimizer, args, kwargs) -> None
```

Parameters:

**hook** (*Callable*) - A user defined hook which is registered on all optimizers.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

torch.optim.optimizer.register_optimizer_step_pre_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/optimizer.py#L289)

Register a pre hook common to all optimizers.

The hook should have the following signature:

```
hook(optimizer, args, kwargs) -> None or modified args and kwargs
```

Parameters:

**hook** (*Callable*) - A user defined hook which is registered on all optimizers.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

## Utilities

torch.optim.swap_in_optimizer_params_and_state(*optimizer*, *swapin_parameters*, *swapin_optim_state*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/_stateless.py#L192)

Temporarily replace an optimizer's parameters and state with the
supplied params and optim states, then restore them on exit.

For the duration of the context, all optimizer APIs (including
user hooks) see the swap-in values; the live optimizer is restored on
exit.

The difference between this API and `optimizer.load_state_dict` is
that `optimizer.load_state_dict` only updates the optimizer's state
and leaves the parameters in `param_groups` untouched. This API also
swaps in the parameters, so that `optimizer.step()` acts on the
swap-in parameter tensors you supply.

Parameters:

- **optimizer** (*Optimizer*) - the live optimizer; its state must already be
initialized.
- **swapin_parameters** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Tensor*](tensors.html#torch.Tensor)*]*) - tensors to use as parameters during the context,
provided in the same order as the existing input parameters to
the optimizer (most commonly in `model.named_parameters()`
order).
- **swapin_optim_state** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) - an `optimizer.state_dict()`-shaped dict
(`{"state": ..., "param_groups": ...}`) holding the state to
install. `"state"` is keyed by packed integer parameter ids
and `"param_groups"` mirrors `optimizer.param_groups`,
with each `"params"` entry as a list of those packed ids
and the remaining keys carrying per-group hyperparameters
(`lr`, `betas`, `foreach`, `capturable`, ...).
Only in-place tensor edits propagate back to the user supplied
`swapin_optim_state`; all other side-effects (e.g.,
assigning a new tensor to the optim state)
are ignored.

Example

One use of this API is to run `optimizer.step()` against
`FakeTensor` versions of the parameters and state for nonstrict
tracing -- capturing an FX graph of the step without touching the
live optimizer:

```
from torch.fx.experimental.proxy_tensor import make_fx
from torch._subclasses import FakeTensorMode
from torch.utils import _pytree as pytree

fake_mode = FakeTensorMode(allow_non_fake_inputs=True)
with fake_mode:
 fake_params = {
 n: fake_mode.from_tensor(p) for n, p in model.named_parameters()
 }
 fake_osd = pytree.tree_map_only(
 torch.Tensor, fake_mode.from_tensor, optimizer.state_dict()
 )

def step_fn(params, osd):
 with swap_in_optimizer_params_and_state(optimizer, params, osd):
 optimizer.step()
 return params, osd

gm = make_fx(step_fn)(fake_params, fake_osd)
```

## Algorithms

| [`Adadelta`](generated/torch.optim.Adadelta.html#torch.optim.Adadelta) | Implements Adadelta algorithm. |
| --- | --- |
| [`Adafactor`](generated/torch.optim.Adafactor.html#torch.optim.Adafactor) | Implements Adafactor algorithm. |
| [`Adagrad`](generated/torch.optim.Adagrad.html#torch.optim.Adagrad) | Implements Adagrad algorithm. |
| [`Adam`](generated/torch.optim.Adam.html#torch.optim.Adam) | Implements Adam algorithm. |
| [`AdamW`](generated/torch.optim.AdamW.html#torch.optim.AdamW) | Implements AdamW algorithm, where weight decay does not accumulate in the momentum nor variance. |
| [`SparseAdam`](generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam) | SparseAdam implements a masked version of the Adam algorithm suitable for sparse gradients. |
| [`Adamax`](generated/torch.optim.Adamax.html#torch.optim.Adamax) | Implements Adamax algorithm (a variant of Adam based on infinity norm). |
| [`ASGD`](generated/torch.optim.ASGD.html#torch.optim.ASGD) | Implements Averaged Stochastic Gradient Descent. |
| [`LBFGS`](generated/torch.optim.LBFGS.html#torch.optim.LBFGS) | Implements L-BFGS algorithm. |
| [`Muon`](generated/torch.optim.Muon.html#torch.optim.Muon) | Implements Muon algorithm. |
| [`NAdam`](generated/torch.optim.NAdam.html#torch.optim.NAdam) | Implements NAdam algorithm. |
| [`RAdam`](generated/torch.optim.RAdam.html#torch.optim.RAdam) | Implements RAdam algorithm. |
| [`RMSprop`](generated/torch.optim.RMSprop.html#torch.optim.RMSprop) | Implements RMSprop algorithm. |
| [`Rprop`](generated/torch.optim.Rprop.html#torch.optim.Rprop) | Implements the resilient backpropagation algorithm. |
| [`SGD`](generated/torch.optim.SGD.html#torch.optim.SGD) | Implements stochastic gradient descent (optionally with momentum). |

Many of our algorithms have various implementations optimized for performance,
readability and/or generality, so we attempt to default to the generally fastest
implementation for the current device if no particular implementation has been
specified by the user.

We have 3 major categories of implementations: for-loop, foreach (multi-tensor), and
fused. The most straightforward implementations are for-loops over the parameters with
big chunks of computation. For-looping is usually slower than our foreach
implementations, which combine parameters into a multi-tensor and run the big chunks
of computation all at once, thereby saving many sequential kernel calls. A few of our
optimizers have even faster fused implementations, which fuse the big chunks of
computation into one kernel. We can think of foreach implementations as fusing
horizontally and fused implementations as fusing vertically on top of that.

In general, the performance ordering of the 3 implementations is fused > foreach > for-loop.
So when applicable, we default to foreach over for-loop. Applicable means the foreach
implementation is available, the user has not specified any implementation-specific kwargs
(e.g., fused, foreach, differentiable), and all tensors are native. Note that while fused
should be even faster than foreach, the implementations are newer and we would like to give
them more bake-in time before flipping the switch everywhere. We summarize the stability status
for each implementation on the second table below, you are welcome to try them out though!

Below is a table showing the available and default implementations of each algorithm:

| Algorithm | Default | Has foreach? | Has fused? |
| --- | --- | --- | --- |
| [`Adadelta`](generated/torch.optim.Adadelta.html#torch.optim.Adadelta) | foreach | yes | no |
| [`Adafactor`](generated/torch.optim.Adafactor.html#torch.optim.Adafactor) | for-loop | no | no |
| [`Adagrad`](generated/torch.optim.Adagrad.html#torch.optim.Adagrad) | foreach | yes | yes (cpu only) |
| [`Adam`](generated/torch.optim.Adam.html#torch.optim.Adam) | foreach | yes | yes |
| [`AdamW`](generated/torch.optim.AdamW.html#torch.optim.AdamW) | foreach | yes | yes |
| [`SparseAdam`](generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam) | for-loop | no | no |
| [`Adamax`](generated/torch.optim.Adamax.html#torch.optim.Adamax) | foreach | yes | no |
| [`ASGD`](generated/torch.optim.ASGD.html#torch.optim.ASGD) | foreach | yes | no |
| [`LBFGS`](generated/torch.optim.LBFGS.html#torch.optim.LBFGS) | for-loop | no | no |
| [`Muon`](generated/torch.optim.Muon.html#torch.optim.Muon) | for-loop | no | no |
| [`NAdam`](generated/torch.optim.NAdam.html#torch.optim.NAdam) | foreach | yes | no |
| [`RAdam`](generated/torch.optim.RAdam.html#torch.optim.RAdam) | foreach | yes | no |
| [`RMSprop`](generated/torch.optim.RMSprop.html#torch.optim.RMSprop) | foreach | yes | no |
| [`Rprop`](generated/torch.optim.Rprop.html#torch.optim.Rprop) | foreach | yes | no |
| [`SGD`](generated/torch.optim.SGD.html#torch.optim.SGD) | foreach | yes | yes |

Below table is showing the stability status for fused implementations:

| Algorithm | CPU | CUDA | MPS |
| --- | --- | --- | --- |
| [`Adadelta`](generated/torch.optim.Adadelta.html#torch.optim.Adadelta) | unsupported | unsupported | unsupported |
| [`Adafactor`](generated/torch.optim.Adafactor.html#torch.optim.Adafactor) | unsupported | unsupported | unsupported |
| [`Adagrad`](generated/torch.optim.Adagrad.html#torch.optim.Adagrad) | beta | unsupported | unsupported |
| [`Adam`](generated/torch.optim.Adam.html#torch.optim.Adam) | beta | stable | beta |
| [`AdamW`](generated/torch.optim.AdamW.html#torch.optim.AdamW) | beta | stable | beta |
| [`SparseAdam`](generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam) | unsupported | unsupported | unsupported |
| [`Adamax`](generated/torch.optim.Adamax.html#torch.optim.Adamax) | unsupported | unsupported | unsupported |
| [`ASGD`](generated/torch.optim.ASGD.html#torch.optim.ASGD) | unsupported | unsupported | unsupported |
| [`LBFGS`](generated/torch.optim.LBFGS.html#torch.optim.LBFGS) | unsupported | unsupported | unsupported |
| [`Muon`](generated/torch.optim.Muon.html#torch.optim.Muon) | unsupported | unsupported | unsupported |
| [`NAdam`](generated/torch.optim.NAdam.html#torch.optim.NAdam) | unsupported | unsupported | unsupported |
| [`RAdam`](generated/torch.optim.RAdam.html#torch.optim.RAdam) | unsupported | unsupported | unsupported |
| [`RMSprop`](generated/torch.optim.RMSprop.html#torch.optim.RMSprop) | unsupported | unsupported | unsupported |
| [`Rprop`](generated/torch.optim.Rprop.html#torch.optim.Rprop) | unsupported | unsupported | unsupported |
| [`SGD`](generated/torch.optim.SGD.html#torch.optim.SGD) | beta | beta | beta |

## How to adjust learning rate

[`torch.optim.lr_scheduler.LRScheduler`](generated/torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler) provides several methods to adjust the learning
rate based on the number of epochs. [`torch.optim.lr_scheduler.ReduceLROnPlateau`](generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html#torch.optim.lr_scheduler.ReduceLROnPlateau)
allows dynamic learning rate reducing based on some validation measurements.

Learning rate scheduling should be applied after optimizer's update; e.g., you
should write your code this way:

Example:

```
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
scheduler = ExponentialLR(optimizer, gamma=0.9)

for epoch in range(20):
 for input, target in dataset:
 optimizer.zero_grad()
 output = model(input)
 loss = loss_fn(output, target)
 loss.backward()
 optimizer.step()
 scheduler.step()
```

Most learning rate schedulers can be called back-to-back (also referred to as
chaining schedulers). The result is that each scheduler is applied one after the
other on the learning rate obtained by the one preceding it.

Example:

```
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
scheduler1 = ExponentialLR(optimizer, gamma=0.9)
scheduler2 = MultiStepLR(optimizer, milestones=[30,80], gamma=0.1)

for epoch in range(20):
 for input, target in dataset:
 optimizer.zero_grad()
 output = model(input)
 loss = loss_fn(output, target)
 loss.backward()
 optimizer.step()
 scheduler1.step()
 scheduler2.step()
```

In many places in the documentation, we will use the following template to refer to schedulers
algorithms.

```
>>> scheduler = ...
>>> for epoch in range(100):
>>> train(...)
>>> validate(...)
>>> scheduler.step()
```

Warning

Prior to PyTorch 1.1.0, the learning rate scheduler was expected to be called before
the optimizer's update; 1.1.0 changed this behavior in a BC-breaking way. If you use
the learning rate scheduler (calling `scheduler.step()`) before the optimizer's update
(calling `optimizer.step()`), this will skip the first value of the learning rate schedule.
If you are unable to reproduce results after upgrading to PyTorch 1.1.0, please check
if you are calling `scheduler.step()` at the wrong time.

| [`lr_scheduler.LRScheduler`](generated/torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler) | Base class for all learning rate schedulers. |
| --- | --- |
| [`lr_scheduler.LambdaLR`](generated/torch.optim.lr_scheduler.LambdaLR.html#torch.optim.lr_scheduler.LambdaLR) | Sets the initial learning rate. |
| [`lr_scheduler.MultiplicativeLR`](generated/torch.optim.lr_scheduler.MultiplicativeLR.html#torch.optim.lr_scheduler.MultiplicativeLR) | Multiply the learning rate of each parameter group by the factor given in the specified function. |
| [`lr_scheduler.StepLR`](generated/torch.optim.lr_scheduler.StepLR.html#torch.optim.lr_scheduler.StepLR) | Decays the learning rate of each parameter group by gamma every step_size epochs. |
| [`lr_scheduler.MultiStepLR`](generated/torch.optim.lr_scheduler.MultiStepLR.html#torch.optim.lr_scheduler.MultiStepLR) | Decays the learning rate of each parameter group by gamma once the number of epoch reaches one of the milestones. |
| [`lr_scheduler.ConstantLR`](generated/torch.optim.lr_scheduler.ConstantLR.html#torch.optim.lr_scheduler.ConstantLR) | Multiply the learning rate of each parameter group by a small constant factor. |
| [`lr_scheduler.LinearLR`](generated/torch.optim.lr_scheduler.LinearLR.html#torch.optim.lr_scheduler.LinearLR) | Decays the learning rate of each parameter group by linearly changing small multiplicative factor. |
| [`lr_scheduler.ExponentialLR`](generated/torch.optim.lr_scheduler.ExponentialLR.html#torch.optim.lr_scheduler.ExponentialLR) | Decays the learning rate of each parameter group by gamma every epoch. |
| [`lr_scheduler.PolynomialLR`](generated/torch.optim.lr_scheduler.PolynomialLR.html#torch.optim.lr_scheduler.PolynomialLR) | Decays the learning rate of each parameter group using a polynomial function in the given total_iters. |
| [`lr_scheduler.CosineAnnealingLR`](generated/torch.optim.lr_scheduler.CosineAnnealingLR.html#torch.optim.lr_scheduler.CosineAnnealingLR) | Set the learning rate of each parameter group using a cosine annealing schedule. |
| [`lr_scheduler.ChainedScheduler`](generated/torch.optim.lr_scheduler.ChainedScheduler.html#torch.optim.lr_scheduler.ChainedScheduler) | Chains a list of learning rate schedulers. |
| [`lr_scheduler.SequentialLR`](generated/torch.optim.lr_scheduler.SequentialLR.html#torch.optim.lr_scheduler.SequentialLR) | Contains a list of schedulers expected to be called sequentially during the optimization process. |
| [`lr_scheduler.ReduceLROnPlateau`](generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html#torch.optim.lr_scheduler.ReduceLROnPlateau) | Reduce learning rate when a metric has stopped improving. |
| [`lr_scheduler.CyclicLR`](generated/torch.optim.lr_scheduler.CyclicLR.html#torch.optim.lr_scheduler.CyclicLR) | Sets the learning rate of each parameter group according to cyclical learning rate policy (CLR). |
| [`lr_scheduler.OneCycleLR`](generated/torch.optim.lr_scheduler.OneCycleLR.html#torch.optim.lr_scheduler.OneCycleLR) | Sets the learning rate of each parameter group according to the 1cycle learning rate policy. |
| [`lr_scheduler.CosineAnnealingWarmRestarts`](generated/torch.optim.lr_scheduler.CosineAnnealingWarmRestarts.html#torch.optim.lr_scheduler.CosineAnnealingWarmRestarts) | Set the learning rate of each parameter group using a cosine annealing schedule. |

## How to utilize named parameters to load optimizer state dict

The function [`load_state_dict()`](generated/torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) stores the optional `param_names` content from the
loaded state dict if present. However, the process of loading the optimizer state is not affected,
as the order of the parameters matters to maintain compatibility (in case of different ordering).
To utilize the loaded parameters names from the loaded state dict, a custom `register_load_state_dict_pre_hook`
needs to be implemented according to the desired behavior.

This can be useful, for instance, when the model architecture changes, but the weights and optimizer states need to
remain unchanged. The following example demonstrates how to implement this customization.

Example:

```
class OneLayerModel(nn.Module):
 def __init__(self):
 super().__init__()
 self.fc = nn.Linear(3, 4)

 def forward(self, x):
 return self.fc(x)

model = OneLayerModel()
optimizer = optim.SGD(model.named_parameters(), lr=0.01, momentum=0.9)
# training..
torch.save(optimizer.state_dict(), PATH)
```

Let's say that `model` implements an expert (MoE), and we want to duplicate it and resume training
for two experts, both initialized the same way as the `fc` layer. For the following `model2` we create two layers identical to `fc` and resume training by loading the model weights and optimizer states from `model` into both `fc1` and `fc2` of `model2` (and adjust them accordingly):

```
class TwoLayerModel(nn.Module):
 def __init__(self):
 super().__init__()
 self.fc1 = nn.Linear(3, 4)
 self.fc2 = nn.Linear(3, 4)

 def forward(self, x):
 return (self.fc1(x) + self.fc2(x)) / 2

model2 = TwoLayerModel()
# adapt and load model weights..
optimizer2 = optim.SGD(model2.named_parameters(), lr=0.01, momentum=0.9)
```

To load the state dict for `optimizer2` with the state dict of the previous optimizer such that both
`fc1` and `fc2` will be initialized with a copy of `fc` optimizer states
(to resume training for each layer from `fc`), we can use the following hook:

```
def adapt_state_dict_ids(optimizer, state_dict):
 adapted_state_dict = deepcopy(optimizer.state_dict())
 # Copy setup parameters (lr, weight_decay, etc.), in case they differ in the loaded state dict.
 for k, v in state_dict['param_groups'][0].items():
 if k not in ['params', 'param_names']:
 adapted_state_dict['param_groups'][0][k] = v

 lookup_dict = {
 'fc1.weight': 'fc.weight',
 'fc1.bias': 'fc.bias',
 'fc2.weight': 'fc.weight',
 'fc2.bias': 'fc.bias'
 }
 clone_deepcopy = lambda d: {k: (v.clone() if isinstance(v, torch.Tensor) else deepcopy(v)) for k, v in d.items()}
 for param_id, param_name in zip(
 optimizer.state_dict()['param_groups'][0]['params'],
 optimizer.state_dict()['param_groups'][0]['param_names']):
 name_in_loaded = lookup_dict[param_name]
 index_in_loaded_list = state_dict['param_groups'][0]['param_names'].index(name_in_loaded)
 id_in_loaded = state_dict['param_groups'][0]['params'][index_in_loaded_list]
 # Copy the state of the corresponding parameter
 if id_in_loaded in state_dict['state']:
 adapted_state_dict['state'][param_id] = clone_deepcopy(state_dict['state'][id_in_loaded])

 return adapted_state_dict

optimizer2.register_load_state_dict_pre_hook(adapt_state_dict_ids)
optimizer2.load_state_dict(torch.load(PATH)) # The previous optimizer saved state_dict
```

This ensures that the adapted state_dict with the correct states for the layers of `model2` will be used
during model loading.
Note that this code is designed specifically for this example (e.g., assuming a single parameter group),
and other cases might require different adaptations.

The following example shows how to handle missing parameters in a loaded
`state dict` when the model structure changes.
The `Model_bypass` adds a new `bypass` layer, which is not present in the original `Model1`.
To resume training, a custom `adapt_state_dict_missing_param` hook is used to adapt the optimizer's `state_dict`,
ensuring existing parameters are mapped correctly, while missing ones (like the bypass layer) remain unchanged
(as initialized in this example).
This approach enables smooth loading and resuming of the optimizer state despite model changes.
The new bypass layer will be trained from scratch:

```
class Model1(nn.Module):
 def __init__(self):
 super().__init__()
 self.fc = nn.Linear(5, 5)

 def forward(self, x):
 return self.fc(x) + x

model = Model1()
optimizer = optim.SGD(model.named_parameters(), lr=0.01, momentum=0.9)
# training..
torch.save(optimizer.state_dict(), PATH)

class Model_bypass(nn.Module):
 def __init__(self):
 super().__init__()
 self.fc = nn.Linear(5, 5)
 self.bypass = nn.Linear(5, 5, bias=False)
 torch.nn.init.eye_(self.bypass.weight)

 def forward(self, x):
 return self.fc(x) + self.bypass(x)

model2 = Model_bypass()
optimizer2 = optim.SGD(model2.named_parameters(), lr=0.01, momentum=0.9)

def adapt_state_dict_missing_param(optimizer, state_dict):
 adapted_state_dict = deepcopy(optimizer.state_dict())
 # Copy setup parameters (lr, weight_decay, etc.), in case they differ in the loaded state dict.
 for k, v in state_dict['param_groups'][0].items():
 if k not in ['params', 'param_names']:
 adapted_state_dict['param_groups'][0][k] = v

 lookup_dict = {
 'fc.weight': 'fc.weight',
 'fc.bias': 'fc.bias',
 'bypass.weight': None,
 }

 clone_deepcopy = lambda d: {k: (v.clone() if isinstance(v, torch.Tensor) else deepcopy(v)) for k, v in d.items()}
 for param_id, param_name in zip(
 optimizer.state_dict()['param_groups'][0]['params'],
 optimizer.state_dict()['param_groups'][0]['param_names']):
 name_in_loaded = lookup_dict[param_name]
 if name_in_loaded in state_dict['param_groups'][0]['param_names']:
 index_in_loaded_list = state_dict['param_groups'][0]['param_names'].index(name_in_loaded)
 id_in_loaded = state_dict['param_groups'][0]['params'][index_in_loaded_list]
 # Copy the state of the corresponding parameter
 if id_in_loaded in state_dict['state']:
 adapted_state_dict['state'][param_id] = clone_deepcopy(state_dict['state'][id_in_loaded])

 return adapted_state_dict

optimizer2.register_load_state_dict_pre_hook(adapt_state_dict_ids)
optimizer2.load_state_dict(torch.load(PATH)) # The previous optimizer saved state_dict
```

As a third example, instead of loading a state according to the order of parameters (the default approach),
this hook can be used to load according to the parameters' names:

```
def names_matching(optimizer, state_dict):
 assert len(state_dict['param_groups']) == len(optimizer.state_dict()['param_groups'])
 adapted_state_dict = deepcopy(optimizer.state_dict())
 for g_ind in range(len(state_dict['param_groups'])):
 assert len(state_dict['param_groups'][g_ind]['params']) == len(
 optimizer.state_dict()['param_groups'][g_ind]['params'])

 for k, v in state_dict['param_groups'][g_ind].items():
 if k not in ['params', 'param_names']:
 adapted_state_dict['param_groups'][g_ind][k] = v

 for param_id, param_name in zip(
 optimizer.state_dict()['param_groups'][g_ind]['params'],
 optimizer.state_dict()['param_groups'][g_ind]['param_names']):
 index_in_loaded_list = state_dict['param_groups'][g_ind]['param_names'].index(param_name)
 id_in_loaded = state_dict['param_groups'][g_ind]['params'][index_in_loaded_list]
 # Copy the state of the corresponding parameter
 if id_in_loaded in state_dict['state']:
 adapted_state_dict['state'][param_id] = deepcopy(state_dict['state'][id_in_loaded])

 return adapted_state_dict
```

## Weight Averaging (SWA and EMA)

[`torch.optim.swa_utils.AveragedModel`](generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel) implements Stochastic Weight Averaging (SWA) and Exponential Moving Average (EMA),
[`torch.optim.swa_utils.SWALR`](generated/torch.optim.swa_utils.SWALR.html#torch.optim.swa_utils.SWALR) implements the SWA learning rate scheduler and
`torch.optim.swa_utils.update_bn()` is a utility function used to update SWA/EMA batch
normalization statistics at the end of training.

SWA has been proposed in [Averaging Weights Leads to Wider Optima and Better Generalization](https://arxiv.org/abs/1803.05407).

EMA is a widely known technique to reduce the training time by reducing the number of weight updates needed.
It is a variation of [Polyak averaging](https://paperswithcode.com/method/polyak-averaging), but using exponential weights instead of equal weights across iterations.

### Constructing averaged models

The `AveragedModel` class serves to compute the weights of the SWA or EMA model.

You can create an SWA averaged model by running:

```
>>> averaged_model = AveragedModel(model)
```

EMA models are constructed by specifying the `multi_avg_fn` argument as follows:

```
>>> decay = 0.999
>>> averaged_model = AveragedModel(model, multi_avg_fn=get_ema_multi_avg_fn(decay))
```

Decay is a parameter between 0 and 1 that controls how fast the averaged parameters are decayed. If not provided to `torch.optim.swa_utils.get_ema_multi_avg_fn()`, the default is 0.999. Decay value should be close to 1.0, as smaller values can cause optimization convergence issues.

`torch.optim.swa_utils.get_ema_multi_avg_fn()` returns a function that applies the following EMA equation to the weights:

W0EMA=W0modelW_0^{\text{EMA}} = W_0^{\text{model}}W0EMA​=W0model​
Wt+1EMA=decay×WtEMA+(1−decay)×Wt+1modelW_{t+1}^{\text{EMA}} = \text{decay} \times W_t^{\text{EMA}} + (1 - \text{decay}) \times W_{t+1}^{\text{model}}Wt+1EMA​=decay×WtEMA​+(1−decay)×Wt+1model​

where `W_t^{\text{EMA}}` is the EMA parameter at step `t`, `W_t^{\text{model}}` is the model parameter at step `t`, and decay is the EMA decay rate (default: 0.999).

Here the model `model` can be an arbitrary [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module) object. `averaged_model`
will keep track of the running averages of the parameters of the `model`. To update these
averages, you should use the `update_parameters()` function after the `optimizer.step()`:

```
>>> averaged_model.update_parameters(model)
```

For SWA and EMA, this call is usually done right after the optimizer `step()`. In the case of SWA, this is usually skipped for some numbers of steps at the beginning of the training.

### Custom averaging strategies

By default, [`torch.optim.swa_utils.AveragedModel`](generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel) computes a running equal average of
the parameters that you provide, but you can also use custom averaging functions with the
`avg_fn` or `multi_avg_fn` parameters:

- `avg_fn` allows defining a function operating on each parameter tuple (averaged parameter, model parameter) and should return the new averaged parameter.
- `multi_avg_fn` allows defining more efficient operations acting on a tuple of parameter lists, (averaged parameter list, model parameter list), at the same time, for example using the `torch._foreach*` functions. This function must update the averaged parameters in-place.

In the following example `ema_model` computes an exponential moving average using the `avg_fn` parameter:

```
>>> ema_avg = lambda averaged_model_parameter, model_parameter, num_averaged:\
>>> 0.9 * averaged_model_parameter + 0.1 * model_parameter
>>> ema_model = torch.optim.swa_utils.AveragedModel(model, avg_fn=ema_avg)
```

In the following example `ema_model` computes an exponential moving average using the more efficient `multi_avg_fn` parameter:

```
>>> ema_model = AveragedModel(model, multi_avg_fn=get_ema_multi_avg_fn(0.9))
```

### SWA learning rate schedules

Typically, in SWA the learning rate is set to a high constant value. `SWALR` is a
learning rate scheduler that anneals the learning rate to a fixed value, and then keeps it
constant. For example, the following code creates a scheduler that linearly anneals the
learning rate from its initial value to 0.05 in 5 epochs within each parameter group:

```
>>> swa_scheduler = torch.optim.swa_utils.SWALR(optimizer, \
>>> anneal_strategy="linear", anneal_epochs=5, swa_lr=0.05)
```

You can also use cosine annealing to a fixed value instead of linear annealing by setting
`anneal_strategy="cos"`.

### Taking care of batch normalization

`update_bn()` is a utility function that allows to compute the batchnorm statistics for the SWA model
on a given dataloader `loader` at the end of training:

```
>>> torch.optim.swa_utils.update_bn(loader, swa_model)
```

`update_bn()` applies the `swa_model` to every element in the dataloader and computes the activation
statistics for each batch normalization layer in the model.

Warning

`update_bn()` assumes that each batch in the dataloader `loader` is either a tensors or a list of
tensors where the first element is the tensor that the network `swa_model` should be applied to.
If your dataloader has a different structure, you can update the batch normalization statistics of the
`swa_model` by doing a forward pass with the `swa_model` on each element of the dataset.

### Putting it all together: SWA

In the example below, `swa_model` is the SWA model that accumulates the averages of the weights.
We train the model for a total of 300 epochs and we switch to the SWA learning rate schedule
and start to collect SWA averages of the parameters at epoch 160:

```
>>> loader, optimizer, model, loss_fn = ...
>>> swa_model = torch.optim.swa_utils.AveragedModel(model)
>>> scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=300)
>>> swa_start = 160
>>> swa_scheduler = SWALR(optimizer, swa_lr=0.05)
>>>
>>> for epoch in range(300):
>>> for input, target in loader:
>>> optimizer.zero_grad()
>>> loss_fn(model(input), target).backward()
>>> optimizer.step()
>>> if epoch > swa_start:
>>> swa_model.update_parameters(model)
>>> swa_scheduler.step()
>>> else:
>>> scheduler.step()
>>>
>>> # Update bn statistics for the swa_model at the end
>>> torch.optim.swa_utils.update_bn(loader, swa_model)
>>> # Use swa_model to make predictions on test data
>>> preds = swa_model(test_input)
```

### Putting it all together: EMA

In the example below, `ema_model` is the EMA model that accumulates the exponentially-decayed averages of the weights with a decay rate of 0.999.
We train the model for a total of 300 epochs and start to collect EMA averages immediately.

```
>>> loader, optimizer, model, loss_fn = ...
>>> ema_model = torch.optim.swa_utils.AveragedModel(model, \
>>> multi_avg_fn=torch.optim.swa_utils.get_ema_multi_avg_fn(0.999))
>>>
>>> for epoch in range(300):
>>> for input, target in loader:
>>> optimizer.zero_grad()
>>> loss_fn(model(input), target).backward()
>>> optimizer.step()
>>> ema_model.update_parameters(model)
>>>
>>> # Update bn statistics for the ema_model at the end
>>> torch.optim.swa_utils.update_bn(loader, ema_model)
>>> # Use ema_model to make predictions on test data
>>> preds = ema_model(test_input)
```

| [`swa_utils.AveragedModel`](generated/torch.optim.swa_utils.AveragedModel.html#torch.optim.swa_utils.AveragedModel) | Implements averaged model for Stochastic Weight Averaging (SWA) and Exponential Moving Average (EMA). |
| --- | --- |
| [`swa_utils.SWALR`](generated/torch.optim.swa_utils.SWALR.html#torch.optim.swa_utils.SWALR) | Anneals the learning rate in each parameter group to a fixed value. |
| [`swa_utils.get_ema_avg_fn`](generated/torch.optim.swa_utils.get_ema_avg_fn.html#torch.optim.swa_utils.get_ema_avg_fn) | Get the function applying exponential moving average (EMA) across multiple params. |
| [`swa_utils.get_swa_avg_fn`](generated/torch.optim.swa_utils.get_swa_avg_fn.html#torch.optim.swa_utils.get_swa_avg_fn) | Get the function applying stochastic weight average (SWA) across a single param. |
| [`swa_utils.get_swa_multi_avg_fn`](generated/torch.optim.swa_utils.get_swa_multi_avg_fn.html#torch.optim.swa_utils.get_swa_multi_avg_fn) | Get the function applying stochastic weight average (SWA) across multiple params. |

torch.optim.swa_utils.get_ema_multi_avg_fn(*decay=0.999*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/swa_utils.py#L42)

Get the function applying exponential moving average (EMA) across multiple params.

The EMA is computed as:

W0EMA=W0modelW_0^{\text{EMA}} = W_0^{\text{model}}

W0EMA​=W0model​
Wt+1EMA=decay×WtEMA+(1−decay)×Wt+1modelW_{t+1}^{\text{EMA}} = \text{decay} \times W_t^{\text{EMA}} + (1 - \text{decay}) \times W_{t+1}^{\text{model}}

Wt+1EMA​=decay×WtEMA​+(1−decay)×Wt+1model​

where WtEMAW_t^{\text{EMA}}WtEMA​ is the EMA parameter at step ttt,
WtmodelW_t^{\text{model}}Wtmodel​ is the model parameter at step ttt,
and decay\text{decay}decay is the decay rate (default: 0.999).

Parameters:

**decay** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Decay rate for EMA. Must be in the range [0, 1]. Default: 0.999

Returns:

A function that updates EMA parameters given current model parameters

Return type:

Callable

torch.optim.swa_utils.update_bn(*loader*, *model*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/optim/swa_utils.py#L371)

Update BatchNorm running_mean, running_var buffers in the model.

It performs one pass over data in loader to estimate the activation
statistics for BatchNorm layers in the model.

Parameters:

- **loader** ([*torch.utils.data.DataLoader*](data.html#torch.utils.data.DataLoader)) - dataset loader to compute the
activation statistics on. Each data batch should be either a
tensor, or a list/tuple whose first element is a tensor
containing data.
- **model** ([*torch.nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - model for which we seek to update BatchNorm
statistics.
- **device** ([*torch.device*](tensor_attributes.html#torch.device)*,**optional*) - If set, data will be transferred to
`device` before being passed into `model`.

Example

```
>>> loader, model = ...
>>> torch.optim.swa_utils.update_bn(loader, model)
```

Note

The update_bn utility assumes that each data batch in `loader`
is either a tensor or a list or tuple of tensors; in the latter case it
is assumed that `model.forward()` should be called on the first
element of the list or tuple corresponding to the data batch.

 This module needs to be documented. Adding here in the meantime
for tracking purposes