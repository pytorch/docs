# torch.nn.utils.spectral_norm.spectral_norm

torch.nn.utils.spectral_norm.spectral_norm(*module*, *name='weight'*, *n_power_iterations=1*, *eps=1e-12*, *dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/6e3cf2e4280672104341718ea51a55799bb3aca4/torch/nn/utils/spectral_norm.py#L262)

Apply spectral normalization to a parameter in the given module.

WSN=Wσ(W),σ(W)=max⁡h:h≠0∥Wh∥2∥h∥2\mathbf{W}_{SN} = \dfrac{\mathbf{W}}{\sigma(\mathbf{W})},
\sigma(\mathbf{W}) = \max_{\mathbf{h}: \mathbf{h} \ne 0} \dfrac{\|\mathbf{W} \mathbf{h}\|_2}{\|\mathbf{h}\|_2}

WSN​=σ(W)W​,σ(W)=h:h=0max​∥h∥2​∥Wh∥2​​

Spectral normalization stabilizes the training of discriminators (critics)
in Generative Adversarial Networks (GANs) by rescaling the weight tensor
with spectral norm σ\sigmaσ of the weight matrix calculated using
power iteration method. If the dimension of the weight tensor is greater
than 2, it is reshaped to 2D in power iteration method to get spectral
norm. This is implemented via a hook that calculates spectral norm and
rescales weight before every `forward()` call.

See [Spectral Normalization for Generative Adversarial Networks](https://arxiv.org/abs/1802.05957) .

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - containing module
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of weight parameter
- **n_power_iterations** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - number of power iterations to
calculate spectral norm
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - epsilon for numerical stability in
calculating norms
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension corresponding to number of outputs,
the default is `0`, except for modules that are instances of
ConvTranspose{1,2,3}d, when it is `1`

Returns:

The original module with the spectral norm hook

Return type:

*T_module*

Note

This function has been reimplemented as
[`torch.nn.utils.parametrizations.spectral_norm()`](torch.nn.utils.parametrizations.spectral_norm.html#torch.nn.utils.parametrizations.spectral_norm) using the new
parametrization functionality in
[`torch.nn.utils.parametrize.register_parametrization()`](torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization). Please use
the newer version. This function will be deprecated in a future version
of PyTorch.

Example:

```
>>> m = spectral_norm(nn.Linear(20, 40))
>>> m
Linear(in_features=20, out_features=40, bias=True)
>>> m.weight_u.size()
torch.Size([40])
```