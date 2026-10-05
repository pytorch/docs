# torch.Tensor.bernoulli

Tensor.bernoulli(***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a result tensor where each result[i]\texttt{result[i]}result[i] is independently
sampled from Bernoulli(self[i])\text{Bernoulli}(\texttt{self[i]})Bernoulli(self[i]). `self` must have
floating point `dtype`, and the result will have the same `dtype`.

See [`torch.bernoulli()`](torch.bernoulli.html#torch.bernoulli)