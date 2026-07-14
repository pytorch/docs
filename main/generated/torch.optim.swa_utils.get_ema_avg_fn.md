# torch.optim.swa_utils.get_ema_avg_fn

torch.optim.swa_utils.get_ema_avg_fn(*decay=0.999*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/optim/swa_utils.py#L119)

Get the function applying exponential moving average (EMA) across multiple params.

The EMA is computed as:

W0EMA=W0modelW_0^{\text{EMA}} = W_0^{\text{model}}

W0EMA​=W0model​
Wt+1EMA=decay×WtEMA+(1−decay)×Wt+1modelW_{t+1}^{\text{EMA}} = \text{decay} \times W_t^{\text{EMA}} + (1 - \text{decay}) \times W_{t+1}^{\text{model}}

Wt+1EMA​=decay×WtEMA​+(1−decay)×Wt+1model​

where WtEMAW_t^{\text{EMA}}WtEMA​ is the EMA parameter at step ttt,
WtmodelW_t^{\text{model}}Wtmodel​ is the model parameter at step ttt,
and decay\text{decay}decay is the decay rate (default: 0.999).

Parameters:

**decay** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Decay rate for EMA. Must be in the range [0, 1]. Default: 0.999

Returns:

A function that updates EMA parameters given current model parameters

Return type:

Callable