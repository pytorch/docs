# load_observer_state_dict

*class*torch.ao.quantization.observer.load_observer_state_dict(*mod*, *obs_dict*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/quantization/observer.py#L2134)

Given input model and a state_dict containing model observer stats,
load the stats back into the model. The observer state_dict can be saved
using torch.ao.quantization.get_observer_state_dict