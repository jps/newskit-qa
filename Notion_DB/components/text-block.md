Text Block | NewsKit design system

Text

Text Block
==========

Text block provides a simple way to display text. It supports text cropping, style presets, and typography presets.

Status
======

Supported

* * *

Introduced
==========

0.17.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/text-block)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-text-block--story-text-block-default)

* * *

Interactive demo
----------------

This demo allows you to preview the Text Block, its variations, and configuration options.

TextBlock Content

Content

No CropDefault (false)true

Render Styled Text asDefault (p)h1h2h3h4h5divspan

With typography-preset overrideDefaulteditorialHeadline010

With style-preset overrideDefaultinkBrand010

    1import React from 'react';
    2import { TextBlock } from 'newskit';
    3
    4export default () => (
    5  <TextBlock>TextBlock Content</TextBlock>
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

The text block contains one element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The text block has options that can be used to provide an appropriate experience for different use cases.

### Render as

By using Render as, the text block can be converted to another heading element or div.

### Text crop

[Text crop functionality](/theme/foundation/fonts/#textcrop) can be disabled on the text block.

### Styling

Styling can be applied to the text block by using [style presets](/theme/presets/style-presets/) and [typography presets.](/theme/presets/typography-presets/)

### Drop cap

The drop cap can be applied to a paragraph to increase the size of the first `initial` letter. It has a number of defaults which define the space around, and the visual appearance of the drop cap.

### Render as

By using Render as, the text block can be converted to another heading element or div.

### Text crop

[Text crop functionality](/theme/foundation/fonts/#textcrop) can be disabled on the text block.

### Styling

Styling can be applied to the text block by using [style presets](/theme/presets/style-presets/) and [typography presets.](/theme/presets/typography-presets/)

### Drop cap

The drop cap can be applied to a paragraph to increase the size of the first `initial` letter. It has a number of defaults which define the space around, and the visual appearance of the drop cap.

* * *

Usage
-----

Here’s how and when to use the text block:

* * *

Do use for text content

Use the text block for any text content, to which typography presets and style presets can be applied.

* * *

Accessibility considerations
----------------------------

As this is an HTML element, this component can utilise any aria attribute, such as [region.](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions)  
  
By default, the text block will render as span. When using, consideration should be given as to what semantic level the text should be set at. This is to aid in the navigation of the page for users using assistive technologies. This can be configured with the as property.

* * *

SEO
---

Similar to accessibility, text should be set at the correct semantic level (eg [<h1> to <h6>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)), to enable crawlers to better index the page.

* * *

API
---

The text block has a range of props that can be used to define an appropriate experience for different use cases.

TextBlock

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Ordered List



](/components/ordered-list/)

Ordered lists make blocks of text easier to read, structuring sequential information into manageable, numbered items.

[

### Unordered List



](/components/unordered-list/)

Unordered lists make blocks of related text easier to read, structuring information of equal value into manageable bulleted items.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)