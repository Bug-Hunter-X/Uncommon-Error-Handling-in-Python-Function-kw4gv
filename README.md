# Uncommon Error in Python Function

This repository demonstrates an uncommon error in Python function handling, specifically focusing on cases where multiple potential exceptions are not thoroughly addressed. The primary example shows a ZeroDivisionError occuring in multiple conditional branches.

## The Bug

The bug lies in the `function_with_uncommon_error` function.  The function attempts to return results depending on the values of `a` and `b`, but it fails to handle both scenarios where either `a` or `b` is zero correctly, leading to a `ZeroDivisionError`.  While it checks for `a` being zero, the `elif` doesn't prevent the error if `b` is zero. 

## The Solution

The solution involves improving the error-handling mechanism. This is typically achieved using `try-except` blocks.