Grid layout | NewsKit design system

Layout

Grid layout
===========

This component is a beta so this page is a work in progress. Grid layout is used to construct a visual grid for responsive page layout. A proxy for CSS grid.

Status
======

Supported

* * *

Introduced
==========

[v5.1.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.1.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/grid-layout)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-grid-layout--story-responsive-example)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=9893%3A158142)

* * *

Interactive demo
----------------

This demo lets you preview the grid layout component, its variations and configuration options.

columnsnonerepeat(4, 1fr)1fr 2fr 1fr100px 1fr 1frauto auto auto100px 150px 200px1fr 1fr

rowsnonerepeat(2, 50px)20px 50px 100px

columnGapspace020space040

autoFlowrowcolumndense

autoColumnsnoneauto100pxminmax(100px, auto)

autoRowsnoneauto10%minmax(20px, auto)

rowGapspace020space040

justifyContentnonecenterstartendstretchspace-betweenspace-aroundspace-evenly

alignContentnonecenterstartendstretchspace-betweenspace-aroundspace-evenly

alignItemsnonecenterstartendstretch

justifyItemsnonecenterstartendstretch

    1import React from 'react';
    2import { GridLayout } from 'newskit';
    3
    4export default () => (
    5  <GridLayout
    6    columns=""
    7    rows=""
    8    columnGap="space020"
    9    autoFlow="row"
    10    autoColumns=""
    11    autoRows=""
    12    rowGap="space020"
    13    justifyContent=""
    14    alignContent=""
    15    alignItems=""
    16    justifyItems=""
    17  />
    18);
    19
    

Edit on CodeSandbox

* * *

Anatomy
-------

The grid layout component contains the following.

Item

Name

Description

Component

Optional

* * *

Options
-------

The grid layout component has options that can be used to provide an appropriate experience for different use cases.

### Row gap & column gap

The row gap and column gap can be set for each breakpoint.

### Max-width

When the defined maximum width of the grid is reached (default set to auto), the grid will become fixed and the margins grow to fill the screen.

### Span

Cells can be set to span any number of columns in the grid. If set to ‘full-width’ the cell will span all 12 columns and breakout across the margin of the grid. It will still be confined by the grid's max-width.

### Order

The order that cells appear can be changed at different breakpoints.

### Offset

Cells can be set to be offset by a specified number of columns.

### Row gap & column gap

The row gap and column gap can be set for each breakpoint.

### Max-width

When the defined maximum width of the grid is reached (default set to auto), the grid will become fixed and the margins grow to fill the screen.

### Span

Cells can be set to span any number of columns in the grid. If set to ‘full-width’ the cell will span all 12 columns and breakout across the margin of the grid. It will still be confined by the grid's max-width.

### Order

The order that cells appear can be changed at different breakpoints.

### Offset

Cells can be set to be offset by a specified number of columns.

* * *

Usage
-----

Here’s how and when to use the grid layout:

* * *

Do align content

Whenever possible, make sure page elements are lined up both horizontally and / or vertically.

* * *

Avoid aligning everything to the grid

Individual elements within the cells should align with each other rather than with the grid columns.

* * *

Tutorial
--------

Learn how to use the grid layout component effectively using the tutorials below.

[

### Grid layout tutorial



](/getting-started/code/grid-layout-step-by-step/)

Step-by-step guide for engineers to build a layout using the grid layout component.

[

### How to build a Section using grid layouts



](https://www.figma.com/file/DkQzpgAZSze5ghznccAI7l/Grid-Layout-Guide)

Guide in Figma for designers to use the grid layout component (internal only).

[

### Grid layout tutorial



](/getting-started/code/grid-layout-step-by-step/)

Step-by-step guide for engineers to build a layout using the grid layout component.

[

### How to build a Section using grid layouts



](https://www.figma.com/file/DkQzpgAZSze5ghznccAI7l/Grid-Layout-Guide)

Guide in Figma for designers to use the grid layout component (internal only).

* * *

Accessibility considerations
----------------------------

The grid layout has the following accessibility considerations:

Ordering

Ordering can be used to render items in a different order to their tab order, this can be useful when building accessible interfaces as it allows the most important items to be focused first, even if they don’t visually appear this way.

* * *

API
---

Below are the properties for the grid layout component:

Grid layout

Grid layout has a range of props to define the experience in different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Attribute

Type

Default

Description

Grid layout item

Grid layout item has a range of props to define the experience in different use cases. Use within the grid layout.

Name

Type

Default

Description

Required

GridLayoutItem is derived from the [block](/components/block/) component, so all it allows stylePresets, transitionPresets, and logicalProps.

* * *

Related components
------------------

[

### Block



](/components/block/)

A simple container component that can take margin, padding, and style presets.

[

### Grid



](/components/grid/)

The grid and cell are used together to construct a visual grid for responsive page layout.

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