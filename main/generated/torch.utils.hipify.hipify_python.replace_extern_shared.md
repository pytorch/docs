# torch.utils.hipify.hipify_python.replace_extern_shared

torch.utils.hipify.hipify_python.replace_extern_shared(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/utils/hipify/hipify_python.py#L529)

Match 'extern __shared__ type foo[];' syntax and use HIP_DYNAMIC_SHARED() MACRO instead.
See: [ROCm/hip](https://github.com/ROCm/hip/blob/master/docs/markdown/hip_kernel_language.md#__shared__)
.. rubric:: Examples

"extern __shared__ char smemChar[];"

=> "HIP_DYNAMIC_SHARED( char, smemChar)"

"extern __shared__ unsigned char smem[];"

=> "HIP_DYNAMIC_SHARED( unsigned char, my_smem)"