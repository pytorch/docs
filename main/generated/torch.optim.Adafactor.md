# Adafactor

*class*torch.optim.Adafactor(*params*, *lr=0.01*, *beta2_decay=-0.8*, *eps=(None, 0.001)*, *d=1.0*, *weight_decay=0.0*, ***, *foreach=None*, *maximize=False*)

Implements Adafactor algorithm.

input:γ(lr), τ(β2 decay), θ0(params), f(θ)(objective), ϵ1,ϵ2 (epsilons), d(clipping threshold), λ(weight decay), maximizeinitialize: R0←0 (second moment row factor), C0←0 (second moment col factor), V^0←0 (second moment for vectors)for t=1 to ... doif maximize:Gt←−∇θft(θt−1)elseGt←∇θft(θt−1)β^2t←1−tτρt←min(γ,1t)αt←max(ϵ2,RMS(θt−1))ρtθt←θt−1−γλθt−1if dim(Gt)>1:Rt←β^2tRt−1+(1−β^2t)(Gt⊙Gt)⋅1mCt←β^2tCt−1+(1−β^2t)1n⊤⋅(Gt⊙Gt)V^t←Rt⋅Ctmax(1n⊤⋅Rt,ϵ1)elseV^t←β^2tV^t−1+(1−β^2t)⋅(Gt⊙Gt)Ut←Gtmax(V^t,ϵ1)U^t←Utmax(1,RMS(Ut)d)θt←θt−1−αtU^treturn θt\begin{aligned}
 &\rule{110mm}{0.4pt} \\
 &\textbf{input} : \gamma \text{(lr)}, \: \tau
 \text{(}\beta_2\text{ decay)}, \: \theta_0 \text{(params)}, \: f(\theta) \text{(objective)}, \\
 &\hspace{15mm} \: \epsilon_1, \epsilon_2 \text{ (epsilons)}, \: d \text{(clipping threshold)}, \\
 &\hspace{15mm} \: \lambda \text{(weight decay)},
 \: \textit{maximize} \\
 &\textbf{initialize} : \: R_0 \leftarrow 0 \text{ (second moment row factor)}, \\
 &\hspace{23mm} \: C_0 \leftarrow 0 \text{ (second moment col factor)}, \\
 &\hspace{23mm} \: \widehat{V}_0 \leftarrow 0 \text{ (second moment for vectors)} \\[-1.ex]
 &\rule{110mm}{0.4pt} \\
 &\textbf{for} \: t=1 \: \textbf{to} \: \ldots \: \textbf{do} \\

 &\hspace{5mm}\textbf{if} \: \textit{maximize}: \\
 &\hspace{10mm}G_t \leftarrow -\nabla_{\theta} f_t (\theta_{t-1}) \\
 &\hspace{5mm}\textbf{else} \\
 &\hspace{10mm}G_t \leftarrow \nabla_{\theta} f_t (\theta_{t-1}) \\
 &\hspace{5mm}\widehat{\beta}_{2_t} \leftarrow 1 - t^{\tau} \\
 &\hspace{5mm}\rho_t \leftarrow min(\gamma, \frac{1}{\sqrt{t}}) \\
 &\hspace{5mm}\alpha_t \leftarrow max(\epsilon_2,
 \text{RMS}(\theta_{t-1}))\rho_t \\
 &\hspace{5mm}\theta_t \leftarrow \theta_{t-1} - \gamma \lambda \theta_{t-1} \\
 &\hspace{5mm}\textbf{if} \: \text{dim}(G_t) > 1: \\
 &\hspace{10mm}R_t \leftarrow \widehat{\beta}_{2_t}R_{t-1}+
 (1-\widehat{\beta}_{2_t})(G_t \odot G_t) \cdot 1_m \\
 &\hspace{10mm}C_t \leftarrow \widehat{\beta}_{2_t}C_{t-1}+
 (1-\widehat{\beta}_{2_t}) 1^\top_n \cdot (G_t \odot G_t) \\
 &\hspace{10mm}\widehat{V}_t \leftarrow
 \frac{R_t \cdot C_t}{max(1^\top_n \cdot R_t, \epsilon_1)} \\
 &\hspace{5mm}\textbf{else} \\
 &\hspace{10mm}\widehat{V}_t \leftarrow \widehat{\beta}_{2_t}\widehat{V}_{t-1}+
 (1-\widehat{\beta}_{2_t}) \cdot (G_t \odot G_t) \\
 &\hspace{5mm}U_t \leftarrow
 \frac{G_t}{max(\sqrt{\widehat{V}_t}, \epsilon_1)} \\
 &\hspace{5mm}\widehat{U}_t \leftarrow \frac{U_t}{max(1, \frac{\text{RMS}(U_t)}{d})} \\
 &\hspace{5mm}\theta_t \leftarrow \theta_{t-1} - \alpha_t \widehat{U}_t \\

 &\rule{110mm}{0.4pt} \\[-1.ex]
 &\bf{return} \: \theta_t \\[-1.ex]
 &\rule{110mm}{0.4pt} \\[-1.ex]
\end{aligned}​input:γ(lr),τ(β2​ decay),θ0​(params),f(θ)(objective),ϵ1​,ϵ2​ (epsilons),d(clipping threshold),λ(weight decay),maximizeinitialize:R0​←0 (second moment row factor),C0​←0 (second moment col factor),V0​←0 (second moment for vectors)fort=1to...doifmaximize:Gt​←−∇θ​ft​(θt−1​)elseGt​←∇θ​ft​(θt−1​)β​2t​​←1−tτρt​←min(γ,t​1​)αt​←max(ϵ2​,RMS(θt−1​))ρt​θt​←θt−1​−γλθt−1​ifdim(Gt​)>1:Rt​←β​2t​​Rt−1​+(1−β​2t​​)(Gt​⊙Gt​)⋅1m​Ct​←β​2t​​Ct−1​+(1−β​2t​​)1n⊤​⋅(Gt​⊙Gt​)Vt​←max(1n⊤​⋅Rt​,ϵ1​)Rt​⋅Ct​​elseVt​←β​2t​​Vt−1​+(1−β​2t​​)⋅(Gt​⊙Gt​)Ut​←max(Vt​​,ϵ1​)Gt​​Ut​←max(1,dRMS(Ut​)​)Ut​​θt​←θt−1​−αt​Ut​returnθt​​

For further details regarding the algorithm we refer to [Adafactor: Adaptive Learning Rates with Sublinear Memory Cost](https://arxiv.org/pdf/1804.04235).

Parameters:

- **params** (*iterable*) - iterable of parameters or named_parameters to optimize
or iterable of dicts defining parameter groups. When using named_parameters,
all parameters in all groups should be named
- **lr** ([*float*](https://docs.python.org/3/library/functions.html#float)*,*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - unlike other optimizers, Adafactor does not require a
learning rate, and Noam Shazeer and Mitchell Stern do not use lr at all.
Deviating from the paper, this implementation uses lr for applying weight
decay and as the maximum value for relative step size rho_t. Note that in
the paper, a constant of 0.01 is used as the maximum value for relative
step size, and so we set 0.01 as the default value. (default: 1e-2)
- **beta2_decay** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the decay rate of beta2. beta2 standardly refers
to the coefficient used for computing the running average of the gradient
squared. (default: -0.8)
- **eps** (*Tuple**[*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*]**,**optional*) - epsilon1 is the term added to the denominator
of the update calculation to improve numerical stability. This use of epsilon1
deviates from the algorithm written in the paper! See note below for more details.
epsilon2 is the term used to avoid having too small a weight update when applying
parameter scaling. (default: (None, 1e-3))
- **d** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the clipping threshold, used to avoid larger-than-desired
updates.
- **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - weight decay coefficient (default: 1e-2)
- **foreach** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether foreach implementation of optimizer is used. Note
that the foreach implementation uses ~ sizeof(params) more peak memory than the
for-loop version due to the intermediates being a tensorlist vs just one tensor.
As Adafactor is commonly used when memory is prohibitive, Adafactor will default
to the slower single tensor for-loop implementation unless this flag is explicitly
True. This behavior is contrary to other optimizers, which will attempt defaulting
to foreach on CUDA for faster runtime. (default: None)
- **maximize** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - maximize the objective with respect to the
params, instead of minimizing (default: False)

Note

The implementation of Adafactor subtly differs from Noam Shazeer and Mitchell Stern
and implementations in some other frameworks with its use of learning rate and
ϵ1\epsilon_1ϵ1​.

Regarding the learning rate hyperparameter: Noam Shazeer and Mitchell Stern do not
use lr at all, as the stated algorithm uses ρt\rho_tρt​ and update clipping to
affect the step size.

This implementation allows lr to influence the maximum value for ρt\rho_tρt​:

ρt←min(γ,1t)\begin{aligned}
 &\hspace{5mm}\rho_t \leftarrow min(\gamma, \frac{1}{\sqrt{t}})
\end{aligned}

​ρt​←min(γ,t​1​)​

This differs from Noam Shazeer and Mitchell Stern, who use a constant of 0.01 as
the maximum value of ρt\rho_tρt​

ρt←min(0.01,1t)\begin{aligned}
 &\hspace{5mm}\rho_t \leftarrow min(0.01, \frac{1}{\sqrt{t}})
\end{aligned}

​ρt​←min(0.01,t​1​)​

Noam Shazeer and Mitchell Stern do not enforce an opinion on how weight decay should
be computed, and so we use the learning rate as a coefficient for decoupled weight
decay, similar to what is suggested in [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101).

Regarding the use of ϵ1\epsilon_1ϵ1​: The implementation attempts to replicate the
presumed intention of Noam Shazeer and Mitchell Stern to use ϵ1\epsilon_1ϵ1​ as
a stabilizing term when the squared gradient becomes small.

This stabilization can be written as

Rt←β^2tRt−1+(1−β^2t)(Gt⊙Gt+1n⋅1m⊤)⋅1mCt←β^2tCt−1+(1−β^2t)1n⊤⋅(Gt⊙Gt+1n⋅1m⊤)V^t←Rt⋅Ctmax(1n⊤⋅Rt,ϵ1)Ut←Gtmax(V^t,ϵ1)\begin{aligned}
 &\hspace{5mm}R_t \leftarrow \widehat{\beta}_{2_t}R_{t-1}+
 (1-\widehat{\beta}_{2_t})(G_t \odot G_t + 1_n \cdot 1^\top_m) \cdot 1_m \\
 &\hspace{5mm}C_t \leftarrow \widehat{\beta}_{2_t}C_{t-1}+
 (1-\widehat{\beta}_{2_t}) 1^\top_n \cdot (G_t \odot G_t + 1_n \cdot 1^\top_m) \\
 &\hspace{5mm}\widehat{V}_t \leftarrow
 \frac{R_t \cdot C_t}{max(1^\top_n \cdot R_t, \epsilon_1)} \\
 &\hspace{5mm}U_t \leftarrow \frac{G_t}{max(\sqrt{\widehat{V}_t}, \epsilon_1)} \\
\end{aligned}

​Rt​←β​2t​​Rt−1​+(1−β​2t​​)(Gt​⊙Gt​+1n​⋅1m⊤​)⋅1m​Ct​←β​2t​​Ct−1​+(1−β​2t​​)1n⊤​⋅(Gt​⊙Gt​+1n​⋅1m⊤​)Vt​←max(1n⊤​⋅Rt​,ϵ1​)Rt​⋅Ct​​Ut​←max(Vt​​,ϵ1​)Gt​​​

where the row and column factors of gradient squared RtR_tRt​ and CtC_tCt​
are left alone, and we apply ϵ1\epsilon_1ϵ1​ at the final calculation of
the variance estimate V^t\widehat{V}_tVt​ and for the update UtU_tUt​.

This is in contrast to Noam Shazeer and Mitchell Stern and other frameworks which
apply ϵ1\epsilon_1ϵ1​ to both row and column factors of the squared gradient, but
not in the calculations after:

Rt←β^2tRt−1+(1−β^2t)(Gt⊙Gt+ϵ11n⋅1m⊤)⋅1mCt←β^2tCt−1+(1−β^2t)1n⊤⋅(Gt⊙Gt+ϵ11n⋅1m⊤)V^t←Rt⋅Ct1n⊤⋅RtUt←GtV^t\begin{aligned}
 &\hspace{5mm}R_t \leftarrow \widehat{\beta}_{2_t}R_{t-1}+
 (1-\widehat{\beta}_{2_t})(G_t \odot G_t + \epsilon_1 1_n \cdot 1^\top_m) \cdot 1_m \\
 &\hspace{5mm}C_t \leftarrow \widehat{\beta}_{2_t}C_{t-1}+
 (1-\widehat{\beta}_{2_t}) 1^\top_n \cdot (G_t \odot G_t + \epsilon_1 1_n \cdot 1^\top_m) \\
 &\hspace{5mm}\widehat{V}_t \leftarrow \frac{R_t \cdot C_t}{1^\top_n \cdot R_t} \\
 &\hspace{5mm}U_t \leftarrow \frac{G_t}{\sqrt{\widehat{V}_t}} \\
\end{aligned}

​Rt​←β​2t​​Rt−1​+(1−β​2t​​)(Gt​⊙Gt​+ϵ1​1n​⋅1m⊤​)⋅1m​Ct​←β​2t​​Ct−1​+(1−β​2t​​)1n⊤​⋅(Gt​⊙Gt​+ϵ1​1n​⋅1m⊤​)Vt​←1n⊤​⋅Rt​Rt​⋅Ct​​Ut​←Vt​​Gt​​​

You may note that Noam Shazeer and Mitchell Stern describe using the sum of squared gradients,
while this implementation uses the mean instead. This choice is mathematically equivalent and
allows for greater numerical stability for large sums.

add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L1102)

Add a param group to the [`Optimizer`](../optim.html#torch.optim.Optimizer) s param_groups.

This can be useful when fine tuning a pre-trained network as frozen layers can be made
trainable and added to the [`Optimizer`](../optim.html#torch.optim.Optimizer) as training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - Specifies what Tensors should be optimized along with group
specific optimization options.

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L880)

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

register_load_state_dict_post_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L844)

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

register_load_state_dict_pre_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L805)

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

register_state_dict_post_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L646)

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

register_state_dict_pre_hook(*hook*, *prepend=False*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L614)

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

register_step_post_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L593)

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

register_step_pre_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L570)

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

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L680)

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

step(*closure=None*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/_adafactor.py#L121)

Perform a single optimization step.

Parameters:

**closure** (*Callable**,**optional*) - A closure that reevaluates the model
and returns the loss.

zero_grad(*set_to_none=True*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/optim/optimizer.py#L1023)

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