Getting Started with Testing | NewsKit design system

Getting Started with Testing
============================

Unit Testing
------------

NewsKit uses Jest and React Testing Library for unit testing.

There is an existing memory leak issue with Jest. See [Memory Leak in Jest](https://github.com/facebook/jest/issues/7874). If your tests are running slow using Jest, we recommended that you try the following arguments:

`--expose-gc`

This allows us to manually trigger garbage collection in Node.

`--logHeapUsage`

Logs the heap usage after every test. When used together with `--expose-gc`, in the current version of Jest, it will force Node.js to swipe all known unused memory for each run of test.

`--maxWorkers`

Node sets the memory limit (--max-old-space-size=) per worker, and this command specifies the maximum number of workers the worker-pool will spawn for running tests. Currently, we set `maxWorkers` to `4` locally and `maxWorkers` to `2` in CI.

`--forceExit`

Force Jest to exit after all tests have completed running. This is useful when resources set up by test code cannot be adequately cleaned up. Jest suggested using `--detectOpenHandles` to help track down the external resources in use (it would require `--forceExit` to be omitted to work). It is advised to tear down external resources after each test to make sure Jest can shut down cleanly.

Snapshot testing
----------------

We recommend using @emotion/jest to do snapshot testing in your project, [see documentation](https://emotion.sh/docs/@emotion/jest)