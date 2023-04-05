Grid | NewsKit design system

Layout

Grid & cell
===========

The grid and cell are used together to construct a visual grid for responsive page layout.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/grid)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-grid--story-grid-default)[View Design](https://www.figma.com/file/3l0UDvk1l2vsXpbtWlYWoP/%F0%9F%9F%A2-NK-NewsKit-Theme?node-id=4208%3A5779)

* * *

Interactive demo
----------------

[This demo](https://newskit-grid-demo.vercel.app/) allows you to preview the grid, the variations, and configuration options.

* * *

Anatomy
-------

The grid contains no required elements and five optional elements.

Item

Name

Description

Component

Optional

* * *

Grid options
------------

The grid has the following options to provide an appropriate experience for different scenarios.

### Breakpoints

There are 5 breakpoints. The breakpoint ranges can be set via the [theme breakpoint values.](https://newskit.co.uk/theme/foundation/breakpoints/#usage)

### Gutter width

The gutter width can be set for each breakpoint. These can be set via the theme or overridden at the component level.

### Margin width

The margin width can be set for each breakpoint. These can be set via the theme or overridden at the component level.

### Max width

The maximum width of the grid can be set. This can be set via the theme or overridden at the component level.

### Breakpoints

There are 5 breakpoints. The breakpoint ranges can be set via the [theme breakpoint values.](https://newskit.co.uk/theme/foundation/breakpoints/#usage)

### Gutter width

The gutter width can be set for each breakpoint. These can be set via the theme or overridden at the component level.

### Margin width

The margin width can be set for each breakpoint. These can be set via the theme or overridden at the component level.

### Max width

The maximum width of the grid can be set. This can be set via the theme or overridden at the component level.

* * *

Cell options
------------

Cells have the following options to provide an appropriate experience for different scenarios.

### Span

Cells can be set to span any number of columns in the grid. If set to ‘full-width’ the cell will span all 12 columns and breakout across the margin of the grid. It will still be confined by the grids max-width.

### Order

The order that cells appear can be changed at different breakpoints.

### Visibility

Cells can be set to be hidden at different breakpoints.

### Offset

Cells can be set to be offset by a specified number of columns.

### Span

Cells can be set to span any number of columns in the grid. If set to ‘full-width’ the cell will span all 12 columns and breakout across the margin of the grid. It will still be confined by the grids max-width.

### Order

The order that cells appear can be changed at different breakpoints.

### Visibility

Cells can be set to be hidden at different breakpoints.

### Offset

Cells can be set to be offset by a specified number of columns.

* * *

Grid behaviours
---------------

The following guidance describes how the grid behaves.

### Max-width

When the maximum width of the grid is reached, the grid will become fixed and the margins grow to fill the screen.

### Nested grids

A grid can be [nested inside of a parent grid](https://github.com/lhaggar/newskit-grid-demo/blob/master/pages/nesting.js) by adding it to a cell of that grid.

### Max-width

When the maximum width of the grid is reached, the grid will become fixed and the margins grow to fill the screen.

### Nested grids

A grid can be [nested inside of a parent grid](https://github.com/lhaggar/newskit-grid-demo/blob/master/pages/nesting.js) by adding it to a cell of that grid.

* * *

Usage
-----

Here’s how and when to use the grid:

* * *

Do align content

Whenever possible, make sure page elements are lined up both horizontally and/or vertically.

* * *

Avoid aligning everything to the grid

Individual elements within the cells should align with each other rather than with the grid columns.

* * *

Avoid making gutters too wide

They should be balanced against the column width to ensure page elements relate to each other.

* * *

Accessibility considerations
----------------------------

The grid has the following accessibility considerations:

Visibility of content

Content passed to cells can be set as [visible and hidden](https://www.newskit.co.uk/components/visibility/) at different breakpoints. When used 'hidden' excludes content from focus order when the screen size matches the applied breakpoint.

* * *

API
---

Grid

The grid has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

Cell

The cell has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The number of columns are set globally at the theme level.

Grid component defaults

The grid has a range of predefined defaults.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Grid Layout



](/components/grid-layout/)

Used to construct a visual grid for responsive page layout. A Proxy for CSS grid.

[

### Block



](/components/block/)

A simple container component that can take margin, padding, and style presets.

[

### Stack



](/components/stack/)

A low-level foundational component used to layout items in a horizontal or vertical stack.

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