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
How It Worksfreq: A standard Python dictionary used to store items as keys and their counts as 
values.freq.get(num, 0): 

This is the safest way to look up a key. The .get() method looks for num in the dictionary. 
If num exists, it returns its current count. 
If num is not in the dictionary yet, instead of throwing a KeyError, it returns the default value: 0.+ 1: Increments the retrieved count by 1.freq[num] = ...: Saves the updated count back into the dictionary.

Step-by-Step ExampleIf you are iterating through a list [5, 5, 2] using a loop like for num in nums::Step

Current numfreq.get(num, 0) evaluates to...Resulting state of freq dictionary15 (First time seen)0 (Key doesn't exist yet, returns default 0 + 1){5: 1}
--> 5 (Seen again)1 (Key exists, returns current value 1 + 1){5: 2}32 (First time seen)0 (Key doesn't exist yet, returns default 0 + 1)
{5: 2, 2: 1}

---------------------------------------------------------------------------------------------
DUTCH NATIONAL FLAG ALGORITHM WHY WE ARE USING IT.

Yes. The **main reason we use the Dutch National Flag algorithm** is:

> We want to sort `0, 1, 2` in **O(n) time and O(1) extra space**, without using a normal sorting algorithm.

But let's understand **why we need it**, instead of memorizing it.

### Think about the problem

Suppose:

```text
[2, 0, 2, 1, 1, 0]
```

We know there are only **three types of numbers**:

```text
0 → should go LEFT
1 → should stay in MIDDLE
2 → should go RIGHT
```

So instead of comparing every number with every other number like normal sorting, we can divide the array into **three regions**.

```text
0s | 1s | unknown | 2s
```

We use:

```text
low    → boundary of 0s
mid    → number we are currently checking
high   → boundary of 2s
```

### Why is this useful?

Imagine:

```text
[0, 0, ?, ?, ?, 2, 2]
       ↑       ↑
      mid     high
```

We already know:

* Everything before `low` is correctly `0`
* Everything after `high` is correctly `2`
* Only the middle part is unknown

Every time we inspect one element, we make the unknown area smaller.

---

### Example

```text
[2, 0, 1, 2, 1, 0]
 ↑              ↑
mid            high
```

`mid` sees `2`.

We know:

> "2 belongs at the right."

So swap it with `high`.

```text
[0, 0, 1, 2, 1, 2]
 ↑        ↑     ↑
low      mid   high
```

Now that `2` is permanently in the right region.

Then we continue.

---

### Why not just use `.sort()`?

We can:

```python
arr.sort()
```

But that's a general-purpose sorting operation.

The Dutch National Flag algorithm takes advantage of a **special property of this problem**:

```text
There are ONLY 0, 1 and 2.
```

Therefore we can achieve:

```text
Normal sorting       → O(n log n)
Dutch National Flag  → O(n)
```

and:

```text
Extra space → O(1)
```

### The real idea to remember

Don't memorize:

> "Dutch National Flag = three pointers."

Instead remember:

> **"0 goes left, 2 goes right, and 1 is already where it should be."**

Then the three pointers naturally make sense:

```text
0s | 1s | UNKNOWN | 2s
 ↑      ↑         ↑
low    mid       high
```

That's **why** we use Dutch National Flag here. It isn't a random trick — we're exploiting the fact that there are only **three possible values**.
