Ordered List | NewsKit design system

Text

Ordered List
============

Ordered lists make blocks of text easier to read, structuring sequential information into manageable, numbered items.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/ordered-list)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-ordered-list--story-ordered-list-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=324%3A6&t=4J9R35wp8IXwtzPU-0)

* * *

Interactive demo
----------------

This demo allows you to preview the ordered list component, its variations, and configuration options.

1.  Prince Harry
2.  Meghan Markle
3.  Royal Family

OverridesDefaultutilityButton020

Style Preset OverridesDefaultinkPositiveinkNegative

Margin Preset Overridesspace010space020

    1import React from 'react';
    2import { OrderedList } from 'newskit';
    3
    4export default () => (
    5  <OrderedList
    6    overrides={{
    7      content: {
    8        typographyPreset: 'editorialParagraph010',
    9        stylePreset: 'inkBase',
    10      },
    11      counter: {
    12        typographyPreset: 'editorialParagraph010',
    13        stylePreset: 'inkBase',
    14      },
    15      spaceInline: 'space010',
    16    }}
    17  />
    18);
    19
    

Edit on CodeSandbox

* * *

Anatomy
-------

The ordered list contains two required elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The ordered list has options that can be used to provide an appropriate experience for different use cases.

### Counter

The counter applied to the content of the ordered list can be overridden to use any typography preset.

### Counter

The counter applied to the content of the ordered list can be overridden to use any typography preset.

* * *

Usage
-----

Here’s how and when to use the ordered list:

* * *

Do use for numerically ordered lists

Ordered list items are numbered, so use them in instances where items need to appear in numerical order.

* * *

Do use to break up sequential information

Use ordered lists to break up blocks of sequential information into manageable numbered items.

* * *

Accessibility considerations
----------------------------

The ordered list has the following accessibility considerations:  
  

*   The `ol` element is for [grouping a collection of items](https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H48) that appear in sequential numerical order.
    
*   Ordered lists are not keyboard operable unless the list items themselves are operable e.g. with [links](https://newskit.co.uk/components/link/).
    
*   Using unordered lists purely as a means of indenting text is discouraged. Refer to [Lists in HTML documents 10.2 in WCAG 2.1](https://www.w3.org/TR/html4/struct/lists.html#h-10.2) This is a stylistic issue and indenting of text can be achieved using the [text block component.](https://newskit.ceng-dev.newsuk.tech/components/text-block/)
    

* * *

API
---

Ordered list

The ordered list has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Any prop valid on a [ol The ordered list element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol) is also valid on the ordered list component.

The ordered list has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Unordered List



](/components/unordered-list/)

Unordered lists make blocks of related text easier to read, structuring information of equal value into manageable bulleted items.

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