# torch.distributions.transforms.identity_transform

torch.distributions.transforms.identity_transform*= ComposeTransform( )*

Composes multiple transforms in a chain.
The transforms being composed are responsible for caching.

Parameters:

- **parts** (list of [`Transform`](../distributions.html#torch.distributions.transforms.Transform)) - A list of transforms to compose.
- **cache_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Size of cache. If zero, no caching is done. If one,
the latest single value is cached. Only 0 and 1 are supported.