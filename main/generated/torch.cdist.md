# torch.cdist

torch.cdist(*x1*, *x2*, *p=2.0*, *compute_mode='use_mm_for_euclid_dist_if_necessary'*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/functional.py#L1483)

Computes the batched p-norm distance between each pair of the two collections of row vectors.

Parameters:

- **x1** ([*Tensor*](../tensors.html#torch.Tensor)) - input tensor where the last two dimensions represent the points and the feature dimension respectively.
The shape can be D1×D2×⋯×Dn×P×MD_1 \times D_2 \times \cdots \times D_n \times P \times MD1​×D2​×⋯×Dn​×P×M,
where PPP is the number of points and MMM is the feature dimension.
- **x2** ([*Tensor*](../tensors.html#torch.Tensor)) - input tensor where the last two dimensions also represent the points and the feature dimension respectively.
The shape can be D1′×D2′×⋯×Dm′×R×MD_1' \times D_2' \times \cdots \times D_m' \times R \times MD1′​×D2′​×⋯×Dm′​×R×M,
where RRR is the number of points and MMM is the feature dimension,
which should match the feature dimension of x1.
- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - p value for the p-norm distance to calculate between each vector pair
∈[0,∞]\in [0, \infty]∈[0,∞].
- **compute_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - 'use_mm_for_euclid_dist_if_necessary' - will use matrix multiplication approach to calculate
euclidean distance (p = 2) if P > 25 or R > 25
'use_mm_for_euclid_dist' - will always use matrix multiplication approach to calculate
euclidean distance (p = 2)
'donot_use_mm_for_euclid_dist' - will never use matrix multiplication approach to calculate
euclidean distance (p = 2)
Default: use_mm_for_euclid_dist_if_necessary.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

If x1 has shape B×P×MB \times P \times MB×P×M and x2 has shape B×R×MB \times R \times MB×R×M then the
output will have shape B×P×RB \times P \times RB×P×R.

This function is equivalent to scipy.spatial.distance.cdist(input,'minkowski', p=p)
if p∈(0,∞)p \in (0, \infty)p∈(0,∞). When p=0p = 0p=0 it is equivalent to
scipy.spatial.distance.cdist(input, 'hamming') * M. When p=∞p = \inftyp=∞, the closest
scipy function is scipy.spatial.distance.cdist(xn, lambda x, y: np.abs(x - y).max()).

Example

```
>>> a = torch.tensor([[0.9041, 0.0196], [-0.3108, -2.4423], [-0.4821, 1.059]])
>>> a
tensor([[ 0.9041, 0.0196],
 [-0.3108, -2.4423],
 [-0.4821, 1.0590]])
>>> b = torch.tensor([[-2.1763, -0.4713], [-0.6986, 1.3702]])
>>> b
tensor([[-2.1763, -0.4713],
 [-0.6986, 1.3702]])
>>> torch.cdist(a, b, p=2)
tensor([[3.1193, 2.0959],
 [2.7138, 3.8322],
 [2.2830, 0.3791]])
```