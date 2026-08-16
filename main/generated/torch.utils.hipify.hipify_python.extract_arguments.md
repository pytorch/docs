# torch.utils.hipify.hipify_python.extract_arguments

torch.utils.hipify.hipify_python.extract_arguments(*start*, *string*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/utils/hipify/hipify_python.py#L1037)

Return the list of arguments in the upcoming function parameter closure.
Example:
string (input): '(blocks, threads, 0, THCState_getCurrentStream(state))'
arguments (output): [{'start': 1, 'end': 7}, {'start': 8, 'end': 16}, {'start': 17, 'end': 19}, {'start': 20, 'end': 53}]