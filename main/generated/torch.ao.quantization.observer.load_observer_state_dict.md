# load_observer_state_dict

*class*torch.ao.quantization.observer.load_observer_state_dict(*mod*, *obs_dict*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/ao/quantization/observer.py#L2046)

Given input model and a state_dict containing model observer stats,
load the stats back into the model. The observer state_dict can be saved
using torch.ao.quantization.get_observer_state_dict