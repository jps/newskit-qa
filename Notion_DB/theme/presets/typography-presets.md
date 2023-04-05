Typography | NewsKit design system

Presets

Typography presets
==================

A collection of foundational font design tokens combined into a preset to define reusable typography styles for specific text elements.

Overview
--------

Typography presets define properties such as font-family, font-weight and line-height, in one design token. In combination with [style presets](/theme/presets/style-presets/),[sizing](/theme/foundation/sizing/), and [spacing](/theme/foundation/spacing/) they provide the visual attributes of a component.

* * *

Default typography presets
--------------------------

Editorial

Utility

Use these styles in more expressive scenarios where you want to align more closely with your brand style, such as title bars and cards.

Example

Token

Font Family

Font Size

Line Height

Font Weight

Letter Spacing

Common uses

Use these styles in more functional scenarios where a clear message needs to be communicated (e.g. buttons, tabs, inline messages and banners).

Example

Token

Font Family

Font Size

Line Height

Font Weight

Letter Spacing

Common uses

* * *

Apply typography presets
------------------------

You can apply typography presets to components in several ways. Learn more about [using a theme](/theme/theming/using-a-theme/) to better understand the trade-offs associated with each approach.  
  
For more advanced use cases, access style presets from the theme by calling [getTypographyPreset](/components/utils/get-defaults/) or Emotion’s [useTheme hook](/components/utils/emotion/).

### Add custom typography presets to the theme

You can add custom typography presets to the theme. See the [creating a theme](/theme/theming/creating-a-theme/) guide for more.

Thoroughly consider adding additional typography presets due to the impact on the theming feature when using multiple themes.

### Extend typography presets

If you need additional CSS attributes on an existing typography preset for ad hoc usage, pass a [text block](/components/text-block/) to the styled function:

    1import {TextBlock, styled} from 'newskit'
    2
    3const ItalicTextBlock = styled(TextBlock)`
    4font-style:italic;
    5`;
    6
    7<ItalicTextBlock stylePreset="editorialParagraph010"> This Text is italic</ItalicTextBlock>

* * *

Text-crop
---------

To keep consistent and predictable spacing from design to code, we use a text cropping utility to remove additional space (leading) around text blocks. This lets you maintain a 4px baseline and keeps designs pixel perfect. See the text crop documentation for more.

* * *

Accessibility
-------------

Legibility is crucial in typography. Here’s how to keep things consistent and readable:

### Font size

While there’s no official minimum font size for the web, it’s generally agreed that 16px for body text is a good starting point.  
  
Of course, text will be smaller for elements such as labels and larger for headers.  
  
We recommend not going smaller than 12px.

### Line Height

Adequate space between lines is critical to text legibility. W3C accessibility guidelines say line spacing should be at least space-and-a-half within paragraphs, and paragraph spacing should be at least 1.5 times larger than line spacing.  
  
NewsKit uses relative line heights to ensure consistent spacing for all headings and body text sizes. Heading and headline styles are set to a default of 1.125x the font size and body text set at 1.5x the font size.

### Line length

Line length (also known as a measure) is the number of characters in a line of text. For readability, keep between 50 and 80 characters, including spaces.  
  
Lines narrower than 50 characters require the eye to jump to the next line too frequently, breaking the reader’s rhythm. Lines wider than 80 characters make it difficult to continue to the correct line in a large body of text.

### Font size

While there’s no official minimum font size for the web, it’s generally agreed that 16px for body text is a good starting point.  
  
Of course, text will be smaller for elements such as labels and larger for headers.  
  
We recommend not going smaller than 12px.

### Line Height

Adequate space between lines is critical to text legibility. W3C accessibility guidelines say line spacing should be at least space-and-a-half within paragraphs, and paragraph spacing should be at least 1.5 times larger than line spacing.  
  
NewsKit uses relative line heights to ensure consistent spacing for all headings and body text sizes. Heading and headline styles are set to a default of 1.125x the font size and body text set at 1.5x the font size.

### Line length

Line length (also known as a measure) is the number of characters in a line of text. For readability, keep between 50 and 80 characters, including spaces.  
  
Lines narrower than 50 characters require the eye to jump to the next line too frequently, breaking the reader’s rhythm. Lines wider than 80 characters make it difficult to continue to the correct line in a large body of text.

Component defaults
==================

A preselected option that is applied to a component to define its appearance or behaviour.

[Learn more about component defaults](/theme/theming/component-defaults/)

Component defaults
==================

A preselected option that is applied to a component to define its appearance or behaviour.

[Learn more about component defaults](/theme/theming/component-defaults/)