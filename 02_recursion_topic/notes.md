Unwinding in recursion means the step-by-step process where the computer finishes the base case and returns back through each previous waiting function call in reverse order.

How Unwinding Works Going down (The Dive): The program calls a function over and over. Each new call pauses the current one and waits for an answer.

Hitting the end (Base Case): The function reaches a stopping point that does not need another call.

Coming back up (The Unwinding): The computer solves the last call, pops it off the call stack, and goes back to the line right after the previous call.

Post-Order Printing and Unwinding A post-order print puts the print statement after the recursive call.Because of this order, the computer cannot print anything on the way down.It must wait until the recursion hits the bottom and starts unwinding back up.

As it unwinds, it runs the print lines in reverse order (from the deepest call back to the first original call).


RECURSION STRUCTURE 

Every recursive function follows the **same 3-part blueprint**:

```python
def recursive_function(data):
    # 1. BASE CASE (When to stop)
    if stop_condition:
        return base_value

    # 2. WORK / PROCESSING (Optional)
    # Do something with data here (or after the step)

    # 3. RECURSIVE STEP (Moving closer to the base case)
    return recursive_function(smaller_data)

```

---

### The 3 Core Rules Explained

#### 1. Base Case (The Guardrail)

* **What it is:** The simplest possible input where the answer is known immediately without further calculation.
* **Why it matters:** Without this, your function loops forever until Python throws a `RecursionError` (Stack Overflow).

#### 2. Recursive Call (The Step)

* **What it is:** The function calling itself.
* **Golden Rule:** The argument **must change** to get closer to the base case (e.g., `n - 1`, `left + 1`, `arr[1:]`).

#### 3. Combination / Return (The Assembly)

* **What it is:** Combining the result of the recursive call with the current step's work to build the final answer.

---

### Applied Examples

#### Example 1: Sum of numbers from $1$ to $N$

```python
def sum_to_n(n):
    # 1. Base Case
    A base case in recursion should be an if statement, not a while loop.
    if n == 1:
        return 1

    # 2 & 3. Recursive Step + Combination
    return n + sum_to_n(n - 1)  # n-1 moves closer to 1

```

#### Example 2: Checking if a string is a Palindrome

```python
def is_palindrome(s, left, right):
    # 1. Base Case
    if left >= right:
        return True

    # 2. Work / Validation
    if s[left] != s[right]:
        return False

    # 3. Recursive Step
    return is_palindrome(s, left + 1, right - 1)

```

---
