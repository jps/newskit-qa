Fonts | NewsKit design system

Foundations

Fonts
=====

Fonts establish styles for content such as headlines and paragraphs, as well as more functional styles for items such as labels, tags and messaging.

Overview
--------

You can use custom typography with NewsKit.  
  
When you [create a theme in code](/theme/theming/creating-a-theme/) or Figma, characteristics such as font family, font weight, letter spacing, line height and font style are applied in a systematic way.  
  
You can group font characteristics as [typography presets](/theme/presets/typography-presets/) that can be applied to text interface elements.

* * *

Font attributes
---------------

### Font family

A font family is a set of fonts with a shared design. For example, the Arial font family contains Arial, Arial Bold, Arial Bold Italic and Arial Italic. Font families are mapped to design tokens. You can apply a font family to any text element using the `fontFamily` attribute on a [typography preset.](/theme/presets/typography-presets/)

Token

Font family

Classification

Consider a web safe fallback font when defining a font family. Learn more about web safe fonts. [Learn more about web safe fonts.](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face)

### Font size

Font size is how large the characters are displayed on screen. It’s mapped to a scale of design tokens. You can apply font size to any text element using the `fontSize` attribute on a [typography preset.](/theme/presets/typography-presets/)

Example

Token

Value

### Font weight

Font weight is the thickness of the character stroke. It’s mapped to a scale of design tokens. You can apply font weight to any text element using the `fontWeight` attribute on a [typography preset.](/theme/presets/typography-presets/)

Example

Token

Value

### Font line-height

Font line height is the vertical space between lines of text. It’s mapped to a scale of design tokens. You can apply font line height to any text element using the `fontLineHeight` attribute on a [typography preset.](/theme/presets/typography-presets/)

Example

Token

Value

To make sure your font styles round up or down to the nearest 4px value, use `getLineHeight`. Your fonts will not be aligned otherwise.

    1lineHeight: getLineHeight(‘fontSize040’, ‘fontLineHeight020’)

The default baseline of NewsKit is 4px, and when calculating line-height for typographical styles we round either up or down to the nearest 4px value. This maintains a consistent visual approach when using typography across your UI designs.

### Font letter-spacing

Font letter spacing is the horizontal space between characters. It’s mapped to a scale of design tokens. You can apply font letter spacing to any text element using the `fontLetterSpacing` attribute on a [typography preset.](/theme/presets/typography-presets/)

Example

Token

Value

### Additional font properties

You can apply the following properties to typography. They can be defined as part of the [style presets.](/theme/presets/style-presets/) Using these properties in style presets promotes consistency through reuse of tokens.

Property

Example

Description

Font smoothing

To ensure typography in components is rendered smooth and crisp (rounded to the nearest pixel instead of subpixel), apply `-webkit-font-smoothing: antialiased`. Set this as a default across your product using Emotion’s global style component.

* * *

Text crop
---------

To reduce ‘pixel pushing', and to keep consistent and predictable spacing across multiple font families, use text cropping to remove additional space (leading) around text. This also helps maintain a 4px baseline, keeping interfaces ‘pixel perfect’.

### Benefits

Text cropping (sometimes referred to as leading trim) gives you a true representation of spacing and alignment when using text blocks.

### Methods

Text cropping works by cropping the bounding box of the text block component. There are several methods to crop both 'top' and 'bottom'; by default, NewsKit uses a pairing of 'cap height' for the 'top' and 'baseline' for 'bottom'. This is done by configuring negative margins.

### Cap height

Crop to the top of an uppercase letter in the typeface (e.g. the top of an uppercase T).

### Baseline

Crop to the baseline of all lowercase letters in the typeface.

### Configure

You can configure text cropping in both the codebase and Figma.

#### Code

Text cropping uses font metrics. This takes into account the nuances of each font and lets you easily generate the code needed using [Capsize](https://seek-oss.github.io/capsize/) .

#### Design

Use the [text crop plugin](https://www.figma.com/community/plugin/951930713294228024/Text-Crop) in Figma to crop a selected text block or all text block components on a page.

### Apply

You can configure text cropping in both the codebase and Figma.

#### Code

When using a text block component [text block](/components/text-block/) in code, text crop is applied by default. You can remove it with a `noCrop`.

    1
    2            import React from 'react';
    3            import { TextBlock } from 'newskit';
    4
    5            export default () => (
    6            <TextBlock noCrop>TextBlock Content</TextBlock>
    7            );
    8          
    

### Examples

### Button before text crop

Without the ability to crop text, the button text becomes misaligned when you change font family or font size.

### Button after text crop

With text cropping applied, the button label is always positioned correctly when you change font family or font size.

### Card before text crop

Without the ability to crop text, the layout of the card is unnecessarily elongated due to the misaligned spacing around the text blocks.

### Card after text crop

With text cropping applied, the spacing in the card is aligned correctly to the text blocks and the overall size of the card is exactly as defined.

* * *

Accessibility Considerations
----------------------------

For typography accessibility considerations, see [typography presets](/theme/presets/typography-presets/).

* * *

Gradients
=========

Gradients are a gradual blending from one colour to another, used to fade content and overlay images.

[Learn more about gradients](/theme/foundation/gradients/)

Gradients
=========

Gradients are a gradual blending from one colour to another, used to fade content and overlay images.

[Learn more about gradients](/theme/foundation/gradients/)