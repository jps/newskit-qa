Get CSS from theme utils | NewsKit design system

Get CSS from theme utils
========================

A group of functions used to retrieve token values from theme or component props. The following functions `getBorderCssFromTheme`, `getColorCssFromTheme`, `getMotionCssFromTheme`, `getOverlayCssFromTheme`, `getShadowCssFromTheme`, `getSizingCssFromTheme`, `getSpacingCssFromTheme`, `getTransitionPresetFromTheme` share the same annotation, therefore we will generalize them as `the getter function`. Also, since those functions are used in the same way, we will use only `getColorCssFromTheme` to build our Syntax and Example sections.

Overview
--------

Tokens are the foundation of every design system. The visual representation of every component is formed by combining multiple tokens into presets and group of presets later stored into [component defaults object.](/theme/theming/component-defaults/) The provided functions, specified above, are used to retrieve the token values from the correspodning getter sections.

Parameters
----------

cssPropertystring | FromThemeCallback

It is a valid CSS property or callback function which will take CSS property as argument

defaultTokenMQ<string>

The getter function will use this as a default token name to retrieve its value from the corresponding theme section.

propsProps

The getter functions are curried and the function returned takes the props of the component (including the theme). If the function is used inside a styled component template literal, or a CSS block, Emotion.js will invoke the curried function, passing the component props.

Syntax
------

    1(string, string) -> props -> CSSObject

    1getColorCssFromTheme(cssProp, defaultToken?)(props)

Return value
------------

Returns a CSS object if valid attributes are received. Returns an empty Object if invalid attributes or no attributes are provided.

Examples
--------

This is the most basic example. Here `Paragraph` component will include the color value for token: `blue020` found in the theme.

The function will accept non token values

You can pass a callback instead of a CSS property to generate a custom CSS Object

More utility getters
====================

The following section details additional theme utility getter functions.

getMediaQueryFromTheme()
------------------------

Contructs a media query from the provided breakpoint keys. Breakpoints are specified in the theme, there are 5: xs, sm, md, lg, xl.

### Syntax

    1getMediaQueryFromTheme(minWidth, maxWidth)(props)

### Parameters

minWidthBreakpointKeys

The min-width for the media query. Can be left falsy if only a max-width is to be used.

maxWidthBreakpointKeys

The max-width for the media query. Can be left falsy if only a min-width is to be used.

propsProps

Is the props of the component including the theme. If the function is used inside a styled component template literal, or a css block, Emotion.js will call the function first with the component props passed in.

### Return value

Returns a media query line, to be used before an opening brace.

Returns an empty screen query (`@media screen`) if no min or max width tokens are provided.

### Example

In this example the `Paragraph` component will use the min-width breakpoint value from `sm`.

In this example the `Paragraph` component will use the min-width breakpoint value from `sm` and the max-width value from `md`.

getDeviceQueryFromTheme()
-------------------------

Target a specific device with media query and apply custom styles to it with either a `CSSObject` or a `SerializedStyles` string.

### Syntax

    1getDeviceQueryFromTheme(Array<Devices>, CSSObject | SerializedStyles)()

### Parameters

targetDevicesArray<Devices>

An array of the devices to be targeted.

cssRulesCSSObject | SerializedStyles

A list of CSS rules that can be passed as either`CSSObject` or`SerializedStyles`;

### Return value

Returns css rules wrapped inside the specific media queries.

### Example

With CSSObject

With SerializedStyles

In this example the `Paragraph` component will be hidden from all models of iPad.

getStylePresetFromTheme()
-------------------------

Retrieve a style preset values as a css template from the current theme. For more information on what consists of style preset see doc [here](/theme/presets/style-presets/).

### Syntax

    1getStylePresetFromTheme(defaultToken, customProp, options)(props)

### Parameters

defaultTokenstring

Is the name of the style preset token to be retrieved. If provided, it is used as an object key on the style presets section of the theme to get the token value.

customPropstring

Is the name of the component prop in which a style preset token name can be provided by the end-user of the component. If provided, the style preset to be retrieved will come from the component prop.

optionsGetStylePresetFromThemeOptions

This prop consists of loading, selected, omitStates and omitStyles options. These are component specific behaviours that can be controlled via either state or passed down from parent as prop.

propsProps

The getter functions are curried and the function returned takes the props of the component (including the theme). If the function is used inside a styled component template literal, or a CSS block, Emotion.js will invoke the curried function, passing the component props.

### Return value

Returns a template string with style preset css styles.

Returns an empty string if invalid attributes or no attributes are provided.

### Example

In this example the `Paragraph` component will use the sizing value

    1<Paragraph stylePreset="linkInline" />

In this example the `Paragraph` component will use `linkInline` style preset set in the default theme.

    1<Paragraph stylePreset="linkInline" loading={true} />

In this example the component has a loading state passed down from the parent component. If so the `loading` style presets, if present, will override the `base` style presets.

    1<Paragraph stylePreset="linkInline" isSelected={true} />

In this example the component has a current state passed down from the parent component. If so the `selected` style presets, if present, will override the `base` style presets.

    1<Paragraph stylePreset="linkInline" omitStates={["disabled"]} />

In this example the component is using the `linkInline` style preset, without using `disabled` state style presets.

    1<Paragraph stylePreset="linkInline" omitStyles={["backgroundColor"]} />

In this example the component is using the `linkInline` style preset, while ignorning all `backgroundColor` across all style presets.

getTypographyPresetFromTheme()
------------------------------

Retrieve a typography preset from the current theme. A typography preset is a collection of typography related styles.

### Syntax

    1getTypographyPresetFromTheme(defaultToken, customProp, options)(props)

### Parameters

defaultTokenThemeToken

Is the name of the typography preset to be retrieved. If provided, it is used as an object key on the typography preset theme section to get the token value.

customPropExclude<keyof Props, 'theme'>

Is the name of the component prop in which a typography preset name can be provided by the end-user of the component. If provided, the typography preset to be retrieved will come from the component prop.

options{withCrop: boolean}

When true, will apply the crop options retrieved from the preset.

propsProps

Is the props of the component including the theme. If the function is used inside a styled component template literal, or a css block, Emotion.js will call the function first with the component props passed in.

### Return value

Returns a typography preset if valid attributes are received.

Returns an empty string if invalid attributes or no attributes are provided.

### Example

In this example the `Paragraph` component will include the typography styles from `editorialParagraph030` found in the theme if the `Paragraph` is used with no props:

    1<Paragraph />

However, it will include styles from `editorialSubheadline050` if the `Paragraph` is used with the `font` prop and the value passed in is `editorialSubheadline050`:

    1<Paragraph typographyPreset="editorialSubheadline050" />

getTransitionPresetFromTheme()
------------------------------

Retrieves a transition preset from the current theme.

### Syntax

    1getTransitionPresetFromTheme(token, componentClassName)

### Parameters

tokenThemeToken

Is the name of the transition preset to be retrieved. This is an object that contains the transition properties.

componentClassNamestring

This is an optional parameter when using the fade, slideLeft, slideRight, slideTop, slideBottom, moveUp and grow presets. The classname is applied to the component as it appears enters, exits or has finished the transition.

### Example

In the example above `backgroundColorChange` is the transition preset that will be applied.

When combined with the following `stylePreset` the paragraphs background will transition between states with different duration.