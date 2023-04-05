Visible, Hidden & ScreenReaderOnly | NewsKit design system

Components

Visible, Hidden & ScreenReaderOnly
==================================

A collection of three components (visibility, hidden and screen reader only) to show and hide content at different breakpoints.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/blob/main/src/grid/visibility.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-visibility--story-visibility-component)

* * *

Components
----------

Visibility comprises three components.

### Visible

Content will be visible if the screen size matches the applied breakpoint.

### Hidden

Content will be hidden if the screen size matches the applied breakpoint.

### ScreenReaderOnly

Wraps an element as the child of the component so it’s readable by a screen reader but not visible to the user (using the ID for reference).

* * *

Code Example
------------

Note

You can toggle on the breakpoint indicator at the top of the screen with the ~ key.

* * *

Screen Reader Only
------------------

The 'ScreenReaderOnly' component wraps an element as the child of the component, making sure that it is not visible to the user but still readable by a screen reader, using the id to reference it.

* * *

Usage
-----

Here’s how and when to use visible, hidden and screen reader only:

* * *

Don’t hide elements required across breakpoints

Have equivalent functionality for all breakpoints (e.g. a drawer for top-level navigation items on xs or sm breakpoints where space is limited).

* * *

Accessibility considerations
----------------------------

Visibility has the following accessibility considerations:

Focus order

When used 'Hidden’ excludes content from focus order when the screen size matches the applied breakpoint.

WAI-ARIA

You can provide context, purpose and additional information for people who are using assistive tools. This benefits users who are blind or low vision or have cognitive disabilities.  
  
Apply an aria-labelledby or aria-describedby attribute to the element you want to be described. Then pass the 'id' for the aria attribute value to screen reader only.

Test all breakpoints carefully when using hidden or visible.

* * *

SEO considerations
------------------

Use visible or hidden where SEO is a consideration, to avoid layout shift.

* * *

API
---

Visible, hidden and screen reader only have a range of props to define the experience in different use cases.

Visible

Visible, hidden and screen reader only have a range of props to define the experience in different use cases.

Name

Type

Default

Description

Required

Hidden

‘Hidden’ has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

ScreenReaderOnly

‘ScreenReaderOnly’ has a range of props that can be used to define an appropriate experience for different use cases.

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

### Grid



](/components/grid/)

The grid and cell are used together to construct a visual grid for responsive page layout.

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