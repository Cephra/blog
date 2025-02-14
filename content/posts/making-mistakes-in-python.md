+++
title = "Making Mistakes in Python"
date = 2025-02-14 21:52:05+00:00
summary = "I talk about mistakes I made in Python due to reused instances. I explain how using a parameter with a default value can lead to unexpected behavior and provide examples of safe alternatives."
+++
## Avoiding Pitfalls: Handling Mistakes in Python Code
### A Cautionary Tale of Reused Instances in Python

As someone who's spent countless hours developing tools like an AI blog post generator, I've learned valuable lessons about designing robust and predictable code. One such lesson was learned the hard way when I encountered unexpected behavior due to reused instances.

I had created a series of wrapper classes that would handle various tasks related to content generation. Each class had a constructor that accepted optional parameters for customization. Specifically, one parameter caught my attention: `history`. Initially, I set its default value to `History()`, intending it to create a new instance of the `History` class whenever the object was instantiated.

However, this seemingly innocuous decision led to issues down the line. When generating content, I noticed that changes made to the history were not being reflected as expected. After some investigation, I discovered that the same instance of the `History` class was being reused across multiple instances. This behavior was causing problems because the history wasn't being properly updated.

### Handling Parameters with Default Values in Python Functions

When designing functions that take optional parameters, it's essential to consider how they behave. Let's examine two different ways to define a function `f` that takes an object `param` as input.

#### Example 1: Unintended Consequences of Reused Instances

```python
def f(param=SomeClass()):
    # unless param is explicitly passed in, the same instance will be used for all calls to f
    param.do_something()
```

In this example, if you don't pass an argument when calling `f`, it will always use the same instance of `SomeClass`. This can lead to unexpected behavior.

#### Example 2: Safely Handling Reused Instances

```python
def f(param=None):
    if param is None:
        param = SomeClass()
```

The second approach is safer and more explicit. If `param` is not provided, it creates a new instance of `SomeClass`. This way, you avoid any potential issues related to reused instances.

#### Benefits of the Second Approach

Using the second example has several benefits:

*   **Explicitness**: It's clear that if no argument is passed, a new instance will be created.
*   **Easier Debugging**: If unexpected behavior occurs, it's easier to identify the issue since each function call has its own object.

In summary, when defining functions with optional parameters, use the second approach (with a default value of `None` and an explicit creation of a new instance if not provided) for safer and more predictable results.
