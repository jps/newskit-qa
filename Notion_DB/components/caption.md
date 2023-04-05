Caption | NewsKit design system

Text

Caption
=======

A caption is a text description of an image or video to describe what is showing.

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/caption)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-caption--story-caption-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=1967%3A5713&t=4rcwseDIwrZdWokj-0)

* * *

Interactive demo
----------------

This demo lets you preview the caption component, its variations, and configuration options.

Hathersage Moor in the Peak District

Credit by Matthew Taylor/Alamy

Caption text

Credit text

    1import React from 'react';
    2import { Caption } from 'newskit';
    3
    4export default () => (
    5  <Caption creditText="Credit by Matthew Taylor/Alamy">
    6    Hathersage Moor in the Peak District
    7  </Caption>
    8);
    9
    

Edit on CodeSandbox

* * *

Anatomy
-------

The caption contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The caption has options that can be used to provide an appropriate experience for different use cases.

### Credit text

A credit to the source can be added underneath the caption text.

### Inset spacing

The caption can be inset with increased spacing.

### Credit text

A credit to the source can be added underneath the caption text.

### Inset spacing

The caption can be inset with increased spacing.

* * *

Usage
-----

The following guidance describes how and when to use the caption component appropriately.

* * *

Don’t include captions inside images

Legibility can be poor and screen readers cannot read the words. Use live text instead.

* * *

Accessibility considerations
----------------------------

Captions help ensure that media like images and video are accessible to everyone by providing supplemental information about what the image is conveying. Captions are displayed within the main content and can be read by assistive technology.

* * *

API
---

Caption

Props

Overrides

The caption has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The caption has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Text Block



](/components/text-block/)

Text block provides a simple way to display text. It supports text cropping, style presets, and typography presets.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)