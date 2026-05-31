# AOTInductor: Ahead-Of-Time Compilation for Torch.Export-ed Models

AOTInductor is a specialized version of
[TorchInductor](https://dev-discuss.pytorch.org/t/torchinductor-a-pytorch-native-compiler-with-define-by-run-ir-and-symbolic-shapes/747),
designed to process exported PyTorch models, optimize them, and produce shared libraries as well
as other relevant artifacts.
These compiled artifacts are specifically crafted for deployment in non-Python environments,
which are frequently employed for inference deployments on the server side.

In this tutorial, you will gain insight into the process of taking a PyTorch model, exporting it,
compiling it into an artifact, and conducting model predictions using C++.

## Model Compilation

To compile a model using AOTInductor, we first need to use
[`torch.export.export()`](export/api_reference.html#torch.export.export) to capture a given PyTorch model into a
computational graph. [torch.export](export.html#torch-export) provides soundness
guarantees and a strict specification on the IR captured, which AOTInductor
relies on.

We will then use `torch._inductor.aoti_compile_and_package()` to compile the
exported program using TorchInductor, and save the compiled artifacts into one
package. The package is in the format of a [PT2 Archive Spec](export/pt2_archive.html#export-pt2-archive).

Note

If you have a CUDA-enabled device on your machine and you installed PyTorch with CUDA support,
the following code will compile the model into a shared library for CUDA execution.
Otherwise, the compiled artifact will run on CPU. For better performance during CPU inference,
it is suggested to enable freezing by setting `export TORCHINDUCTOR_FREEZING=1`
before running the Python script below. The same behavior works in an environment with Intel®
GPU as well.

```
import os
import torch

class Model(torch.nn.Module):
 def __init__(self):
 super().__init__()
 self.fc1 = torch.nn.Linear(10, 16)
 self.relu = torch.nn.ReLU()
 self.fc2 = torch.nn.Linear(16, 1)
 self.sigmoid = torch.nn.Sigmoid()

 def forward(self, x):
 x = self.fc1(x)
 x = self.relu(x)
 x = self.fc2(x)
 x = self.sigmoid(x)
 return x

with torch.no_grad():
 device = "cuda" if torch.cuda.is_available() else "cpu"
 model = Model().to(device=device)
 example_inputs=(torch.randn(8, 10, device=device),)
 batch_dim = torch.export.Dim("batch", min=1, max=1024)
 # [Optional] Specify the first dimension of the input x as dynamic.
 exported = torch.export.export(model, example_inputs, dynamic_shapes={"x": {0: batch_dim}})
 # [Note] In this example we directly feed the exported module to aoti_compile_and_package.
 # Depending on your use case, e.g. if your training platform and inference platform
 # are different, you may choose to save the exported model using torch.export.save and
 # then load it back using torch.export.load on your inference platform to run AOT compilation.
 output_path = torch._inductor.aoti_compile_and_package(
 exported,
 # [Optional] Specify the generated shared library path. If not specified,
 # the generated artifact is stored in your system temp directory.
 package_path=os.path.join(os.getcwd(), "model.pt2"),
 # [Optional] Specify Inductor configs
 # This specific max_autotune option will turn on more extensive kernel autotuning for
 # better performance.
 inductor_configs={"max_autotune": True,},
 )
```

In this illustrative example, the `Dim` parameter is employed to designate the first dimension of
the input variable "x" as dynamic. Notably, the path and name of the compiled library remain unspecified,
resulting in the shared library being stored in a temporary directory.
To access this path from the C++ side, we save it to a file for later retrieval within the C++ code.

## Inference in Python

There are multiple ways to deploy the compiled artifact for inference, and one of that is using Python.
We have provided a convenient utility API in Python `torch._inductor.aoti_load_package()` for loading
and running the artifact, as shown in the following example:

```
import os
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = torch._inductor.aoti_load_package(os.path.join(os.getcwd(), "model.pt2"))
print(model(torch.randn(8, 10, device=device)))
```

The input at inference time should have the same size, dtype, and stride as the input at export time.

## Inference in C++

Next, we use the following example C++ file `inference.cpp` to load the compiled artifact,
enabling us to conduct model predictions directly within a C++ environment.

```
#include <iostream>
#include <vector>

#include <torch/torch.h>
#include <torch/csrc/inductor/aoti_package/model_package_loader.h>

int main() {
 c10::InferenceMode mode;

 torch::inductor::AOTIModelPackageLoader loader("model.pt2");
 // Assume running on CUDA
 std::vector<torch::Tensor> inputs = {torch::randn({8, 10}, at::kCUDA)};
 std::vector<torch::Tensor> outputs = loader.run(inputs);
 std::cout << "Result from the first inference:"<< std::endl;
 std::cout << outputs[0] << std::endl;

 // The second inference uses a different batch size and it works because we
 // specified that dimension as dynamic when compiling model.pt2.
 std::cout << "Result from the second inference:"<< std::endl;
 // Assume running on CUDA
 std::cout << loader.run({torch::randn({1, 10}, at::kCUDA)})[0] << std::endl;

 return 0;
}
```

For building the C++ file, you can make use of the provided `CMakeLists.txt` file, which
automates the process of invoking `python model.py` for AOT compilation of the model and compiling
`inference.cpp` into an executable binary named `aoti_example`.

```
cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(aoti_example)

find_package(Torch REQUIRED)

add_executable(aoti_example inference.cpp model.pt2)

add_custom_command(
 OUTPUT model.pt2
 COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/model.py
 DEPENDS model.py
)

target_link_libraries(aoti_example "${TORCH_LIBRARIES}")
set_property(TARGET aoti_example PROPERTY CXX_STANDARD 17)
```

Provided the directory structure resembles the following, you can execute the subsequent commands
to construct the binary. It is essential to note that the `CMAKE_PREFIX_PATH` variable
is crucial for CMake to locate the LibTorch library, and it should be set to an absolute path.
Please be mindful that your path may vary from the one illustrated in this example.

```
aoti_example/
 CMakeLists.txt
 inference.cpp
 model.py
```

```
$ mkdir build
$ cd build
$ CMAKE_PREFIX_PATH=/path/to/python/install/site-packages/torch/share/cmake cmake ..
$ cmake --build . --config Release
```

After the `aoti_example` binary has been generated in the `build` directory, executing it will
display results akin to the following:

```
$ ./aoti_example
Result from the first inference:
0.4866
0.5184
0.4462
0.4611
0.4744
0.4811
0.4938
0.4193
[ CUDAFloatType{8,1} ]
Result from the second inference:
0.4883
0.4703
[ CUDAFloatType{2,1} ]
```

## Troubleshooting

Below are some useful tools for debugging AOT Inductor.

Debugging Tools

- [torch._logging](../../logging.html)
- [AOTInductor Minifier](torch.compiler_aot_inductor_minifier.html)
- [AOTInductor Debugging Guide](torch.compiler_aot_inductor_debugging_guide.html)

To enable runtime checks on inputs, set the environment variable `AOTI_RUNTIME_CHECK_INPUTS` to 1. This will raise a `RuntimeError` if the inputs to the compiled model differ in size, data type, or strides from those used during export.

## API Reference

torch._inductor.aoti_compile_and_package(*exported_program*, *_deprecated_unused_args=None*, *_deprecated_unused_kwargs=None*, ***, *package_path=None*, *inductor_configs=None*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/_inductor/__init__.py#L57)

Compiles the exported program with AOTInductor, and packages it into a .pt2
artifact specified by the input package_path. To load the package, you can
call `torch._inductor.aoti_load_package(package_path)`.

An example usage is as follows:

```
ep = torch.export.export(M(), ...)
aoti_file = torch._inductor.aoti_compile_and_package(
 ep, package_path="my_package.pt2"
)
compiled_model = torch._inductor.aoti_load_package("my_package.pt2")
```

To compile and save multiple models into a single `.pt2` artifact, you can do
the following:

```
ep1 = torch.export.export(M1(), ...)
aoti_file1 = torch._inductor.aot_compile(
 ep1, ..., options={"aot_inductor.package": True}
)
ep2 = torch.export.export(M2(), ...)
aoti_file2 = torch._inductor.aot_compile(
 ep2, ..., options={"aot_inductor.package": True}
)

from torch._inductor.package import package_aoti, load_package

package_aoti("my_package.pt2", {"model1": aoti_file1, "model2": aoti_file2})

compiled_model1 = load_package("my_package.pt2", "model1")
compiled_model2 = load_package("my_package.pt2", "model2")
```

Parameters:

- **exported_program** ([*ExportedProgram*](export/api_reference.html#torch.export.ExportedProgram)) - An exported program created through a call from torch.export
- **package_path** (*FileLike**|**None*) - Optional specified path to the generated .pt2 artifact.
- **inductor_configs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**Any**]**|**None*) - Optional dictionary of configs to control inductor.

Returns:

Path to the generated artifact

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

torch._inductor.aoti_load_package(*path*, *run_single_threaded=False*, *device_index=-1*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/_inductor/__init__.py#L241)

Loads the model from the PT2 package.

If multiple models were packaged into the PT2, this will load the default
model. To load a specific model, you can directly call the load API

```
from torch._inductor.package import load_package

compiled_model1 = load_package("my_package.pt2", "model1")
compiled_model2 = load_package("my_package.pt2", "model2")
```

Parameters:

- **path** (*FileLike*) - Path to the .pt2 package
- **run_single_threaded** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether the model should be run without
thread synchronization logic. This is useful to avoid conflicts with
CUDAGraphs.
- **device_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The index of the device to which the PT2 package is
to be loaded. By default, device_index=-1 is used, which corresponds
to the device cuda when using CUDA. Passing device_index=1 would
load the package to cuda:1, for example.

Return type:

AOTICompiledModel