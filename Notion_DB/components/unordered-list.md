Unordered List | NewsKit design system

Text

Unordered List
==============

Unordered lists make blocks of related text easier to read, structuring information of equal value into manageable bulleted items.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/unordered-list)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-unordered-list--story-unordered-list-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2058%3A880)

* * *

Interactive demo
----------------

This demo allows you to preview the unordered list component, its variations, and configuration options.

*   NewsKit provides components, guidelines and standards to enable digital product teams to create high-quality, consistent products quickly. NewsKit is built on modular design principles and backed by best practice guidance for design and development.
    
*   Unordered list items are not numbered, so use them in instances where ordering is not a factor. Where items are required to appear in numerical order use an ordered list.
    
*   Use unordered lists to break up blocks of related content into manageable bulleted items to make the information easier for users to read
    

List Data

List Data

List Data

List Data

List Item MarkerUnsetstar

Marker Aligncenterstartend

Marker SizeDefault (iconSize005)iconSize010iconSize020

Margin Preset OverridesDefaultincreaseSpacing

OverridesDefaultutilityButton020

Style Preset OverridesDefaultinkPositiveinkNegative

    1import React from 'react';
    2import { UnorderedList } from 'newskit';
    3
    4export default () => (
    5  <UnorderedList
    6    overrides={{
    7      marker: {
    8        size: 'iconSize005',
    9        spaceInline: 'space020',
    10        stylePreset: 'inkBase',
    11      },
    12      spaceStack: 'space040',
    13      content: {
    14        typographyPreset: 'editorialParagraph010',
    15        stylePreset: 'inkBase',
    16      },
    17    }}
    18  >
    19    {[
    20      'NewsKit provides components, guidelines and standards to enable digital product teams to create high-quality, consistent products quickly. NewsKit is built on modular design principles and backed by best practice guidance for design and development.',
    21      'Unordered list items are not numbered, so use them in instances where ordering is not a factor. Where items are required to appear  in numerical order use an ordered list.',
    22      'Use unordered lists to break up blocks of related content into  manageable bulleted items to make the information easier for users to read',
    23    ]}
    24  </UnorderedList>
    25);
    26
    

Edit on CodeSandbox

* * *

Anatomy
-------

The unordered list contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The unordered list has options that can be used to provide an appropriate experience for different use cases.

### Marker

The marker applied to the content of the unordered list can be overridden to use any icon.

### Marker alignment

The marker can be aligned at the centre, start, or end of the unordered list content.

### Marker

The marker applied to the content of the unordered list can be overridden to use any icon.

### Marker alignment

The marker can be aligned at the centre, start, or end of the unordered list content.

* * *

Usage
-----

Here’s how and when to use the unordered list:

* * *

Do use for non-sequential lists

Unordered list items are not numbered, so use them in instances where ordering is not a factor. Where items are required to appear in numerical order use an ordered list.

* * *

Don't use for numerically ordered lists

Avoid unordered lists in instances where items are required to appear in numerical order. Instead use an ordered list.

* * *

Do use for bulleted lists that are easier to read

Use unordered lists to break up blocks of related content into manageable bulleted items to make the information easier for users to read.

* * *

Accessibility considerations
----------------------------

The unordered list has the following accessibility considerations:  
  

*   The ul element is for [grouping a collection of items](https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H48) that don't need to be in a specific numerical order.
    
*   Unordered list are not keyboard operable unless the list items themselves are operable e.g. with links.
    
*   Using unordered lists purely as a means of indenting text is discouraged. Refer to [Lists in HTML documents 10.2 in WCAG 2.1](https://www.w3.org/TR/html4/struct/lists.html#h-10.2) This is a stylistic issue and indenting of text can be achieved using the [text block component.](https://newskit.ceng-dev.newsuk.tech/components/text-block/)
    

* * *

API
---

Unordered list

The unordered list has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Any prop valid on an [ul The unordered list element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), is also valid on the unordered list component.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Ordered List



](/components/ordered-list/)

Ordered lists make blocks of text easier to read, structuring sequential information into manageable, numbered items.

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