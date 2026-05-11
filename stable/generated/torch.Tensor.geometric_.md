# torch.Tensor.geometric_

Tensor.geometric_(*p*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with elements drawn from the geometric distribution:

P(X=k)=(1−p)k−1p,k=1,2,...P(X=k) = (1 - p)^{k - 1} p, k = 1, 2, ...P(X=k)=(1−p)k−1p,k=1,2,...

Note

`torch.Tensor.geometric_()` k-th trial is the first success hence draws samples in {1,2,...}\{1, 2, \ldots\}{1,2,...}, whereas
[`torch.distributions.geometric.Geometric()`](../distributions.html#torch.distributions.geometric.Geometric) (k+1)(k+1)(k+1)-th trial is the first success
hence draws samples in {0,1,...}\{0, 1, \ldots\}{0,1,...}.