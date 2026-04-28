# Autoload Mechanism

The **Autoload** mechanism in PyTorch simplifies the integration of a custom backend by enabling automatic discovery and initialization at runtime. This eliminates the need for explicit imports or manual initialization, allowing developers to seamlessly integrate a new accelerator or backend into PyTorch.

## Background

The **Autoload Device Extension** proposal in PyTorch is centered on improving support for various hardware backend devices, especially those implemented as out-of-the-tree extensions (not part of PyTorch's main codebase). Currently, users must manually import or load these device-specific extensions to use them, which complicates the experience and increases cognitive overhead.

In contrast, in-tree devices (devices officially supported within PyTorch) are seamlessly integrated--users don't need extra imports or steps. The goal of autoloading is to make out-of-the-tree devices just as easy to use, so users can follow the standard PyTorch device programming model without explicit loading or code changes. This would allow existing PyTorch applications to run on new devices without any modification, making hardware support more user-friendly and reducing barriers to adoption.

For more information about the background of **Autoload**, please refer to its [RFC](https://github.com/pytorch/pytorch/issues/122468).

## Design

The core idea of **Autoload** is to Use Python's plugin discovery (entry points) so PyTorch automatically loads out-of-tree device extensions when torch is imported--no explicit user import needed.

For more instructions of the design of **Autoload**, please refer to [**How it works**](https://docs.pytorch.org/tutorials/unstable/python_extension_autoload.html#how-it-works).

## Implementation

This tutorial will take **OpenReg** as a new out-of-the-tree device and guide you through the steps to enable and use the **Autoload** mechanism.

### Entry Point Setup

To enable **Autoload**, register the `_autoload` function as an entry point in [setup.py](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/setup.py) file.

Python

```
1 setup(
 2 packages=find_packages(),
 3 package_data=package_data,
 4 ext_modules=ext_modules,
 5 cmdclass={
 6 "clean": BuildClean, # type: ignore[misc]
 7 },
 8 include_package_data=False,
 9 entry_points={
10 "torch.backends": [
11 "torch_openreg = torch_openreg:_autoload",
12 ],
13 },
14 )
```

### Backend Setup

Define the initialization hook `_autoload` for backend initialization in [torch_openreg](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/torch_openreg/__init__.py). This hook will be automatically invoked by PyTorch during startup.

PYTHON

```
1def _autoload():
2 # It is a placeholder function here to be registered as an entry point.
3 pass
4
5
```

## Result

After setting up the entry point and backend, build and install your backend. Now, we can use the new accelerator without explicitly importing it.

 Without Autoload

```
>>> import torch
>>> import torch_openreg
>>> torch.tensor(1, device="openreg")
tensor(1, device='openreg:0')
```

 With Autoload

```
>>> import torch # Automatically import torch_openreg
>>>
>>> torch.tensor(1, device="openreg")
tensor(1, device='openreg:0')
```