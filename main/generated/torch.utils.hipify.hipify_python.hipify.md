# torch.utils.hipify.hipify_python.hipify

torch.utils.hipify.hipify_python.hipify(*project_directory*, *show_detailed=False*, *extensions=('.cu', '.cuh', '.c', '.cc', '.cpp', '.h', '.in', '.hpp')*, *header_extensions=('.cuh', '.h', '.hpp')*, *output_directory=''*, *header_include_dirs=()*, *includes=('*',)*, *extra_files=()*, *out_of_place_only=False*, *ignores=()*, *show_progress=True*, *hip_clang_launch=False*, *is_pytorch_extension=False*, *hipify_extra_files_only=False*, *clean_ctx=None*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/utils/hipify/hipify_python.py#L1092)

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), *HipifyResult*]