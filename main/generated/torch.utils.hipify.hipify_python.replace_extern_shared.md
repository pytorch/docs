# torch.utils.hipify.hipify_python.replace_extern_shared

torch.utils.hipify.hipify_python.replace_extern_shared(*input_string*)[[source]](https://github.com/pytorch/pytorch/blob/a84b7baa33f893ab92176c08a85b14455e60b2fc/torch/utils/hipify/hipify_python.py#L521)

Match 'extern __shared__ type foo[];' syntax and use HIP_DYNAMIC_SHARED() MACRO instead.
See: [ROCm/hip](https://github.com/ROCm/hip/blob/master/docs/markdown/hip_kernel_language.md#__shared__)
.. rubric:: Examples

"extern __shared__ char smemChar[];"

=> "HIP_DYNAMIC_SHARED( char, smemChar)"

"extern __shared__ unsigned char smem[];"

=> "HIP_DYNAMIC_SHARED( unsigned char, my_smem)"