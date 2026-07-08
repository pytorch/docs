# torch.distributions.constraints.dependent

torch.distributions.constraints.dependent*= Dependent()*

Placeholder for variables whose support depends on other variables.
These variables obey no simple coordinate-wise constraints.

Parameters:

- **is_discrete** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Optional value of `.is_discrete` in case this
can be computed statically. If not provided, access to the
`.is_discrete` attribute will raise a NotImplementedError.
- **event_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Optional value of `.event_dim` in case this
can be computed statically. If not provided, access to the
`.event_dim` attribute will raise a NotImplementedError.