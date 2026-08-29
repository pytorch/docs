# torch.nn.utils.parametrizations.orthogonal

torch.nn.utils.parametrizations.orthogonal(*module*, *name='weight'*, *orthogonal_map=None*, ***, *use_trivialization=True*)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/nn/utils/parametrizations.py#L193)

Apply an orthogonal or unitary parametrization to a matrix or a batch of matrices.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C, the parametrized
matrix Q∈Km×nQ \in \mathbb{K}^{m \times n}Q∈Km×n is **orthogonal** as

QHQ=Inif m≥nQQH=Imif m<n\begin{align*}
 Q^{\text{H}}Q &= \mathrm{I}_n \mathrlap{\qquad \text{if }m \geq n}\\
 QQ^{\text{H}} &= \mathrm{I}_m \mathrlap{\qquad \text{if }m < n}
\end{align*}QHQQQH​=In​if m≥n=Im​if m<n​

where QHQ^{\text{H}}QH is the conjugate transpose when QQQ is complex
and the transpose when QQQ is real-valued, and
In\mathrm{I}_nIn​ is the n-dimensional identity matrix.
In plain words, QQQ will have orthonormal columns whenever m≥nm \geq nm≥n
and orthonormal rows otherwise.

If the tensor has more than two dimensions, we consider it as a batch of matrices of shape (..., m, n).

The matrix QQQ may be parametrized via three different `orthogonal_map` in terms of the original tensor:

- `"matrix_exp"`/`"cayley"`:
the [`matrix_exp()`](torch.matrix_exp.html#torch.matrix_exp) Q=exp⁡(A)Q = \exp(A)Q=exp(A) and the [Cayley map](https://en.wikipedia.org/wiki/Cayley_transform#Matrix_map)
Q=(In+A/2)(In−A/2)−1Q = (\mathrm{I}_n + A/2)(\mathrm{I}_n - A/2)^{-1}Q=(In​+A/2)(In​−A/2)−1 are applied to a skew-symmetric
AAA to give an orthogonal matrix.
- `"householder"`: computes a product of Householder reflectors
([`householder_product()`](torch.linalg.householder_product.html#torch.linalg.householder_product)).

`"matrix_exp"`/`"cayley"` often make the parametrized weight converge faster than
`"householder"`, but they are slower to compute for very thin or very wide matrices.

If `use_trivialization=True` (default), the parametrization implements the "Dynamic Trivialization Framework",
where an extra matrix B∈Kn×nB \in \mathbb{K}^{n \times n}B∈Kn×n is stored under
`module.parametrizations.weight[0].base`. This helps the
convergence of the parametrized layer at the expense of some extra memory use.
See [Trivializations for Gradient-Based Optimization on Manifolds](https://arxiv.org/abs/1909.09501) .

Initial value of QQQ:
If the original tensor is not parametrized and `use_trivialization=True` (default), the initial value
of QQQ is that of the original tensor if it is orthogonal (or unitary in the complex case)
and it is orthogonalized via the QR decomposition otherwise (see [`torch.linalg.qr()`](torch.linalg.qr.html#torch.linalg.qr)).
Same happens when it is not parametrized and `orthogonal_map="householder"` even when `use_trivialization=False`.
Otherwise, the initial value is the result of the composition of all the registered
parametrizations applied to the original tensor.

Note

This function is implemented using the parametrization functionality
in [`register_parametrization()`](torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization).

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module on which to register the parametrization.
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of the tensor to make orthogonal. Default: `"weight"`.
- **orthogonal_map** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - One of the following: `"matrix_exp"`, `"cayley"`, `"householder"`.
Default: `"matrix_exp"` if the matrix is square or complex, `"householder"` otherwise.
- **use_trivialization** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to use the dynamic trivialization framework.
Default: `True`.

Returns:

The original module with an orthogonal parametrization registered to the specified
weight

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)

Example:

```
>>> orth_linear = orthogonal(nn.Linear(20, 40))
>>> orth_linear
ParametrizedLinear(
in_features=20, out_features=40, bias=True
(parametrizations): ModuleDict(
 (weight): ParametrizationList(
 (0): _Orthogonal()
 )
)
)
>>> Q = orth_linear.weight
>>> torch.dist(Q.T @ Q, torch.eye(20))
tensor(4.9332e-07)
```