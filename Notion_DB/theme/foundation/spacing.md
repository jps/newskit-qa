Spacing | NewsKit design system

Foundations

Spacing
=======

Space helps to guide the user and provide a pleasant and consistent experience within products.

Overview
--------

Space is the distance between elements on a screen. It’s often referred to as whitespace.  
  
Good use of whitespace can de-clutter and group content to provide a visual hierarchy. This helps users focus on what matters and reduces cognitive load.

Space tokens
------------

Space tokens define spacing throughout NewsKit, such as the distance between an icon and the label in a button. The space tokens define three categories to control margin and padding for specific use cases: spaceInset, spaceInline and spaceStack.  
  
Here are the available space tokens:

Token

Value

Description

Be specific

Avoid using generic spacing tokens whenever possible in favour of more specific options such as space inset, space inline and space stack. Only use the generic variables when these don’t meet your needs.

### Code usage

You can override and apply space inset to components using [component defaults](/theme/theming/component-defaults/).  
  
For more advanced use cases, you can access these values from the theme by calling [getResponsiveSpacing](/components/utils/get-defaults/), emotion's [useTheme hook](/components/utils/hooks/), or [getSpacingCssFromTheme](/components/utils/get-css-from-theme/).

* * *

Logical props
-------------

We have added the following properties to our components to make it easier for users to set the spacing they desire.  
  
You can use space tokens with 12 different [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-inline-start)to logically apply space to a side, or combination of sides.  
  
Logical props can define either [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-inline-start#examples) or [margins](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-inline#examples), depending on the element's writing mode, directionality, or text orientation. orientation. For example, if the reading direction is `right to left` (instead of `left to right`) the`paddingInlineStart` would be on the right instead of the left.

### paddingInlineStart

Applies space to the start position (left) of an element.

### paddingInlineEnd

Applies space to the end (right) position of an element.

### paddingInline

Applies space to both the start (left) and end (right) positions of an element.

### paddingBlockStart

Applies space to the start position (top) of an element.

### paddingBlockEnd

Applies space to the end position (bottom) of an element.

### paddingBlock

Applies space to both the start (top) and end (bottom) positions of an element.

### marginInlineStart

Applies space to the start position (left) of an element.

### marginInlineEnd

Applies space to the end (right) position of an element.

### marginInline

Applies space to both the start (left) and end (right) positions of an element.

### marginBlockStart

Applies space to the start position (top) of an element.

### marginBlockEnd

Applies space to the end position (bottom) of an element.

### marginBlock

Applies space to both the start (top) and end (bottom) positions of an element.

### paddingInlineStart

Applies space to the start position (left) of an element.

### paddingInlineEnd

Applies space to the end (right) position of an element.

### paddingInline

Applies space to both the start (left) and end (right) positions of an element.

### paddingBlockStart

Applies space to the start position (top) of an element.

### paddingBlockEnd

Applies space to the end position (bottom) of an element.

### paddingBlock

Applies space to both the start (top) and end (bottom) positions of an element.

### marginInlineStart

Applies space to the start position (left) of an element.

### marginInlineEnd

Applies space to the end (right) position of an element.

### marginInline

Applies space to both the start (left) and end (right) positions of an element.

### marginBlockStart

Applies space to the start position (top) of an element.

### marginBlockEnd

Applies space to the end position (bottom) of an element.

### marginBlock

Applies space to both the start (top) and end (bottom) positions of an element.

Text crop
---------

To keep spacing consistent and predictable from design to code, we use a [text-crop](/theme/theming/creating-a-theme/) utility that removes additional space (leading) around a text block. This lets us maintain a 4px baseline and keep designs pixel perfect.

* * *

Style Presets
=============

A collection of foundational design tokens combined into a preset.

[Learn more about style presets](/theme/presets/style-presets/)

Style Presets
=============

A collection of foundational design tokens combined into a preset.

[Learn more about style presets](/theme/presets/style-presets/)