# torch.polar

torch.polar(*abs*, *angle*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Constructs a complex tensor whose elements are Cartesian coordinates
corresponding to the polar coordinates with absolute value [`abs`](torch.abs.html#torch.abs) and angle
[`angle`](torch.angle.html#torch.angle).

out=abs⋅cos⁡(angle)+abs⋅sin⁡(angle)⋅j\text{out} = \text{abs} \cdot \cos(\text{angle}) + \text{abs} \cdot \sin(\text{angle}) \cdot j

out=abs⋅cos(angle)+abs⋅sin(angle)⋅j

Note

torch.polar is similar to
[std::polar](https://en.cppreference.com/w/cpp/numeric/complex/polar)
and does not compute the polar decomposition
of a complex tensor like Python's cmath.polar and SciPy's linalg.polar do.
The behavior of this function is undefined if abs is negative or NaN, or if angle is
infinite.

Parameters:

- **abs** ([*Tensor*](../tensors.html#torch.Tensor)) - The absolute value the complex tensor. Must be float or double.
- **angle** ([*Tensor*](../tensors.html#torch.Tensor)) - The angle of the complex tensor. Must be same dtype as
[`abs`](torch.abs.html#torch.abs).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)) - If the inputs are `torch.float32`, must be
`torch.complex64`. If the inputs are `torch.float64`, must be
`torch.complex128`.

Example:

```
>>> import numpy as np
>>> abs = torch.tensor([1, 2], dtype=torch.float64)
>>> angle = torch.tensor([np.pi / 2, 5 * np.pi / 4], dtype=torch.float64)
>>> z = torch.polar(abs, angle)
>>> z
tensor([(0.0000+1.0000j), (-1.4142-1.4142j)], dtype=torch.complex128)
```