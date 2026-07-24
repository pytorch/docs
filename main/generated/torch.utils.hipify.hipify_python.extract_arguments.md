# torch.utils.hipify.hipify_python.extract_arguments

torch.utils.hipify.hipify_python.extract_arguments(*start*, *string*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/utils/hipify/hipify_python.py#L1037)

Return the list of arguments in the upcoming function parameter closure.
Example:
string (input): '(blocks, threads, 0, THCState_getCurrentStream(state))'
arguments (output): [{'start': 1, 'end': 7}, {'start': 8, 'end': 16}, {'start': 17, 'end': 19}, {'start': 20, 'end': 53}]