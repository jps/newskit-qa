Structured list | NewsKit design system

Layout

Structured list
===============

Structured lists group similar or related content together.

Status
======

Supported

* * *

Introduced
==========

v3.5.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/structured-list)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-structured-list--story-structured-list-default)

* * *

Interactive demo
----------------

This demo lets you preview the structured list component, its variations and configuration options.

*   [
    
    Label
    
    A short description of the label
    
    
    
    
    
    ](/)
*   Label
    
    A short description of the label
    
*   Label
    
    A short description of the label
    

DividerTrueFalse

    1import React from 'react';
    2import { StructuredList } from 'newskit';
    3
    4export default () => <StructuredList />;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The Structured list contains three required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The structured list has options for different use cases:

### List item and cell layouts

Achieve multiple layouts by configuring the structured list cell using nested grids and the `pullRight` prop.

### List item dividers

Visually separate list items by applying [dividers](/components/divider/) to the bottom of a list item, via the divider prop.

### Interactive items

Make structured list items interactive by supplying a link for an item.

If you pass a href to the component, it renders a chevron in the last cell and the item becomes interactive. To show that the item is interactive, the stylePreset and cursor are set to ‘pointer’.

### List item and cell layouts

Achieve multiple layouts by configuring the structured list cell using nested grids and the `pullRight` prop.

### List item dividers

Visually separate list items by applying [dividers](/components/divider/) to the bottom of a list item, via the divider prop.

### Interactive items

Make structured list items interactive by supplying a link for an item.

If you pass a href to the component, it renders a chevron in the last cell and the item becomes interactive. To show that the item is interactive, the stylePreset and cursor are set to ‘pointer’.

* * *

States
------

The structured list has the following states:

### Base

The default style before the user interacts with the list item.

### Hover

The list item changes style to let the user know it’s interactive.

### Active

The list item changes style to let the user know they’ve interacted with it.

### Disabled

Communicates that a list item exists, but isn’t available in that scenario. When the user hovers over a list item in a disabled state, the cursor shows as ‘not allowed’.  
  
Disabled list items maintain layout consistency and communicate that a list item may become available if another condition is met.

### Focus

Communicates that a user has highlighted a list item (e.g. via keyboard or voice).

* * *

Behaviours
----------

Here’s how the structured list behaves:

### Alignment

On xs and sm breakpoints, the content of the third cell aligns to the vertical centre, and the content of the second cell moves below the first cell.  
  
On md and above breakpoints, the content of the third cell aligns to the top.

### Alignment

On xs and sm breakpoints, the content of the third cell aligns to the vertical centre, and the content of the second cell moves below the first cell.  
  
On md and above breakpoints, the content of the third cell aligns to the top.

* * *

Accessibility considerations
----------------------------

The structured list has the following accessibility considerations:

Focus order

Order

Element

Role

Keyboard Interactions

Command

Description

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

API
---

Structured list

Props

Overrides

The structured list has a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Name

Type

Default

Description

Required

The structured list has a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Attribute

Type

Default

Description

Structured list item

Props

Overrides

The structured list item has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Name

Type

Default

Description

Required

The structured list item has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Attribute

Type

Default

Description

Structured list cell

The structured list cell has a range of props to define the experience in different use cases.

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Block



](/components/block/)

A simple container component that can take margin, padding, and style presets.

[

### Divider



](/components/divider/)

A thin line that separates content.

[

### Grid



](/components/grid/)

The grid and cell are used together to construct a visual grid for responsive page layout.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)