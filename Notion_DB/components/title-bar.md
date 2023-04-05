Title bar | NewsKit design system

Text

Title bar
=========

The title bar provides a headline for the content below with optional supporting actions.

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/title-bar)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-title-bar--story-title-bar)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/(v4)-NK-Web-Components?node-id=4145%3A123621&t=7UUQdJ2TqSKpYWOY-0)

* * *

Interactive demo
----------------

This demo lets you preview the title bar component, its variations, and configuration options.

### Heading

[Link](/)

Children

Render heading ash1h2h3h4h5h6span

Action itemUnsetLinkButton

    1import React from 'react';
    2import { TitleBar } from 'newskit';
    3
    4export default () => (
    5  <TitleBar headingAs="h3">Heading</TitleBar>
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

The title bar contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The title bar has options for different use cases:

### Actions

An action, such as a link, can be added to the title bar. They are positioned to the container's right, aligned to the title.

### Width

The container takes the entire width of the specified grid area, for example, 12 columns, six columns etc.

### Border

A border can be applied to the container to provide visual separation from the preceding or the following content.

### Heading tag

By default, the [title](https://newskit.co.uk/components/headline/) is set to h3. The tag can be set to 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' | 'span'.

### Actions

An action, such as a link, can be added to the title bar. They are positioned to the container's right, aligned to the title.

### Width

The container takes the entire width of the specified grid area, for example, 12 columns, six columns etc.

### Border

A border can be applied to the container to provide visual separation from the preceding or the following content.

### Heading tag

By default, the [title](https://newskit.co.uk/components/headline/) is set to h3. The tag can be set to 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' | 'span'.

* * *

Behaviours
----------

The following guidance describes how the title bar behaves.

### Actions are hidden at the xs breakpoint.

The action item is default hidden on an extra small (xs) breakpoint (below 480px). This allows the action to be placed at the bottom of the following content for an improved user experience.

### Actions are hidden at the xs breakpoint.

The action item is default hidden on an extra small (xs) breakpoint (below 480px). This allows the action to be placed at the bottom of the following content for an improved user experience.

* * *

Usage
-----

The following guidance describes how and when to use the title bar component appropriately.

* * *

Do use a title bar to create sections of content.

Use a title bar to create content sections. Add a link to additional content if available.

* * *

Accessibility considerations
----------------------------

The title bar has the following accessibility considerations:

Focus order

Order

Element

Role

Keyboard interactions

Command

Description

* * *

SEO
---

Title text should be set at the correct semantic level (e.g. [<h1> to <h6>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) ) to enable crawlers to better index the page.

* * *

API
---

Title bar

The title bar has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

The title bar has a range of props that can be used to define an appropriate experience for different use cases.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Link



](/components/link/)

Links allow users to navigate to a new location or to additional information.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)