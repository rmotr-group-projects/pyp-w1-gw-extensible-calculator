# Hint 2

The last feature we need to implement is the calculator's history. For that, we will need to save a record in the calculator's internal history for each operation we execute.

## Saving history records

Each record must contain the following information:
- Execution date and time
- Operation name
- Given parameters
- Result of the execution

As the result of the operation must be included, we need to save the record in the history **after** executing the operation, inside the `perform_operation` function.

For that we can use a helper function like this:

```python
def save_in_history(calc, operation, params, result):
    calc['history'].append(
        # we will append a tuple to the history
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         operation,
         params,
         result)
    )
```

We can then call the helper function from inside `perform_operation`, like this:

```python
def perform_operation(calc, operation, params):
    # validate parameters
    # execute operation and get the result
    save_in_history(calc, operation, params, result)
    return result
```


## Repeat last operation

Once we collect the history, we are able to call the last operation without actually executing the math underneath. For that, we just need to pick the last record in the history, and return the `result`.

```python
def repeat_last_operation(calc):
    history = calc['history']
    if not history:
        return None
    return history[-1][-1]
```
