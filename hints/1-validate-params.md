# Hint 1

Before executing any operation in our calculator, 
we need to make sure that given parameters are valid. That means:
- The `params` argument must be of type `tuple`.
- All elements contained in the tuple must be either `int` or `float`.

We could approach that in the following way:

```python
# simple way
def are_valid_params(params):
    if not isinstance(params, tuple):
        return False
    for elem in params:
        if not isinstance(elem, (int, float)):
          return False
    return True
```

or in this way:

```python
# fancy way
def are_valid_params(params):
    try:
        assert isinstance(params, tuple)
        assert all([isinstance(value, (int, float)) for value in params])
    except AssertionError:
        return False
    return True
```

With this helper function, we can check that given params are valid and then keep executing the calculator normally.

```python
def perform_operation(calc, operation, params):
    # your code here
    if not are_valid_params(params):
        raise InvalidParams('Given params are invalid.')
    # your code here
```
