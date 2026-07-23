# PairwiseDistance

*class*torch.nn.modules.distance.PairwiseDistance(*p=2.0*, *eps=1e-06*, *keepdim=False*)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/nn/modules/distance.py#L10)

Computes the pairwise distance between input vectors, or between columns of input matrices.

Distances are computed using `p`-norm, with constant `eps` added to avoid division by zero
if `p` is negative, i.e.:

dist(x,y)=∥x−y+ϵe∥p,\mathrm{dist}\left(x, y\right) = \left\Vert x-y + \epsilon e \right\Vert_p,

dist(x,y)=∥x−y+ϵe∥p​,

where eee is the vector of ones and the `p`-norm is given by.

∥x∥p=(∑i=1n∣xi∣p)1/p.\Vert x \Vert _p = \left( \sum_{i=1}^n \vert x_i \vert ^ p \right) ^ {1/p}.

∥x∥p​=(i=1∑n​∣xi​∣p)1/p.
Parameters:

- **p** (*real**,**optional*) - the norm degree. Can be negative. Default: 2
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small value to avoid division by zero.
Default: 1e-6
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Determines whether or not to keep the vector dimension.
Default: False

Shape:

- Input1: (N,D)(N, D)(N,D) or (D)(D)(D) where N = batch dimension and D = vector dimension
- Input2: (N,D)(N, D)(N,D) or (D)(D)(D), same shape as the Input1
- Output: (N)(N)(N) or ()()() based on input dimension.
If `keepdim` is `True`, then (N,1)(N, 1)(N,1) or (1)(1)(1) based on input dimension.

Examples

```
>>> pdist = nn.PairwiseDistance(p=2)
>>> input1 = torch.randn(100, 128)
>>> input2 = torch.randn(100, 128)
>>> output = pdist(input1, input2)
```

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/nn/modules/distance.py#L57)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)