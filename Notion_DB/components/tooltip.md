Tooltip | NewsKit design system

Feedback & Status

Tooltip
=======

Tooltips display short, informational messages when a user hovers over or focusses on a UI element.

Status
======

Supported

* * *

Introduced
==========

[v5.7.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.7.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/tooltip)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-tooltip--story-tooltip-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/(v4)-NK-Web-Components?node-id=7827%3A137510&t=tMmC9eY3t1cyYBbd-0)

* * *

Anatomy
-------

The tooltip component contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The tooltip has options for different use cases:

### Size

Set a maxWidth and minWidth for the tooltip. Height is set automatically based on the content.

### Placement

Choose from 12 different tooltip placements.

### Pointer

Add a pointer to indicate the element to which the tooltip is attributed. Set it to 'visible' or 'hidden' as required.  
  
The pointer changes position depending on the placement of the tooltip.

### Offset

Change the space between the tooltip and the element with spacing tokens. By default, there's 8px of space between the tooltip and the element, measured from the tip of the pointer, or from the panel if you’re not using a pointer.  
  
If no pointer is visible, the offset can still be set via overrides.

### Size

Set a maxWidth and minWidth for the tooltip. Height is set automatically based on the content.

### Placement

Choose from 12 different tooltip placements.

### Pointer

Add a pointer to indicate the element to which the tooltip is attributed. Set it to 'visible' or 'hidden' as required.  
  
The pointer changes position depending on the placement of the tooltip.

### Offset

Change the space between the tooltip and the element with spacing tokens. By default, there's 8px of space between the tooltip and the element, measured from the tip of the pointer, or from the panel if you’re not using a pointer.  
  
If no pointer is visible, the offset can still be set via overrides.

* * *

Behaviours
----------

Here’s how the tooltip behaves:

### Triggering and closing the tooltip

The tooltip is triggered when the user hovers and/or focusses on the UI element to which it is attributed. Removing focus or hover dismisses the tooltip.

### Shift

The tooltip shifts to remain in view while the pointer maintains context to the element it is attributed to.  
  
Learn more about shift at the Floating UI library.

### Flip

The tooltip flips to the opposite side once it's about to overflow the visible area, with the pointer maintaining the context that the tooltip is attributed to. Once it detects enough space on its preferred side, it flips back to its original position.  
  
Learn more about flip at the [Floating UI library.](https://floating-ui.com/docs/flip)

### Transition and delay

When triggered, the tooltip transitions using the `fade` transition preset.

A delay is applied to the first hovered item, after which there is no (or reduced) delay on subsequent tooltips until the user has stopped hovering over any relevant components.

### Triggering and closing the tooltip

The tooltip is triggered when the user hovers and/or focusses on the UI element to which it is attributed. Removing focus or hover dismisses the tooltip.

### Shift

The tooltip shifts to remain in view while the pointer maintains context to the element it is attributed to.  
  
Learn more about shift at the Floating UI library.

### Flip

The tooltip flips to the opposite side once it's about to overflow the visible area, with the pointer maintaining the context that the tooltip is attributed to. Once it detects enough space on its preferred side, it flips back to its original position.  
  
Learn more about flip at the [Floating UI library.](https://floating-ui.com/docs/flip)

### Transition and delay

When triggered, the tooltip transitions using the `fade` transition preset.

A delay is applied to the first hovered item, after which there is no (or reduced) delay on subsequent tooltips until the user has stopped hovering over any relevant components.

* * *

Usage
-----

Here’s how and when to use the tooltip:

* * *

Do use tooltips for supplemental information

Tooltips are intended for displaying supplemental information related to an element on hover or focus.

* * *

Don’t use tooltips for essential information

Avoid putting essential information in tooltips, as the content won’t be announced by screen readers. Content passed to the tooltip should match the aria-label and description.

* * *

Do make tooltips clear and concise

Avoid putting large chunks of text in tooltips as this can result in cognitive overload for some users.

* * *

Don’t put interactive context within tooltips

Avoid placing interactive content (e.g. links or buttons) within a tooltip. Consider using a [Popover](/components/popover/) instead.

* * *

Do keep tooltips in view until the user focuses away

Allow the mouse to easily move over the tooltip without dismissing it. Tooltips should remain in view until a user hovers or focusses away from them.

* * *

Don’t use rich text formatting

Rich text formatting (e.g. bold, italics, icons) won’t be conveyed to screen reader users.

* * *

Do add to icon buttons and standalone links for context

You can apply the tooltip to the icon button or standalone link to provide extra context on the intended action or destination.

* * *

Don’t let tooltips time out

Avoid using a timeout to hide the tooltip.

* * *

Don’t cover the attributed element

Avoid covering the element that the tooltip is attributed to, as it will lose its context.

Tooltip is not triggered if an element inside it has a disabled prop. If you would like to wrap a disabled component around Tooltip, [add a wrapper element](https://mui.com/material-ui/react-tooltip/#disabled-elements) `span` for example.

* * *

Accessibility considerations
----------------------------

The tooltip has the following accessibility considerations:

*   Tooltips must be discoverable and readable with a mouse or other pointer device, keyboard, screen reader, zoom software and any other assistive technology.
    
*   Tooltips should provide information that’s helpful for learning the UI, but isn’t required to operate it.
    
*   When open, tooltips shouldn’t block the user from performing any other task on the screen. You should test this across all breakpoints.
    

Focus order

Don’t pass links or other interactive elements to a tooltip. Tooltips are for short, informational messages on hover or focus.

Keyboard Interactions

Command

Description

WAI-ARIA

Element

Attribute

Value

Description

User supplied

By default, the tooltip only describes its child element. The content of the tooltip acts as an accessible description and `aria-describedby` is added to the tooltip's child elements.  
  
If the tooltip provides the only visual label (e.g. an icon button) then you should use the tooltip to label its child elements. Otherwise, the children will have no accessible name and the tooltip will violate [success criterion 2.5.3 in WCAG 2.1.](https://www.w3.org/WAI/WCAG21/Understanding/label-in-name.html)  
  
You can pass the `asLabel` prop to make the tooltip act as a label. In this case, `role=tooltip`is removed, and if tooltip content is a string, `aria-label`is added to child elements. Otherwise, `aria-labelledby` is added.

* * *

SEO considerations
------------------

The tooltip and its content are rendered to the DOM, but only visible to the user when the tooltip is open.

* * *

API
---

The tooltip has a range of props to define the experience in different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Props

Overrides

Name

Type

Default

Description

Required

If the tooltip is wrapping a functional component, ensure that the functional component accepts a ref using [forwardRef.](https://reactjs.org/docs/forwarding-refs.html)

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Banner



](/components/banner/)

Communicates essential information without blocking an experience.

[

### Flag



](/components/flag/)

A flag is a non-interactive visual indicator used to communicate status.

[

### Toast



](/components/toast/)

A Toast communicates confirmation of an action or a low-priority message that does not need to completely interrupt the user experience.

[

### Inline Message



](/components/inline-message/)

An Inline message communicates contextual information. They are positioned inline, in close proximity to the element they are adding context to.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)