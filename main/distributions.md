# Probability distributions - torch.distributions

The `distributions` package contains parameterizable probability distributions
and sampling functions. This allows the construction of stochastic computation
graphs and stochastic gradient estimators for optimization. This package
generally follows the design of the TensorFlow Distributions package.

It is not possible to directly backpropagate through random samples. However,
there are two main methods for creating surrogate functions that can be
backpropagated through. These are the score function estimator/likelihood ratio
estimator/REINFORCE and the pathwise derivative estimator. REINFORCE is commonly
seen as the basis for policy gradient methods in reinforcement learning, and the
pathwise derivative estimator is commonly seen in the reparameterization trick
in variational autoencoders. Whilst the score function only requires the value
of samples f(x)f(x)f(x), the pathwise derivative requires the derivative
f′(x)f'(x)f′(x). The next sections discuss these two in a reinforcement learning
example. For more details see
Gradient Estimation Using Stochastic Computation Graphs .

## Score function

When the probability density function is differentiable with respect to its
parameters, we only need `sample()` and
`log_prob()` to implement REINFORCE:

Δθ=αr∇θlog⁡πθ(a∣s)\Delta\theta = \alpha r \nabla_\theta \log \pi_\theta(a \mid s)Δθ=αr∇θ​logπθ​(a∣s)

where θ\thetaθ are the parameters, α\alphaα is the learning rate,
rrr is the reward and πθ(a∣s)\pi_\theta(a \mid s)πθ​(a∣s) is the probability of
taking action aaa in state sss given policy πθ\pi_\thetaπθ​.

In practice we would sample an action from the output of a network, apply this
action in an environment, and then use `log_prob` to construct an equivalent
loss function. Note that we use a negative because optimizers use gradient
descent, whilst the rule above assumes gradient ascent. With a categorical
policy, the code for implementing REINFORCE would be as follows:

```
probs = policy_network(state)
# Note that this is equivalent to what used to be called multinomial
m = Categorical(probs)
action = m.sample()
next_state, reward = env.step(action)
loss = -m.log_prob(action) * reward
loss.backward()
```

## Pathwise derivative

The other way to implement these stochastic/policy gradients would be to use the
reparameterization trick from the
`rsample()` method, where the
parameterized random variable can be constructed via a parameterized
deterministic function of a parameter-free random variable. The reparameterized
sample therefore becomes differentiable. The code for implementing the pathwise
derivative would be as follows:

```
params = policy_network(state)
m = Normal(*params)
# Any distribution with .has_rsample == True could work based on the application
action = m.rsample()
next_state, reward = env.step(action) # Assuming that reward is differentiable
loss = -reward
loss.backward()
```

## Distribution

*class*torch.distributions.distribution.Distribution(*batch_shape=()*, *event_shape=()*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L15)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Distribution is the abstract base class for probability distributions.

Parameters:

- **batch_shape** ([*torch.Size*](size.html#torch.Size)) - The shape over which parameters are batched.
- **event_shape** ([*torch.Size*](size.html#torch.Size)) - The shape of a single sample (without batching).
- **validate_args** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to validate arguments. Default: None.

*property*arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]*

Returns a dictionary from argument names to
`Constraint` objects that
should be satisfied by each argument of this distribution. Args that
are not tensors need not appear in this dict.

*property*batch_shape*: [Size](size.html#torch.Size)*

Returns the shape over which parameters are batched.

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L204)

Returns the cumulative density/mass function evaluated at
value.

Parameters:

**value** ([*Tensor*](tensors.html#torch.Tensor)) -

Return type:

[*Tensor*](tensors.html#torch.Tensor)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L248)

Returns entropy of distribution, batched over batch_shape.

Returns:

Tensor of shape batch_shape.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L224)

Returns tensor containing all values supported by a discrete
distribution. The result will enumerate over dimension 0, so the shape
of the result will be (cardinality,) + batch_shape + event_shape
(where event_shape = () for univariate distributions).

Note that this enumerates over all batched tensors in lock-step
[[0, 0], [1, 1], ...]. With expand=False, enumeration happens
along dim 0, but with the remaining batch dimensions being
singleton dimensions, [[0], [1], ...

To iterate over the full Cartesian product use
itertools.product(m.enumerate_support()).

Parameters:

**expand** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to expand the support over the
batch dims to match the distribution's batch_shape.

Returns:

Tensor iterating over dimension 0.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*event_shape*: [Size](size.html#torch.Size)*

Returns the shape of a single sample (without batching).

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L86)

Returns a new distribution instance (or populates an existing instance
provided by a derived class) with batch dimensions expanded to
batch_shape. This method calls [`expand`](generated/torch.Tensor.expand.html#torch.Tensor.expand) on
the distribution's parameters. As such, this does not allocate new
memory for the expanded distribution instance. Additionally,
this does not repeat any args checking or parameter broadcasting in
__init__.py, when an instance is first created.

Parameters:

- **batch_shape** ([*torch.Size*](size.html#torch.Size)) - the desired expanded size.
- **_instance** - new instance provided by subclasses that
need to override .expand.

Returns:

New distribution instance with batch dimensions expanded to
batch_shape.

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L214)

Returns the inverse cumulative density/mass function evaluated at
value.

Parameters:

**value** ([*Tensor*](tensors.html#torch.Tensor)) -

Return type:

[*Tensor*](tensors.html#torch.Tensor)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L194)

Returns the log of the probability density/mass function evaluated at
value.

Parameters:

**value** ([*Tensor*](tensors.html#torch.Tensor)) -

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

Returns the mean of the distribution.

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

Returns the mode of the distribution.

perplexity()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L257)

Returns perplexity of distribution, batched over batch_shape.

Returns:

Tensor of shape batch_shape.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L175)

Generates a sample_shape shaped reparameterized sample or sample_shape
shaped batch of reparameterized samples if the distribution parameters
are batched.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L167)

Generates a sample_shape shaped sample or sample_shape shaped batch of
samples if the distribution parameters are batched.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample_n(*n*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L183)

Generates n samples or n batches of samples if the distribution
parameters are batched.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*static*set_default_validate_args(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/distribution.py#L29)

Sets whether validation is enabled or disabled.

The default behavior mimics Python's `assert` statement: validation
is on by default, but is disabled if Python is run in optimized mode
(via `python -O`). Validation may be expensive, so you may want to
disable it once a model is working.

Parameters:

**value** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to enable validation.

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

Returns the standard deviation of the distribution.

*property*support*: Constraint | [None](https://docs.python.org/3/library/constants.html#None)*

Returns a `Constraint` object
representing this distribution's support.

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

Returns the variance of the distribution.

## ExponentialFamily

*class*torch.distributions.exp_family.ExponentialFamily(*batch_shape=()*, *event_shape=()*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exp_family.py#L11)

Bases: `Distribution`

ExponentialFamily is the abstract base class for probability distributions belonging to an
exponential family, whose probability mass/density function is defined below

pF(x;θ)=exp⁡(⟨t(x),θ⟩−F(θ)+k(x))p_{F}(x; \theta) = \exp(\langle t(x), \theta\rangle - F(\theta) + k(x))pF​(x;θ)=exp(⟨t(x),θ⟩−F(θ)+k(x))

where θ\thetaθ denotes the natural parameters, t(x)t(x)t(x) denotes the sufficient statistic,
F(θ)F(\theta)F(θ) is the log normalizer function for a given family and k(x)k(x)k(x) is the carrier
measure.

Note

This class is an intermediary between the Distribution class and distributions which belong
to an exponential family mainly to check the correctness of the .entropy() and analytic KL
divergence methods. We use this class to compute the entropy and KL divergence using the AD
framework and Bregman divergences (courtesy of: Frank Nielsen and Richard Nock, Entropies and
Cross-entropies of Exponential Families).

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exp_family.py#L55)

Method to compute the entropy using Bregman divergence of the log normalizer.

## Bernoulli

*class*torch.distributions.bernoulli.Bernoulli(*probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L20)

Bases: `ExponentialFamily`

Creates a Bernoulli distribution parameterized by `probs`
or `logits` (but not both).

Samples are binary (0 or 1). They take the value 1 with probability p
and 0 with probability 1 - p.

Example:

```
>>> m = Bernoulli(torch.tensor([0.3]))
>>> m.sample() # 30% chance 1; 70% chance 0
tensor([ 0.])
```

Parameters:

- **probs** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the probability of sampling 1
- **logits** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the log-odds of sampling 1
- **validate_args** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to validate arguments, None by default

arg_constraints*= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L127)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L132)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L74)

has_enumerate_support*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L121)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/bernoulli.py#L116)

support*= Boolean()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Beta

*class*torch.distributions.beta.Beta(*concentration1*, *concentration0*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/beta.py#L15)

Bases: `ExponentialFamily`

Beta distribution parameterized by `concentration1` and `concentration0`.

Example:

```
>>> m = Beta(torch.tensor([0.5]), torch.tensor([0.5]))
>>> m.sample() # Beta distributed with concentration concentration1 and concentration0
tensor([ 0.1046])
```

Parameters:

- **concentration1** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - 1st concentration parameter of the distribution
(often referred to as alpha)
- **concentration0** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - 2nd concentration parameter of the distribution
(often referred to as beta)

arg_constraints*= {'concentration0': GreaterThan(lower_bound=0.0), 'concentration1': GreaterThan(lower_bound=0.0)}*

*property*concentration0*: [Tensor](tensors.html#torch.Tensor)*

*property*concentration1*: [Tensor](tensors.html#torch.Tensor)*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/beta.py#L93)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/beta.py#L63)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/beta.py#L87)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/beta.py#L84)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= Interval(lower_bound=0.0, upper_bound=1.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Binomial

*class*torch.distributions.binomial.Binomial(*total_count=1*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L23)

Bases: `Distribution`

Creates a Binomial distribution parameterized by `total_count` and
either `probs` or `logits` (but not both). `total_count` must be
broadcastable with `probs`/`logits`.

Example:

```
>>> m = Binomial(100, torch.tensor([0 , .2, .8, 1]))
>>> x = m.sample()
tensor([ 0., 22., 71., 100.])

>>> m = Binomial(torch.tensor([[5.], [10.]]), torch.tensor([0.5, 0.8]))
>>> x = m.sample()
tensor([[ 4., 5.],
 [ 7., 6.]])
```

Parameters:

- **total_count** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*Tensor*](tensors.html#torch.Tensor)) - number of Bernoulli trials
- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - Event probabilities
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - Event log-odds

arg_constraints*= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0), 'total_count': IntegerGreaterThan(lower_bound=0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L160)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L170)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L87)

has_enumerate_support*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L140)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/binomial.py#L133)

*property*support

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Categorical

*class*torch.distributions.categorical.Categorical(*probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L13)

Bases: `Distribution`

Creates a categorical distribution parameterized by either `probs` or
`logits` (but not both).

Note

It is equivalent to the distribution that [`torch.multinomial()`](generated/torch.multinomial.html#torch.multinomial)
samples from.

Samples are integers from {0,...,K−1}\{0, \ldots, K-1\}{0,...,K−1} where K is `probs.size(-1)`.

If probs is 1-dimensional with length-K, each element is the relative probability
of sampling the class at that index.

If probs is N-dimensional, the first N-1 dimensions are treated as a batch of
relative probability vectors.

Note

The probs argument must be non-negative, finite and have a non-zero sum,
and it will be normalized to sum to 1 along the last dimension. `probs`
will return this normalized value.
The logits argument will be interpreted as unnormalized log probabilities
and can therefore be any real number. It will likewise be normalized so that
the resulting probabilities sum to 1 along the last dimension. `logits`
will return this normalized value.

See also: [`torch.multinomial()`](generated/torch.multinomial.html#torch.multinomial)

Example:

```
>>> m = Categorical(torch.tensor([ 0.25, 0.25, 0.25, 0.25 ]))
>>> m.sample() # equal probability of 0, 1, 2, 3
tensor(3)
```

Parameters:

- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - event probabilities
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - event log probabilities (unnormalized)

arg_constraints*= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L159)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L165)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L87)

has_enumerate_support*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L151)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/categorical.py#L144)

*property*support

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Cauchy

*class*torch.distributions.cauchy.Cauchy(*loc*, *scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L15)

Bases: `Distribution`

Samples from a Cauchy (Lorentz) distribution. The distribution of the ratio of
independent normally distributed random variables with means 0 follows a
Cauchy distribution.

Example:

```
>>> m = Cauchy(torch.tensor([0.0]), torch.tensor([1.0]))
>>> m.sample() # sample from a Cauchy distribution with loc=0 and scale=1
tensor([ 2.3214])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - mode or median of the distribution.
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - half width at half maximum.

arg_constraints*= {'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L90)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L98)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L51)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L95)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L81)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/cauchy.py#L76)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Chi2

*class*torch.distributions.chi2.Chi2(*df*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/chi2.py#L11)

Bases: `Gamma`

Creates a Chi-squared distribution parameterized by shape parameter `df`.
This is exactly equivalent to `Gamma(alpha=0.5*df, beta=0.5)`

Example:

```
>>> m = Chi2(torch.tensor([1.0]))
>>> m.sample() # Chi2 distributed with shape df=1
tensor([ 0.1046])
```

Parameters:

**df** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - shape parameter of the distribution

arg_constraints*= {'df': GreaterThan(lower_bound=0.0)}*

*property*df*: [Tensor](tensors.html#torch.Tensor)*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/chi2.py#L36)

## ContinuousBernoulli

*class*torch.distributions.continuous_bernoulli.ContinuousBernoulli(*probs=None*, *logits=None*, *lims=(0.499, 0.501)*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L22)

Bases: `ExponentialFamily`

Creates a continuous Bernoulli distribution parameterized by `probs`
or `logits` (but not both).

The distribution is supported in [0, 1] and parameterized by 'probs' (in
(0,1)) or 'logits' (real-valued). Note that, unlike the Bernoulli, 'probs'
does not correspond to a probability and 'logits' does not correspond to
log-odds, but the same names are used due to the similarity with the
Bernoulli. See [1] for more details.

Example:

```
>>> m = ContinuousBernoulli(torch.tensor([0.3]))
>>> m.sample()
tensor([ 0.2538])
```

Parameters:

- **probs** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - (0,1) valued parameters
- **logits** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - real valued parameters whose sigmoid matches 'probs'

[1] The continuous Bernoulli: fixing a pervasive error in variational
autoencoders, Loaiza-Ganem G and Cunningham JP, NeurIPS 2019.
[https://arxiv.org/abs/1907.06845](https://arxiv.org/abs/1907.06845)

arg_constraints*= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L196)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L224)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L91)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L212)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L187)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L182)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/continuous_bernoulli.py#L176)

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

support*= Interval(lower_bound=0.0, upper_bound=1.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Dirichlet

*class*torch.distributions.dirichlet.Dirichlet(*concentration*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/dirichlet.py#L38)

Bases: `ExponentialFamily`

Creates a Dirichlet distribution parameterized by concentration `concentration`.

Example:

```
>>> m = Dirichlet(torch.tensor([0.5, 0.5]))
>>> m.sample() # Dirichlet distributed with concentration [0.5, 0.5]
tensor([ 0.1046, 0.8954])
```

Parameters:

**concentration** ([*Tensor*](tensors.html#torch.Tensor)) - concentration parameter of the distribution
(often referred to as alpha)

arg_constraints*= {'concentration': IndependentConstraint(GreaterThan(lower_bound=0.0), 1)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/dirichlet.py#L122)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/dirichlet.py#L75)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/dirichlet.py#L90)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/dirichlet.py#L85)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= Simplex()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Exponential

*class*torch.distributions.exponential.Exponential(*rate*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L14)

Bases: `ExponentialFamily`

Creates a Exponential distribution parameterized by `rate`.

Example:

```
>>> m = Exponential(torch.tensor([1.0]))
>>> m.sample() # Exponential distributed with rate=1
tensor([ 0.1046])
```

Parameters:

**rate** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - rate = 1 / scale of the distribution

arg_constraints*= {'rate': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L77)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L85)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L60)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L82)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L72)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/exponential.py#L68)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThanEq(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## FisherSnedecor

*class*torch.distributions.fishersnedecor.FisherSnedecor(*df1*, *df2*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/fishersnedecor.py#L15)

Bases: `Distribution`

Creates a Fisher-Snedecor distribution parameterized by `df1` and `df2`.

Example:

```
>>> m = FisherSnedecor(torch.tensor([1.0]), torch.tensor([2.0]))
>>> m.sample() # Fisher-Snedecor-distributed with df1=1 and df2=2
tensor([ 0.2453])
```

Parameters:

- **df1** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - degrees of freedom parameter 1
- **df2** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - degrees of freedom parameter 2

arg_constraints*= {'df1': GreaterThan(lower_bound=0.0), 'df2': GreaterThan(lower_bound=0.0)}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/fishersnedecor.py#L52)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/fishersnedecor.py#L98)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/fishersnedecor.py#L86)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= GreaterThan(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Gamma

*class*torch.distributions.gamma.Gamma(*concentration*, *rate*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L18)

Bases: `ExponentialFamily`

Creates a Gamma distribution parameterized by shape `concentration` and `rate`.

Example:

```
>>> m = Gamma(torch.tensor([1.0]), torch.tensor([1.0]))
>>> m.sample() # Gamma distributed with concentration=1 and rate=1
tensor([ 0.1046])
```

Parameters:

- **concentration** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - shape parameter of the distribution
(often referred to as alpha)
- **rate** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - rate parameter of the distribution
(often referred to as beta), rate = 1 / scale

arg_constraints*= {'concentration': GreaterThan(lower_bound=0.0), 'rate': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L129)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L113)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L70)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L102)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L88)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*, ***, *generator=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gamma.py#L79)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= GreaterThanEq(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## GeneralizedPareto

*class*torch.distributions.generalized_pareto.GeneralizedPareto(*loc*, *scale*, *concentration*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L14)

Bases: `Distribution`

Creates a Generalized Pareto distribution parameterized by `loc`, `scale`, and `concentration`.

The Generalized Pareto distribution is a family of continuous probability distributions on the real line.
Special cases include Exponential (when `loc` = 0, `concentration` = 0), Pareto (when `concentration` > 0,
`loc` = `scale` / `concentration`), and Uniform (when `concentration` = -1).

This distribution is often used to model the tails of other distributions. This implementation is based on the
implementation in TensorFlow Probability.

Example:

```
>>> m = GeneralizedPareto(torch.tensor([0.1]), torch.tensor([2.0]), torch.tensor([0.4]))
>>> m.sample() # sample from a Generalized Pareto distribution with loc=0.1, scale=2.0, and concentration=0.4
tensor([ 1.5623])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Location parameter of the distribution
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Scale parameter of the distribution
- **concentration** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Concentration parameter of the distribution

arg_constraints*= {'concentration': Real(), 'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L104)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L137)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L60)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L107)

log_cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L101)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L75)

log_survival_function(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L90)

*property*mean

*property*mode

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/generalized_pareto.py#L70)

*property*support

Return type:

_DependentProperty

*property*variance

## Geometric

*class*torch.distributions.geometric.Geometric(*probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/geometric.py#L20)

Bases: `Distribution`

Creates a Geometric distribution parameterized by `probs`,
where `probs` is the probability of success of Bernoulli trials.

P(X=k)=(1−p)kp,k=0,1,...P(X=k) = (1-p)^{k} p, k = 0, 1, ...P(X=k)=(1−p)kp,k=0,1,...

Note

`torch.distributions.geometric.Geometric()` (k+1)(k+1)(k+1)-th trial is the first success
hence draws samples in {0,1,...}\{0, 1, \ldots\}{0,1,...}, whereas
[`torch.Tensor.geometric_()`](generated/torch.Tensor.geometric_.html#torch.Tensor.geometric_) k-th trial is the first success hence draws samples in {1,2,...}\{1, 2, \ldots\}{1,2,...}.

Example:

```
>>> m = Geometric(torch.tensor([0.3]))
>>> m.sample() # underlying Bernoulli has 30% chance 1; 70% chance 0
tensor([ 2.])
```

Parameters:

- **probs** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the probability of sampling 1. Must be in range (0, 1]
- **logits** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the log-odds of sampling 1.

arg_constraints*= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/geometric.py#L140)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/geometric.py#L89)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/geometric.py#L132)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/geometric.py#L120)

support*= IntegerGreaterThan(lower_bound=0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Gumbel

*class*torch.distributions.gumbel.Gumbel(*loc*, *scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gumbel.py#L17)

Bases: `TransformedDistribution`

Samples from a Gumbel Distribution.

Examples:

```
>>> m = Gumbel(torch.tensor([1.0]), torch.tensor([2.0]))
>>> m.sample() # sample from Gumbel distribution with loc=1, scale=2
tensor([ 1.0124])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Location parameter of the distribution
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Scale parameter of the distribution

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gumbel.py#L90)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gumbel.py#L61)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/gumbel.py#L68)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## HalfCauchy

*class*torch.distributions.half_cauchy.HalfCauchy(*scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L15)

Bases: `TransformedDistribution`

Creates a half-Cauchy distribution parameterized by scale where:

```
X ~ Cauchy(0, scale)
Y = |X| ~ HalfCauchy(scale)
```

Example:

```
>>> m = HalfCauchy(torch.tensor([1.0]))
>>> m.sample() # half-cauchy distributed with scale=1
tensor([ 2.3214])
```

Parameters:

**scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - scale of the full Cauchy distribution

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'scale': GreaterThan(lower_bound=0.0)}*

base_dist*: Cauchy*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L83)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L91)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L48)

has_rsample*= True*

icdf(*prob*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L88)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_cauchy.py#L73)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*scale*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThanEq(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## HalfNormal

*class*torch.distributions.half_normal.HalfNormal(*scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L15)

Bases: `TransformedDistribution`

Creates a half-normal distribution parameterized by scale where:

```
X ~ Normal(0, scale)
Y = |X| ~ HalfNormal(scale)
```

Example:

```
>>> m = HalfNormal(torch.tensor([1.0]))
>>> m.sample() # half-normal distributed with scale=1
tensor([ 0.1046])
```

Parameters:

**scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - scale of the full Normal distribution

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'scale': GreaterThan(lower_bound=0.0)}*

base_dist*: Normal*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L75)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L83)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L48)

has_rsample*= True*

icdf(*prob*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L80)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/half_normal.py#L68)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*scale*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThanEq(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Independent

*class*torch.distributions.independent.Independent(*base_distribution*, *reinterpreted_batch_ndims*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L18)

Bases: `Distribution`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`D`]

Reinterprets some of the batch dims of a distribution as event dims.

This is mainly useful for changing the shape of the result of
`log_prob()`. For example to create a diagonal Normal distribution with
the same shape as a Multivariate Normal distribution (so they are
interchangeable), you can:

```
>>> from torch.distributions.multivariate_normal import MultivariateNormal
>>> from torch.distributions.normal import Normal
>>> loc = torch.zeros(3)
>>> scale = torch.ones(3)
>>> mvn = MultivariateNormal(loc, scale_tril=torch.diag(scale))
>>> [mvn.batch_shape, mvn.event_shape]
[torch.Size([]), torch.Size([3])]
>>> normal = Normal(loc, scale)
>>> [normal.batch_shape, normal.event_shape]
[torch.Size([3]), torch.Size([])]
>>> diagn = Independent(normal, 1)
>>> [diagn.batch_shape, diagn.event_shape]
[torch.Size([]), torch.Size([3])]
```

Parameters:

- **base_distribution** (*torch.distributions.distribution.Distribution*) - a
base distribution
- **reinterpreted_batch_ndims** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of batch dims to
reinterpret as event dims

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {}*

base_dist*: D*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L124)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L128)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L71)

*property*has_enumerate_support*: [bool](https://docs.python.org/3/library/functions.html#bool)*

*property*has_rsample*: [bool](https://docs.python.org/3/library/functions.html#bool)*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L120)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L117)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/independent.py#L114)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*support

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## InverseGamma

*class*torch.distributions.inverse_gamma.InverseGamma(*concentration*, *rate*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/inverse_gamma.py#L14)

Bases: `TransformedDistribution`

Creates an inverse gamma distribution parameterized by `concentration` and `rate`
where:

```
X ~ Gamma(concentration, rate)
Y = 1 / X ~ InverseGamma(concentration, rate)
```

Example:

```
>>> m = InverseGamma(torch.tensor([2.0]), torch.tensor([3.0]))
>>> m.sample()
tensor([ 1.2953])
```

Parameters:

- **concentration** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - shape parameter of the distribution
(often referred to as alpha)
- **rate** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - rate = 1 / scale of the distribution
(often referred to as beta)

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'concentration': GreaterThan(lower_bound=0.0), 'rate': GreaterThan(lower_bound=0.0)}*

base_dist*: Gamma*

*property*concentration*: [Tensor](tensors.html#torch.Tensor)*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/inverse_gamma.py#L86)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/inverse_gamma.py#L58)

has_rsample*= True*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*rate*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThan(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Kumaraswamy

*class*torch.distributions.kumaraswamy.Kumaraswamy(*concentration1*, *concentration0*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/kumaraswamy.py#L24)

Bases: `TransformedDistribution`

Samples from a Kumaraswamy distribution.

Example:

```
>>> m = Kumaraswamy(torch.tensor([1.0]), torch.tensor([1.0]))
>>> m.sample() # sample from a Kumaraswamy distribution with concentration alpha=1 and beta=1
tensor([ 0.1729])
```

Parameters:

- **concentration1** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - 1st concentration parameter of the distribution
(often referred to as alpha)
- **concentration0** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - 2nd concentration parameter of the distribution
(often referred to as beta)

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'concentration0': GreaterThan(lower_bound=0.0), 'concentration1': GreaterThan(lower_bound=0.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/kumaraswamy.py#L98)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/kumaraswamy.py#L72)

has_rsample*= True*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

support*= Interval(lower_bound=0.0, upper_bound=1.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## LKJCholesky

*class*torch.distributions.lkj_cholesky.LKJCholesky(*dim*, *concentration=1.0*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lkj_cholesky.py#L23)

Bases: `Distribution`

LKJ distribution for lower Cholesky factor of correlation matrices.
The distribution is controlled by `concentration` parameter η\etaη
to make the probability of the correlation matrix MMM generated from
a Cholesky factor proportional to det⁡(M)η−1\det(M)^{\eta - 1}det(M)η−1. Because of that,
when `concentration == 1`, we have a uniform distribution over Cholesky
factors of correlation matrices:

```
L ~ LKJCholesky(dim, concentration)
X = L @ L' ~ LKJCorr(dim, concentration)
```

Note that this distribution samples the
Cholesky factor of correlation matrices and not the correlation matrices
themselves and thereby differs slightly from the derivations in [1] for
the LKJCorr distribution. For sampling, this uses the Onion method from
[1] Section 3.

Example:

```
>>> l = LKJCholesky(3, 0.5)
>>> l.sample() # l @ l.T is a sample of a correlation 3x3 matrix
tensor([[ 1.0000, 0.0000, 0.0000],
 [ 0.3516, 0.9361, 0.0000],
 [-0.1899, 0.4748, 0.8593]])
```

Parameters:

- **dimension** (*dim*) - dimension of the matrices
- **concentration** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - concentration/shape parameter of the
distribution (often referred to as eta)

**References**

[1] Generating random correlation matrices based on vines and extended onion method (2009),
Daniel Lewandowski, Dorota Kurowicka, Harry Joe.
Journal of Multivariate Analysis. 100. 10.1016/j.jmva.2009.04.008

arg_constraints*= {'concentration': GreaterThan(lower_bound=0.0)}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lkj_cholesky.py#L93)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lkj_cholesky.py#L126)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lkj_cholesky.py#L105)

support*= CorrCholesky()*

## Laplace

*class*torch.distributions.laplace.Laplace(*loc*, *scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L14)

Bases: `Distribution`

Creates a Laplace distribution parameterized by `loc` and `scale`.

Example:

```
>>> m = Laplace(torch.tensor([0.0]), torch.tensor([1.0]))
>>> m.sample() # Laplace distributed with loc=0, scale=1
tensor([ 0.1046])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - mean of the distribution
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - scale of the distribution

arg_constraints*= {'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L92)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L103)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L64)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L99)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L87)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/laplace.py#L73)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## LogNormal

*class*torch.distributions.log_normal.LogNormal(*loc*, *scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/log_normal.py#L13)

Bases: `TransformedDistribution`

Creates a log-normal distribution parameterized by
`loc` and `scale` where:

```
X ~ Normal(loc, scale)
Y = exp(X) ~ LogNormal(loc, scale)
```

Example:

```
>>> m = LogNormal(torch.tensor([0.0]), torch.tensor([1.0]))
>>> m.sample() # log-normal distributed with mean=0 and stddev=1
tensor([ 0.1046])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - mean of log of distribution
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - standard deviation of log of the distribution

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

base_dist*: Normal*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/log_normal.py#L74)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/log_normal.py#L49)

has_rsample*= True*

*property*loc*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*scale*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThan(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## LowRankMultivariateNormal

*class*torch.distributions.lowrank_multivariate_normal.LowRankMultivariateNormal(*loc*, *cov_factor*, *cov_diag*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lowrank_multivariate_normal.py#L54)

Bases: `Distribution`

Creates a multivariate normal distribution with covariance matrix having a low-rank form
parameterized by `cov_factor` and `cov_diag`:

```
covariance_matrix = cov_factor @ cov_factor.T + cov_diag
```

Example

```
>>> m = LowRankMultivariateNormal(
... torch.zeros(2), torch.tensor([[1.0], [0.0]]), torch.ones(2)
... )
>>> m.sample() # normally distributed with mean=`[0,0]`, cov_factor=`[[1],[0]]`, cov_diag=`[1,1]`
tensor([-0.2102, -0.5429])
```

Parameters:

- **loc** ([*Tensor*](tensors.html#torch.Tensor)) - mean of the distribution with shape batch_shape + event_shape
- **cov_factor** ([*Tensor*](tensors.html#torch.Tensor)) - factor part of low-rank form of covariance matrix with shape
batch_shape + event_shape + (rank,)
- **cov_diag** ([*Tensor*](tensors.html#torch.Tensor)) - diagonal part of low-rank form of covariance matrix with shape
batch_shape + event_shape

Note

The computation for determinant and inverse of covariance matrix is avoided when
cov_factor.shape[1] << cov_factor.shape[0] thanks to [Woodbury matrix identity](https://en.wikipedia.org/wiki/Woodbury_matrix_identity) and
[matrix determinant lemma](https://en.wikipedia.org/wiki/Matrix_determinant_lemma).
Thanks to these formulas, we just need to compute the determinant and inverse of
the small size "capacitance" matrix:

```
capacitance = I + cov_factor.T @ inv(cov_diag) @ cov_factor
```

arg_constraints*= {'cov_diag': IndependentConstraint(GreaterThan(lower_bound=0.0), 1), 'cov_factor': IndependentConstraint(Real(), 2), 'loc': IndependentConstraint(Real(), 1)}*

*property*covariance_matrix*: [Tensor](tensors.html#torch.Tensor)*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lowrank_multivariate_normal.py#L242)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lowrank_multivariate_normal.py#L141)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lowrank_multivariate_normal.py#L225)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*precision_matrix*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/lowrank_multivariate_normal.py#L214)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*scale_tril*: [Tensor](tensors.html#torch.Tensor)*

support*= IndependentConstraint(Real(), 1)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## MixtureSameFamily

*class*torch.distributions.mixture_same_family.MixtureSameFamily(*mixture_distribution*, *component_distribution*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/mixture_same_family.py#L13)

Bases: `Distribution`

The MixtureSameFamily distribution implements a (batch of) mixture
distribution where all components are from different parameterizations of
the same distribution type. It is parameterized by a Categorical
"selecting distribution" (over k components) and a component
distribution, i.e., a Distribution with a rightmost batch shape
(equal to [k]) which indexes each (batch of) component.

Examples:

```
>>> # Construct Gaussian Mixture Model in 1D consisting of 5 equally
>>> # weighted normal distributions
>>> mix = D.Categorical(torch.ones(5,))
>>> comp = D.Normal(torch.randn(5,), torch.rand(5,))
>>> gmm = MixtureSameFamily(mix, comp)

>>> # Construct Gaussian Mixture Model in 2D consisting of 5 equally
>>> # weighted bivariate normal distributions
>>> mix = D.Categorical(torch.ones(5,))
>>> comp = D.Independent(D.Normal(
... torch.randn(5,2), torch.rand(5,2)), 1)
>>> gmm = MixtureSameFamily(mix, comp)

>>> # Construct a batch of 3 Gaussian Mixture Models in 2D each
>>> # consisting of 5 random weighted bivariate normal distributions
>>> mix = D.Categorical(torch.rand(3,5))
>>> comp = D.Independent(D.Normal(
... torch.randn(3,5,2), torch.rand(3,5,2)), 1)
>>> gmm = MixtureSameFamily(mix, comp)
```

Parameters:

- **mixture_distribution** (*Categorical*) - torch.distributions.Categorical-like
instance. Manages the probability of selecting components.
The number of categories must match the rightmost batch
dimension of the component_distribution. Must have either
scalar batch_shape or batch_shape matching
component_distribution.batch_shape[:-1]
- **component_distribution** (*Distribution*) - torch.distributions.Distribution-like
instance. Right-most batch dimension indexes component.

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {}*

cdf(*x*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/mixture_same_family.py#L161)

*property*component_distribution*: Distribution*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/mixture_same_family.py#L111)

has_rsample*= False*

log_prob(*x*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/mixture_same_family.py#L168)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mixture_distribution*: Categorical*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/mixture_same_family.py#L178)

*property*support

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Multinomial

*class*torch.distributions.multinomial.Multinomial(*total_count=1*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multinomial.py#L14)

Bases: `Distribution`

Creates a Multinomial distribution parameterized by `total_count` and
either `probs` or `logits` (but not both). The innermost dimension of
`probs` indexes over categories. All other dimensions index over batches.

Note that `total_count` need not be specified if only `log_prob()` is
called (see example below)

Note

The probs argument must be non-negative, finite and have a non-zero sum,
and it will be normalized to sum to 1 along the last dimension. `probs`
will return this normalized value.
The logits argument will be interpreted as unnormalized log probabilities
and can therefore be any real number. It will likewise be normalized so that
the resulting probabilities sum to 1 along the last dimension. `logits`
will return this normalized value.

- `sample()` requires a single shared total_count for all
parameters and samples.
- `log_prob()` allows different total_count for each parameter and
sample.

Example:

```
>>> m = Multinomial(100, torch.tensor([ 1., 1., 1., 1.]))
>>> x = m.sample() # equal probability of 0, 1, 2, 3
tensor([ 21., 24., 30., 25.])

>>> Multinomial(probs=torch.tensor([1., 1., 1., 1.])).log_prob(x)
tensor([-4.1338])
```

Parameters:

- **total_count** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of trials
- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - event probabilities
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - event log probabilities (unnormalized)

arg_constraints*= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multinomial.py#L126)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multinomial.py#L81)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multinomial.py#L139)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multinomial.py#L112)

*property*support

Return type:

_DependentProperty

total_count*: [int](https://docs.python.org/3/library/functions.html#int)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## MultivariateNormal

*class*torch.distributions.multivariate_normal.MultivariateNormal(*loc*, *covariance_matrix=None*, *precision_matrix=None*, *scale_tril=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multivariate_normal.py#L88)

Bases: `Distribution`

Creates a multivariate normal (also called Gaussian) distribution
parameterized by a mean vector and a covariance matrix.

The multivariate normal distribution can be parameterized either
in terms of a positive definite covariance matrix Σ\mathbf{\Sigma}Σ
or a positive definite precision matrix Σ−1\mathbf{\Sigma}^{-1}Σ−1
or a lower-triangular matrix L\mathbf{L}L with positive-valued
diagonal entries, such that
Σ=LL⊤\mathbf{\Sigma} = \mathbf{L}\mathbf{L}^\topΣ=LL⊤. This triangular matrix
can be obtained via e.g. Cholesky decomposition of the covariance.

Example

```
>>> m = MultivariateNormal(torch.zeros(2), torch.eye(2))
>>> m.sample() # normally distributed with mean=`[0,0]` and covariance_matrix=`I`
tensor([-0.2102, -0.5429])
```

Parameters:

- **loc** ([*Tensor*](tensors.html#torch.Tensor)) - mean of the distribution
- **covariance_matrix** ([*Tensor*](tensors.html#torch.Tensor)) - positive-definite covariance matrix
- **precision_matrix** ([*Tensor*](tensors.html#torch.Tensor)) - positive-definite precision matrix
- **scale_tril** ([*Tensor*](tensors.html#torch.Tensor)) - lower-triangular factor of covariance, with positive-valued diagonal

Note

Only one of `covariance_matrix` or `precision_matrix` or
`scale_tril` can be specified.

Using `scale_tril` will be more efficient: all computations internally
are based on `scale_tril`. If `covariance_matrix` or
`precision_matrix` is passed instead, it is only used to compute
the corresponding lower triangular matrices using a Cholesky decomposition.

arg_constraints*= {'covariance_matrix': PositiveDefinite(), 'loc': IndependentConstraint(Real(), 1), 'precision_matrix': PositiveDefinite(), 'scale_tril': LowerCholesky()}*

*property*covariance_matrix*: [Tensor](tensors.html#torch.Tensor)*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multivariate_normal.py#L266)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multivariate_normal.py#L198)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multivariate_normal.py#L256)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*precision_matrix*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/multivariate_normal.py#L251)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*scale_tril*: [Tensor](tensors.html#torch.Tensor)*

support*= IndependentConstraint(Real(), 1)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## NegativeBinomial

*class*torch.distributions.negative_binomial.NegativeBinomial(*total_count*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/negative_binomial.py#L20)

Bases: `Distribution`

Creates a Negative Binomial distribution, i.e. distribution
of the number of successful independent and identical Bernoulli trials
before `total_count` failures are achieved. The probability
of success of each Bernoulli trial is `probs`.

Parameters:

- **total_count** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - non-negative number of negative Bernoulli
trials to stop, although the distribution is still valid for real
valued count
- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - Event probabilities of success in the half open interval [0, 1)
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - Event log-odds for probabilities of success

arg_constraints*= {'logits': Real(), 'probs': HalfOpenInterval(lower_bound=0.0, upper_bound=1.0), 'total_count': GreaterThanEq(lower_bound=0)}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/negative_binomial.py#L75)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/negative_binomial.py#L130)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/negative_binomial.py#L125)

support*= IntegerGreaterThan(lower_bound=0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Normal

*class*torch.distributions.normal.Normal(*loc*, *scale*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L15)

Bases: `ExponentialFamily`

Creates a normal (also called Gaussian) distribution parameterized by
`loc` and `scale`.

Example:

```
>>> m = Normal(torch.tensor([0.0]), torch.tensor([1.0]))
>>> m.sample() # normally distributed with loc=0 and scale=1
tensor([ 0.1046])
```

Parameters:

- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - mean of the distribution (often referred to as mu)
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - standard deviation of the distribution
(often referred to as sigma)

arg_constraints*= {'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L103)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L113)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L68)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L110)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L87)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L82)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/normal.py#L77)

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## OneHotCategorical

*class*torch.distributions.one_hot_categorical.OneHotCategorical(*probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L14)

Bases: `Distribution`

Creates a one-hot categorical distribution parameterized by `probs` or
`logits`.

Samples are one-hot coded vectors of size `probs.size(-1)`.

Note

The probs argument must be non-negative, finite and have a non-zero sum,
and it will be normalized to sum to 1 along the last dimension. `probs`
will return this normalized value.
The logits argument will be interpreted as unnormalized log probabilities
and can therefore be any real number. It will likewise be normalized so that
the resulting probabilities sum to 1 along the last dimension. `logits`
will return this normalized value.

See also: `torch.distributions.Categorical()` for specifications of
`probs` and `logits`.

Example:

```
>>> m = OneHotCategorical(torch.tensor([ 0.25, 0.25, 0.25, 0.25 ]))
>>> m.sample() # equal probability of 0, 1, 2, 3
tensor([ 0., 0., 0., 1.])
```

Parameters:

- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - event probabilities
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - event log probabilities (unnormalized)

arg_constraints*= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L117)

enumerate_support(*expand=True*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L120)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L61)

has_enumerate_support*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L111)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/one_hot_categorical.py#L104)

support*= OneHot()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Pareto

*class*torch.distributions.pareto.Pareto(*scale*, *alpha*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/pareto.py#L15)

Bases: `TransformedDistribution`

Samples from a Pareto Type 1 distribution.

Example:

```
>>> m = Pareto(torch.tensor([1.0]), torch.tensor([1.0]))
>>> m.sample() # sample from a Pareto distribution with scale=1 and alpha=1
tensor([ 1.5623])
```

Parameters:

- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Scale parameter of the distribution
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Shape parameter of the distribution

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'alpha': GreaterThan(lower_bound=0.0), 'scale': GreaterThan(lower_bound=0.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/pareto.py#L73)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/pareto.py#L45)

Return type:

*Pareto*

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*support*: Constraint*

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Poisson

*class*torch.distributions.poisson.Poisson(*rate*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/poisson.py#L14)

Bases: `ExponentialFamily`

Creates a Poisson distribution parameterized by `rate`, the rate parameter.

Samples are nonnegative integers, with a pmf given by

rateke−ratek!\mathrm{rate}^k \frac{e^{-\mathrm{rate}}}{k!}

ratekk!e−rate​

Example:

```
>>> m = Poisson(torch.tensor([4]))
>>> m.sample()
tensor([ 3.])
```

Parameters:

**rate** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the rate parameter

arg_constraints*= {'rate': GreaterThanEq(lower_bound=0.0)}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/poisson.py#L62)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/poisson.py#L75)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/poisson.py#L70)

support*= IntegerGreaterThan(lower_bound=0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## RelaxedBernoulli

*class*torch.distributions.relaxed_bernoulli.RelaxedBernoulli(*temperature*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L122)

Bases: `TransformedDistribution`

Creates a RelaxedBernoulli distribution, parametrized by
`temperature`, and either `probs` or `logits`
(but not both). This is a relaxed version of the Bernoulli distribution,
so the values are in (0, 1), and has reparametrizable samples.

Example:

```
>>> m = RelaxedBernoulli(torch.tensor([2.2]),
... torch.tensor([0.1, 0.2, 0.3, 0.99]))
>>> m.sample()
tensor([ 0.2951, 0.3442, 0.8918, 0.9021])
```

Parameters:

- **temperature** ([*Tensor*](tensors.html#torch.Tensor)) - relaxation temperature
- **probs** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the probability of sampling 1
- **logits** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the log-odds of sampling 1

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0)}*

base_dist*: LogitRelaxedBernoulli*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L160)

has_rsample*= True*

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

support*= Interval(lower_bound=0.0, upper_bound=1.0)*

*property*temperature*: [Tensor](tensors.html#torch.Tensor)*

## LogitRelaxedBernoulli

*class*torch.distributions.relaxed_bernoulli.LogitRelaxedBernoulli(*temperature*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L22)

Bases: `Distribution`

Creates a LogitRelaxedBernoulli distribution parameterized by `probs`
or `logits` (but not both), which is the logit of a RelaxedBernoulli
distribution.

Samples are logits of values in (0, 1). See [1] for more details.

Parameters:

- **temperature** ([*Tensor*](tensors.html#torch.Tensor)) - relaxation temperature
- **probs** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the probability of sampling 1
- **logits** (*Number**,*[*Tensor*](tensors.html#torch.Tensor)) - the log-odds of sampling 1

[1] The Concrete Distribution: A Continuous Relaxation of Discrete Random
Variables (Maddison et al., 2017)

[2] Categorical Reparametrization with Gumbel-Softmax
(Jang et al., 2017)

arg_constraints*= {'logits': Real(), 'probs': Interval(lower_bound=0.0, upper_bound=1.0)}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L75)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L114)

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*param_shape*: [Size](size.html#torch.Size)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_bernoulli.py#L104)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= Real()*

## RelaxedOneHotCategorical

*class*torch.distributions.relaxed_categorical.RelaxedOneHotCategorical(*temperature*, *probs=None*, *logits=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_categorical.py#L109)

Bases: `TransformedDistribution`

Creates a RelaxedOneHotCategorical distribution parametrized by
`temperature`, and either `probs` or `logits`.
This is a relaxed version of the `OneHotCategorical` distribution, so
its samples are on simplex, and are reparametrizable.

Example:

```
>>> m = RelaxedOneHotCategorical(torch.tensor([2.2]),
... torch.tensor([0.1, 0.2, 0.3, 0.4]))
>>> m.sample()
tensor([ 0.1294, 0.2324, 0.3859, 0.2523])
```

Parameters:

- **temperature** ([*Tensor*](tensors.html#torch.Tensor)) - relaxation temperature
- **probs** ([*Tensor*](tensors.html#torch.Tensor)) - event probabilities
- **logits** ([*Tensor*](tensors.html#torch.Tensor)) - unnormalized log probability for each event

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'logits': IndependentConstraint(Real(), 1), 'probs': Simplex()}*

base_dist*: ExpRelaxedCategorical*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/relaxed_categorical.py#L149)

has_rsample*= True*

*property*logits*: [Tensor](tensors.html#torch.Tensor)*

*property*probs*: [Tensor](tensors.html#torch.Tensor)*

support*= Simplex()*

*property*temperature*: [Tensor](tensors.html#torch.Tensor)*

## StudentT

*class*torch.distributions.studentT.StudentT(*df*, *loc=0.0*, *scale=1.0*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/studentT.py#L15)

Bases: `Distribution`

Creates a Student's t-distribution parameterized by degree of
freedom `df`, mean `loc` and scale `scale`.

Example:

```
>>> m = StudentT(torch.tensor([2.0]))
>>> m.sample() # Student's t-distributed with degrees of freedom=2
tensor([ 0.1046])
```

Parameters:

- **df** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - degrees of freedom
- **loc** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - mean of the distribution
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - scale of the distribution

arg_constraints*= {'df': GreaterThan(lower_bound=0.0), 'loc': Real(), 'scale': GreaterThan(lower_bound=0.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/studentT.py#L114)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/studentT.py#L76)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/studentT.py#L101)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/studentT.py#L87)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## TransformedDistribution

*class*torch.distributions.transformed_distribution.TransformedDistribution(*base_distribution*, *transforms*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L16)

Bases: `Distribution`

Extension of the Distribution class, which applies a sequence of Transforms
to a base distribution. Let f be the composition of transforms applied:

```
X ~ BaseDistribution
Y = f(X) ~ TransformedDistribution(BaseDistribution, f)
log p(Y) = log p(X) + log |det (dX/dY)|
```

Note that the `.event_shape` of a `TransformedDistribution` is the
maximum shape of its base distribution and its transforms, since transforms
can introduce correlations among events.

An example for the usage of `TransformedDistribution` would be:

```
# Building a Logistic Distribution
# X ~ Uniform(0, 1)
# f = a + b * logit(X)
# Y ~ f(X) ~ Logistic(a, b)
base_distribution = Uniform(0, 1)
transforms = [SigmoidTransform().inv, AffineTransform(loc=a, scale=b)]
logistic = TransformedDistribution(base_distribution, transforms)
```

For more examples, please look at the implementations of
`Gumbel`,
`HalfCauchy`,
`HalfNormal`,
`LogNormal`,
`Pareto`,
`Weibull`,
`RelaxedBernoulli` and
`RelaxedOneHotCategorical`

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {}*

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L204)

Computes the cumulative distribution function by inverting the
transform(s) and computing the score of the base distribution.

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L112)

*property*has_rsample*: [bool](https://docs.python.org/3/library/functions.html#bool)*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L217)

Computes the inverse cumulative distribution function using
transform(s) and computing the score of the base distribution.

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L168)

Scores the sample by inverting the transform(s) and computing the score
using the score of the base distribution and the log abs det jacobian.

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L156)

Generates a sample_shape shaped reparameterized sample or sample_shape
shaped batch of reparameterized samples if the distribution parameters
are batched. Samples first from base distribution and applies
transform() for every transform in the list.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transformed_distribution.py#L143)

Generates a sample_shape shaped sample or sample_shape shaped batch of
samples if the distribution parameters are batched. Samples first from
base distribution and applies transform() for every transform in the
list.

*property*support

Return type:

_DependentProperty

## Uniform

*class*torch.distributions.uniform.Uniform(*low*, *high*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L14)

Bases: `Distribution`

Generates uniformly distributed random samples from the half-open interval
`[low, high)`.

Example:

```
>>> m = Uniform(torch.tensor([0.0]), torch.tensor([5.0]))
>>> m.sample() # uniformly distributed in the range [0.0, 5.0)
tensor([ 2.3418])
```

Parameters:

- **low** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - lower range (inclusive).
- **high** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - upper range (exclusive).

*property*arg_constraints

cdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L97)

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L107)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L71)

has_rsample*= True*

icdf(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L103)

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L90)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/uniform.py#L85)

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*stddev*: [Tensor](tensors.html#torch.Tensor)*

*property*support

Return type:

_DependentProperty

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## VonMises

*class*torch.distributions.von_mises.VonMises(*loc*, *concentration*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/von_mises.py#L110)

Bases: `Distribution`

A circular von Mises distribution.

This implementation uses polar coordinates. The `loc` and `value` args
can be any real number (to facilitate unconstrained optimization), but are
interpreted as angles modulo 2 pi.

Example::

```
>>> m = VonMises(torch.tensor([1.0]), torch.tensor([1.0]))
>>> m.sample() # von Mises distributed with loc=1 and concentration=1
tensor([1.9777])
```

Parameters:

- **loc** ([*torch.Tensor*](tensors.html#torch.Tensor)) - an angle in radians.
- **concentration** ([*torch.Tensor*](tensors.html#torch.Tensor)) - concentration parameter

arg_constraints*= {'concentration': GreaterThan(lower_bound=0.0), 'loc': Real()}*

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/von_mises.py#L190)

has_rsample*= False*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/von_mises.py#L144)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

The provided mean is the circular one.

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

sample(*sample_shape=()*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/von_mises.py#L173)

The sampling algorithm for the von Mises distribution is based on the
following paper: D.J. Best and N.I. Fisher, "Efficient simulation of the
von Mises distribution." Applied Statistics (1979): 152-157.

Sampling is always done in double precision internally to avoid a hang
in _rejection_sample() for small values of the concentration, which
starts to happen for single precision around 1e-4 (see issue #88443).

support*= Real()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

The provided variance is the circular one.

## Weibull

*class*torch.distributions.weibull.Weibull(*scale*, *concentration*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/weibull.py#L16)

Bases: `TransformedDistribution`

Samples from a two-parameter Weibull distribution.

Example

```
>>> m = Weibull(torch.tensor([1.0]), torch.tensor([1.0]))
>>> m.sample() # sample from a Weibull distribution with scale=1, concentration=1
tensor([ 0.4784])
```

Parameters:

- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Scale parameter of distribution (lambda).
- **concentration** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - Concentration parameter of distribution (k/shape).
- **validate_args** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to validate arguments. Default: None.

arg_constraints*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Constraint]**= {'concentration': GreaterThan(lower_bound=0.0), 'scale': GreaterThan(lower_bound=0.0)}*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/weibull.py#L91)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/weibull.py#L58)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

support*= GreaterThan(lower_bound=0.0)*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## Wishart

*class*torch.distributions.wishart.Wishart(*df*, *covariance_matrix=None*, *precision_matrix=None*, *scale_tril=None*, *validate_args=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/wishart.py#L33)

Bases: `ExponentialFamily`

Creates a Wishart distribution parameterized by a symmetric positive definite matrix Σ\SigmaΣ,
or its Cholesky decomposition Σ=LL⊤\mathbf{\Sigma} = \mathbf{L}\mathbf{L}^\topΣ=LL⊤

Example

```
>>> m = Wishart(torch.Tensor([2]), covariance_matrix=torch.eye(2))
>>> m.sample() # Wishart distributed with mean=`df * I` and
>>> # variance(x_ij)=`df` for i != j and variance(x_ij)=`2 * df` for i == j
```

Parameters:

- **df** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](tensors.html#torch.Tensor)) - real-valued parameter larger than the (dimension of Square matrix) - 1
- **covariance_matrix** ([*Tensor*](tensors.html#torch.Tensor)) - positive-definite covariance matrix
- **precision_matrix** ([*Tensor*](tensors.html#torch.Tensor)) - positive-definite precision matrix
- **scale_tril** ([*Tensor*](tensors.html#torch.Tensor)) - lower-triangular factor of covariance, with positive-valued diagonal

Note

Only one of `covariance_matrix` or `precision_matrix` or
`scale_tril` can be specified.
Using `scale_tril` will be more efficient: all computations internally
are based on `scale_tril`. If `covariance_matrix` or
`precision_matrix` is passed instead, it is only used to compute
the corresponding lower triangular matrices using a Cholesky decomposition.
'torch.distributions.LKJCholesky' is a restricted Wishart distribution.[1]

**References**

[1] Wang, Z., Wu, Y. and Chu, H., 2018. On equivalence of the LKJ distribution and the restricted Wishart distribution.
[2] Sawyer, S., 2007. Wishart Distributions and Inverse-Wishart Sampling.
[3] Anderson, T. W., 2003. An Introduction to Multivariate Statistical Analysis (3rd ed.).
[4] Odell, P. L. & Feiveson, A. H., 1966. A Numerical Procedure to Generate a Sample Covariance Matrix. JASA, 61(313):199-203.
[5] Ku, Y.-C. & Bloomfield, P., 2010. Generating Random Wishart Matrices with Fractional Degrees of Freedom in OX.

*property*arg_constraints

*property*covariance_matrix*: [Tensor](tensors.html#torch.Tensor)*

entropy()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/wishart.py#L324)

expand(*batch_shape*, *_instance=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/wishart.py#L160)

has_rsample*= True*

log_prob(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/wishart.py#L303)

*property*mean*: [Tensor](tensors.html#torch.Tensor)*

*property*mode*: [Tensor](tensors.html#torch.Tensor)*

*property*precision_matrix*: [Tensor](tensors.html#torch.Tensor)*

rsample(*sample_shape=()*, *max_try_correction=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/wishart.py#L251)

Warning

In some cases, sampling algorithm based on Bartlett decomposition may return singular matrix samples.
Several tries to correct singular samples are performed by default, but it may end up returning
singular matrix samples. Singular samples may return -inf values in .log_prob().
In those cases, the user should validate the samples and either fix the value of df
or adjust max_try_correction value for argument in .rsample accordingly.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

*property*scale_tril*: [Tensor](tensors.html#torch.Tensor)*

support*= PositiveDefinite()*

*property*variance*: [Tensor](tensors.html#torch.Tensor)*

## `KL Divergence`

torch.distributions.kl.kl_divergence(*p*, *q*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/kl.py#L165)

Compute Kullback-Leibler divergence KL(p∥q)KL(p \| q)KL(p∥q) between two distributions.

KL(p∥q)=∫p(x)log⁡p(x)q(x) dxKL(p \| q) = \int p(x) \log\frac {p(x)} {q(x)} \,dxKL(p∥q)=∫p(x)logq(x)p(x)​dx
Parameters:

- **p** (*Distribution*) - A `Distribution` object.
- **q** (*Distribution*) - A `Distribution` object.

Returns:

A batch of KL divergences of shape batch_shape.

Return type:

[Tensor](tensors.html#torch.Tensor)

Raises:

[**NotImplementedError**](https://docs.python.org/3/library/exceptions.html#NotImplementedError) - If the distribution types have not been registered via
 `register_kl()`.

KL divergence is currently implemented for the following distribution pairs:

- `Bernoulli` and `Bernoulli`
- `Bernoulli` and `Poisson`
- `Beta` and `Beta`
- `Beta` and `ContinuousBernoulli`
- `Beta` and `Exponential`
- `Beta` and `Gamma`
- `Beta` and `Normal`
- `Beta` and `Pareto`
- `Beta` and `Uniform`
- `Binomial` and `Binomial`
- `Categorical` and `Categorical`
- `Cauchy` and `Cauchy`
- `ContinuousBernoulli` and `ContinuousBernoulli`
- `ContinuousBernoulli` and `Exponential`
- `ContinuousBernoulli` and `Normal`
- `ContinuousBernoulli` and `Pareto`
- `ContinuousBernoulli` and `Uniform`
- `Dirichlet` and `Dirichlet`
- `Exponential` and `Beta`
- `Exponential` and `ContinuousBernoulli`
- `Exponential` and `Exponential`
- `Exponential` and `Gamma`
- `Exponential` and `Gumbel`
- `Exponential` and `Normal`
- `Exponential` and `Pareto`
- `Exponential` and `Uniform`
- `ExponentialFamily` and `ExponentialFamily`
- `Gamma` and `Beta`
- `Gamma` and `ContinuousBernoulli`
- `Gamma` and `Exponential`
- `Gamma` and `Gamma`
- `Gamma` and `Gumbel`
- `Gamma` and `Normal`
- `Gamma` and `Pareto`
- `Gamma` and `Uniform`
- `Geometric` and `Geometric`
- `Gumbel` and `Beta`
- `Gumbel` and `ContinuousBernoulli`
- `Gumbel` and `Exponential`
- `Gumbel` and `Gamma`
- `Gumbel` and `Gumbel`
- `Gumbel` and `Normal`
- `Gumbel` and `Pareto`
- `Gumbel` and `Uniform`
- `HalfNormal` and `HalfNormal`
- `Independent` and `Independent`
- `Laplace` and `Beta`
- `Laplace` and `ContinuousBernoulli`
- `Laplace` and `Exponential`
- `Laplace` and `Gamma`
- `Laplace` and `Laplace`
- `Laplace` and `Normal`
- `Laplace` and `Pareto`
- `Laplace` and `Uniform`
- `LowRankMultivariateNormal` and `LowRankMultivariateNormal`
- `LowRankMultivariateNormal` and `MultivariateNormal`
- `MultivariateNormal` and `LowRankMultivariateNormal`
- `MultivariateNormal` and `MultivariateNormal`
- `Normal` and `Beta`
- `Normal` and `ContinuousBernoulli`
- `Normal` and `Exponential`
- `Normal` and `Gamma`
- `Normal` and `Gumbel`
- `Normal` and `Laplace`
- `Normal` and `Normal`
- `Normal` and `Pareto`
- `Normal` and `Uniform`
- `OneHotCategorical` and `OneHotCategorical`
- `Pareto` and `Beta`
- `Pareto` and `ContinuousBernoulli`
- `Pareto` and `Exponential`
- `Pareto` and `Gamma`
- `Pareto` and `Normal`
- `Pareto` and `Pareto`
- `Pareto` and `Uniform`
- `Poisson` and `Bernoulli`
- `Poisson` and `Binomial`
- `Poisson` and `Poisson`
- `TransformedDistribution` and `TransformedDistribution`
- `Uniform` and `Beta`
- `Uniform` and `ContinuousBernoulli`
- `Uniform` and `Exponential`
- `Uniform` and `Gamma`
- `Uniform` and `Gumbel`
- `Uniform` and `Normal`
- `Uniform` and `Pareto`
- `Uniform` and `Uniform`

torch.distributions.kl.register_kl(*type_p*, *type_q*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/kl.py#L51)

Decorator to register a pairwise function with `kl_divergence()`.
Usage:

```
@register_kl(Normal, Normal)
def kl_normal_normal(p, q):
 # insert implementation here
```

Lookup returns the most specific (type,type) match ordered by subclass. If
the match is ambiguous, a RuntimeWarning is raised. For example to
resolve the ambiguous situation:

```
@register_kl(BaseP, DerivedQ)
def kl_version1(p, q): ...
@register_kl(DerivedP, BaseQ)
def kl_version2(p, q): ...
```

you should register a third most-specific implementation, e.g.:

```
register_kl(DerivedP, DerivedQ)(kl_version1) # Break the tie.
```

Parameters:

- **type_p** ([*type*](https://docs.python.org/3/library/functions.html#type)) - A subclass of `Distribution`.
- **type_q** ([*type*](https://docs.python.org/3/library/functions.html#type)) - A subclass of `Distribution`.

## `Transforms`

*class*torch.distributions.transforms.AbsTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L736)

Transform via the mapping y=∣x∣y = |x|y=∣x∣.

*class*torch.distributions.transforms.AffineTransform(*loc*, *scale*, *event_dim=0*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L752)

Transform via the pointwise affine mapping y=loc+scale×xy = \text{loc} + \text{scale} \times xy=loc+scale×x.

Parameters:

- **loc** ([*Tensor*](tensors.html#torch.Tensor)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - Location parameter.
- **scale** ([*Tensor*](tensors.html#torch.Tensor)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - Scale parameter.
- **event_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Optional size of event_shape. This should be zero
for univariate random variables, 1 for distributions over vectors,
2 for distributions over matrices, etc.

*class*torch.distributions.transforms.CatTransform(*tseq*, *dim=0*, *lengths=None*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L1076)

Transform functor that applies a sequence of transforms tseq
component-wise to each submatrix at dim, of length lengths[dim],
in a way compatible with [`torch.cat()`](generated/torch.cat.html#torch.cat).

Example:

```
x0 = torch.cat([torch.range(1, 10), torch.range(1, 10)], dim=0)
x = torch.cat([x0, x0], dim=0)
t0 = CatTransform([ExpTransform(), identity_transform], dim=0, lengths=[10, 10])
t = CatTransform([t0, t0], dim=0, lengths=[20, 20])
y = t(x)
```

*class*torch.distributions.transforms.ComposeTransform(*parts*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L286)

Composes multiple transforms in a chain.
The transforms being composed are responsible for caching.

Parameters:

- **parts** (list of `Transform`) - A list of transforms to compose.
- **cache_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Size of cache. If zero, no caching is done. If one,
the latest single value is cached. Only 0 and 1 are supported.

*class*torch.distributions.transforms.CorrCholeskyTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L859)

Transforms an unconstrained real vector xxx with length D∗(D−1)/2D*(D-1)/2D∗(D−1)/2 into the
Cholesky factor of a D-dimension correlation matrix. This Cholesky factor is a lower
triangular matrix with positive diagonals and unit Euclidean norm for each row.
The transform is processed as follows:

> 1. First we convert x into a lower triangular matrix in row order.
> 2. For each row XiX_iXi​ of the lower triangular part, we apply a *signed* version of
> class `StickBreakingTransform` to transform XiX_iXi​ into a
> unit Euclidean length vector using the following steps:
> - Scales into the interval (−1,1)(-1, 1)(−1,1) domain: ri=tanh⁡(Xi)r_i = \tanh(X_i)ri​=tanh(Xi​).
> - Transforms into an unsigned domain: zi=ri2z_i = r_i^2zi​=ri2​.
> - Applies si=StickBreakingTransform(zi)s_i = StickBreakingTransform(z_i)si​=StickBreakingTransform(zi​).
> - Transforms back into signed domain: yi=sign(ri)∗siy_i = sign(r_i) * \sqrt{s_i}yi​=sign(ri​)∗si​​.

*class*torch.distributions.transforms.CumulativeDistributionTransform(*distribution*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L1319)

Transform via the cumulative distribution function of a probability distribution.

Parameters:

**distribution** (*Distribution*) - Distribution whose cumulative distribution function to use for
the transformation.

Example:

```
# Construct a Gaussian copula from a multivariate normal.
base_dist = MultivariateNormal(
 loc=torch.zeros(2),
 scale_tril=LKJCholesky(2).sample(),
)
transform = CumulativeDistributionTransform(Normal(0, 1))
copula = TransformedDistribution(base_dist, [transform])
```

*class*torch.distributions.transforms.ExpTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L571)

Transform via the mapping y=exp⁡(x)y = \exp(x)y=exp(x).

*class*torch.distributions.transforms.IndependentTransform(*base_transform*, *reinterpreted_batch_ndims*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L417)

Wrapper around another transform to treat
`reinterpreted_batch_ndims`-many extra of the right most dimensions as
dependent. This has no effect on the forward or backward transforms, but
does sum out `reinterpreted_batch_ndims`-many of the rightmost dimensions
in `log_abs_det_jacobian()`.

Parameters:

- **base_transform** (`Transform`) - A base transform.
- **reinterpreted_batch_ndims** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of extra rightmost
dimensions to treat as dependent.

*class*torch.distributions.transforms.LowerCholeskyTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L1034)

Transform from unconstrained matrices to lower-triangular matrices with
nonnegative diagonal entries.

This is useful for parameterizing positive definite matrices in terms of
their Cholesky factorization.

*class*torch.distributions.transforms.PositiveDefiniteTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L1056)

Transform from unconstrained matrices to positive-definite matrices.

*class*torch.distributions.transforms.PowerTransform(*exponent*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L594)

Transform via the mapping y=xexponenty = x^{\text{exponent}}y=xexponent.

*class*torch.distributions.transforms.ReshapeTransform(*in_shape*, *out_shape*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L495)

Unit Jacobian transform to reshape the rightmost part of a tensor.

Note that `in_shape` and `out_shape` must have the same number of
elements, just as for [`torch.Tensor.reshape()`](generated/torch.Tensor.reshape.html#torch.Tensor.reshape).

Parameters:

- **in_shape** ([*torch.Size*](size.html#torch.Size)) - The input event shape.
- **out_shape** ([*torch.Size*](size.html#torch.Size)) - The output event shape.
- **cache_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Size of cache. If zero, no caching is done. If one,
the latest single value is cached. Only 0 and 1 are supported. (Default 0.)

*class*torch.distributions.transforms.SigmoidTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L642)

Transform via the mapping y=11+exp⁡(−x)y = \frac{1}{1 + \exp(-x)}y=1+exp(−x)1​ and x=logit(y)x = \text{logit}(y)x=logit(y).

*class*torch.distributions.transforms.SoftplusTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L667)

Transform via the mapping Softplus(x)=log⁡(1+exp⁡(x))\text{Softplus}(x) = \log(1 + \exp(x))Softplus(x)=log(1+exp(x)).
The implementation reverts to the linear function when x>20x > 20x>20.

*class*torch.distributions.transforms.TanhTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L691)

Transform via the mapping y=tanh⁡(x)y = \tanh(x)y=tanh(x).

It is equivalent to

```
ComposeTransform(
 [
 AffineTransform(0.0, 2.0),
 SigmoidTransform(),
 AffineTransform(-1.0, 2.0),
 ]
)
```

However this might not be numerically stable, thus it is recommended to use TanhTransform
instead.

Note that one should use cache_size=1 when it comes to NaN/Inf values.

*class*torch.distributions.transforms.SoftmaxTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L942)

Transform from unconstrained space to the simplex via y=exp⁡(x)y = \exp(x)y=exp(x) then
normalizing.

This is not bijective and cannot be used for HMC. However this acts mostly
coordinate-wise (except for the final normalization), and thus is
appropriate for coordinate-wise optimization algorithms.

*class*torch.distributions.transforms.StackTransform(*tseq*, *dim=0*, *cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L1218)

Transform functor that applies a sequence of transforms tseq
component-wise to each submatrix at dim
in a way compatible with [`torch.stack()`](generated/torch.stack.html#torch.stack).

Example:

```
x = torch.stack([torch.range(1, 10), torch.range(1, 10)], dim=1)
t = StackTransform([ExpTransform(), identity_transform], dim=1)
y = t(x)
```

*class*torch.distributions.transforms.StickBreakingTransform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L978)

Transform from unconstrained space to the simplex of one additional
dimension via a stick-breaking process.

This transform arises as an iterated sigmoid transform in a stick-breaking
construction of the Dirichlet distribution: the first logit is
transformed via sigmoid to the first probability and the probability of
everything else, and then the process recurses.

This is bijective and appropriate for use in HMC; however it mixes
coordinates together and is less appropriate for optimization.

*class*torch.distributions.transforms.Transform(*cache_size=0*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L47)

Abstract class for invertible transformations with computable log
det jacobians. They are primarily used in
`torch.distributions.TransformedDistribution`.

Caching is useful for transforms whose inverses are either expensive or
numerically unstable. Note that care must be taken with memoized values
since the autograd graph may be reversed. For example while the following
works with or without caching:

```
y = t(x)
t.log_abs_det_jacobian(x, y).backward() # x will receive gradients.
```

However the following will error when caching due to dependency reversal:

```
y = t(x)
z = t.inv(y)
grad(z.sum(), [y]) # error because z is x
```

Derived classes should implement one or both of `_call()` or
`_inverse()`. Derived classes that set bijective=True should also
implement `log_abs_det_jacobian()`.

Parameters:

**cache_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Size of cache. If zero, no caching is done. If one,
the latest single value is cached. Only 0 and 1 are supported.

Variables:

- **domain** (`Constraint`) - The constraint representing valid inputs to this transform.
- **codomain** (`Constraint`) - The constraint representing valid outputs to this transform
which are inputs to the inverse transform.
- **bijective** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether this transform is bijective. A transform
`t` is bijective iff `t.inv(t(x)) == x` and
`t(t.inv(y)) == y` for every `x` in the domain and `y` in
the codomain. Transforms that are not bijective should at least
maintain the weaker pseudoinverse properties
`t(t.inv(t(x)) == t(x)` and `t.inv(t(t.inv(y))) == t.inv(y)`.
- **sign** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*Tensor*](tensors.html#torch.Tensor)) - For bijective univariate transforms, this
should be +1 or -1 depending on whether transform is monotone
increasing or decreasing.

*property*inv*: Transform*

Returns the inverse `Transform` of this transform.
This should satisfy `t.inv.inv is t`.

*property*sign*: [int](https://docs.python.org/3/library/functions.html#int)*

Returns the sign of the determinant of the Jacobian, if applicable.
In general this only makes sense for bijective transforms.

log_abs_det_jacobian(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L190)

Computes the log det jacobian log |dy/dx| given input and output.

forward_shape(*shape*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L199)

Infers the shape of the forward computation, given the input shape.
Defaults to preserving shape.

inverse_shape(*shape*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/transforms.py#L206)

Infers the shapes of the inverse computation, given the output shape.
Defaults to preserving shape.

| [`identity_transform`](generated/torch.distributions.transforms.identity_transform.html#torch.distributions.transforms.identity_transform) | Composes multiple transforms in a chain. |
| --- | --- |

## `Constraints`

*class*torch.distributions.constraints.Constraint[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L80)

Abstract base class for constraints.

A constraint object represents a region over which a variable is valid,
e.g. within which a variable can be optimized.

Variables:

- **is_discrete** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether constrained space is discrete.
Defaults to False.
- **event_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of rightmost dimensions that together define
an event. The `check()` method will remove this many dimensions
when computing validity.

check(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L98)

Returns a byte tensor of `sample_shape + batch_shape` indicating
whether each event in value satisfies this constraint.

torch.distributions.constraints.cat[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L653)

alias of `_Cat`

torch.distributions.constraints.dependent_property[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L182)

alias of `_DependentProperty`

torch.distributions.constraints.greater_than[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L428)

alias of `_GreaterThan`

torch.distributions.constraints.greater_than_eq[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L446)

alias of `_GreaterThanEq`

torch.distributions.constraints.independent[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L231)

alias of `_IndependentConstraint`

torch.distributions.constraints.integer_interval[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L354)

alias of `_IntegerInterval`

torch.distributions.constraints.interval[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L482)

alias of `_Interval`

torch.distributions.constraints.half_open_interval[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L503)

alias of `_HalfOpenInterval`

torch.distributions.constraints.is_dependent(*constraint*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L156)

Checks if `constraint` is a `_Dependent` object.

Parameters:

**constraint** - A `Constraint` object.

Returns:

True if `constraint` can be refined to the type `_Dependent`, False otherwise.

Return type:

`bool`

Examples

```
>>> import torch
>>> from torch.distributions import Bernoulli
>>> from torch.distributions.constraints import is_dependent
```

```
>>> dist = Bernoulli(probs=torch.tensor([0.6], requires_grad=True))
>>> constraint1 = dist.arg_constraints["probs"]
>>> constraint2 = dist.arg_constraints["logits"]
```

```
>>> for constraint in [constraint1, constraint2]:
>>> if is_dependent(constraint):
>>> continue
```

torch.distributions.constraints.less_than[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L464)

alias of `_LessThan`

*class*torch.distributions.constraints.MixtureSameFamilyConstraint(*base_constraint*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L280)

Constraint for the `MixtureSameFamily`
distribution that adds back the rightmost batch dimension before
performing the validity check with the component distribution
constraint.

Parameters:

**base_constraint** - The `Constraint` object of
the component distribution of
the `MixtureSameFamily` distribution.

check(*value*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L309)

Check validity of `value` as a possible outcome of sampling
the `MixtureSameFamily` distribution.

torch.distributions.constraints.multinomial[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L536)

alias of `_Multinomial`

torch.distributions.constraints.stack[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraints.py#L696)

alias of `_Stack`

| [`dependent`](generated/torch.distributions.constraints.dependent.html#torch.distributions.constraints.dependent) | Placeholder for variables whose support depends on other variables. |
| --- | --- |

## `Constraint Registry`

PyTorch provides two global `ConstraintRegistry` objects that link
`Constraint` objects to
`Transform` objects. These objects both
input constraints and return transforms, but they have different guarantees on
bijectivity.

1. `biject_to(constraint)` looks up a bijective
`Transform` from `constraints.real`
to the given `constraint`. The returned transform is guaranteed to have
`.bijective = True` and should implement `.log_abs_det_jacobian()`.
2. `transform_to(constraint)` looks up a not-necessarily bijective
`Transform` from `constraints.real`
to the given `constraint`. The returned transform is not guaranteed to
implement `.log_abs_det_jacobian()`.

The `transform_to()` registry is useful for performing unconstrained
optimization on constrained parameters of probability distributions, which are
indicated by each distribution's `.arg_constraints` dict. These transforms often
overparameterize a space in order to avoid rotation; they are thus more
suitable for coordinate-wise optimization algorithms like Adam:

```
loc = torch.zeros(100, requires_grad=True)
unconstrained = torch.zeros(100, requires_grad=True)
scale = transform_to(Normal.arg_constraints["scale"])(unconstrained)
loss = -Normal(loc, scale).log_prob(data).sum()
```

The `biject_to()` registry is useful for Hamiltonian Monte Carlo, where
samples from a probability distribution with constrained `.support` are
propagated in an unconstrained space, and algorithms are typically rotation
invariant.:

```
dist = Exponential(rate)
unconstrained = torch.zeros(100, requires_grad=True)
sample = biject_to(dist.support)(unconstrained)
potential_energy = -dist.log_prob(sample).sum()
```

Note

An example where `transform_to` and `biject_to` differ is
`constraints.simplex`: `transform_to(constraints.simplex)` returns a
`SoftmaxTransform` that simply
exponentiates and normalizes its inputs; this is a cheap and mostly
coordinate-wise operation appropriate for algorithms like SVI. In
contrast, `biject_to(constraints.simplex)` returns a
`StickBreakingTransform` that
bijects its input down to a one-fewer-dimensional space; this a more
expensive less numerically stable transform but is needed for algorithms
like HMC.

The `biject_to` and `transform_to` objects can be extended by user-defined
constraints and transforms using their `.register()` method either as a
function on singleton constraints:

```
transform_to.register(my_constraint, my_transform)
```

or as a decorator on parameterized constraints:

```
@transform_to.register(MyConstraintClass)
def my_factory(constraint):
 assert isinstance(constraint, MyConstraintClass)
 return MyTransform(constraint.param1, constraint.param2)
```

You can create your own registry by creating a new `ConstraintRegistry`
object.

*class*torch.distributions.constraint_registry.ConstraintRegistry[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraint_registry.py#L80)

Registry to link constraints to transforms.

register(*constraint*, *factory=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/distributions/constraint_registry.py#L89)

Registers a `Constraint`
subclass in this registry. Usage:

```
@my_registry.register(MyConstraintClass)
def construct_transform(constraint):
 assert isinstance(constraint, MyConstraint)
 return MyTransform(constraint.arg_constraints)
```

Parameters:

- **constraint** (subclass of `Constraint`) - A subclass of `Constraint`, or
a singleton object of the desired class.
- **factory** (*Callable*) - A callable that inputs a constraint object and returns
a `Transform` object.

| [`biject_to`](generated/torch.distributions.constraint_registry.biject_to.html#torch.distributions.constraint_registry.biject_to) | Registry to link constraints to transforms. |
| --- | --- |
| [`transform_to`](generated/torch.distributions.constraint_registry.transform_to.html#torch.distributions.constraint_registry.transform_to) | Registry to link constraints to transforms. |

| [`broadcast_all`](generated/torch.distributions.utils.broadcast_all.html#torch.distributions.utils.broadcast_all) | Given a list of values (possibly containing numbers), returns a list where each value is broadcasted based on the following rules: |
| --- | --- |
| [`clamp_probs`](generated/torch.distributions.utils.clamp_probs.html#torch.distributions.utils.clamp_probs) | Clamps the probabilities to be in the open interval (0, 1). |
| [`logits_to_probs`](generated/torch.distributions.utils.logits_to_probs.html#torch.distributions.utils.logits_to_probs) | Converts a tensor of logits into probabilities. |
| [`probs_to_logits`](generated/torch.distributions.utils.probs_to_logits.html#torch.distributions.utils.probs_to_logits) | Converts a tensor of probabilities into logits. |
| [`tril_matrix_to_vec`](generated/torch.distributions.utils.tril_matrix_to_vec.html#torch.distributions.utils.tril_matrix_to_vec) | Convert a D x D matrix or a batch of matrices into a (batched) vector which comprises of lower triangular elements from the matrix in row order. |
| [`vec_to_tril_matrix`](generated/torch.distributions.utils.vec_to_tril_matrix.html#torch.distributions.utils.vec_to_tril_matrix) | Convert a vector or a batch of vectors into a batched D x D lower triangular matrix containing elements from the vector in row order. |