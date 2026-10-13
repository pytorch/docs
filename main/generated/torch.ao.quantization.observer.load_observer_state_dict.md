# load_observer_state_dict

*class*torch.ao.quantization.observer.load_observer_state_dict(*mod*, *obs_dict*)[[source]](https://github.com/pytorch/pytorch/blob/f6c4d435cf6682e89d565983c0975951782dc5e2/torch/ao/quantization/observer.py#L2024)

Given input model and a state_dict containing model observer stats,
load the stats back into the model. The observer state_dict can be saved
using torch.ao.quantization.get_observer_state_dict