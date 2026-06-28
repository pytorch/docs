# torch.utils.hipify.hipify_python.extract_arguments

torch.utils.hipify.hipify_python.extract_arguments(*start*, *string*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/utils/hipify/hipify_python.py#L1037)

Return the list of arguments in the upcoming function parameter closure.
Example:
string (input): '(blocks, threads, 0, THCState_getCurrentStream(state))'
arguments (output): [{'start': 1, 'end': 7}, {'start': 8, 'end': 16}, {'start': 17, 'end': 19}, {'start': 20, 'end': 53}]