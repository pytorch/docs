# torch.frac

torch.frac(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the fractional portion of each element in `input`.

outi=inputi−⌊∣inputi∣⌋∗sgn⁡(inputi)\text{out}_{i} = \text{input}_{i} - \left\lfloor |\text{input}_{i}| \right\rfloor * \operatorname{sgn}(\text{input}_{i})

outi​=inputi​−⌊∣inputi​∣⌋∗sgn(inputi​)

Example:

```
>>> torch.frac(torch.tensor([1, 2.5, -3.2]))
tensor([ 0.0000, 0.5000, -0.2000])
```