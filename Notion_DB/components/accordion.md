Accordion | NewsKit design system

Navigation

Accordion
=========

Accordions show and hide related content. Use them to break up long pages into segmented, prioritised sections.

Status
======

Supported

* * *

Introduced
==========

[v5.6.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.6.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/accordion)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-accordion--story-accordion-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=324%3A4)

* * *

Anatomy
-------

The accordion component contains three required elements and no optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The accordion has options for different use cases:

### Single accordion or accordion group

Use the accordion as a single instance, or in a group of accordions stacked vertically.

### Heading level

The accordion title is wrapped in a heading tag (<h3> by default). Alter it to fit the information architecture of the page.

### Icon

Change the indicator icon from the default chevron.

### Single accordion or accordion group

Use the accordion as a single instance, or in a group of accordions stacked vertically.

### Heading level

The accordion title is wrapped in a heading tag (<h3> by default). Alter it to fit the information architecture of the page.

### Icon

Change the indicator icon from the default chevron.

* * *

States
------

The accordion has the following states:

### Base

The default style before the user interacts with the accordion.

### Focus

The accordion has a visual focus state when in focus. The focus state outlines the heading container.

### Hover

The header and cursor change style to let the user know the accordion is interactive.

### Disabled

Communicates that an accordion exists, but isn’t available in that scenario. When the user hovers over a checkbox in a disabled state, the cursor shows as ‘not allowed’.

* * *

Behaviours
----------

Here’s how the accordion behaves:

### Collapsed/expanded

The Accordion has two states:

*   collapsed with the panel closed
    
*   expanded with the panel open
    

The default state is collapsed. The chevron icon points down when the Accordion panel is collapsed and points up when the Accordion panel is expanded.

### First expanded on load

The first Accordion in a group is expanded on load.

### Expand all

All panels in a group are expanded on load.

### Expand single

Only one panel can be expanded at a time. When the user expands another accordion panel, the current panel collapses.

### Collapsed/expanded

The Accordion has two states:

*   collapsed with the panel closed
    
*   expanded with the panel open
    

The default state is collapsed. The chevron icon points down when the Accordion panel is collapsed and points up when the Accordion panel is expanded.

### First expanded on load

The first Accordion in a group is expanded on load.

### Expand all

All panels in a group are expanded on load.

### Expand single

Only one panel can be expanded at a time. When the user expands another accordion panel, the current panel collapses.

* * *

Usage
-----

Here’s how and when to use the accordion:

* * *

Do use for supporting information

Use accordions to provide supporting information.

* * *

Don’t use for important information

Avoid concealing crucial information in an accordion.

* * *

Do make headlines short and clear

Give accordions short, meaningful headings that tell users what’s inside the panel. Group together related topics.

* * *

Don’t nest accordions

Avoid nesting accordions within themselves.

* * *

Accessibility considerations
----------------------------

The accordion has the following accessibility considerations:  
  

*   Accordions must be discoverable and readable with a mouse, other pointer devices, keyboard, screen reader, zoom tools and any other assistive technology.
    
*   Exercise care in choosing how accordions are used and the content they contain. Hiding content in accordions can make it more difficult for a user to scan the page and increases cognitive load.
    

Focus order

Order

Element

Role

Keyboard interactions

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

*   Ensure all text, icons and images are visible in the accordion so that information can be crawled and indexed.
    
*   The accordion component and its content are rendered to the DOM, but only visible to the user when the panel is open.
    

* * *

API
---

Accordion

Props

Overrides

The accordion has a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define its appearance.

Name

Type

Default

Description

Required

The accordion has a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

Accordion group

The accordion group has a range of props that can be used to define an appropriate experience for different use cases. Use this component to group accordions together.

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Link



](/components/link/)

Links allow users to navigate to a new location or to additional information.

[

### Menu



](/components/menu/)

A Menu displays a list of navigational items. They are displayed either at the top of a screen, or at the side where space allows.

[

### Tabs



](/components/tabs/)

Allows users to alternate between views within the same context.

[

### Tag



](/components/tag/)

Tags are used to classify content, typically using keywords.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)