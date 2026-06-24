# torch.utils.cpp_extension

torch.utils.cpp_extension.CppExtension(*name*, *sources*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L1378)

Create a `setuptools.Extension` for C++.

Convenience method that creates a `setuptools.Extension` with the
bare minimum (but often sufficient) arguments to build a C++ extension.

All arguments are forwarded to the `setuptools.Extension`
constructor. Full list arguments can be found at
[https://setuptools.pypa.io/en/latest/userguide/ext_modules.html#extension-api-reference](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html#extension-api-reference)

Warning

The PyTorch python API (as provided in libtorch_python) cannot be built
with the flag `py_limited_api=True`. When this flag is passed, it is
the user's responsibility in their library to not use APIs from
libtorch_python (in particular pytorch/python bindings) and to only use
APIs from libtorch (aten objects, operators and the dispatcher). For
example, to give access to custom ops from python, the library should
register the ops through the dispatcher.

Contrary to CPython setuptools, who does not define -DPy_LIMITED_API
as a compile flag when py_limited_api is specified as an option for
the "bdist_wheel" command in `setup`, PyTorch does! We will specify
-DPy_LIMITED_API=min_supported_cpython to best enforce consistency,
safety, and sanity in order to encourage best practices. To target a
different version, set min_supported_cpython to the hexcode of the
CPython version of choice.

Example

```
>>> from setuptools import setup
>>> from torch.utils.cpp_extension import BuildExtension, CppExtension
>>> setup(
... name='extension',
... ext_modules=[
... CppExtension(
... name='extension',
... sources=['extension.cpp'],
... extra_compile_args=['-g'],
... extra_link_args=['-Wl,--no-as-needed', '-lm'])
... ],
... cmdclass={
... 'build_ext': BuildExtension
... })
```

torch.utils.cpp_extension.CUDAExtension(*name*, *sources*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L1448)

Create a `setuptools.Extension` for CUDA/C++.

Convenience method that creates a `setuptools.Extension` with the
bare minimum (but often sufficient) arguments to build a CUDA/C++
extension. This includes the CUDA include path, library path and runtime
library.

All arguments are forwarded to the `setuptools.Extension`
constructor. Full list arguments can be found at
[https://setuptools.pypa.io/en/latest/userguide/ext_modules.html#extension-api-reference](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html#extension-api-reference)

Warning

The PyTorch python API (as provided in libtorch_python) cannot be built
with the flag `py_limited_api=True`. When this flag is passed, it is
the user's responsibility in their library to not use APIs from
libtorch_python (in particular pytorch/python bindings) and to only use
APIs from libtorch (aten objects, operators and the dispatcher). For
example, to give access to custom ops from python, the library should
register the ops through the dispatcher.

Contrary to CPython setuptools, who does not define -DPy_LIMITED_API
as a compile flag when py_limited_api is specified as an option for
the "bdist_wheel" command in `setup`, PyTorch does! We will specify
-DPy_LIMITED_API=min_supported_cpython to best enforce consistency,
safety, and sanity in order to encourage best practices. To target a
different version, set min_supported_cpython to the hexcode of the
CPython version of choice.

Example

```
>>> from setuptools import setup
>>> from torch.utils.cpp_extension import BuildExtension, CUDAExtension
>>> setup(
... name='cuda_extension',
... ext_modules=[
... CUDAExtension(
... name='cuda_extension',
... sources=['extension.cpp', 'extension_kernel.cu'],
... extra_compile_args={'cxx': ['-g'],
... 'nvcc': ['-O2']},
... extra_link_args=['-Wl,--no-as-needed', '-lcuda'])
... ],
... cmdclass={
... 'build_ext': BuildExtension
... })
```

Compute capabilities:

By default the extension will be compiled to run on all archs of the cards visible during the
building process of the extension, plus PTX. If down the road a new card is installed the
extension may need to be recompiled. If a visible card has a compute capability (CC) that's
newer than the newest version for which your nvcc can build fully-compiled binaries, PyTorch
will make nvcc fall back to building kernels with the newest version of PTX your nvcc does
support (see below for details on PTX).

You can override the default behavior using TORCH_CUDA_ARCH_LIST to explicitly specify which
CCs you want the extension to support:

`TORCH_CUDA_ARCH_LIST="6.1 8.6" python build_my_extension.py`
`TORCH_CUDA_ARCH_LIST="5.2 6.0 6.1 7.0 7.5 8.0 8.6+PTX" python build_my_extension.py`

The +PTX option causes extension kernel binaries to include PTX instructions for the specified
CC. PTX is an intermediate representation that allows kernels to runtime-compile for any CC >=
the specified CC (for example, 8.6+PTX generates PTX that can runtime-compile for any GPU with
CC >= 8.6). This improves your binary's forward compatibility. However, relying on older PTX to
provide forward compat by runtime-compiling for newer CCs can modestly reduce performance on
those newer CCs. If you know exact CC(s) of the GPUs you want to target, you're always better
off specifying them individually. For example, if you want your extension to run on 8.0 and 8.6,
"8.0+PTX" would work functionally because it includes PTX that can runtime-compile for 8.6, but
"8.0 8.6" would be better.

Note that while it's possible to include all supported archs, the more archs get included the
slower the building process will be, as it will build a separate kernel image for each arch.

Note that CUDA-11.5 nvcc will hit internal compiler error while parsing torch/extension.h on Windows.
To workaround the issue, move python binding logic to pure C++ file.

Example use:

#include <ATen/ATen.h>
at::Tensor SigmoidAlphaBlendForwardCuda(....)

Instead of:

#include <torch/extension.h>
torch::Tensor SigmoidAlphaBlendForwardCuda(...)

Currently open issue for nvcc bug: [pytorch/pytorch#69460](https://github.com/pytorch/pytorch/issues/69460)
Complete workaround code example: [facebookresearch/pytorch3d](https://github.com/facebookresearch/pytorch3d/commit/cb170ac024a949f1f9614ffe6af1c38d972f7d48)

Relocatable device code linking:

If you want to reference device symbols across compilation units (across object files),
the object files need to be built with relocatable device code (-rdc=true or -dc).
An exception to this rule is "dynamic parallelism" (nested kernel launches) which is not used a lot anymore.
Relocatable device code is less optimized so it needs to be used only on object files that need it.
Using -dlto (Device Link Time Optimization) at the device code compilation step and dlink step
helps reduce the potential perf degradation of -rdc.
Note that it needs to be used at both steps to be useful.

If you have rdc objects you need to have an extra -dlink (device linking) step before the CPU symbol linking step.
There is also a case where -dlink is used without -rdc:
when an extension is linked against a static lib containing rdc-compiled objects
like the [NVSHMEM library]([https://developer.nvidia.com/nvshmem](https://developer.nvidia.com/nvshmem)).

Note: Ninja is required to build a CUDA Extension with RDC linking.

Example

```
>>> CUDAExtension(
... name='cuda_extension',
... sources=['extension.cpp', 'extension_kernel.cu'],
... dlink=True,
... dlink_libraries=["dlink_lib"],
... extra_compile_args={'cxx': ['-g'],
... 'nvcc': ['-O2', '-rdc=true']})
```

torch.utils.cpp_extension.SyclExtension(*name*, *sources*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L1640)

Creates a `setuptools.Extension` for SYCL/C++.

Convenience method that creates a `setuptools.Extension` with the
bare minimum (but often sufficient) arguments to build a SYCL/C++
extension.

All arguments are forwarded to the `setuptools.Extension`
constructor.

Warning

The PyTorch python API (as provided in libtorch_python) cannot be built
with the flag `py_limited_api=True`. When this flag is passed, it is
the user's responsibility in their library to not use APIs from
libtorch_python (in particular pytorch/python bindings) and to only use
APIs from libtorch (aten objects, operators and the dispatcher). For
example, to give access to custom ops from python, the library should
register the ops through the dispatcher.

Contrary to CPython setuptools, who does not define -DPy_LIMITED_API
as a compile flag when py_limited_api is specified as an option for
the "bdist_wheel" command in `setup`, PyTorch does! We will specify
-DPy_LIMITED_API=min_supported_cpython to best enforce consistency,
safety, and sanity in order to encourage best practices. To target a
different version, set min_supported_cpython to the hexcode of the
CPython version of choice.

Example

```
>>> from torch.utils.cpp_extension import BuildExtension, SyclExtension
>>> setup(
... name='xpu_extension',
... ext_modules=[
... SyclExtension(
... name='xpu_extension',
... sources=['extension.cpp', 'extension_kernel.cpp'],
... extra_compile_args={'cxx': ['-g', '-std=c++20', '-fPIC']})
... ],
... cmdclass={
... 'build_ext': BuildExtension
... })
```

By default the extension will be compiled to run on all archs of the cards visible during the
building process of the extension. If down the road a new card is installed the
extension may need to be recompiled. You can override the default behavior using
TORCH_XPU_ARCH_LIST to explicitly specify which device architectures you want the extension
to support:

`TORCH_XPU_ARCH_LIST="pvc,xe-lpg" python build_my_extension.py`

Note that while it's possible to include all supported archs, the more archs get included the
slower the building process will be, as it will build a separate kernel image for each arch.

Note: Ninja is required to build SyclExtension.

torch.utils.cpp_extension.BuildExtension(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L734)

A custom `setuptools` build extension .

This `setuptools.build_ext` subclass takes care of passing the
minimum required compiler flags (e.g. `-std=c++20`) as well as mixed
C++/CUDA/SYCL compilation (and support for CUDA/SYCL files in general).

When using `BuildExtension`, it is allowed to supply a dictionary
for `extra_compile_args` (rather than the usual list) that maps from
languages/compilers (the only expected values are `cxx`, `nvcc` or
`sycl`) to a list of additional compiler flags to supply to the compiler.
This makes it possible to supply different flags to the C++, CUDA and SYCL
compiler during mixed compilation.

`use_ninja` (bool): If `use_ninja` is `True` (default), then we
attempt to build using the Ninja backend. Ninja greatly speeds up
compilation compared to the standard `setuptools.build_ext`.
Fallbacks to the standard distutils backend if Ninja is not available.

Note

By default, the Ninja backend uses #CPUS + 2 workers to build the
extension. This may use up too many resources on some systems. One
can control the number of workers by setting the MAX_JOBS environment
variable to a non-negative number.

torch.utils.cpp_extension.load(*name*, *sources*, *extra_cflags=None*, *extra_cuda_cflags=None*, *extra_sycl_cflags=None*, *extra_ldflags=None*, *extra_include_paths=None*, *build_directory=None*, *verbose=False*, *with_cuda=None*, *with_sycl=None*, *is_python_module=True*, *is_standalone=False*, *keep_intermediates=True*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L1818)

Load a PyTorch C++ extension just-in-time (JIT).

To load an extension, a Ninja build file is emitted, which is used to
compile the given sources into a dynamic library. This library is
subsequently loaded into the current Python process as a module and
returned from this function, ready for use.

By default, the directory to which the build file is emitted and the
resulting library compiled to is `<tmp>/torch_extensions/<name>`, where
`<tmp>` is the temporary folder on the current platform and `<name>`
the name of the extension. This location can be overridden in two ways.
First, if the `TORCH_EXTENSIONS_DIR` environment variable is set, it
replaces `<tmp>/torch_extensions` and all extensions will be compiled
into subfolders of this directory. Second, if the `build_directory`
argument to this function is supplied, it overrides the entire path, i.e.
the library will be compiled into that folder directly.

To compile the sources, the default system compiler (`c++`) is used,
which can be overridden by setting the `CXX` environment variable. To pass
additional arguments to the compilation process, `extra_cflags` or
`extra_ldflags` can be provided. For example, to compile your extension
with optimizations, pass `extra_cflags=['-O3']`. You can also use
`extra_cflags` to pass further include directories.

CUDA support with mixed compilation is provided. Simply pass CUDA source
files (`.cu` or `.cuh`) along with other sources. Such files will be
detected and compiled with nvcc rather than the C++ compiler. This includes
passing the CUDA lib64 directory as a library directory, and linking
`cudart`. You can pass additional flags to nvcc via
`extra_cuda_cflags`, just like with `extra_cflags` for C++. Various
heuristics for finding the CUDA install directory are used, which usually
work fine. If not, setting the `CUDA_HOME` environment variable is the
safest option.

SYCL support with mixed compilation is provided. Simply pass SYCL source
files (`.sycl`) along with other sources. Such files will be detected
and compiled with SYCL compiler (such as Intel DPC++ Compiler) rather
than the C++ compiler. You can pass additional flags to SYCL compiler
via `extra_sycl_cflags`, just like with `extra_cflags` for C++.
SYCL compiler is expected to be found via system PATH environment
variable.

Parameters:

- **name** - The name of the extension to build. This MUST be the same as the
name of the pybind11 module!
- **sources** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) - A list of relative or absolute paths to C++ source files.
- **extra_cflags** - optional list of compiler flags to forward to the build.
- **extra_cuda_cflags** - optional list of compiler flags to forward to nvcc
when building CUDA sources.
- **extra_sycl_cflags** - optional list of compiler flags to forward to SYCL
compiler when building SYCL sources.
- **extra_ldflags** - optional list of linker flags to forward to the build.
- **extra_include_paths** - optional list of include directories to forward
to the build.
- **build_directory** - optional path to use as build workspace.
- **verbose** - If `True`, turns on verbose logging of load steps.
- **with_cuda** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|**None*) - Determines whether CUDA headers and libraries are added to
the build. If set to `None` (default), this value is
automatically determined based on the existence of `.cu` or
`.cuh` in `sources`. Set it to True` to force CUDA headers
and libraries to be included.
- **with_sycl** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*|**None*) - Determines whether SYCL headers and libraries are added to
the build. If set to `None` (default), this value is
automatically determined based on the existence of `.sycl` in
`sources`. Set it to True` to force SYCL headers and
libraries to be included.
- **is_python_module** - If `True` (default), imports the produced shared
library as a Python module. If `False`, behavior depends on
`is_standalone`.
- **is_standalone** - If `False` (default) loads the constructed extension
into the process as a plain dynamic library. If `True`, build a
standalone executable.

Returns:

Returns the loaded PyTorch extension as a Python module.

If `is_python_module` is `False` and `is_standalone` is `False`:

Returns nothing. (The shared library is loaded into the process as
a side effect.)

If `is_standalone` is `True`.

Return the path to the executable. (On Windows, TORCH_LIB_PATH is
added to the PATH environment variable as a side effect.)

Return type:

If `is_python_module` is `True`

Example

```
>>> from torch.utils.cpp_extension import load
>>> module = load(
... name='extension',
... sources=['extension.cpp', 'extension_kernel.cu'],
... extra_cflags=['-O2'],
... verbose=True)
```

torch.utils.cpp_extension.load_inline(*name*, *cpp_sources*, *cuda_sources=None*, *sycl_sources=None*, *functions=None*, *extra_cflags=None*, *extra_cuda_cflags=None*, *extra_sycl_cflags=None*, *extra_ldflags=None*, *extra_include_paths=None*, *build_directory=None*, *verbose=False*, *with_cuda=None*, *with_sycl=None*, *is_python_module=True*, *with_pytorch_error_handling=True*, *keep_intermediates=True*, *use_pch=False*, *no_implicit_headers=False*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L2100)

Load a PyTorch C++ extension just-in-time (JIT) from string sources.

This function behaves exactly like `load()`, but takes its sources as
strings rather than filenames. These strings are stored to files in the
build directory, after which the behavior of `load_inline()` is
identical to `load()`.

See [the
tests](https://github.com/pytorch/pytorch/blob/master/test/test_cpp_extensions_jit.py)
for good examples of using this function.

Sources may omit two required parts of a typical non-inline C++ extension:
the necessary header includes, as well as the (pybind11) binding code. More
precisely, strings passed to `cpp_sources` are first concatenated into a
single `.cpp` file. This file is then prepended with `#include
<torch/extension.h>`

Furthermore, if the `functions` argument is supplied, bindings will be
automatically generated for each function specified. `functions` can
either be a list of function names, or a dictionary mapping from function
names to docstrings. If a list is given, the name of each function is used
as its docstring.

The sources in `cuda_sources` are concatenated into a separate `.cu`
file and prepended with `torch/types.h`, `cuda.h` and
`cuda_runtime.h` includes. The `.cpp` and `.cu` files are compiled
separately, but ultimately linked into a single library. Note that no
bindings are generated for functions in `cuda_sources` per se. To bind
to a CUDA kernel, you must create a C++ function that calls it, and either
declare or define this C++ function in one of the `cpp_sources` (and
include its name in `functions`).

The sources in `sycl_sources` are concatenated into a separate `.sycl`
file and prepended with `torch/types.h`, `sycl/sycl.hpp` includes.
The `.cpp` and `.sycl` files are compiled separately, but ultimately
linked into a single library. Note that no bindings are generated for
functions in `sycl_sources` per se. To bind to a SYCL kernel, you must
create a C++ function that calls it, and either declare or define this
C++ function in one of the `cpp_sources` (and include its name
in `functions`).

See `load()` for a description of arguments omitted below.

Parameters:

- **cpp_sources** - A string, or list of strings, containing C++ source code.
- **cuda_sources** - A string, or list of strings, containing CUDA source code.
- **sycl_sources** - A string, or list of strings, containing SYCL source code.
- **functions** - A list of function names for which to generate function
bindings. If a dictionary is given, it should map function names to
docstrings (which are otherwise just the function names).
- **with_cuda** - Determines whether CUDA headers and libraries are added to
the build. If set to `None` (default), this value is
automatically determined based on whether `cuda_sources` is
provided. Set it to `True` to force CUDA headers
and libraries to be included.
- **with_sycl** - Determines whether SYCL headers and libraries are added to
the build. If set to `None` (default), this value is
automatically determined based on whether `sycl_sources` is
provided. Set it to `True` to force SYCL headers
and libraries to be included.
- **with_pytorch_error_handling** - Determines whether pytorch error and
warning macros are handled by pytorch instead of pybind. To do
this, each function `foo` is called via an intermediary `_safe_foo`
function. This redirection might cause issues in obscure cases
of cpp. This flag should be set to `False` when this redirect
causes issues.
- **no_implicit_headers** - If `True`, skips automatically adding headers, most notably
`#include <torch/extension.h>` and `#include <torch/types.h>` lines.
Use this option to improve cold start times when you
already include the necessary headers in your source code. Default: `False`.

Example

```
>>> from torch.utils.cpp_extension import load_inline
>>> source = """
at::Tensor sin_add(at::Tensor x, at::Tensor y) {
 return x.sin() + y.sin();
}
"""
>>> module = load_inline(name='inline_extension',
... cpp_sources=[source],
... functions=['sin_add'])
```

Note

Since load_inline will just-in-time compile the source code, please ensure
that you have the right toolchains installed in the runtime. For example,
when loading C++, make sure a C++ compiler is available. If you're loading
a CUDA extension, you will need to additionally install the corresponding CUDA
toolkit (nvcc and any other dependencies your code has). Compiling toolchains
are not included when you install torch and must be additionally installed.

During compiling, by default, the Ninja backend uses #CPUS + 2 workers to build
the extension. This may use up too many resources on some systems. One
can control the number of workers by setting the MAX_JOBS environment
variable to a non-negative number.

torch.utils.cpp_extension.include_paths(*device_type='cpu'*, *torch_include_dirs=True*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L1721)

Get the include paths required to build a C++ or CUDA or SYCL extension.

Parameters:

**device_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Defaults to "cpu".

Returns:

A list of include path strings.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

torch.utils.cpp_extension.get_compiler_abi_compatibility_and_version(*compiler*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L571)

Determine if the given compiler is ABI-compatible with PyTorch alongside its version.

Parameters:

**compiler** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The compiler executable name to check (e.g. `g++`).
Must be executable in a shell process.

Returns:

A tuple that contains a boolean that defines if the compiler is (likely) ABI-incompatible with PyTorch,
followed by a TorchVersion string that contains the compiler version separated by dots.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[bool](https://docs.python.org/3/library/functions.html#bool), *TorchVersion*]

torch.utils.cpp_extension.verify_ninja_availability()[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L2559)

Raise `RuntimeError` if [ninja](https://ninja-build.org/) build system is not available on the system, does nothing otherwise.

torch.utils.cpp_extension.is_ninja_available()[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/utils/cpp_extension.py#L2549)

Return `True` if the [ninja](https://ninja-build.org/) build system is available on the system, `False` otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)