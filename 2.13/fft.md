# torch.fft

Discrete Fourier transforms and related functions.

## Fast Fourier Transforms

| [`fft`](generated/torch.fft.fft.html#torch.fft.fft) | Computes the one dimensional discrete Fourier transform of `input`. |
| --- | --- |
| [`ifft`](generated/torch.fft.ifft.html#torch.fft.ifft) | Computes the one dimensional inverse discrete Fourier transform of `input`. |
| [`fft2`](generated/torch.fft.fft2.html#torch.fft.fft2) | Computes the 2 dimensional discrete Fourier transform of `input`. |
| [`ifft2`](generated/torch.fft.ifft2.html#torch.fft.ifft2) | Computes the 2 dimensional inverse discrete Fourier transform of `input`. |
| [`fftn`](generated/torch.fft.fftn.html#torch.fft.fftn) | Computes the N dimensional discrete Fourier transform of `input`. |
| [`ifftn`](generated/torch.fft.ifftn.html#torch.fft.ifftn) | Computes the N dimensional inverse discrete Fourier transform of `input`. |
| [`rfft`](generated/torch.fft.rfft.html#torch.fft.rfft) | Computes the one dimensional Fourier transform of real-valued `input`. |
| [`irfft`](generated/torch.fft.irfft.html#torch.fft.irfft) | Computes the inverse of [`rfft()`](generated/torch.fft.rfft.html#torch.fft.rfft). |
| [`rfft2`](generated/torch.fft.rfft2.html#torch.fft.rfft2) | Computes the 2-dimensional discrete Fourier transform of real `input`. |
| [`irfft2`](generated/torch.fft.irfft2.html#torch.fft.irfft2) | Computes the inverse of [`rfft2()`](generated/torch.fft.rfft2.html#torch.fft.rfft2). |
| [`rfftn`](generated/torch.fft.rfftn.html#torch.fft.rfftn) | Computes the N-dimensional discrete Fourier transform of real `input`. |
| [`irfftn`](generated/torch.fft.irfftn.html#torch.fft.irfftn) | Computes the inverse of [`rfftn()`](generated/torch.fft.rfftn.html#torch.fft.rfftn). |
| [`hfft`](generated/torch.fft.hfft.html#torch.fft.hfft) | Computes the one dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfft`](generated/torch.fft.ihfft.html#torch.fft.ihfft) | Computes the inverse of [`hfft()`](generated/torch.fft.hfft.html#torch.fft.hfft). |
| [`hfft2`](generated/torch.fft.hfft2.html#torch.fft.hfft2) | Computes the 2-dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfft2`](generated/torch.fft.ihfft2.html#torch.fft.ihfft2) | Computes the 2-dimensional inverse discrete Fourier transform of real `input`. |
| [`hfftn`](generated/torch.fft.hfftn.html#torch.fft.hfftn) | Computes the n-dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfftn`](generated/torch.fft.ihfftn.html#torch.fft.ihfftn) | Computes the N-dimensional inverse discrete Fourier transform of real `input`. |

## Helper Functions

| [`fftfreq`](generated/torch.fft.fftfreq.html#torch.fft.fftfreq) | Computes the discrete Fourier Transform sample frequencies for a signal of size `n`. |
| --- | --- |
| [`rfftfreq`](generated/torch.fft.rfftfreq.html#torch.fft.rfftfreq) | Computes the sample frequencies for [`rfft()`](generated/torch.fft.rfft.html#torch.fft.rfft) with a signal of size `n`. |
| [`fftshift`](generated/torch.fft.fftshift.html#torch.fft.fftshift) | Reorders n-dimensional FFT data, as provided by [`fftn()`](generated/torch.fft.fftn.html#torch.fft.fftn), to have negative frequency terms first. |
| [`ifftshift`](generated/torch.fft.ifftshift.html#torch.fft.ifftshift) | Inverse of [`fftshift()`](generated/torch.fft.fftshift.html#torch.fft.fftshift). |