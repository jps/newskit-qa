Borders | NewsKit design system

Foundations

Borders
=======

Borders direct attention, identify components, communicate state, and express a brand.

Border Radius
-------------

Applying a Border Radius to an element rounds its corners. NewsKit uses a simple set of design token to ensure consistency throughout the UI.

Border radius

Token

Token value

### Code example

    1borderRadius: '{{borders.borderRadiusDefault}}'

* * *

Border Width
------------

Applying a Border Width to an element defines the width of the element’s border. NewsKit uses a simple set of design token to ensure consistency throughout the UI.

Border width

Token

Token value

### Code example

    1borderWidth: '{{borders.borderWidth000}} {{borders.borderWidth000}} {{borders.borderWidth010}} {{borders.borderWidth000}}'

Note

In addition to the Border Radius and Border Width foundations, Border Colour and Border Style can be applied to a UI element using the borderColor and borderStyle attribute on a Style Preset.

* * *

Border Colour
-------------

Applying a Border Colour to an element defines the colour of the element's border. Border colour utilises Interface and Interactive colour tokens.

### Code example

    1borderColor: '{{colors.interactivePrimary030}}'

* * *

Border Style
------------

Applying a Border Style to an element defines the style of the element’s border. Border Style utilises the standard CSS Border Style values.

### Code example

    1borderStyle: 'solid'

* * *

Breakpoints
===========

Breakpoints allow content to adapt to different viewports responsively.

[Learn more about breakpoints](/theme/foundation/breakpoints/)

Breakpoints
===========

Breakpoints allow content to adapt to different viewports responsively.

[Learn more about breakpoints](/theme/foundation/breakpoints/)