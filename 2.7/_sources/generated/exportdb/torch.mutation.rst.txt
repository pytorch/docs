torch.mutation
==================
user_input_mutation
^^^^^^^^^^^^^^^^^^^

.. note::

    Tags: :doc:`torch.mutation <torch.mutation>`

    Support Level: SUPPORTED

Original source code:

.. code-block:: python

    # mypy: allow-untyped-defs
    import torch
    
    
    class UserInputMutation(torch.nn.Module):
        """
        Directly mutate user input in forward
        """
    
        def forward(self, x):
            x.mul_(2)
            return x.cos()
    
    
    example_args = (torch.randn(3, 2),)
    tags = {"torch.mutation"}
    model = UserInputMutation()
    

    torch.export.export(model, example_args)

Result:

.. code-block::

    ExportedProgram:
        class GraphModule(torch.nn.Module):
            def forward(self, x: "f32[3, 2]"):
                     mul_: "f32[3, 2]" = torch.ops.aten.mul_.Tensor(x, 2);  x = None
                
                     cos: "f32[3, 2]" = torch.ops.aten.cos.default(mul_);  mul_ = None
                return (cos,)
                
    Graph signature: ExportGraphSignature(input_specs=[InputSpec(kind=<InputKind.USER_INPUT: 1>, arg=TensorArgument(name='x'), target=None, persistent=None)], output_specs=[OutputSpec(kind=<OutputKind.USER_OUTPUT: 1>, arg=TensorArgument(name='cos'), target=None)])
    Range constraints: {}
    
