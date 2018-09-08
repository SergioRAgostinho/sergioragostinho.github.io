---
title: Parameter order in C++ functions
location: Lisbon, Portugal
excerpt: A brief reflection on parameter ordering in functions.
tags: [development, c++]
---

## Introduction

One of the most common (minor) problems a developer faces at some point in his life, besides finding the perfect keyboard which maximizes your *type-fu*, is having to decide parameter order when writing a function signature. This is a question which is common to all programing languages, but the best answer is specific to each one. In this post I'll address it from a C++ perspective.

```c++
// T is a generic type

void function_a (const T& in_1, const T& in_2, T& out_1, T& out_2);

void function_b (T& out_1, T& out_2, const T& in_1, const T& in_2);

void function_c (const T& in_1, T& out_1, const T& in_2, T& out_2);
```


Consider the code snippet above and assume there's no functional difference between functions `a`, `b` and `c` other than the parameter order. Which one would you pick?

> Does it even matter?

I'm going to burn a couple of bytes out of your Internet bandwidth convincing you that yes, it does. Picking a good parameter order allows you to save time when using that code later on by fully exploiting a neat C++ feature called **default arguments**. Also, if you ever underwent the task of reviewing code yourself, you're likely to have noticed that quality code usually exhibits a clear structure and enforces a strict set of patterns which are applied recurrently. I expect you to be able to do the same, applying the ideas you'll read here.

## Default Arguments

- Difference between parameter and argument

- cpp reference : http://en.cppreference.com/w/cpp/language/default_arguments

## Back to the Ordering Problem

### Mixing Inputs and Outputs

> Is there a problem in mixing input and output parameters?

- There's no reason to do it.

### Inputs or Outputs first?

- outs should be first than ins
	- main reason is the default parameter mechanism
	- The ones which change are


### How to order Inputs


## Summary
