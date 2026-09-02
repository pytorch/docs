# torch.cpu.get_capabilities

torch.cpu.get_capabilities()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cpu/__init__.py#L35)

Returns an immutable mapping of CPU capabilities detected at runtime.

This function queries the CPU for supported instruction sets and features
using cpuinfo. The result is cached after the first call for efficiency.

The returned mapping contains architecture-specific capabilities:

For x86/x86_64:

- SSE family: sse, sse2, sse3, ssse3, sse4_1, sse4_2, sse4a
- AVX family: avx, avx2, avx_vnni
- AVX-512 family: avx512_f, avx512_cd, avx512_dq, avx512_bw, avx512_vl,
avx512_ifma, avx512_vbmi, avx512_vbmi2, avx512_bitalg, avx512_vpopcntdq,
avx512_vnni, avx512_bf16, avx512_fp16, avx512_vp2intersect,
avx512_4vnniw, avx512_4fmaps
- AVX10 family: avx10_1, avx10_2
- AVX-VNNI-INT: avx_vnni_int8, avx_vnni_int16, avx_ne_convert
- AMX: amx_bf16, amx_tile, amx_int8, amx_fp16
- FMA: fma3, fma4
- Other: f16c, bmi, bmi2, popcnt, lzcnt, aes, sha, clflush, clflushopt, clwb

For ARM64:

- SIMD: neon, fp16_arith, bf16, i8mm, dot
- SVE: sve, sve2, sve_bf16, sve_max_length (when supported)
- SME: sme, sme2, sme_max_length (when supported)
- Other: atomics, fhm, rdm, crc32, aes, sha1, sha2, pmull

Common to all architectures:

- architecture: string identifying the CPU architecture

Returns:

An immutable mapping where keys are capability names
(e.g., 'avx2', 'sve') and values are booleans indicating
support, or integers for properties like vector lengths.

Return type:

MappingProxyType

Example

```
>>> caps = torch.cpu.get_capabilities()
>>> if caps.get("avx2", False):
... print("AVX2 is supported")
>>> print(f"Architecture: {caps['architecture']}")
```