Breadcrumbs | NewsKit design system

Navigation

Breadcrumbs
===========

Breadcrumbs are used for secondary navigation.

Status
======

Supported

* * *

Introduced
==========

[v6.6.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v6.6.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/breadcrumbs)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-breadcrumbs--story-default)

* * *

Interactive demo
----------------

This demo allows you to preview the breadcrumbs component variations, and configuration options.

Sizesmallmediumlarge

SeparatorDefaultIcon

showTrailingSeparatortruefalse

    1import React from 'react';
    2import { Breadcrumbs } from 'newskit';
    3
    4export default () => (
    5  <Breadcrumbs size="medium" overrides={{}} />
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

Breadcrumbs contain three required elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

Breadcrumbs have options that can be used to provide an appropriate experience for different use cases.

### Size

There are three sizes of breadcrumb items: small, medium, and large.

### Separator

The separator can be customised to use an alternative component, or the icon overridden.  
  
Separators are non-interactive.  
  
The last trailing separator can be set to be visible via the `showTrailingSeparator` prop.

### Size

There are three sizes of breadcrumb items: small, medium, and large.

### Separator

The separator can be customised to use an alternative component, or the icon overridden.  
  
Separators are non-interactive.  
  
The last trailing separator can be set to be visible via the `showTrailingSeparator` prop.

* * *

States
------

Breadcrumbs have states including, base, selected, hover, active, and focus. By default, the selected breadcrumb item is non-interactive.

### Base

Breadcrumb items have a base state. This is the base style of the breadcrumb item before it has been interacted with by a user.

### Selected

The selected breadcrumb item (current) is non-interactive and appears visually in a selected state.

### Hover

Breadcrumb items have a hover state. The style of the breadcrumb item changes to visually communicate and provide feedback to the user that the breadcrumb item is an interactive element.

### Active

Breadcrumb items have an active state. The style of the breadcrumb item changes to visually communicate and provide feedback to the user that the breadcrumb item has been interacted with.

### Focus

Breadcrumb items in a focus state communicate that a user has highlighted a breadcrumb item, using an input method such as a keyboard or voice.

* * *

Behaviours
----------

The following guidance describes how breadcrumbs behave.

### Selected breadcrumb item

By default, the current page breadcrumb item is displayed as non-interactive and is set via the `selected` prop.

### Selected breadcrumb item

By default, the current page breadcrumb item is displayed as non-interactive and is set via the `selected` prop.

* * *

Usage
-----

Here’s how and when to use breadcrumbs:

* * *

Do use breadcrumbs for secondary navigation

Use breadcrumbs for internal secondary navigation links.

* * *

Dont use as the primary navigation

Don’t use breadcrumbs as the primary navigation for a website. Instead, use the menu component.

* * *

Do add breadcrumbs after primary navigation

Breadcrumbs should be placed horizontally after the primary page navigation and before the main page content.

* * *

Don't wrap across multiple lines

Avoid wrapping breadcrumb items across multiple lines.

* * *

Do keep breadcrumb items short

Breadcrumb item names should be short and clearly reflect the page it links to.

* * *

Don't have external breadcrumb items

Breadcrumb items shouldn’t be used for external links.

* * *

Don't make the last breadcrumb item interactive

The last breadcrumb item (current) should not be a link. It can be set to hidden if the current page is clearly labelled elsewhere (e.g. an article headline).

* * *

Don't use breadcrumbs for a multi-step process

Don’t use breadcrumbs as a method of taking users through a multi-step process. Use a stepper component instead.

* * *

Accessibility considerations
----------------------------

Breadcrumbs have the following accessibility considerations:  
  

*   Breadcrumbs are structured using an [ordered list](https://www.newskit.co.uk/components/ordered-list/). This is because nav elements labeled as ‘breadcrumb’ identify the structure as a breadcrumb trail, making it a navigation landmark so that it is easy to locate.
    
*   To prevent screen reader announcement of the visual separators between breadcrumb items, they are added via CSS, hidden via `aria-hidden`.
    
*   The separators that appear between breadcrumb items are non-interactive.
    

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

SEO
---

*   Breadcrumbs should appear after the primary page navigation in the [DOM order](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).
    
*   Consider mobile-first indexing when using breadcrumbs to ensure optimal page indexing and ranking. For more information, refer to [mobile-first indexing best practices from Google Search Central.](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing#:~:text=Mobile%2Dfirst%20indexing%20means%20Google,page%20to%20a%20user's%20query.)
    
*   The rendered breadcrumbs are built using a [native HTML nav element](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Breadcrumb_Navigation), this should ensure that it is easy for crawlers to discover.
    
*   Navigational Items should have clear descriptive full-page titles in the breadcrumb trail to allow crawlers to correctly identify content.
    
*   It is recommended to have a simple (clickable) link for each level on the trail, except for the current page.
    
*   You can choose to display breadcrumbs on a page, e.g. once below the primary navigation and above the footer in the DOM (across all devices).
    

* * *

API
---

Breadcrumb

The breadcrumb has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Breadcrumbs have a range of predefined elements and attributes that can be overridden to define their appearance.

Attribute

Type

Default

Description

Breadcrumb item

Props

Overrides

The breadcrumb item has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

Please refer to the [button component](https://storybook.newskit.co.uk/?path=/docs/components-button--story-button-default) for details of the props and other overrides.

You can choose to hide the selected (current) breadcrumb item by using [hidden.](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden)

Attribute

Type

Default

Description

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