Link | NewsKit design system

Navigation

Link
====

Links allow users to navigate to a new location or to additional information.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/link)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-link--story-link-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=324%3A4)

* * *

Interactive demo
----------------

This demo allows you to preview the inline and standalone links, their variations, and configuration options.

[Link](http://example.com)

content

href

eventContextUnsetother event data

externalUnsettruefalse

    1import React from 'react';
    2import { LinkStandalone } from 'newskit';
    3
    4export default () => (
    5  <LinkStandalone href="http://example.com">
    6    Link
    7  </LinkStandalone>
    8);
    9
    

Edit on CodeSandbox

* * *

Anatomy
-------

The link contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The link has options that can be used to provide an appropriate experience for different use cases.

### Inline and standalone links

Links can be either inline (within a paragraph or body text) or standalone.  
  
The inline link doesn't have any text cropping applied. It is recommended to crop the whole paragraph, where the inline link appears.  
  
The standalone link has text cropping applied by default.

### External link

Navigates the user to an external site. Can be inline or standalone, indicated with a trailing icon.  
  

If the external prop is enabled, it automatically checks if the passed href is external or internal to the website where the link is used. If the href is external, an icon indicating this will be rendered after (trailing) the label.

### Inline and standalone links

Links can be either inline (within a paragraph or body text) or standalone.  
  
The inline link doesn't have any text cropping applied. It is recommended to crop the whole paragraph, where the inline link appears.  
  
The standalone link has text cropping applied by default.

### External link

Navigates the user to an external site. Can be inline or standalone, indicated with a trailing icon.  
  

If the external prop is enabled, it automatically checks if the passed href is external or internal to the website where the link is used. If the href is external, an icon indicating this will be rendered after (trailing) the label.

* * *

States
------

The link has the following states:

### Base

The base style of the link before the user has interacted with it.

### Hover

The style of the link changes to let the user know the link is interactive.

### Focus

Communicates that the user has highlighted a link, using an input method such as a keyboard or voice.

### Active

The link has an active state. The style of the link changes to visually communicate and provide feedback to the user that the link has been interacted with.

### Visited

The style of the link changes to let the user know the link has previously been visited.

### Visited hover

The style of the link changes to let the user know the link has been previously visited and is currently being hovered.

* * *

Usage
-----

Here’s how and when to use the link:

* * *

Do use inline links within paragraphs

Use inline links within paragraphs or sentences to link to content on the same page or other pages.

* * *

Do use standalone links within navigation components

Use standalone links outside of body content, for example within navigational components such as menus, headers, and footers.

* * *

Do use icons for external links

Use a trailing icon to indicate the link takes the user to an external site.

* * *

Accessibility considerations
----------------------------

The link has the following accessibility considerations:  
  

*   [Avoid opening links in a new tab or window](https://www.w3.org/TR/WCAG20-TECHS/G200.html), as it can be disorienting for users and can cause problems for users who are unable to visually perceive that the new tab has opened.
    
*   If there is a need for a link to open in a new tab, include the words 'opens in new tab' within the link text.
    

Focus Order

Order

Element

Role

Keyboard Interactions

Command

Description

WAI-ARIA

By default, there is no aria-label set in the link component. The text inside the anchor will be read by the screen reader, so it is important that links are descriptive. This is so that there is a clear expectation about where the link will take the user. If the text is not descriptive enough, an `aria-label` will be necessary to understand where the link is taking the user to.

Element

Attribute

Value

Description

User supplied

[WCAG 2.0](https://webaim.org/techniques/hypertext/link_text#underlining) has additional requirements for body text links that are not underlined by default.

* * *

API
---

LinkInline

The LinkInline has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Any prop valid on an [anchor HTML element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a), is also valid on the LinkInline component.

The LinkInline has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

LinkStandalone

The LinkStandalone has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Any prop valid on an [anchor HTML element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a), is also valid on the LinkStandalone component.

The LinkStandalone has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

LinkStandalone is a seperately exported component, which does not include an underline by default.

* * *

Related components
------------------

[

### Tag



](/components/tag/)

Tags are used to classify content, typically using keywords.

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