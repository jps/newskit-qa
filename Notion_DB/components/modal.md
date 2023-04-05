Modal | NewsKit design system

Layout

Modal
=====

Modals are layout panels that present critical information, or request the user’s input, without navigating away from the current page.

Status
======

Supported

* * *

Introduced
==========

v3.8.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-modal--story-modal-default)[View Design](https://github.com/newscorp-ghfb/newskit)

* * *

Interactive demo
----------------

This demo lets you preview the modal component, its variations and configuration options.

Use props bellow to open and configure the modal.

openTrueFalse

closePositionUnsetLeftRightNone

Header

hideOverlayTrueFalse

    1import React from 'react';
    2import { Modal } from 'newskit';
    3
    4export default () => <Modal header="" />;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The modal contains one required element and four optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The modal has options for different use cases:

### Placement

The modal appears as follows across different breakpoints:

*   **xs/sm**  
    The modal is positioned in the centre of the screen. Any content passed to the modal panel causes it to grow from the centre until it reaches the max height.
    
*   **md/lg/xl**  
    The modal is positioned horizontally in the centre of the screen and positioned vertically offset from the top of the screen. Any content passed to the modal panel causes it to grow downwards until it reaches the max height.
    

### Close button position

Position the close button on the right (default) or left of the modal header.

The header and close button are optional. However, you should always include a close button to adhere to [ARIA principles](https://www.w3.org/TR/wai-aria-practices-1.2/#keyboard-interaction-7).

### Width

Customise the width of a modal for each breakpoint to allow for more or less space as needed.

### Focus trapping

You can specify the tab order of interactive elements inside the modal. Focus is trapped inside the modal until the user closes it.  
  
There is no focus trapping when the overlay is hidden (modeless).

### Overlay

Set the modal overlay to visible or hidden.

### Placement

The modal appears as follows across different breakpoints:

*   **xs/sm**  
    The modal is positioned in the centre of the screen. Any content passed to the modal panel causes it to grow from the centre until it reaches the max height.
    
*   **md/lg/xl**  
    The modal is positioned horizontally in the centre of the screen and positioned vertically offset from the top of the screen. Any content passed to the modal panel causes it to grow downwards until it reaches the max height.
    

### Close button position

Position the close button on the right (default) or left of the modal header.

The header and close button are optional. However, you should always include a close button to adhere to [ARIA principles](https://www.w3.org/TR/wai-aria-practices-1.2/#keyboard-interaction-7).

### Width

Customise the width of a modal for each breakpoint to allow for more or less space as needed.

### Focus trapping

You can specify the tab order of interactive elements inside the modal. Focus is trapped inside the modal until the user closes it.  
  
There is no focus trapping when the overlay is hidden (modeless).

### Overlay

Set the modal overlay to visible or hidden.

* * *

Behaviours
----------

Here’s how the modal behaves:

### Height

The height of a modal panel is calculated as a percentage of the available screen. The modal panel grows vertically to fit the content passed into it, until it reaches the max height.

### Entrance and exit motion

When the user launches the modal, the overlay fades in from 0% to 100% opacity (transitions) and the modal panel slides upward from the centre of the screen (transforms:translate the x or y axis). When the user dismisses the modal, the same animation occurs in reverse.

### Triggering and closing the modal

Control visibility via the open prop (the modal is hidden by default). To close the modal, the user can click the close button or overlay, or press the Esc key. Any of these actions will trigger the onDismiss callback.

### Content overflow

When the content is too long to fit, content overflows and scroll is applied. The header becomes fixed and the content can then independently scroll to bring overflowed content into view.

### Lock scroll

When a modal is present, the content behind isn’t scrollable (scroll-locked).

### Height

The height of a modal panel is calculated as a percentage of the available screen. The modal panel grows vertically to fit the content passed into it, until it reaches the max height.

### Entrance and exit motion

When the user launches the modal, the overlay fades in from 0% to 100% opacity (transitions) and the modal panel slides upward from the centre of the screen (transforms:translate the x or y axis). When the user dismisses the modal, the same animation occurs in reverse.

### Triggering and closing the modal

Control visibility via the open prop (the modal is hidden by default). To close the modal, the user can click the close button or overlay, or press the Esc key. Any of these actions will trigger the onDismiss callback.

### Content overflow

When the content is too long to fit, content overflows and scroll is applied. The header becomes fixed and the content can then independently scroll to bring overflowed content into view.

### Lock scroll

When a modal is present, the content behind isn’t scrollable (scroll-locked).

* * *

Usage
-----

Here’s how and when to use the modal:

* * *

Use modals for critical information

Modals are appropriate for notifications that give the user critical information related to a task. For non-critical information, consider a toast or inline notification instead.

* * *

Don’t use modals for marketing

Avoid using modals for marketing or advertising purposes. They’re intended for critical information or requests for user input.

* * *

Keep modals close to related content

A modal should be in close proximity to the content it relates to.

* * *

Accessibility considerations
----------------------------

The modal has the following accessibility considerations:

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

*   Ensure all text, icons and images are visible in the modal so information can be crawled and indexed by search engines.
    
*   The modal and its content are rendered to the DOM but only visible to the user when the modal is open.
    

* * *

API
---

Modal

Props

Overrides

The modal has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that you can override to define their appearance.

Name

Type

Default

Description

Required

The modal has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that you can override to define their appearance.

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

### Drawer



](/components/drawer/)

A layout panel that slides out the side of the screen revealing content like navigation or filters.

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