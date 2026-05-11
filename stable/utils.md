# torch.utils

| [`rename_privateuse1_backend`](generated/torch.utils.rename_privateuse1_backend.html#torch.utils.rename_privateuse1_backend) | Rename the privateuse1 backend device to make it more convenient to use as a device name within PyTorch APIs. |
| --- | --- |
| [`generate_methods_for_privateuse1_backend`](generated/torch.utils.generate_methods_for_privateuse1_backend.html#torch.utils.generate_methods_for_privateuse1_backend) | Automatically generate attributes and methods for the custom backend after rename privateuse1 backend. |
| [`get_cpp_backtrace`](generated/torch.utils.get_cpp_backtrace.html#torch.utils.get_cpp_backtrace) | Return a string containing the C++ stack trace of the current thread. |
| [`set_module`](generated/torch.utils.set_module.html#torch.utils.set_module) | Set the module attribute on a python object for a given object for nicer printing |
| [`swap_tensors`](generated/torch.utils.swap_tensors.html#torch.utils.swap_tensors) | This function swaps the content of the two Tensor objects. |

# torch.utils.collect_env

| [`check_release_file`](generated/torch.utils.collect_env.check_release_file.html#torch.utils.collect_env.check_release_file) | |
| --- | --- |
| [`is_xnnpack_available`](generated/torch.utils.collect_env.is_xnnpack_available.html#torch.utils.collect_env.is_xnnpack_available) | |
| [`main`](generated/torch.utils.collect_env.main.html#torch.utils.collect_env.main) | |
| [`pretty_str`](generated/torch.utils.collect_env.pretty_str.html#torch.utils.collect_env.pretty_str) | |
| [`run`](generated/torch.utils.collect_env.run.html#torch.utils.collect_env.run) | Return (return-code, stdout, stderr). |
| [`run_and_parse_first_match`](generated/torch.utils.collect_env.run_and_parse_first_match.html#torch.utils.collect_env.run_and_parse_first_match) | Run command using run_lambda, returns the first regex match if it exists. |
| [`run_and_read_all`](generated/torch.utils.collect_env.run_and_read_all.html#torch.utils.collect_env.run_and_read_all) | Run command using run_lambda; reads and returns entire output if rc is 0. |
| [`run_and_return_first_line`](generated/torch.utils.collect_env.run_and_return_first_line.html#torch.utils.collect_env.run_and_return_first_line) | Run command using run_lambda and returns first line if output is not empty. |

# torch.utils.flop_counter

| [`baddbmm_flop`](generated/torch.utils.flop_counter.baddbmm_flop.html#torch.utils.flop_counter.baddbmm_flop) | Count flops for the baddbmm operation. |
| --- | --- |
| [`bmm_flop`](generated/torch.utils.flop_counter.bmm_flop.html#torch.utils.flop_counter.bmm_flop) | Count flops for the bmm operation. |
| [`conv_backward_flop`](generated/torch.utils.flop_counter.conv_backward_flop.html#torch.utils.flop_counter.conv_backward_flop) | |
| [`conv_flop`](generated/torch.utils.flop_counter.conv_flop.html#torch.utils.flop_counter.conv_flop) | Count flops for convolution. |
| [`conv_flop_count`](generated/torch.utils.flop_counter.conv_flop_count.html#torch.utils.flop_counter.conv_flop_count) | Count flops for convolution. |
| [`register_flop_formula`](generated/torch.utils.flop_counter.register_flop_formula.html#torch.utils.flop_counter.register_flop_formula) | |
| [`sdpa_backward_flop`](generated/torch.utils.flop_counter.sdpa_backward_flop.html#torch.utils.flop_counter.sdpa_backward_flop) | Count flops for self-attention backward. |
| [`sdpa_backward_flop_count`](generated/torch.utils.flop_counter.sdpa_backward_flop_count.html#torch.utils.flop_counter.sdpa_backward_flop_count) | |
| [`sdpa_flop`](generated/torch.utils.flop_counter.sdpa_flop.html#torch.utils.flop_counter.sdpa_flop) | Count flops for self-attention. |
| [`sdpa_flop_count`](generated/torch.utils.flop_counter.sdpa_flop_count.html#torch.utils.flop_counter.sdpa_flop_count) | Count flops for self-attention. |
| [`shape_wrapper`](generated/torch.utils.flop_counter.shape_wrapper.html#torch.utils.flop_counter.shape_wrapper) | |

# torch.utils.hipify.hipify_python

The Python Hipify script.
##
# Copyright (c) 2015-2016 Advanced Micro Devices, Inc. All rights reserved.
# 2017-2018 Advanced Micro Devices, Inc. and
# Facebook Inc. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

| [`compute_stats`](generated/torch.utils.hipify.hipify_python.compute_stats.html#torch.utils.hipify.hipify_python.compute_stats) | |
| --- | --- |
| [`extract_arguments`](generated/torch.utils.hipify.hipify_python.extract_arguments.html#torch.utils.hipify.hipify_python.extract_arguments) | Return the list of arguments in the upcoming function parameter closure. |
| [`file_add_header`](generated/torch.utils.hipify.hipify_python.file_add_header.html#torch.utils.hipify.hipify_python.file_add_header) | |
| [`file_specific_replacement`](generated/torch.utils.hipify.hipify_python.file_specific_replacement.html#torch.utils.hipify.hipify_python.file_specific_replacement) | |
| [`find_bracket_group`](generated/torch.utils.hipify.hipify_python.find_bracket_group.html#torch.utils.hipify.hipify_python.find_bracket_group) | Finds the first balanced parentheses. |
| [`find_closure_group`](generated/torch.utils.hipify.hipify_python.find_closure_group.html#torch.utils.hipify.hipify_python.find_closure_group) | Generalization for finding a balancing closure group |
| [`find_parentheses_group`](generated/torch.utils.hipify.hipify_python.find_parentheses_group.html#torch.utils.hipify.hipify_python.find_parentheses_group) | Finds the first balanced bracket. |
| [`fix_static_global_kernels`](generated/torch.utils.hipify.hipify_python.fix_static_global_kernels.html#torch.utils.hipify.hipify_python.fix_static_global_kernels) | Static global kernels in HIP results in a compilation error. |
| [`hip_header_magic`](generated/torch.utils.hipify.hipify_python.hip_header_magic.html#torch.utils.hipify.hipify_python.hip_header_magic) | If the file makes kernel builtin calls and does not include the cuda_runtime.h header, then automatically add an #include to match the "magic" includes provided by NVCC. |
| [`hipify`](generated/torch.utils.hipify.hipify_python.hipify.html#torch.utils.hipify.hipify_python.hipify) | |
| [`is_caffe2_gpu_file`](generated/torch.utils.hipify.hipify_python.is_caffe2_gpu_file.html#torch.utils.hipify.hipify_python.is_caffe2_gpu_file) | |
| [`is_cusparse_file`](generated/torch.utils.hipify.hipify_python.is_cusparse_file.html#torch.utils.hipify.hipify_python.is_cusparse_file) | |
| [`is_out_of_place`](generated/torch.utils.hipify.hipify_python.is_out_of_place.html#torch.utils.hipify.hipify_python.is_out_of_place) | |
| [`is_pytorch_file`](generated/torch.utils.hipify.hipify_python.is_pytorch_file.html#torch.utils.hipify.hipify_python.is_pytorch_file) | |
| [`is_special_file`](generated/torch.utils.hipify.hipify_python.is_special_file.html#torch.utils.hipify.hipify_python.is_special_file) | |
| [`match_extensions`](generated/torch.utils.hipify.hipify_python.match_extensions.html#torch.utils.hipify.hipify_python.match_extensions) | Helper method to see if filename ends with certain extension |
| [`matched_files_iter`](generated/torch.utils.hipify.hipify_python.matched_files_iter.html#torch.utils.hipify.hipify_python.matched_files_iter) | |
| [`openf`](generated/torch.utils.hipify.hipify_python.openf.html#torch.utils.hipify.hipify_python.openf) | |
| [`preprocess_file_and_save_result`](generated/torch.utils.hipify.hipify_python.preprocess_file_and_save_result.html#torch.utils.hipify.hipify_python.preprocess_file_and_save_result) | |
| [`preprocessor`](generated/torch.utils.hipify.hipify_python.preprocessor.html#torch.utils.hipify.hipify_python.preprocessor) | Executes the CUDA -> HIP conversion on the specified file. |
| [`processKernelLaunches`](generated/torch.utils.hipify.hipify_python.processKernelLaunches.html#torch.utils.hipify.hipify_python.processKernelLaunches) | Replace the CUDA style Kernel launches with the HIP style kernel launches. |
| [`replace_extern_shared`](generated/torch.utils.hipify.hipify_python.replace_extern_shared.html#torch.utils.hipify.hipify_python.replace_extern_shared) | Match 'extern __shared__ type foo[];' syntax and use HIP_DYNAMIC_SHARED() MACRO instead. |
| [`replace_math_functions`](generated/torch.utils.hipify.hipify_python.replace_math_functions.html#torch.utils.hipify.hipify_python.replace_math_functions) | FIXME: Temporarily replace std:: invocations of math functions with non-std:: versions to prevent linker errors NOTE: This can lead to correctness issues when running tests, since the correct version of the math function (exp/expf) might not get called. |
| [`str2bool`](generated/torch.utils.hipify.hipify_python.str2bool.html#torch.utils.hipify.hipify_python.str2bool) | ArgumentParser doesn't support type=bool. |

 This module needs to be documented. Adding here in the meantime
for tracking purposes