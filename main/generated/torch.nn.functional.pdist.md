# torch.nn.functional.pdist

torch.nn.functional.pdist(*input*, *p=2*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/nn/functional.py#L5640)

Computes the p-norm distance between every pair of row vectors in the input.
This is identical to the upper triangular portion, excluding the diagonal, of
torch.norm(input[:, None] - input, dim=2, p=p). This function will be faster
if the rows are contiguous.

If input has shape N×MN \times MN×M then the output will have shape
12N(N−1)\frac{1}{2} N (N - 1)21​N(N−1).

This function is equivalent to `scipy.spatial.distance.pdist(input,
'minkowski', p=p)` if p∈(0,∞)p \in (0, \infty)p∈(0,∞). When p=0p = 0p=0 it is
equivalent to `scipy.spatial.distance.pdist(input, 'hamming') * M`.
When p=∞p = \inftyp=∞, the closest scipy function is
`scipy.spatial.distance.pdist(xn, lambda x, y: np.abs(x - y).max())`.

Parameters:

- **input** - input tensor of shape N×MN \times MN×M.
- **p** - p value for the p-norm distance to calculate between each vector pair
∈[0,∞]\in [0, \infty]∈[0,∞].