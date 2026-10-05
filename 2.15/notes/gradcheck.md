# Gradcheck mechanics

This note presents an overview of how the [`gradcheck()`](../autograd.html#module-torch.autograd.gradcheck) and `gradgradcheck()` functions work.

It will cover both forward and backward mode AD for both real and complex-valued functions as well as higher-order derivatives.
This note also covers both the default behavior of gradcheck as well as the case where `fast_mode=True` argument is passed (referred to as fast gradcheck below).

## Notations and background information

Throughout this note, we will use the following convention:

1. xxx, yyy, aaa, bbb, vvv, uuu, ururur and uiuiui are real-valued vectors and zzz is a complex-valued vector that can be rewritten in terms of two real-valued vectors as z=a+ibz = a + i bz=a+ib.
2. NNN and MMM are two integers that we will use for the dimension of the input and output space respectively.
3. f:RN→RMf: \mathcal{R}^N \to \mathcal{R}^Mf:RN→RM is our basic real-to-real function such that y=f(x)y = f(x)y=f(x).
4. g:CN→RMg: \mathcal{C}^N \to \mathcal{R}^Mg:CN→RM is our basic complex-to-real function such that y=g(z)y = g(z)y=g(z).

For the simple real-to-real case, we write as JfJ_fJf​ the Jacobian matrix associated with fff of size M×NM \times NM×N.
This matrix contains all the partial derivatives such that the entry at position (i,j)(i, j)(i,j) contains ∂yi∂xj\frac{\partial y_i}{\partial x_j}∂xj​∂yi​​.
Backward mode AD is then computing, for a given vector vvv of size MMM, the quantity vTJfv^T J_fvTJf​.
Forward mode AD on the other hand is computing, for a given vector uuu of size NNN, the quantity JfuJ_f uJf​u.

For functions that contain complex values, the story is a lot more complex. We only provide the gist here and the full description can be found at [Autograd for Complex Numbers](autograd.html#complex-autograd-doc).

The constraints to satisfy complex differentiability (Cauchy-Riemann equations) are too restrictive for all real-valued loss functions, so we instead opted to use Wirtinger calculus.
In a basic setting of Wirtinger calculus, the chain rule requires access to both the Wirtinger derivative (called WWW below) and the Conjugate Wirtinger derivative (called CWCWCW below).
Both WWW and CWCWCW need to be propagated because in general, despite their name, one is not the complex conjugate of the other.

To avoid having to propagate both values, for backward mode AD, we always work under the assumption that the function whose derivative is being calculated is either a real-valued function or is part of a bigger real-valued function. This assumption means that all the intermediary gradients we compute during the backward pass are also associated with real-valued functions.
In practice, this assumption is not restrictive when doing optimization as such problem require real-valued objectives (as there is no natural ordering of the complex numbers).

Under this assumption, using WWW and CWCWCW definitions, we can show that W=CW∗W = CW^*W=CW∗ (we use ∗*∗ to denote complex conjugation here) and so only one of the two values actually need to be "backwarded through the graph" as the other one can easily be recovered.
To simplify internal computations, PyTorch uses 2∗CW2 * CW2∗CW as the value it backwards and returns when the user asks for gradients.
Similarly to the real case, when the output is actually in RM\mathcal{R}^MRM, backward mode AD does not compute 2∗CW2 * CW2∗CW but only vT(2∗CW)v^T (2 * CW)vT(2∗CW) for a given vector v∈RMv \in \mathcal{R}^Mv∈RM.

For forward mode AD, we use a similar logic, in this case, assuming that the function is part of a larger function whose input is in R\mathcal{R}R. Under this assumption, we can make a similar claim that every intermediary result corresponds to a function whose input is in R\mathcal{R}R and in this case, using WWW and CWCWCW definitions, we can show that W=CWW = CWW=CW for the intermediary functions.
To make sure the forward and backward mode compute the same quantities in the elementary case of a one dimensional function, the forward mode also computes 2∗CW2 * CW2∗CW.
Similarly to the real case, when the input is actually in RN\mathcal{R}^NRN, forward mode AD does not compute 2∗CW2 * CW2∗CW but only (2∗CW)u(2 * CW) u(2∗CW)u for a given vector u∈RNu \in \mathcal{R}^Nu∈RN.

## Default backward mode gradcheck behavior

### Real-to-real functions

To test a function f:RN→RM,x→yf: \mathcal{R}^N \to \mathcal{R}^M, x \to yf:RN→RM,x→y, we reconstruct the full Jacobian matrix JfJ_fJf​ of size M×NM \times NM×N in two ways: analytically and numerically.
The analytical version uses our backward mode AD while the numerical version uses finite difference.
The two reconstructed Jacobian matrices are then compared elementwise for equality.

#### Default real input numerical evaluation

If we consider the elementary case of a one-dimensional function (N=M=1N = M = 1N=M=1), then we can use the basic finite difference formula from [the wikipedia article](https://en.wikipedia.org/wiki/Finite_difference). We use the "central difference" for better numerical properties:

∂y∂x≈f(x+eps)−f(x−eps)2∗eps\frac{\partial y}{\partial x} \approx \frac{f(x + eps) - f(x - eps)}{2 * eps}∂x∂y​≈2∗epsf(x+eps)−f(x−eps)​

This formula easily generalizes for multiple outputs (M>1M \gt 1M>1) by having ∂y∂x\frac{\partial y}{\partial x}∂x∂y​ be a column vector of size M×1M \times 1M×1 like f(x+eps)f(x + eps)f(x+eps).
In that case, the above formula can be reused as-is and approximates the full Jacobian matrix with only two evaluations of the user function (namely f(x+eps)f(x + eps)f(x+eps) and f(x−eps)f(x - eps)f(x−eps)).

It is more computationally expensive to handle the case with multiple inputs (N>1N \gt 1N>1). In this scenario, we loop over all the inputs one after the other and apply the epsepseps perturbation for each element of xxx one after the other. This allows us to reconstruct the JfJ_fJf​ matrix column by column.

#### Default real input analytical evaluation

For the analytical evaluation, we use the fact, as described above, that backward mode AD computes vTJfv^T J_fvTJf​.
For functions with a single output, we simply use v=1v = 1v=1 to recover the full Jacobian matrix with a single backward pass.

For functions with more than one output, we resort to a for-loop which iterates over the outputs where each vvv is a one-hot vector corresponding to each output one after the other. This allows to reconstruct the JfJ_fJf​ matrix row by row.

### Complex-to-real functions

To test a function g:CN→RM,z→yg: \mathcal{C}^N \to \mathcal{R}^M, z \to yg:CN→RM,z→y with z=a+ibz = a + i bz=a+ib, we reconstruct the (complex-valued) matrix that contains 2∗CW2 * CW2∗CW.

#### Default complex input numerical evaluation

Consider the elementary case where N=M=1N = M = 1N=M=1 first. We know from (chapter 3 of) [this research paper](https://arxiv.org/pdf/1701.00392.pdf) that:

CW:=∂y∂z∗=12∗(∂y∂a+i∂y∂b)CW := \frac{\partial y}{\partial z^*} = \frac{1}{2} * (\frac{\partial y}{\partial a} + i \frac{\partial y}{\partial b})CW:=∂z∗∂y​=21​∗(∂a∂y​+i∂b∂y​)

Note that ∂y∂a\frac{\partial y}{\partial a}∂a∂y​ and ∂y∂b\frac{\partial y}{\partial b}∂b∂y​, in the above equation, are R→R\mathcal{R} \to \mathcal{R}R→R derivatives.
To evaluate these numerically, we use the method described above for the real-to-real case.
This allows us to compute the CWCWCW matrix and then multiply it by 222.

Note that the code, as of time of writing, computes this value in a slightly convoluted way:

```
# Code from https://github.com/pytorch/pytorch/blob/58eb23378f2a376565a66ac32c93a316c45b6131/torch/autograd/gradcheck.py#L99-L105
# Notation changes in this code block:
# s here is y above
# x, y here are a, b above

ds_dx = compute_gradient(eps)
ds_dy = compute_gradient(eps * 1j)
# conjugate wirtinger derivative
conj_w_d = 0.5 * (ds_dx + ds_dy * 1j)
# wirtinger derivative
w_d = 0.5 * (ds_dx - ds_dy * 1j)
d[d_idx] = grad_out.conjugate() * conj_w_d + grad_out * w_d.conj()

# Since grad_out is always 1, and W and CW are complex conjugate of each other, the last line ends up computing exactly `conj_w_d + w_d.conj() = conj_w_d + conj_w_d = 2 * conj_w_d`.
```

#### Default complex input analytical evaluation

Since backward mode AD computes exactly twice the CWCWCW derivative already, we simply use the same trick as for the real-to-real case here and reconstruct the matrix row by row when there are multiple real outputs.

### Functions with complex outputs

In this case, the user-provided function does not follow the assumption from the autograd that the function we compute backward AD for is real-valued.
This means that using autograd directly on this function is not well defined.
To solve this, we will replace the test of the function h:PN→CMh: \mathcal{P}^N \to \mathcal{C}^Mh:PN→CM (where P\mathcal{P}P can be either R\mathcal{R}R or C\mathcal{C}C), with two functions: hrhrhr and hihihi such that:

hr(q):=real(f(q))hi(q):=imag(f(q))\begin{aligned}
 hr(q) &:= real(f(q)) \\
 hi(q) &:= imag(f(q))
\end{aligned}hr(q)hi(q)​:=real(f(q)):=imag(f(q))​

where q∈Pq \in \mathcal{P}q∈P.
We then do a basic gradcheck for both hrhrhr and hihihi using either the real-to-real or complex-to-real case described above, depending on P\mathcal{P}P.

Note that, the code, as of time of writing, does not create these functions explicitly but perform the chain rule with the realrealreal or imagimagimag functions manually by passing the grad_out\text{grad\_out}grad_out arguments to the different functions.
When grad_out=1\text{grad\_out} = 1grad_out=1, then we are considering hrhrhr.
When grad_out=1j\text{grad\_out} = 1jgrad_out=1j, then we are considering hihihi.

## Fast backward mode gradcheck

While the above formulation of gradcheck is great, both, to ensure correctness and debuggability, it is very slow because it reconstructs the full Jacobian matrices.
This section presents a way to perform gradcheck in a faster way without affecting its correctness.
The debuggability can be recovered by adding special logic when we detect an error. In that case, we can run the default version that reconstructs the full matrix to give full details to the user.

The high level strategy here is to find a scalar quantity that can be computed efficiently by both the numerical and analytical methods and that represents the full matrix computed by the slow gradcheck well enough to ensure that it will catch any discrepancy in the Jacobians.

### Fast gradcheck for real-to-real functions

The scalar quantity that we want to compute here is vTJfuv^T J_f uvTJf​u for a given random vector v∈RMv \in \mathcal{R}^Mv∈RM and a random unit norm vector u∈RNu \in \mathcal{R}^Nu∈RN.

For the numerical evaluation, we can efficiently compute

Jfu≈f(x+u∗eps)−f(x−u∗eps)2∗eps.J_f u \approx \frac{f(x + u * eps) - f(x - u * eps)}{2 * eps}.Jf​u≈2∗epsf(x+u∗eps)−f(x−u∗eps)​.

We then perform the dot product between this vector and vvv to get the scalar value of interest.

For the analytical version, we can use backward mode AD to compute vTJfv^T J_fvTJf​ directly. We then perform the dot product with uuu to get the expected value.

### Fast gradcheck for complex-to-real functions

Similar to the real-to-real case, we want to perform a reduction of the full matrix. But the 2∗CW2 * CW2∗CW matrix is complex-valued and so in this case, we will compare to complex scalars.

Due to some constraints on what we can compute efficiently in the numerical case and to keep the number of numerical evaluations to a minimum, we compute the following (albeit surprising) scalar value:

s:=2∗vT(real(CW)ur+i∗imag(CW)ui)s := 2 * v^T (real(CW) ur + i * imag(CW) ui)s:=2∗vT(real(CW)ur+i∗imag(CW)ui)

where v∈RMv \in \mathcal{R}^Mv∈RM, ur∈RNur \in \mathcal{R}^Nur∈RN and ui∈RNui \in \mathcal{R}^Nui∈RN.

#### Fast complex input numerical evaluation

We first consider how to compute sss with a numerical method. To do so, keeping in mind that we're considering g:CN→RM,z→yg: \mathcal{C}^N \to \mathcal{R}^M, z \to yg:CN→RM,z→y with z=a+ibz = a + i bz=a+ib, and that CW=12∗(∂y∂a+i∂y∂b)CW = \frac{1}{2} * (\frac{\partial y}{\partial a} + i \frac{\partial y}{\partial b})CW=21​∗(∂a∂y​+i∂b∂y​), we rewrite it as follows:

s=2∗vT(real(CW)ur+i∗imag(CW)ui)=2∗vT(12∗∂y∂aur+i∗12∗∂y∂bui)=vT(∂y∂aur+i∗∂y∂bui)=vT((∂y∂aur)+i∗(∂y∂bui))\begin{aligned}
 s &= 2 * v^T (real(CW) ur + i * imag(CW) ui) \\
 &= 2 * v^T (\frac{1}{2} * \frac{\partial y}{\partial a} ur + i * \frac{1}{2} * \frac{\partial y}{\partial b} ui) \\
 &= v^T (\frac{\partial y}{\partial a} ur + i * \frac{\partial y}{\partial b} ui) \\
 &= v^T ((\frac{\partial y}{\partial a} ur) + i * (\frac{\partial y}{\partial b} ui))
\end{aligned}s​=2∗vT(real(CW)ur+i∗imag(CW)ui)=2∗vT(21​∗∂a∂y​ur+i∗21​∗∂b∂y​ui)=vT(∂a∂y​ur+i∗∂b∂y​ui)=vT((∂a∂y​ur)+i∗(∂b∂y​ui))​

In this formula, we can see that ∂y∂aur\frac{\partial y}{\partial a} ur∂a∂y​ur and ∂y∂bui\frac{\partial y}{\partial b} ui∂b∂y​ui can be evaluated the same way as the fast version for the real-to-real case.
Once these real-valued quantities have been computed, we can reconstruct the complex vector on the right side and do a dot product with the real-valued vvv vector.

#### Fast complex input analytical evaluation

For the analytical case, things are simpler and we rewrite the formula as:

s=2∗vT(real(CW)ur+i∗imag(CW)ui)=vTreal(2∗CW)ur+i∗vTimag(2∗CW)ui)=real(vT(2∗CW))ur+i∗imag(vT(2∗CW))ui\begin{aligned}
 s &= 2 * v^T (real(CW) ur + i * imag(CW) ui) \\
 &= v^T real(2 * CW) ur + i * v^T imag(2 * CW) ui) \\
 &= real(v^T (2 * CW)) ur + i * imag(v^T (2 * CW)) ui
\end{aligned}s​=2∗vT(real(CW)ur+i∗imag(CW)ui)=vTreal(2∗CW)ur+i∗vTimag(2∗CW)ui)=real(vT(2∗CW))ur+i∗imag(vT(2∗CW))ui​

We can thus use the fact that the backward mode AD provides us with an efficient way to compute vT(2∗CW)v^T (2 * CW)vT(2∗CW) and then perform a dot product of the real part with ururur and the imaginary part with uiuiui before reconstructing the final complex scalar sss.

#### Why not use a complex uuu

At this point, you might be wondering why we did not select a complex uuu and just performed the reduction 2∗vTCWu′2 * v^T CW u'2∗vTCWu′.
To dive into this, in this paragraph, we will use the complex version of uuu noted u′=ur′+iui′u' = ur' + i ui'u′=ur′+iui′.
Using such complex u′u'u′, the problem is that when doing the numerical evaluation, we would need to compute:

2∗CWu′=(∂y∂a+i∂y∂b)(ur′+iui′)=∂y∂aur′+i∂y∂aui′+i∂y∂bur′−∂y∂bui′\begin{aligned}
 2*CW u' &= (\frac{\partial y}{\partial a} + i \frac{\partial y}{\partial b})(ur' + i ui') \\
 &= \frac{\partial y}{\partial a} ur' + i \frac{\partial y}{\partial a} ui' + i \frac{\partial y}{\partial b} ur' - \frac{\partial y}{\partial b} ui'
\end{aligned}2∗CWu′​=(∂a∂y​+i∂b∂y​)(ur′+iui′)=∂a∂y​ur′+i∂a∂y​ui′+i∂b∂y​ur′−∂b∂y​ui′​

Which would require four evaluations of real-to-real finite difference (twice as much compared to the approached proposed above).
Since this approach does not have more degrees of freedom (same number of real valued variables) and we try to get the fastest possible evaluation here, we use the other formulation above.

### Fast gradcheck for functions with complex outputs

Just like in the slow case, we consider two real-valued functions and use the appropriate rule from above for each function.

## Gradgradcheck implementation

PyTorch also provide a utility to verify second order gradients. The goal here is to make sure that the backward implementation is also properly differentiable and computes the right thing.

This feature is implemented by considering the function F:x,v→vTJfF: x, v \to v^T J_fF:x,v→vTJf​ and use the gradcheck defined above on this function.
Note that vvv in this case is just a random vector with the same type as f(x)f(x)f(x).

The fast version of gradgradcheck is implemented by using the fast version of gradcheck on that same function FFF.