# torch.utils.hipify.hipify_python.replace_math_functions

torch.utils.hipify.hipify_python.replace_math_functions(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/utils/hipify/hipify_python.py#L478)

FIXME: Temporarily replace std:: invocations of math functions
with non-std:: versions to prevent linker errors NOTE: This
can lead to correctness issues when running tests, since the
correct version of the math function (exp/expf) might not get
called. Plan is to remove this function once HIP supports
std:: math function calls inside device code