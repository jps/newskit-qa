Drawer | NewsKit design system

Layout

Drawer
======

Drawers are layout panels that slide out from the side of the screen to reveal content like navigation or filters.

Status
======

Supported

* * *

Introduced
==========

v3.0.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/develop/src/drawer)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-drawer--story-drawer-default)[View Design](https://www.figma.com/file/VYOAzpSq02PoR7cci6SJlE/?node-id=324%3A2)

* * *

Interactive demo
----------------

This demo lets you preview the drawer component, its variations and configuration options.

openTrueFalse

placementLeftRightTopBottom

closePositionUnsetLeftRightNone

Header

hideOverlayTrueFalse

inlineTrueFalse

    1import React from 'react';
    2import { Drawer } from 'newskit';
    3
    4export default () => (
    5  <Drawer placement="left" header="" hideOverlay inline />
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

The drawer contains two required elements and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The drawer has options for different use cases:

### Placement

The drawer can appear from the left (default), right, top, or bottom of the screen.

### Close position

When appearing from the left or right of the screen, the close icon button is positioned on the side the drawer originates from. When appearing from the top or bottom of the screen, the close icon button is positioned on the right as default. You can change the close button position to either left or right for all four placements.

Note

The header and close button are optional. However, you should always include a close button to adhere to [ARIA principles](https://www.w3.org/TR/wai-aria-practices-1.2/#keyboard-interaction-7).

### Width

Customise the width of a drawer placed on either the left or right (height is 100%).

### Height

Customise the height of a drawer placed on either the top or bottom (width is 100%).

### Placement

The drawer can appear from the left (default), right, top, or bottom of the screen.

### Close position

When appearing from the left or right of the screen, the close icon button is positioned on the side the drawer originates from. When appearing from the top or bottom of the screen, the close icon button is positioned on the right as default. You can change the close button position to either left or right for all four placements.

Note

The header and close button are optional. However, you should always include a close button to adhere to [ARIA principles](https://www.w3.org/TR/wai-aria-practices-1.2/#keyboard-interaction-7).

### Width

Customise the width of a drawer placed on either the left or right (height is 100%).

### Height

Customise the height of a drawer placed on either the top or bottom (width is 100%).

* * *

Behaviours
----------

Here's how the drawer behaves:

### Animation

When the user launches the drawer, the overlay fades in from 0% to 100% opacity (transitions) and the drawer panel slides in from the edge of the screen (transforms:translate the x or y axis). When the user dismisses the drawer, the same animation occurs in reverse.

### Triggering & closing the drawer

Control visibility via the open prop (the drawer is hidden by default). To close the drawer, the user can click the close icon button or overlay, or press the Esc key. Any of these actions will trigger the onDismiss callback.

### Content overflow

When the content is too long to fit, content overflows and Scroll is applied. The header becomes fixed and the content can then independently scroll to bring overflowed content into view.

### Disable page scrolling when launched

When a drawer is present the content behind is not scrollable (scroll-locked).

### Animation

When the user launches the drawer, the overlay fades in from 0% to 100% opacity (transitions) and the drawer panel slides in from the edge of the screen (transforms:translate the x or y axis). When the user dismisses the drawer, the same animation occurs in reverse.

### Triggering & closing the drawer

Control visibility via the open prop (the drawer is hidden by default). To close the drawer, the user can click the close icon button or overlay, or press the Esc key. Any of these actions will trigger the onDismiss callback.

### Content overflow

When the content is too long to fit, content overflows and Scroll is applied. The header becomes fixed and the content can then independently scroll to bring overflowed content into view.

### Disable page scrolling when launched

When a drawer is present the content behind is not scrollable (scroll-locked).

* * *

Usage
-----

Here's how and when to use the drawer:

* * *

Use for navigation, filtering and checkout

Drawers are appropriate for navigation, for filtering content, or in checkout flows.

* * *

Don't use for top-level navigation on larger screens

Avoid using drawers for top-level navigation items when there's space to expose them on larger screens.

* * *

Keep drawers close to related content

A drawer should be in close proximity to the content it relates to.

* * *

Don't nest tiered drawers

Avoid nesting tiered drawers as this can cause usability issues. Consider an alternative component (e.g. accordion) or rethink the page structure.

* * *

Accessibility considerations
----------------------------

The drawer has the following accessibility considerations:

Focus order

Order

Element

Role

Upon opening, focus transfers to the first interactive element in the specified order (i.e. if there are interactive elements passed to the header, this will be the first focussable element).

You can change the element that gets focus by adding a data-autofocus attribute to another HTML element.

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

SEO considerations
------------------

1.  Ensure all text, icons and images are visible in the drawer so that information can be crawled and indexed.
2.  The drawer and its content are rendered to the DOM, but only visible to the user when the drawer is open.

* * *

API
---

The drawer has a range of props to define the experience in different use cases.

Drawer

The drawer has a range of props that can be used to define an appropriate experience for different use cases.

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

### Modal



](/components/modal/)

A Modal is a layout panel that presents critical information or requests users input without navigating away from the current page.

[

### Popover



](/components/popover/)

A Popover (also known as a Popper) is a layout component that displays non-critical information when a user clicks or taps on a UI element.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)