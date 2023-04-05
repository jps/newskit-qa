Tag | NewsKit design system

Navigation

Tag
===

Tags are used to classify content, typically using keywords.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/tag)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-tag--story-tag-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=1952%3A3407)

* * *

Interactive demo
----------------

This demo allows you to preview the tag component, its variations, and configuration options.

[Tag Content](https://www.newskit.co.uk/)

Content

Link

DisabledTrueFalse

Tag Sizesmallmediumlarge

OverridesDefaultStyle PresetTypography Preset

    1import React from 'react';
    2import { Tag } from 'newskit';
    3
    4export default () => (
    5  <Tag href="https://www.newskit.co.uk/" size="medium">
    6    Tag Content
    7  </Tag>
    8);
    9
    

Edit on CodeSandbox

* * *

Anatomy
-------

The tag contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The tag has options that can be used to provide an appropriate experience for different use cases.

### Size

There are three sizes of tag: small, medium, and large.

### Icons (leading & trailing)

Icons can be displayed in a tag and can be positioned either before (leading) or after (trailing) the label in the tag.

### Label

Labels can be displayed in a tag. A label can give more context to what a tag indicates.

### Size

There are three sizes of tag: small, medium, and large.

### Icons (leading & trailing)

Icons can be displayed in a tag and can be positioned either before (leading) or after (trailing) the label in the tag.

### Label

Labels can be displayed in a tag. A label can give more context to what a tag indicates.

* * *

States
------

The tag has the following states:

### Base

The tag has a base state. This is the base style of the tag before it has been interacted with by a user.

### Hover

The tag has a hover state. The style of the tag changes to visually communicate and provide feedback to the user that the tag is an interactive element.

### Focus

The tag in a focus state communicates that a user has highlighted a tag, using an input method such as a keyboard or voice.

### Active

The tag has an active state. The style of the tag changes to visually communicate and provide feedback to the user that the tag has been interacted with.

* * *

Behaviours
----------

The following guidance describes how a tag behaves.

### Fixed and full width

Tags can be displayed in two ways, but consideration should be made to how they will respond and react to containers around them:  
  
Fixed width - size dependent on content (label, icons).  
  
Full width - size responsive to the container it is applied to.

### Fixed and full width

Tags can be displayed in two ways, but consideration should be made to how they will respond and react to containers around them:  
  
Fixed width - size dependent on content (label, icons).  
  
Full width - size responsive to the container it is applied to.

* * *

Usage
-----

Here’s how and when to use tags:

* * *

Do make sure tags relate to the content

Tags should always have a direct relationship to the content they represent.

* * *

Don't make tags too wide

Avoid using full-width tags in wide containers. They are generally appropriate for small devices or contained components.

* * *

Do make sure tags have sufficient clearance

Do allow a sufficient hit area when placing two or more tags inline make sure they are a sufficient size or have spacing between them to avoid users accidentally hitting the wrong tag.

* * *

Don't have multiple words for labels

Avoid having multiple words for tag labels. They should be short and clear.

* * *

Accessibility considerations
----------------------------

The tag has the following accessibility considerations:

Focus order

Order

Element

Role

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

SEO
---

*   Tags are good for site navigation (for crawlers and users).
    
*   Ensure icons have alt text applied.
    

* * *

API
---

Tag

The tag has a range of props that can be used to define an appropriate experience for different use cases.

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

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)