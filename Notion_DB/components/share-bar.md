Share bar | NewsKit design system

Actions & Inputs

Share Bar
=========

Share bars lets users share content to social media and other channels. They’re typically embedded within article pages. This component is deprecated and will be removed in the next major release.

Status
======

Deprecated

* * *

Introduced
==========

v0.20.1

* * *

[View code](https://github.com/newscorp-ghfb/newskit)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/deprecated-share-bar--story-horizontal)[View Design](https://github.com/newscorp-ghfb/newskit)

* * *

Interactive demo
----------------

This demo lets you preview the share bar component, its variations and configuration options.

Label

Label

VerticalTrueFalse

    1import React from 'react';
    2import { ShareBar } from 'newskit';
    3
    4export default () => <ShareBar label="Label" />;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The share bar component contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The share bar has options for different use cases:

### Orientation

Display the share bar horizontally or vertically.

### Label

Hide the label on the share bar. Hiding the label reduces visual noise, but may give less context.

### Orientation

Display the share bar horizontally or vertically.

### Label

Hide the label on the share bar. Hiding the label reduces visual noise, but may give less context.

* * *

Usage
-----

Here’s how and when to use the share bar component:

* * *

Don’t use a share bar for more than five items

The maximum number of items in a share bar should be kept to a minimum. It is not recommended to have more than 5 items.

* * *

Don’t add actions that are not relevant

Do not add actions that are not relevant to social sharing in a share bar (saving, commenting etc).

* * *

Accessibility considerations
----------------------------

Focus order

Order

Element

Role

WAI-ARIA

Element

Attribute

Value

Description

User supplied

If you have more than one share bar on a page, all share bar components (or their containers) should have a role set to the region and a unique aria-label.

When using an icon button in the share bar, set an aria-label (e.g. “share to Facebook”) on the icon button.

* * *

SEO considerations
------------------

Ensure icons have Alt Text applied.

* * *

API
---

Here are the properties for the share bar component:

Share bar

Share bar has a range of props to define the experience in different use cases.

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

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)