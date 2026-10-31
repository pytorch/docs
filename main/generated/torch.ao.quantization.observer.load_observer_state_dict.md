# load_observer_state_dict

*class*torch.ao.quantization.observer.load_observer_state_dict(*mod*, *obs_dict*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/ao/quantization/observer.py#L2046)

Given input model and a state_dict containing model observer stats,
load the stats back into the model. The observer state_dict can be saved
using torch.ao.quantization.get_observer_state_dict