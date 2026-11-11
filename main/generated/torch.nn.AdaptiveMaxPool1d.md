# AdaptiveMaxPool1d

*class*torch.nn.AdaptiveMaxPool1d(*output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/6ced8259c1c883abd806189dbf32b9707f69adeb/torch/nn/modules/pooling.py#L1329)

Applies a 1D adaptive max pooling over an input signal composed of several input planes.

The output size is LoutL_{out}Lout​, for any input size.
The number of output features is equal to the number of input planes.

Each output element is the maximum over a region of the input whose bounds are
derived from the input and output sizes:

start(k)=⌊k×LinLout⌋end(k)=⌈(k+1)×LinLout⌉\text{start}(k) = \left\lfloor \frac{k \times L_{in}}{L_{out}} \right\rfloor
\qquad
\text{end}(k) = \left\lceil \frac{(k + 1) \times L_{in}}{L_{out}} \right\rceil

start(k)=⌊Lout​k×Lin​​⌋end(k)=⌈Lout​(k+1)×Lin​​⌉
out(Ni,Cj,k)=max⁡start(k)≤l<end(k)input(Ni,Cj,l)out(N_i, C_j, k) = \max_{\text{start}(k) \le l < \text{end}(k)} input(N_i, C_j, l)

out(Ni​,Cj​,k)=start(k)≤l<end(k)max​input(Ni​,Cj​,l)

When LinL_{in}Lin​ is not divisible by LoutL_{out}Lout​, these regions may have
different sizes and may overlap. For example, an input of size 5 pooled to size 3
uses the regions [0,2)[0, 2)[0,2), [1,4)[1, 4)[1,4) and [3,5)[3, 5)[3,5).

Parameters:

- **output_size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*|*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - the target output size LoutL_{out}Lout​.
- **return_indices** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - if `True`, will return the indices along with the outputs.
Useful to pass to nn.MaxUnpool1d. Default: `False`

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​), where
Lout=output_sizeL_{out}=\text{output\_size}Lout​=output_size.

Examples

```
>>> # target output size of 5
>>> m = nn.AdaptiveMaxPool1d(5)
>>> input = torch.randn(1, 64, 8)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/6ced8259c1c883abd806189dbf32b9707f69adeb/torch/nn/modules/pooling.py#L1370)

Runs the forward pass.