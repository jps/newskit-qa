Component Defaults Utils | NewsKit design system

Component Defaults Utils
========================

A group of functions used to retrieve values from the [component defaults or overrides objects](/theme/theming/component-defaults/).

Overview
--------

Each component has its own component defaults object as well as overrides prop. Component defaults map foundation and preset tokens to the component, describing the default look and feel. As well as being able to override these defaults in the theme, component overrides allow you to change these tokens as desired when rendering individual instances.  

The provided functions, specified below, are used to retrieve the CSS objects sitting behind the theme tokens. These functions don't access the theme directly themselves, they just orchestrate the process of fetching theme values, utilising the other _get from theme_ functions.

getStylePreset and getTypographyPreset parameters
-------------------------------------------------

defaultPathstring | undefined

It is an object-path used to access deep properties in the component defaults.  
Component defaults objects can have a nested structure that mirrors the structure of the component. Root level key of this object is always the name of the component.  
Example: "headline.kicker", "byline.divider", "shareBar" If not provided (undefined or false passed) desired value is looked up only in the respective overrides object.

overridePathstring | false = ""

It is an object-path used to access deep properties in the overrides.  
Overrides objects can have as well a nested structure that mirrors the structure of the component.  
Example: "kicker", "divider", "" (empty string)

optionsParameters<FromThemeUtil>\[2\]

This prop consists of different options used to control component-specific behaviours.

propsProps

Is the props of the component including the theme. If the function is used inside a styled component template literal, or a CSS block, Emotion.js will call the function first with the component props passed in.

Syntax
------

    1
    2  getStylePreset(defaultPath, overridePath, options)(props)
    3  
    4  options: {
    5    nestedCssSelector?: string;
    6    isLoading?: boolean;
    7    isSelected?: boolean;
    8    isDisabled?: boolean;
    9    isInvalid?: boolean;
    10    isValid?: boolean;
    11    isSvg?: boolean;
    12    omitStates?: StylePresetStates[];
    13    filterStates?: StylePresetStates[];
    14    omitStyles?: StylePresetStyleKeys[];
    15    filterStyles?: StylePresetStyleKeys[];
    16  };
    17  
    

Used to retrieve values mapped to the stylePreset key in the component defaults/overrides.

    1
    2  getTypographyPreset(defaultPath, overridePath, options)(props)
    3  
    4  options: {
    5    withCrop?: boolean;
    6  };
    7  
    

Used to retrieve values mapped to the typographyPreset key in the component defaults/overrides.

getResponsiveSpace, getResponsiveSize, getResponsiveMotion and getResponsiveBorder parameters
---------------------------------------------------------------------------------------------

cssPropertystring

It is a valid CSS property or callback function which will take CSS property as argument

defaultPathstring | undefined

It is an object-path used to access deep properties in the component defaults.  
Component defaults objects can have a nested structure that mirrors the structure of the component. Root level key of this object is always the name of the component.  
Example: "headline.kicker", "byline.divider", "shareBar" If not provided (undefined or false passed) desired value is looked up only in the respective overrides object.

overridePathstring | false = ""

It is an object-path used to access deep properties in the overrides.  
Overrides objects can have as well a nested structure that mirrors the structure of the component.  
Example: "kicker", "divider", "" (empty string)

defaultsObjectKeystring

Object key from component-defaults that is holding the value that we are trying to get

propsProps

Is the props of the component including the theme. If the function is used inside a styled component template literal, or a CSS block, Emotion.js will call the function first with the component props passed in.

    1
    2  getResponsiveSpace(cssProperty, defaultPath, overridePath, defaultsObjectKey)(props)
    3  // example
    4  getResponsiveSpace('marginRight', 'drawer.panel', 'panel', 'spaceInline')(props)
    5  // returns {marginRight: value} or media query object when token is MQ<T>
    6  
    

Example return value when the defaultPath is `MQ<string>`

    1// drawer.panel  in component defaults
    2{
    3  spaceInline: {
    4    xs: 'sizing010',
    5    sm: 'sizing020',
    6    md: 'sizing030',
    7  }
    8}
    9// Using getResponsiveSpace
    10getResponsiveSpace('marginRight', 'drawer.panel', 'panel', 'spaceInline')(props)
    11  
    12// returns media query object
    13{
    14'@media screen and (max-width: 479px)': {marginRight: '4px'},
    15'@media screen and (min-width: 480px) and (max-width: 767px)': {marginRight: '8px'},
    16'@media screen and (min-width: 768px)': {marginRight: '12px'},
    17}
    18
    

Used to retrieve space token

    1
    2  getResponsiveSize(cssProperty, defaultPath, overridePath, defaultsObjectKey)(props)
    3  // example
    4  getResponsiveSize('width', 'drawer.panel', 'panel', 'size')(props)
    5  // returns {width: value} or media query object when token is MQ<T>
    6  
    

Used to retrieve size token

    1
    2  getResponsiveMotion(cssProperty, defaultPath, overridePath, defaultsObjectKey)(props)
    3  // example
    4  getResponsiveMotion('transitionDuration', 'drawer.panel', 'panel', 'motionDuration')(props)
    5  // returns {transitionDuration: value} or media query object when token is MQ<T>
    6  
    

Used to retrieve motion token

    1
    2  getResponsiveBorder(cssProperty, defaultPath, overridePath, defaultsObjectKey)(props)
    3  // example
    4  getResponsiveBorder('borderWidth', 'drawer.panel', 'panel', 'weight')(props)
    5  // returns {borderWidth: value} or media query object when token is MQ<T>
    6  
    

Used to retrieve border token

You can use a callback function instead of passing directly cssProperty

    1
    2  // callback
    3  const cb = (space) => ({paddingLeft: space, paddingRight: space})
    4  // example
    5  getResponsiveSpace(cb, 'drawer.panel', 'panel', 'spaceInset')(props)
    6  // returns {paddingLeft: value, paddingRight: value} or media query object when token is MQ<T>
    7  
    

getStylePreset, getTypographyPreset, getResponsiveSpace, getResponsiveSize, getResponsiveMotion and getResponsiveBorder Return value
------------------------------------------------------------------------------------------------------------------------------------

Returns a CSS object, mapped to a theme token (mapped to a key in the component defaults/overrides) if valid attributes are received.

Here is an example of using the different functions:

Deprecated getSpacingInlineHorizontal, getSpacingInlineVertical, getSpacingStackHorizontal, getSpacingStackVertical and getSpacingInset
---------------------------------------------------------------------------------------------------------------------------------------

    1
    2  // @deprecated
    3  getSpacingInlineHorizontal(defaultPath, overridePath, options)(props)
    4  
    5  getResponsiveSpace('marginRight', defaultPath, overridePath, 'spaceInline')(props)
    6  
    

Used to retrieve value mapped to the [spaceInline](/theme/foundation/spacing/) key in the component defaults/overrides and places it as margin-right CSS property when the text or itmes flow is horizontal.

    1
    2    // @deprecated
    3    getSpacingInlineVertical(defaultPath, overridePath, options)(props)
    4    
    5    getResponsiveSpace('marginBottom', defaultPath, overridePath, 'spaceInline')(props)
    6  
    

Used to retrieve value mapped to the [spaceInline](/theme/foundation/spacing/) key in the component defaults/overrides and places it as margin-bottom CSS property when the text or itmes flow is vertical.

    1
    2    // @deprecated
    3    getSpacingStackHorizontal(defaultPath, overridePath, options)(props)
    4  
    5    getResponsiveSpace('marginRight', defaultPath, overridePath, 'spaceStack')(props)
    6  
    

Used to retrieve value mapped to the [spaceStack](/theme/foundation/spacing/) key in the component defaults/overrides and places it as margin-bottom CSS property when the text or itmes flow is horizontal.

    1
    2    // @deprecated
    3    getSpacingStackVertical(defaultPath, overridePath, options)(props)
    4  
    5    getResponsiveSpace('marginBottom', defaultPath, overridePath, 'spaceStack')(props)
    6  
    

Used to retrieve value mapped to the [spaceStack](/theme/foundation/spacing/) key in the component defaults/overrides and places it as margin-right CSS property when the text or itmes flow is vertical.

    1
    2    // @deprecated
    3    getSpacingInset(defaultPath, overridePath, options)(props)
    4  
    5    getResponsiveSpace('padding', defaultPath, overridePath, 'spaceInset')(props)
    6  
    

Used to retrieve value mapped to the spaceInsite key in the component defaults/overrides and applies it as padding CSS property to an element.

getSpacingInlineHorizontal, getSpacingInlineVertical, getSpacingStackHorizontal, getSpacingStackVertical and getSpacingInset Return value
-----------------------------------------------------------------------------------------------------------------------------------------

Returns a CSS value, or object, mapped to a theme token (mapped to a key in the component defaults/overrides) if valid attributes are received.

Returns an empty string if invalid attributes or no attributes are provided.