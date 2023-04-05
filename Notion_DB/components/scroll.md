Scroll | NewsKit design system

Navigation

Scroll
======

The scroll component adds scroll behaviour to overflowed content.

Status
======

Supported

* * *

Introduced
==========

v0.8.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/scroll)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-scroll--story-scroll-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2141%3A40757)

* * *

Interactive demo
----------------

This demo allows you to preview the scroll component, its variations, and configuration options.

Item 1

Item 2

Item 3

Item 4

Item 5

Item 6

Item 7

Item 8

Item 9

Item 10

VerticalTrueFalse

ScrollBarTrueFalse

Scroll With Controlsno controlshoverstatic

Scroll Stepdefault10050

Scroll Snapno snapstartcenterend

    1import React from 'react';
    2import { Scroll } from 'newskit';
    3
    4export default () => <Scroll />;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The scroll component contains one required element and two optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The scroll component has options that can be used to provide an appropriate experience for different use cases.

### Orientation

The scroll component can be displayed horizontally or vertically, depending on the desired scroll direction.

### Control visibility

Controls (icon buttons) can be enabled on the scroll. If enabled, they can be set to appear persistently or on hover.

### Scroll bar visibility

A scroll bar can be displayed in the scroll component to provide users with extra context of the horizontal or vertical position of the content being scrolled.

### Scroll step distance

Scroll step distance can be adjusted to increase or decrease the distance scrolled when the controls are clicked.

### Scroll snap alignment

*   `start` aligns the scroll item snapping position to the left.
    
*   `center` centers the scroll item snapping position.
    
*   `end` aligns the scroll item snapping position to the right.
    

\`ScrollSnapAlignment\` can be used inside to a scroll component to individually set where the component should align.

### Orientation

The scroll component can be displayed horizontally or vertically, depending on the desired scroll direction.

### Control visibility

Controls (icon buttons) can be enabled on the scroll. If enabled, they can be set to appear persistently or on hover.

### Scroll bar visibility

A scroll bar can be displayed in the scroll component to provide users with extra context of the horizontal or vertical position of the content being scrolled.

### Scroll step distance

Scroll step distance can be adjusted to increase or decrease the distance scrolled when the controls are clicked.

### Scroll snap alignment

*   `start` aligns the scroll item snapping position to the left.
    
*   `center` centers the scroll item snapping position.
    
*   `end` aligns the scroll item snapping position to the right.
    

\`ScrollSnapAlignment\` can be used inside to a scroll component to individually set where the component should align.

* * *

Behaviours
----------

The following guidance describes how the scroll component behaves.

### Overlays

Overlays are displayed when content is overflowing at either the start, the end, or both.  
  
You can change the style or visually hide the overlays by overriding the [style preset.](/theme/presets/style-presets/)

### Overlays

Overlays are displayed when content is overflowing at either the start, the end, or both.  
  
You can change the style or visually hide the overlays by overriding the [style preset.](/theme/presets/style-presets/)

* * *

Usage
-----

Here’s how and when to use scroll:

* * *

Do hide scroll controls for mobile

Hide controls on mobile breakpoints to encourage a user to swipe, as this is common mobile device behaviour.

* * *

Do use an appropriate step distance

When using controls, use an appropriate step distance if all scrollable items have similar widths.

* * *

Accessibility considerations
----------------------------

The scroll component has the following accessibility considerations:

Focus order

Scroll controls are not focussable. When the scroll element is in focus, users are able to scroll the element natively e.g. keyboard, mouse scroll wheel.

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

Scroll

The scroll component has a range of props that can be used to define an appropriate experience for different use cases.

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

ScrollSnapAlignment

ScrollSnapAlignment has a range of props that can be used to define an appropriate experience for different use cases. It can be used inside to a scroll component to individually set where the component should align.

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Menu



](/components/menu/)

A Menu displays a list of navigational items. They are displayed either at the top of a screen, or at the side where space allows.

[

### Tabs



](/components/tabs/)

Allows users to alternate between views within the same context.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)