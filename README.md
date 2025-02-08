# Instructions

First, learn some python basics using the [class guide](https://gwu-cs-db-s24.github.io/hw1/).

Then apply that knowledge to solve these simple problems.

## Steps

1. Fill in the bodies for all of the functions in `main.py` following the instructions in the comments.
2. You can add your own tests that call the functions at the bottom of the file.
3. To verify your code, add your tests in `tests.py` need to evaluate all edge-cases.

You will be graded on the correctness of your `main.py` functions.

## Hints

Write these functions, one at a time, and write the tests to check the output of those functions as they are written.
As with all development, do it *iteratively*!

If, instead, you implement all functions, you'll likely have to go back and re-implement functions once you catch bugs while testings.

## Testing

Testing is hard, but very important!
Software engineers generally follow modern Test Driven Development (TDD) which is based on the idea that all features are tested, and when new code is added to a project, all tests are run to make sure that nothing breaks.
This is the *only way* for new team members (that will be you!) to efficiently interact with large code-bases.
It enables you to have confidence in your changes and updates.

So what do you consider when implementing tests?
Recall the tests written in software engineering.
You might characterize them as "test all conditions"!
For every feature, with some specification, you want to write a separate test for each of important conditions within that specification.
