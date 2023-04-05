Block | NewsKit design system

Components

Block
=====

Blocks are simple container components that you can apply style and space to. They’re the equivalent of frames in Figma.

Status
======

Supported

* * *

Introduced
==========

v0.1.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/blob/main/src/block/block.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-block--story-block-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/?node-id=324%3A2)

* * *

Interactive demo
----------------

This demo lets you preview the block component, its variations and configuration options.

This is a block

Children

Render asDefault (div)span

spaceStackDefaultspace020

stylePresetDefaultflagSolidPrimary

    1import React from 'react';
    2import { Block } from 'newskit';
    3
    4export default () => <Block>This is a block</Block>;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The block contains one required element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The block has options for different use cases:

### Render as

Convert the block to a ‘span’.

### Style

Apply styling to the block with [style presets](https://www.newskit.co.uk/theme/presets/style-presets/) .

### Spacing

Apply three types of spacing to the block: space inline, space stack and space inset.

### Render as

Convert the block to a ‘span’.

### Style

Apply styling to the block with [style presets](https://www.newskit.co.uk/theme/presets/style-presets/) .

### Spacing

Apply three types of spacing to the block: space inline, space stack and space inset.

* * *

Usage
-----

Here’s how and when to use the block:

* * *

Use the block to apply spacing and style presets

Use the block as a container to easily apply spacing and style presets around other elements.

* * *

Don’t use for equal spacing on multiple elements

Avoid using the block when you need to apply equal spacing to multiple elements. Use [stack](https://www.newskit.co.uk/components/stack/) or [grid](https://www.newskit.co.uk/components/grid/) instead.

* * *

Accessibility considerations
----------------------------

The block is an HTML element, so you can use any ARIA attribute (e.g. region). [Learn more ARIA at MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA).

* * *

SEO considerations
------------------

There are no SEO considerations for the block.

* * *

API
---

The block has a range of props to define the experience in different use cases.

Block

Name

Type

Default

Description

Required

The block can utilise any valid [HTML attribute.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes).

* * *

Related components
------------------

[

### Card



](/components/card/)

Contain preview content and actions about a single subject.

[

### Grid



](/components/grid/)

The grid and cell are used together to construct a visual grid for responsive page layout.

[

### Grid Layout



](/components/grid-layout/)

Used to construct a visual grid for responsive page layout. A Proxy for CSS grid.

[

### Stack



](/components/stack/)

A low-level foundational component used to layout items in a horizontal or vertical stack.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)