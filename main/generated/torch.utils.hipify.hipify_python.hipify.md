# torch.utils.hipify.hipify_python.hipify

torch.utils.hipify.hipify_python.hipify(*project_directory*, *show_detailed=False*, *extensions=('.cu', '.cuh', '.c', '.cc', '.cpp', '.h', '.in', '.hpp')*, *header_extensions=('.cuh', '.h', '.hpp')*, *output_directory=''*, *header_include_dirs=()*, *includes=('*',)*, *extra_files=()*, *out_of_place_only=False*, *ignores=()*, *show_progress=True*, *hip_clang_launch=False*, *is_pytorch_extension=False*, *hipify_extra_files_only=False*, *clean_ctx=None*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/utils/hipify/hipify_python.py#L1092)

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), *HipifyResult*]