Stack | NewsKit design system

Layout

Stack
=====

A stack is a layout component that abstracts the implementation of [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

Status
======

Supported

* * *

Introduced
==========

v0.7.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/stack)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-stack--story-stack-default)

* * *

We recommend using the [grid layout component](/components/grid-layout/) instead of the Stack component.

Interactive demo
----------------

This demo allows you to preview the stack, its variations, and configuration options.

This

Is

A

Stack

Example

Showing

Multiple

Tags

Stack Flowvertical-leftvertical-centervertical-rightvertical-stretchhorizontal-tophorizontal-centerhorizontal-bottomhorizontal-stretch

InlineTrueFalse

Stack Distributionflex-startcenterflex-endspace-aroundspace-betweenspace-evenly

spaceInlineUnsetspace010space020space030space040

spaceStackUnsetspace010space020space030space040

HeightDefault (100%)AutoCustom (500px)

WrapwrapDefault (nowrap)

ListTrueFalse

AriaLabel

    1import React from 'react';
    2import { Stack } from 'newskit';
    3
    4export default () => (
    5  <Stack
    6    flow="vertical-left"
    7    stackDistribution="flex-start"
    8    spaceInline=""
    9    spaceStack=""
    10    height="100%"
    11    wrap="nowrap"
    12    ariaLabel="list content label"
    13  />
    14);
    15
    

Edit on CodeSandbox

* * *

Anatomy
-------

The stack is comprised of one required element and one optional element

Item

Name

Description

Component

Optional

* * *

Overview
--------

The stack specifies the layout of its children components and can be used to quickly and easily layout elements on a page without needing to write any CSS. [Auto-layout](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties) is the equivalent of a stack in Figma.

* * *

Distribution
------------

Its children can be distributed by using the ‘distribution’ property, which is a direct mapping to the flexbox property [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)

Center

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Flex-start

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="flex-start"
    4>
    5  ...
    6</Stack>

Flex-end

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="flex-end"
    4>
    5  ...
    6</Stack>

Space-around

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="space-around"
    4>
    5  ...
    6</Stack>

Space-between

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="space-between"
    4>
    5  ...
    6</Stack>

Space-evenly

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="space-evenly"
    4>
    5  ...
    6</Stack>

* * *

Flow
----

The stack supports eight different flows: four vertical and four horizontal. For elements to expand on the cross-axis, they will need to be either `display:flex` or `display:flex-inline`.

Horizontal-stretch

1

2

3

4

5

    1<Stack
    2  flow="horizontal-stretch"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Horizontal-top

1

2

3

4

5

    1<Stack
    2  flow="horizontal-top"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Horizontal-center

1

2

3

4

5

    1<Stack
    2  flow="horizontal-center"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Horizontal-bottom

1

2

3

4

5

    1<Stack
    2  flow="horizontal-bottom"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Vertical-left

1

2

3

4

5

    1<Stack
    2  flow="vertical-left"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Vertical-center

1

2

3

4

5

    1<Stack
    2  flow="vertical-center"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Vertical-right

1

2

3

4

5

    1<Stack
    2  flow="vertical-right"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

Vertical-stretch

1

2

3

4

5

    1<Stack
    2  flow="vertical-stretch"
    3  stackDistribution="center"
    4>
    5  ...
    6</Stack>

* * *

Wrap
----

The stack has the ability to wrap elements to prevent them from overflowing.

Horizontal-top

1

2

3

4

5

6

7

8

9

10

    1<Stack
    2  wrap="wrap" 
    3  flow="horizontal-top"
    4>
    5  ...
    6</Stack>

Vertical-left

1

2

3

4

5

6

7

8

9

10

    1<Stack
    2  wrap="wrap"
    3  flow="vertical-left"
    4>
    5  ...
    6</Stack>

* * *

Spacing
-------

The stack supports adding a fixed space between its children and rows of children when the stack is wrapping `spaceInline` will be applied in the flow of the elements.

Horizontal - spaceInline

1

2

3

4

5

    1<Stack
    2  flow="horizontal-top"
    3  spaceInline="space040"
    4>
    5  ...
    6</Stack>

Horizontal - spaceStack

1

2

3

4

5

    1<Stack
    2  flow="horizontal-top"
    3  spaceStack="space040"
    4  width="150px"
    5  wrap="wrap"
    6>
    7  ...
    8</Stack>

Vertical - spaceInline

1

2

3

4

5

    1<Stack
    2  flow="vertical-left"
    3  spaceInline="space040"
    4>
    5  ...
    6</Stack>

Vertical-spaceStack

1

2

3

4

5

    1<Stack
    2  flow="vertical-left"
    3  spaceStack="space040"
    4  height="150px"
    5  wrap="wrap"
    6>
    7  ...
    8</Stack>

* * *

Ordering
--------

The stack supports the ability to define the order of the elements within the stack.

Ordering

1

2

3

    1<Stack flow="horizontal-center">
    2    <StackChild order={2}>
    3        <StackItem>1</StackItem>
    4    </StackChild>
    5    <StackChild order={3}>
    6        <StackItem>2</StackItem>
    7    </StackChild>
    8    <StackChild order={1}>
    9        <StackItem>3</StackItem>
    10    </StackChild>
    11</Stack>

* * *

Reverse
-------

The stack supports the ability to be reversed

flowReverse

1

2

3

    1<Stack flowReverse flow="horizontal-center">
    2    <StackItem>1</StackItem>
    3    <StackItem>2</StackItem>
    4    <StackItem>3</StackItem>
    5</Stack>

* * *

StackChild
----------

The `StackChild` provides a utility that allows items to be placed out of order. This is particularly useful for building accessible interfaces. It is required for the component to be used within a stack. Its behaviour is derived from the functionality of a child element in a classic [flexbox container](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) .

StackChild

1

2

3

    1<Stack flow="horizontal-center">
    2    <StackChild>
    3        <StackItem>1</StackItem>
    4    </StackChild>
    5    <StackChild>
    6        <StackItem>2</StackItem>
    7    </StackChild>
    8    <StackChild>
    9        <StackItem>3</StackItem>
    10    </StackChild>
    11</Stack>

* * *

Accessibility considerations
----------------------------

The stack can be used to build accessible interfaces.

WAI-ARIA

Element

Attribute

Value

Description

User supplied

StackChild can accept an order prop to visually display elements in a different order than they appear on the DOM, while preserving the tab order.

* * *

API
---

Stack

The stack has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

StackChild

The stackChild has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Grid



](/components/grid/)

The grid and cell are used together to construct a visual grid for responsive page layout.

[

### Grid Layout



](/components/grid-layout/)

Used to construct a visual grid for responsive page layout. A Proxy for CSS grid.

[

### Block



](/components/block/)

A simple container component that can take margin, padding, and style presets.

[

### Visibility



](/components/visibility/)

A pair of components which can be used to show and hide content at different breakpoints.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)