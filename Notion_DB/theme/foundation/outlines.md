Outlines | NewsKit design system

Foundations

Outlines
========

Outlines provide visual cues about the focus or active states of elements.

Overview
--------

The NewsKit design system provides a consistent default outline on elements using the following properties.

Outline Colour
--------------

Applying an Outline Colour to an element defines the colour of the element's outline. Outline colour utilises Interface and Interactive colour tokens.

### Code example

    1outlineColor: '{{outlines.outlineColorDefault}}'

* * *

Outline Style
-------------

Applying an Outline Style to an element defines the style of the element’s outline. Outline Style utilises the standard CSS outline Style values.

Outline Style

Token

Token value

### Code example

    1outlineStyle: '{{outlines.outlineStyleDefault}}'

Note

Safari's implementation of outline CSS is significantly different to other main browsers. The solid style will not have rounded corners, and using auto will not allow control over its colour. See Safari Outline Style.

* * *

Outline Width
-------------

Applying an Outline Width to an element defines the width of the element’s outline. NewsKit uses a simple set of design token to ensure consistency throughout the UI.

Outline Width

Token

Token value

### Code example

    1outlineWidth: '{{outlines.outlineWidthDefault}}'

If you wish to move away from the default provided, we recommend using [border](/theme/foundation/borders/) tokens

* * *

Outline Offset
--------------

Applying an Outline Offset to an element defines the offset of the element’s outline. NewsKit uses a simple set of design tokens to ensure consistency throughout the UI.

Outline Offset

Token

Token value

### Code example

    1outlineOffset: '{{outlines.outlineOffsetDefault}}'

If you wish to move away from the default provided, we recommend using [border](/theme/foundation/borders/) tokens

Note

Safari's implementation of outline CSS is significantly different to other main browsers. You may find your offset is not the same on Safari. See Safari Outline Style.

* * *

Safari Outline Style
--------------------

Add a different Outline Style for Safari

Safari Outline Style

Token

Token value

### Code example

    1safariOutlineStyle: '{{outlines.safariOutlineStyleDefault}}'

* * *

Safari Outline Offset
---------------------

Add a different Outline Offset for Safari

Safari Outline Offset

Token

Token value

### Code example

    1safariOutlineOffset: '-7px'

* * *

Opacity
=======

Opacity creates translucent interface elements.

[Learn more about opacity](/theme/foundation/opacity/)

Opacity
=======

Opacity creates translucent interface elements.

[Learn more about opacity](/theme/foundation/opacity/)