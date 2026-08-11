# Muon

*class*torch.optim.Muon(*params*, *lr=0.001*, *weight_decay=0.1*, *momentum=0.95*, *nesterov=True*, *ns_coefficients=(3.4445, -4.775, 2.0315)*, *eps=1e-07*, *ns_steps=5*, *adjust_lr_fn=None*)

Implements Muon algorithm.

input:γ (lr), λ (weight decay), μ (momentum), nesterov∈{True,False},(a,b,c) (NS coefficients), ε (epsilon), k (NS steps), θ0 (params), f(θ) (objective)initialize:B0←0 (momentum buffer)for t=1 to ... dogt←∇θft(θt−1)Bt←μBt−1+gtB~t←{gt+μBt,if nesterov=TrueBt,if nesterov=FalseOt←NSk(a,b,c) ⁣(B~t; ε)θt←θt−1−γ λ θt−1(decoupled weight decay)γ←AdjustLR ⁣(γ; shape ⁣(θt))θt←θt−γ Otreturn θts\begin{aligned}
 &\rule{110mm}{0.4pt} \\
 &\textbf{input} : \gamma \text{ (lr)},\ \lambda \text{ (weight decay)},\
 \mu \text{ (momentum)},\ \textit{nesterov}\in\{True,False\},\\
 &\hspace{13mm}(a,b,c)\ \text{ (NS coefficients)},\
 \varepsilon \text{ (epsilon)},\ k \text{ (NS steps)},\
 \theta_0 \text{ (params)},\ f(\theta) \text{ (objective)} \\
 &\textbf{initialize} : B_0 \leftarrow 0 \text{ (momentum buffer)} \\[-1.ex]
 &\rule{110mm}{0.4pt} \\
 &\textbf{for}\ t=1\ \textbf{to}\ \ldots\ \textbf{do} \\[0.25ex]
 &\hspace{5mm} g_t \leftarrow \nabla_{\theta} f_t(\theta_{t-1}) \\[0.25ex]
 &\hspace{5mm} B_t \leftarrow \mu B_{t-1} + g_t \\[0.25ex]
 &\hspace{5mm} \widetilde{B}_t \leftarrow
 \begin{cases}
 g_t + \mu B_t, & \text{if nesterov}=True \\
 B_t, & \text{if nesterov}=False
 \end{cases} \\[1.0ex]
 &\hspace{5mm} O_t \leftarrow \mathrm{NS}^{(a,b,c)}_{k}\!\big(\widetilde{B}_t;\ \varepsilon\big) \\[0.5ex]
 &\hspace{5mm} \theta_t \leftarrow \theta_{t-1} - \gamma\,\lambda\,\theta_{t-1}
 \quad\text{(decoupled weight decay)} \\[0.25ex]

 &\hspace{5mm} \gamma \leftarrow \mathrm{AdjustLR}\!\big(\gamma;\ \mathrm{shape}\!\big(\theta_t \big) \big) \\[0.25ex]
 &\hspace{5mm} \theta_t \leftarrow \theta_t - \gamma\, O_t \\
 &\rule{110mm}{0.4pt} \\[-1.ex]
 &\mathbf{return}\ \theta_t \\[-1.ex]
 &\rule{110mm}{0.4pt}s
\end{aligned}​input:γ (lr), λ (weight decay), μ (momentum), nesterov∈{True,False},(a,b,c) (NS coefficients), ε (epsilon), k (NS steps), θ0​ (params), f(θ) (objective)initialize:B0​←0 (momentum buffer)for t=1 to ... dogt​←∇θ​ft​(θt−1​)Bt​←μBt−1​+gt​Bt​←{gt​+μBt​,Bt​,​if nesterov=Trueif nesterov=False​Ot​←NSk(a,b,c)​(Bt​; ε)θt​←θt−1​−γλθt−1​(decoupled weight decay)γ←AdjustLR(γ; shape(θt​))θt​←θt​−γOt​return θt​s​

Here, NSk(a,b,c)(⋅;ε)\mathrm{NS}^{(a,b,c)}_{k}(\cdot;\varepsilon)NSk(a,b,c)​(⋅;ε) denotes kkk iterations of the
Newton-Schulz orthogonalization operator parameterized by coefficients (a,b,c)(a,b,c)(a,b,c)
with numerical stabilization ε\varepsilonε.

The purpose for AdjustLR ⁣(γ; shape ⁣(θt))\mathrm{AdjustLR}\!\big(\gamma;\ \mathrm{shape}\!\big(\theta_t \big) \big)AdjustLR(γ; shape(θt​))
is to make the orthogonalized update scale consistently across rectangular matrices.

Keller's original implementation scales the update by max⁡ ⁣(1,AB)\sqrt{\max\!\left(1, \frac{A}{B}\right)}max(1,BA​)​,
where AAA and BBB are dimensions of the matrix being optimized, which represent fan-out
and fan-in for a Linear weight matrix.

Moonshot's implementation focuses on matching RMSRMSRMS of AdamW. The adjustment is computed as:
γ←0.2γ max⁡ ⁣(A,B)\gamma \leftarrow {0.2}\gamma\,\sqrt{\max\!\left({A}, {B}\right)}γ←0.2γmax(A,B)​
The method is adopted from [Muon is Scalable for LLM Training](https://arxiv.org/pdf/2502.16982). Research
results show that with this adjustment Muon can directly reuse the learning rate
and weight decay tuned for AdamW.

Jeremy Bernstein in [Deriving Muon](https://jeremybernste.in/writing/deriving-muon) proposes a scaling condition on the spectral norm, which
scales the update by AB\sqrt{\frac{A}{B}}BA​​. This is similar to the Keller's "original"
implementation but removes clamping down to 1.

We provide these options for the learning rate adjustment: "original", which follows Keller's
implementation, "match_rms_adamw", which refers to Moonshot's implementation, and "spectral_unclamped",
which matches Bernstein's implementation. If adjust_lr_fn is not specified, the default is "original".

For further details regarding the algorithm we refer to [Muon: An optimizer for hidden layers in neural networks](https://kellerjordan.github.io/posts/muon/),
[Muon is Scalable for LLM Training](https://arxiv.org/pdf/2502.16982), and [Deriving Muon](https://jeremybernste.in/writing/deriving-muon).

Parameters:

- **params** (*iterable*) - iterable of parameters or named_parameters to optimize
or iterable of dicts defining parameter groups. When using named_parameters,
all parameters in all groups should be named. Note that Muon is an optimizer for 2D parameters of neural network hidden layers. Other
parameters, such as bias, and embedding, should be optimized by a standard method such as AdamW.
- **lr** ([*float*](https://docs.python.org/3/library/functions.html#float)*,*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - learning rate (default: 1e-3).
- **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - weight decay (L2 penalty). (default: 0.1)
- **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - momentum factor (default: 0.95)
- **nesterov** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - enables Nesterov momentum. Only applicable
when momentum is non-zero
- **ns_coefficients** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**three floats**,**optional*) - coefficients (a,b,c) for the
Newton-Schulz orthogonalization polynomial (default: (3.4445, -4.775, 2.0315))
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - term added to the denominator for numerical stability. (default: 1e-07)
- **ns_steps** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - number of Newton-Schulz iteration steps. (default: 5)
- **adjust_lr_fn** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - function to adjust learning rate. One of "original", "match_rms_adamw", and "spectral_unclamped".
If not specified, we will default to use "original". (default: None)

Example

```
>>> # Muon only supports 2D params; use a standard optimizer
>>> # such as AdamW for biases, embeddings, and other non-2D
>>> # parameters.
>>> muon_params = [
... p for p in model.parameters() if p.ndim == 2
... ]
>>> other_params = [
... p for p in model.parameters() if p.ndim != 2
... ]
>>> optim_muon = torch.optim.Muon(
... muon_params, lr=0.02, momentum=0.95
... )
>>> optim_adamw = torch.optim.AdamW(
... other_params, lr=3e-4, weight_decay=0.01
... )
>>> optim_muon.zero_grad()
>>> optim_adamw.zero_grad()
>>> loss_fn(model(input), target).backward()
>>> optim_muon.step()
>>> optim_adamw.step()
```

add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L1126)

Add a param group to the [`Optimizer`](../optim.html#torch.optim.Optimizer) s param_groups.

This can be useful when fine tuning a pre-trained network as frozen layers can be made
trainable and added to the [`Optimizer`](../optim.html#torch.optim.Optimizer) as training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Specifies what Tensors should be optimized along with group
specific optimization options.

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L899)

Load the optimizer state.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - optimizer state. Should be an object returned
from a call to `state_dict()`.

Warning

Make sure this method is called after initializing [`torch.optim.lr_scheduler.LRScheduler`](torch.optim.lr_scheduler.LRScheduler.html#torch.optim.lr_scheduler.LRScheduler),
as calling it beforehand will overwrite the loaded learning rates.

Note

The names of the parameters (if they exist under the "param_names" key of each param group
in `state_dict()`) will not affect the loading process.
To use the parameters' names for custom cases (such as when the parameters in the loaded state dict
differ from those initialized in the optimizer),
a custom `register_load_state_dict_pre_hook` should be implemented to adapt the loaded dict
accordingly.
If `param_names` exist in loaded state dict `param_groups` they will be saved and override
the current names, if present, in the optimizer state. If they do not exist in loaded state dict,
the optimizer `param_names` will remain unchanged.

Example

```
>>> optimizer = ... # initialized optimizer matching the saved state
>>> scheduler1 = torch.optim.lr_scheduler.LinearLR(
... optimizer,
... start_factor=0.1,
... end_factor=1,
... total_iters=20,
... )
>>> scheduler2 = torch.optim.lr_scheduler.CosineAnnealingLR(
... optimizer,
... T_max=80,
... eta_min=3e-5,
... )
>>> lr = torch.optim.lr_scheduler.SequentialLR(
... optimizer,
... schedulers=[scheduler1, scheduler2],
... milestones=[20],
... )
>>> lr.load_state_dict(torch.load("./save_seq.pt"))
>>> # now load the optimizer checkpoint after loading the LRScheduler
>>> optimizer.load_state_dict(torch.load("./save_optim.pt"))
```

register_load_state_dict_post_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L863)

Register a load_state_dict post-hook which will be called after
[`load_state_dict()`](torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) is called. It should have the
following signature:

```
hook(optimizer) -> None
```

The `optimizer` argument is the optimizer instance being used.

The hook will be called with argument `self` after calling
`load_state_dict` on `self`. The registered hook can be used to
perform post-processing after `load_state_dict` has loaded the
`state_dict`.

Parameters:

- **hook** (*Callable*) - The user defined hook to be registered.
- **prepend** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, the provided post `hook` will be fired before
all the already registered post-hooks on `load_state_dict`. Otherwise,
the provided `hook` will be fired after all the already registered
post-hooks. (default: False)

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register_load_state_dict_pre_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L824)

Register a load_state_dict pre-hook which will be called before
[`load_state_dict()`](torch.optim.Optimizer.load_state_dict.html#torch.optim.Optimizer.load_state_dict) is called. It should have the
following signature:

```
hook(optimizer, state_dict) -> state_dict or None
```

The `optimizer` argument is the optimizer instance being used and the
`state_dict` argument is a shallow copy of the `state_dict` the user
passed in to `load_state_dict`. The hook may modify the state_dict inplace
or optionally return a new one. If a state_dict is returned, it will be used
to be loaded into the optimizer.

The hook will be called with argument `self` and `state_dict` before
calling `load_state_dict` on `self`. The registered hook can be used to
perform pre-processing before the `load_state_dict` call is made.

Parameters:

- **hook** (*Callable*) - The user defined hook to be registered.
- **prepend** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, the provided pre `hook` will be fired before
all the already registered pre-hooks on `load_state_dict`. Otherwise,
the provided `hook` will be fired after all the already registered
pre-hooks. (default: False)

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register_state_dict_post_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L665)

Register a state dict post-hook which will be called after [`state_dict()`](torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict) is called.

It should have the following signature:

```
hook(optimizer, state_dict) -> state_dict or None
```

The hook will be called with arguments `self` and `state_dict` after generating
a `state_dict` on `self`. The hook may modify the state_dict inplace or optionally
return a new one. The registered hook can be used to perform post-processing
on the `state_dict` before it is returned.

Parameters:

- **hook** (*Callable*) - The user defined hook to be registered.
- **prepend** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, the provided post `hook` will be fired before
all the already registered post-hooks on `state_dict`. Otherwise,
the provided `hook` will be fired after all the already registered
post-hooks. (default: False)

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register_state_dict_pre_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L633)

Register a state dict pre-hook which will be called before [`state_dict()`](torch.optim.Optimizer.state_dict.html#torch.optim.Optimizer.state_dict) is called.

It should have the following signature:

```
hook(optimizer) -> None
```

The `optimizer` argument is the optimizer instance being used.
The hook will be called with argument `self` before calling `state_dict` on `self`.
The registered hook can be used to perform pre-processing before the `state_dict`
call is made.

Parameters:

- **hook** (*Callable*) - The user defined hook to be registered.
- **prepend** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, the provided pre `hook` will be fired before
all the already registered pre-hooks on `state_dict`. Otherwise,
the provided `hook` will be fired after all the already registered
pre-hooks. (default: False)

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register_step_post_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L612)

Register an optimizer step post hook which will be called after optimizer step.

It should have the following signature:

```
hook(optimizer, args, kwargs) -> None
```

The `optimizer` argument is the optimizer instance being used.

Parameters:

**hook** (*Callable*) - The user defined hook to be registered.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register_step_pre_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L589)

Register an optimizer step pre hook which will be called before optimizer step.

It should have the following signature:

```
hook(optimizer, args, kwargs) -> None or modified args and kwargs
```

The `optimizer` argument is the optimizer instance being used. If
args and kwargs are modified by the pre-hook, then the transformed
values are returned as a tuple containing the new_args and new_kwargs.

Parameters:

**hook** (*Callable*) - The user defined hook to be registered.

Returns:

a handle that can be used to remove the added hook by calling
`handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L699)

Return the state of the optimizer as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict).

It contains two entries:

- `state`: a Dict holding current optimization state. Its content

differs between optimizer classes, but some common characteristics
hold. For example, state is saved per parameter, and the parameter
itself is NOT saved. `state` is a Dictionary mapping parameter ids
to a Dict with state corresponding to each parameter.
- `param_groups`: a List containing all parameter groups where each

parameter group is a Dict. Each parameter group contains metadata
specific to the optimizer, such as learning rate and weight decay,
as well as a List of parameter IDs of the parameters in the group.
If a param group was initialized with `named_parameters()` the names
content will also be saved in the state dict.

NOTE: The parameter IDs may look like indices but they are just IDs
associating state with param_group. When loading from a state_dict,
the optimizer will zip the param_group `params` (int IDs) and the
optimizer `param_groups` (actual `nn.Parameter` s) in order to
match state WITHOUT additional verification.

A returned state dict might look something like:

```
{
 'state': {
 0: {'momentum_buffer': tensor(...), ...},
 1: {'momentum_buffer': tensor(...), ...},
 2: {'momentum_buffer': tensor(...), ...},
 3: {'momentum_buffer': tensor(...), ...}
 },
 'param_groups': [
 {
 'lr': 0.01,
 'weight_decay': 0,
 ...
 'params': [0]
 'param_names' ['param0'] (optional)
 },
 {
 'lr': 0.001,
 'weight_decay': 0.5,
 ...
 'params': [1, 2, 3]
 'param_names': ['param1', 'layer.weight', 'layer.bias'] (optional)
 }
 ]
}
```

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

step(*closure=None*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/_muon.py#L167)

Performs a single optimization step.

zero_grad(*set_to_none=True*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/optim/optimizer.py#L1047)

Reset the gradients of all optimized [`torch.Tensor`](../tensors.html#torch.Tensor) s.

Parameters:

**set_to_none** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) -

Instead of setting to zero, set the grads to None. Default: `True`

This will in general have lower memory footprint, and can modestly improve performance.
However, it changes certain behaviors. For example:

1. When the user tries to access a gradient and perform manual ops on it,
a None attribute or a Tensor full of 0s will behave differently.
2. If the user requests `zero_grad(set_to_none=True)` followed by a backward pass, `.grad`s
are guaranteed to be None for params that did not receive a gradient.
3. `torch.optim` optimizers have a different behavior if the gradient is 0 or None
(in one case it does the step with a gradient of 0 and in the other it skips
the step altogether).