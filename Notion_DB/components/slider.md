Slider | NewsKit design system

Actions & Inputs

Slider
======

Sliders allow users to choose a value or values within a range.

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/slider)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-slider--story-slider-1-and-2-thumbs)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=324%3A4)

* * *

Interactive demo
----------------

This demo allows you to preview the slider component, its variations, and configuration options.

Min

Max

Values

Values

Step

DisabledTrueFalse

Min LabelUnsetTextComponent

Max LabelUnsetTextComponent

Label PositionDefault (inline)beforeafter

Thumb LabelUnsettrueComponent

VerticalUnsettrue

    1import React from 'react';
    2import { Slider } from 'newskit';
    3
    4export default () => (
    5  <Slider
    6    min={0}
    7    max={100}
    8    values={[50]}
    9    step={1}
    10    labelPosition="inline"
    11  />
    12);
    13
    

Edit on CodeSandbox

* * *

Anatomy
-------

The slider component contains three required elements and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The slider has options for different use cases:

### Orientation

The slider can be displayed horizontally or vertically.

### Min and max

The min and max values of the slider can be customised. You can also add additional values to the slider.

### Step distance

Slider step distance can be adjusted to increase or decrease the number of steps when the thumb is dragged along the track.

### Min/max labels

Min/max labels can be added to the track.

### Thumb label

A label can be added to the thumb, showing the current value.

### Label position

*   Inline - Aligns the track labels inline.
    
*   Before - Labels appear above or to the left of the track, depending on the orientation.
    
*   After - Labels appear below or to the right of the track, depending on the orientation.
    

### Thumb icon

An icon can be placed inside the thumb.

### Track weight

The weight of the slider track can be customised to give more or less affordance.

### Indicator weight

The weight of the slider indicator can be customised to give more or less affordance.

### Feedback

The optional feedback element is non-interactive and appears behind the thumb control on hover.

### Orientation

The slider can be displayed horizontally or vertically.

### Min and max

The min and max values of the slider can be customised. You can also add additional values to the slider.

### Step distance

Slider step distance can be adjusted to increase or decrease the number of steps when the thumb is dragged along the track.

### Min/max labels

Min/max labels can be added to the track.

### Thumb label

A label can be added to the thumb, showing the current value.

### Label position

*   Inline - Aligns the track labels inline.
    
*   Before - Labels appear above or to the left of the track, depending on the orientation.
    
*   After - Labels appear below or to the right of the track, depending on the orientation.
    

### Thumb icon

An icon can be placed inside the thumb.

### Track weight

The weight of the slider track can be customised to give more or less affordance.

### Indicator weight

The weight of the slider indicator can be customised to give more or less affordance.

### Feedback

The optional feedback element is non-interactive and appears behind the thumb control on hover.

* * *

States
------

The slider has the following states:

### Base

The default style before the user interacts with the slider.

### Hover

The thumb control changes style to let the user know it’s interactive.

### Active

The thumb control changes style to let users know they’ve interacted with it.

### Focus

Communicates that a user has highlighted a thumb control item (e.g. via keyboard or voice).

### Disabled

Communicates that a slider exists but isn’t available in that scenario. When the user hovers over a slider in a disabled state, the cursor shows as ‘not allowed’.

* * *

Behaviours
----------

Here’s how the slider behaves:

### Thumb control

A draggable ‘thumb’ control on the slider track allows users to choose a numeric value between a predefined minimum and maximum. The slider supports multiple values, i.e. you can have multiple ‘thumbs’.

### Thumb control

A draggable ‘thumb’ control on the slider track allows users to choose a numeric value between a predefined minimum and maximum. The slider supports multiple values, i.e. you can have multiple ‘thumbs’.

* * *

Usage
-----

Here’s how and when to use the slider:

* * *

Do use labels for context

Use labels to give more context to the values that the slider represents.

* * *

Do show values to provide context

Represent slider value units as it helps provide context e.g., ‘%' or 'px’.

* * *

Do prefix values

If the slider values range from negative to positive, prefix the value with a ‘+' plus or '-’ minus sign.

* * *

Accessibility considerations
----------------------------

Focus Order

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

Slider

The slider has a range of props to define the experience in different use cases.

Props

Overrides

Name

Type

Default

Description

Required

The slider has a range of props to define the experience in different use cases.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

[

### Select



](/components/select/)

Select components allow users to select one option from a list.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)