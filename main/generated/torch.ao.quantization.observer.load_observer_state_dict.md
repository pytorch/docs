# load_observer_state_dict

*class*torch.ao.quantization.observer.load_observer_state_dict(*mod*, *obs_dict*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/ao/quantization/observer.py#L2023)

Given input model and a state_dict containing model observer stats,
load the stats back into the model. The observer state_dict can be saved
using torch.ao.quantization.get_observer_state_dict