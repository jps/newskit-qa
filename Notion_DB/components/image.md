Image | NewsKit design system

Media

Image
=====

Images are a type of visual media. They can appear at fixed sizes, percentages, and aspect ratios.

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/image)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-image--story-image-fixed-width-and-height-px)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/(v4)-NK-Web-Components?node-id=4341%3A145047&t=NntLsFMIL5G5rK8U-0)

* * *

Interactive demo
----------------

This demo allows you to preview the image component, its variations, and configuration options.

![Example](static/placeholder-3x2.png)

src

alt

width

height

Loading Aspect Ratio

Placeholder iconUnsettrue

Image Style PresetimageSharpimageRoundedMediumimageCircle

    1import React from 'react';
    2import { Image } from 'newskit';
    3
    4export default () => (
    5  <Image
    6    src="static/placeholder-3x2.png"
    7    alt="Example"
    8    width="300"
    9    height="200"
    10    loadingAspectRatio="3:2"
    11    overrides={{ stylePreset: 'imageSharp' }}
    12  />
    13);
    14
    

Edit on CodeSandbox

* * *

Anatomy
-------

The image component contains two required elements and two optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The image has options for different use cases:

### Image dimensions

The width and height dimensions of an image can be set to fixed sizes or percentages.

### Placeholder icon

The image has a placeholder icon that can be used to display a custom icon e.g. brand logo.

### Caption

A [caption](/components/caption/) component can be added to an image with an optional credit to the image source.

### Image dimensions

The width and height dimensions of an image can be set to fixed sizes or percentages.

### Placeholder icon

The image has a placeholder icon that can be used to display a custom icon e.g. brand logo.

### Caption

A [caption](/components/caption/) component can be added to an image with an optional credit to the image source.

* * *

States
------

The image has the following states:

### Base

The default style of the image when loaded.

### Loading

Communicates that an image will be shown available when loading is complete, indicated with a placeholder icon. This state can be skipped when the renderOnServer prop is set to 'true'.

* * *

Behaviours
----------

Here’s how the image behaves:

### Loading

When in a loading state, the loading container of the image can determine the height or width of the image if only one dimension is provided. Image loading can be set to 'lazy' which will wait until the browser estimates it will be needed. Or 'eager' which will load the image as soon as possible.

### Loading

When in a loading state, the loading container of the image can determine the height or width of the image if only one dimension is provided. Image loading can be set to 'lazy' which will wait until the browser estimates it will be needed. Or 'eager' which will load the image as soon as possible.

* * *

Usage
-----

Here's how and when to use the image:

* * *

Don’t use text in images

Avoid including text in images, as screen readers will not be able to read the words.

* * *

Accessibility considerations
----------------------------

Image alt text

*   Always provide an [alternative text description](https://www.w3.org/WAI/tutorials/images/) that describes the information or function the image represents via the alt prop. This will allow screen readers and any other assistive technology to understand the image.
    
*   This [alt-decision](https://www.w3.org/WAI/tutorials/images/decision-tree/) tree is helpful for determining whether and how to provide alternative text.
    
*   Alt-text is not usually visible but is read out by screen readers or displayed if an image does not load or if images have been switched off.
    

* * *

SEO
---

Ensure placeholder icons have alt text applied.

* * *

API
---

Image

The image has a range of props to define the experience in different use cases.

Props

Overrides

Name

Type

Default

Description

Required

The image has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

It is not recommended to have both height and width values expressed as percentages. Both width and aspectRatio should be supplied in a consistent manner.

* * *

Related components
------------------

[

### Icons



](/components/icons/)

Small SVG shapes, ranging from basic UI shapes to brand logos.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)