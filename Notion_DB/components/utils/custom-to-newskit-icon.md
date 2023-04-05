customToNewsKitIcon() | NewsKit design system

customToNewsKitIcon()
=====================

Syntax
------

    1customToNewsKitIcon(displayName, CustomIcon, overrides)

Overview
--------

Transform SVG markup into a Newskit icon that works well with theme tokens and `getFromTheme` util functions.

Parameters
----------

displayNamestring

The display name of the icon. It is required an icon name to start either with **\`IconFilled\`** or **\`IconOutlined\`** prefix, depending on the imported icon type.  
E.g: If importing an **MenuBook** icon, the final icon display name should be **\`IconFilledMenuBook\`** or **\`IconOutlinedMenuBook\`**

CustomIconReact.ComponentType<SvgProps>

NewsKit Svg component with SVG passed to it's children, props should be spread on the root Svg component, see example below.

overridesSvgProps\["overrides"\]

Default [override props](/components/icons/#props) passed to the transformed icon. Overrides can still be passed to the icon to overwrite these values at render time.

Return value
------------

Returns a NewsKit icon.

Example
-------