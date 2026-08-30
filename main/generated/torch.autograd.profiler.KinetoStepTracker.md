# KinetoStepTracker

*class*torch.autograd.profiler.KinetoStepTracker[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/profiler.py#L1295)

Provides an abstraction for incrementing the step count globally.

Previously, we only had one place to mark that a step() has occurred
in the program via pytorch profiler step(). We will now add step hooks
in the Optimizer class [pytorch/pytorch#88446](https://github.com/pytorch/pytorch/issues/88446)

- This could mean programs that already call profiler.step() every
iteration can end up double incrementing step count.
- If a model uses multiple optimizers we can also have double or more
counting of the step.

We fix this by adding a layer of abstraction before calling step()
to the kineto library. The idea is to maintain steps per requester in a dict:

```
{
 "ProfilerStep": 100, # triggered by profiler step() call
 "Optimizer1Step": 100, # Optimizer 1 or 2 are just examples, could be SGD, Adam etc
 "Optimizer2Step": 100,
}
```

To figure out the global step count just take the max of dict values (100).

If one of the count increments the max will go up.

```
{
 "ProfilerStep": 100,
 "Optimizer1Step": 101, # Optimizer1 got incremented first say
 "Optimizer2Step": 100,
}
```

Then global step count is 101
We only call the kineto step() function when global count increments.

NOTE: Please do not use the KinetoStepTracker in modules beside the Optimizer
for now. The result could be incorrect increments of the step count.

*classmethod*current_step()[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/profiler.py#L1379)

Get the latest step for any requester

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

*classmethod*erase_step_count(*requester*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/profiler.py#L1347)

Remove a given requester.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

*classmethod*increment_step(*requester*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/profiler.py#L1354)

Increments the step count for the requester.

Additionally if the max over all step counts has incremented then
trigger the _kineto_step() returns global step count

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

*classmethod*init_step_count(*requester*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/autograd/profiler.py#L1340)

Initialize for a given requester.