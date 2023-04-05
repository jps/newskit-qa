Popover | NewsKit design system

Layout

Popover
=======

Popovers (also known as poppers) display non-critical information when a user clicks or taps on a UI element.

Status
======

Supported

* * *

Introduced
==========

[v5.6.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.6.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/popover)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-popover--story-popover-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=7296%3A137983)

* * *

Anatomy
-------

The popover contains one required element and four optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The popover has options for different use cases:

### Size

Set a maxWidth and minWidth for the popover. Height is set automatically based on the content.

### Placement

Choose from 12 different tooltip placements.

### Pointer

Add a pointer to indicate the element to which the popover is attributed. Set it to ‘visible’ or ‘hidden’ as required.  
  
The pointer changes position depending on the placement of the popover.

### Offset

Change the space between the popover and the element with spacing tokens via overrides. By default, there’s 8px of space between the popover and the element, measured from the tip of the pointer or the near edge of the popover if no pointer is visible.

### Close position

Position the close button to the right (default) or left.

Note

The close button is optional. However, you should include it to adhere to [ARIA principles.](https://www.w3.org/WAI/ARIA/apg/#keyboard-interaction-7)

### Size

Set a maxWidth and minWidth for the popover. Height is set automatically based on the content.

### Placement

Choose from 12 different tooltip placements.

### Pointer

Add a pointer to indicate the element to which the popover is attributed. Set it to ‘visible’ or ‘hidden’ as required.  
  
The pointer changes position depending on the placement of the popover.

### Offset

Change the space between the popover and the element with spacing tokens via overrides. By default, there’s 8px of space between the popover and the element, measured from the tip of the pointer or the near edge of the popover if no pointer is visible.

### Close position

Position the close button to the right (default) or left.

Note

The close button is optional. However, you should include it to adhere to [ARIA principles.](https://www.w3.org/WAI/ARIA/apg/#keyboard-interaction-7)

* * *

Behaviours
----------

Here’s how the popover behaves:

### Triggering and closing the popover

The popover is triggered when the user clicks and/or taps on the UI element to which it is attributed. Clicking or tapping on the UI element again dismisses the popover.

### Focus

Upon focus of the popover, the first interactive element in the specified order will receive focus (i.e. if there are interactive elements passed to the header area, this will be the first focussable element).

### Shift

The popover shifts in order to remain in view of the visible area, with the pointer maintaining the context that the popover is attributed to.  
  
[Learn more about shift at the Floating UI library.](https://floating-ui.com/docs/shift)

### Flip

The popover flips to the opposite side once it’s about to overflow the visible area, with the pointer maintaining the context that the popover is attributed to. Once enough space is detected on its preferred side, it flips back to its original position.  
  
[Learn more about flip at the Floating UI library.](https://floating-ui.com/docs/flip)

### Transition

When triggered, the popover transitions using the `fade` transition preset.

### Triggering and closing the popover

The popover is triggered when the user clicks and/or taps on the UI element to which it is attributed. Clicking or tapping on the UI element again dismisses the popover.

### Focus

Upon focus of the popover, the first interactive element in the specified order will receive focus (i.e. if there are interactive elements passed to the header area, this will be the first focussable element).

### Shift

The popover shifts in order to remain in view of the visible area, with the pointer maintaining the context that the popover is attributed to.  
  
[Learn more about shift at the Floating UI library.](https://floating-ui.com/docs/shift)

### Flip

The popover flips to the opposite side once it’s about to overflow the visible area, with the pointer maintaining the context that the popover is attributed to. Once enough space is detected on its preferred side, it flips back to its original position.  
  
[Learn more about flip at the Floating UI library.](https://floating-ui.com/docs/flip)

### Transition

When triggered, the popover transitions using the `fade` transition preset.

* * *

Usage
-----

Here’s how and when to use the popover:

* * *

Use popovers for non-critical information

Popovers are intended for displaying non-critical information related to an element. Content passed to a popover should match the Aria-label and description.

* * *

Don’t use overlays with popovers

Avoid using an overlay with a popover, as they’re intended for non-critical information and shouldn’t prevent a user from performing other tasks on the screen. If you’re displaying critical information, consider a [modal](/components/modal/) instead.

* * *

Make popovers clear and concise

Avoid large chunks of text in popovers. Too much text can cause cognitive overload, and users with smaller screens or who are zoomed in can lose their place.

* * *

Don’t use rich text formatting

Rich text formatting (e.g. bold, italics, icons) won’t be conveyed to screen reader users.

* * *

Keep popovers in view until dismissed

Popovers should remain in view until the user dismisses them.

* * *

Don’t cover the attributed element

Avoid covering the element that the popover is attributed to, as it will lose its context.

* * *

Accessibility considerations
----------------------------

The popover has the following accessibility considerations:

*   Popovers must be discoverable and readable with a mouse or other pointer device, keyboard, screen reader, zoom software and any other assistive technology
    
*   Popovers should provide information that’s helpful for learning the UI, but isn’t required to operate it
    
*   When open, popovers shouldn’t block the user from performing any other task on the screen. You should test this across all breakpoints
    

Focus order

Order

Element

Role

Focus trapping is not available for the popover.

Upon focus of the popover, the first interactive element in the specified order will receive focus (i.e. if there are interactive elements passed to the header, this will be the first focussable element).

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

By default, the popover only describes its child element. The content of the popover acts as an accessible description and `aria-describedby` is added to the popover's child elements.  
  
If the popover provides the only visual label (e.g. an icon button) then you should use the popover to label its child elements. Otherwise, the children will have no accessible name and the popover will violate [success criterion 2.5.3 in WCAG 2.1.](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html)  
  
You can pass the `asLabel` prop to make the popover act as a label. In this case, `role=popover` will be removed, and if popover content is a string, `aria-label` is added to child elements. Otherwise, `aria-labelledby` will be added.

* * *

SEO considerations
------------------

*   Ensure all text, icons and images are visible in the popover so that information can be crawled and indexed
    
*   The popover component and its content are rendered to the DOM, but only visible to the user when the popover is open.
    

* * *

API
---

Popover

Props

Overrides

The popover has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that can be overridden to define its appearance.

Name

Type

Default

Description

Required

If the popover is wrapping a functional component, ensure that the functional component accepts a ref using [forwardRef.](https://reactjs.org/docs/forwarding-refs.html)

The popover has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that can be overridden to define its appearance.

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

### Modal



](/components/modal/)

A Modal is a layout panel that presents critical information or requests users input without navigating away from the current page.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)