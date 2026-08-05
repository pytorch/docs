# get_combined_dict

*class*torch.ao.quantization.utils.get_combined_dict(*default_dict*, *additional_dict*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/ao/quantization/utils.py#L140)

Combines two dictionaries.

This function takes two dictionaries as input and returns a new dictionary
that contains all the key-value pairs from both input dictionaries.
If there are any duplicate keys in the additional_dict, the values
from the additional_dict will overwrite those in the default_dict.
:param default_dict: The main dictionary that will be used as the base
:type default_dict: dict
:param additional_dict: The dictionary used to update default_dict
:type additional_dict: dict

Returns:

The resulting dictionary

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)

Example

```
>>> x = dict(a=1, b=1)
>>> y = dict(b=2, c=3)
>>> get_combined_dict(x, y)
{'a': 1, 'b': 2, 'c': 3}
```