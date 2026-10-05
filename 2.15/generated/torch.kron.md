# torch.kron

torch.kron(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the Kronecker product, denoted by ⊗\otimes⊗, of `input` and `other`.

If `input` is a (a0×a1×⋯×an)(a_0 \times a_1 \times \dots \times a_n)(a0​×a1​×⋯×an​) tensor and `other` is a
(b0×b1×⋯×bn)(b_0 \times b_1 \times \dots \times b_n)(b0​×b1​×⋯×bn​) tensor, the result will be a
(a0∗b0×a1∗b1×⋯×an∗bn)(a_0*b_0 \times a_1*b_1 \times \dots \times a_n*b_n)(a0​∗b0​×a1​∗b1​×⋯×an​∗bn​) tensor with the following entries:

(input⊗other)k0,k1,...,kn=inputi0,i1,...,in∗otherj0,j1,...,jn,(\text{input} \otimes \text{other})_{k_0, k_1, \dots, k_n} =
 \text{input}_{i_0, i_1, \dots, i_n} * \text{other}_{j_0, j_1, \dots, j_n},

(input⊗other)k0​,k1​,...,kn​​=inputi0​,i1​,...,in​​∗otherj0​,j1​,...,jn​​,

where kt=it∗bt+jtk_t = i_t * b_t + j_tkt​=it​∗bt​+jt​ for 0≤t≤n0 \leq t \leq n0≤t≤n.
If one tensor has fewer dimensions than the other it is unsqueezed until it has the same number of dimensions.

Supports real-valued and complex-valued inputs.

Note

This function generalizes the typical definition of the Kronecker product for two matrices to two tensors,
as described above. When `input` is a (m×n)(m \times n)(m×n) matrix and `other` is a
(p×q)(p \times q)(p×q) matrix, the result will be a (p∗m×q∗n)(p*m \times q*n)(p∗m×q∗n) block matrix:

A⊗B=[a11B⋯a1nB⋮⋱⋮am1B⋯amnB]\mathbf{A} \otimes \mathbf{B}=\begin{bmatrix}
a_{11} \mathbf{B} & \cdots & a_{1 n} \mathbf{B} \\
\vdots & \ddots & \vdots \\
a_{m 1} \mathbf{B} & \cdots & a_{m n} \mathbf{B} \end{bmatrix}

A⊗B=​a11​B⋮am1​B​⋯⋱⋯​a1n​B⋮amn​B​​

where `input` is A\mathbf{A}A and `other` is B\mathbf{B}B.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) -
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) -

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The output tensor. Ignored if `None`. Default: `None`

Examples:

```
>>> mat1 = torch.eye(2)
>>> mat2 = torch.ones(2, 2)
>>> torch.kron(mat1, mat2)
tensor([[1., 1., 0., 0.],
 [1., 1., 0., 0.],
 [0., 0., 1., 1.],
 [0., 0., 1., 1.]])

>>> mat1 = torch.eye(2)
>>> mat2 = torch.arange(1, 5).reshape(2, 2)
>>> torch.kron(mat1, mat2)
tensor([[1., 2., 0., 0.],
 [3., 4., 0., 0.],
 [0., 0., 1., 2.],
 [0., 0., 3., 4.]])
```