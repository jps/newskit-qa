Sizing | NewsKit design system

Foundations

Sizing
======

Standardised sizing increases visual consistency in an interface.

Overview
--------

NewsKit uses a simple, standard sizing scale. The size of every UI element, and the space between elements, is defined by a 4px rule (or pt/rem).

All UI elements align to a 4px square baseline grid to:

*   Increase visual consistency
    
*   Increase efficiency (fewer design choices = less code)
    
*   Make communication easier and reduce back and forth between design and engineering as the intent is clear and results are more predictable
    
*   Create a visual rhythm
    

If text is centred within a component (e.g. button) it’s already evenly distributed and doesn’t need to sit on the grid.

* * *

Why 4px?
--------

In addition to the above:

*   Most popular screen sizes are divisible by four, so grid columns fit the screen in the majority of use cases.
    
*   Many platforms allow users to set their preferred ‘density’, increasing or decreasing font size or whitespace in and between page elements. A 4px rule lets you scale consistently while maintaining the grid.
    

* * *

Touch target areas
------------------

To ensure there’s always a sufficient area for users to click or tap on interactive elements, NewsKit has a variety of component sizes (e.g. small, medium and large buttons and text inputs).  
  
On mobile breakpoints and devices, all interactive elements should have a touch target area no less than 44px². This is the minimum standard for iOS and Android.

In most cases when there are multiple interactive elements in close proximity, make sure touch target areas are separated by enough clear space (16px) to balance information density and usability.

* * *

Sizing tokens
-------------

Sizing tokens specify sizes throughout NewsKit, such as for icons, space and minimum or maximum widths or heights. Sizing tokens also define space tokens. The available sizes are:

Example

Token

Value

* * *

Code Usage
----------

You can override and apply sizing to components. See the [component defaults](/theme/theming/component-defaults/) page for details.  
  
For more advanced use cases, you can access these values from the theme by calling [getResponsiveSize](/components/utils/get-defaults/), emotion’s [useTheme hook](/components/utils/emotion/), or [getSizingCssFromTheme](/components/utils/get-css-from-theme/).

* * *

Spacing
=======

Space provides content hierarchy, reduces visual clutter and shows relationships between elements.

[Learn more about spacing](/theme/foundation/spacing/)

Spacing
=======

Space provides content hierarchy, reduces visual clutter and shows relationships between elements.

[Learn more about spacing](/theme/foundation/spacing/)