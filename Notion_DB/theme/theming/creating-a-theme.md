Creating Themes | NewsKit design system

Creating Themes
===============

Overview
--------

Themes represent the brand's identity, controlling the appearance of all NewsKit components. They are Javascript objects that contain the foundations, presets, and component defaults. NewsKit's theme creator provides sensible defaults so the consumer can override as much or as little as they wish. Currently the NewsKit component library houses 2 themes:

*   NewsKit Light - the default which all themes inherit from.
*   NewsKit Dark - an inverse of the light theme.

You can switch between these two themes on this documentation site by clicking the button in the top right. Details on how to use a theme in your project can be found [here](/theme/theming/using-a-theme/).

createTheme Function
--------------------

To create a theme you use the `createTheme` function exported from NewsKit. The createTheme function returns an `UncompiledTheme` object which can be passed to the `NewsKitProvider` or `ThemeProvider` component. When the provider is passed an uncompiled theme object, it will compile it automatically. If you wish to pre-compile your theme, you can do this by passing your theme to the `compileTheme` function exported from NewsKit. It is recommended you let the provider compile your theme automatically - you should not need to compile your theme yourself. More information on theme compilation is below.

`createTheme` takes one argument - an object - with the following properties:

namestring

This is the optional name of your theme.

baseThemeUncompiledTheme = NewsKit light theme

This is the theme which your new theme will inherit from - by default this is the NewsKit light theme. You can use the baseTheme functionality to create sub-themes. More information on this can be found below.

overridesPartial<UncompiledTheme> = {}

This is where you put all your custom theme values to create your theme, e.g. colours, font config, style presets, e.t.c. The overrides object structure matches the theme, think of this as being deep merged over the baseTheme.

checkOverridesboolean = false

If true, the theme creator will check your provided overrides against your base theme (or the NewsKit Light default, if not set) for unecessary overriding. For example, if red070 is set to #d20600 in the base theme, and you override red070 to the same #d20600 value, this will trigger a console warning. You can change this logging behaviour using the property below. To maximise performance, it is recommended you do not set this to true in production.

warningLogger(message: string) => void = console.warn

This logger is only used when checkOverrides is true. When using checkOverrides you can set your own logging behaviour by passing a suitable function. This can be useful if you wish to unit test your theme by passing an error throwing function or mock, for example. There is an example of this below.

### Sub-themes

Sub-themes can be used to style sub-brands or sections on a website. For example, your website might contain a sports section which uses the same theme, except the brand and interface colours change from blue to green. Creating sub-themes is simple. You use the `createTheme` function as you would normally except you also pass a base theme. Your base theme would be your main theme (e.g. the one with blue interface colours), and the overrides you provide would then change the elements where appropriate (e.g. changing those interface colours to green). This allows you to take advantage of the existing main theme - keeping things consistent - while still maintaining the ability to tweak elements for specific branding identities. You can use a sub-theme the same as any other regular theme. Sub-themes can even be used as base themes if desired - there is no limit to the depth of nesting themes and sub-themes.

Note that base themes passed to the theme creation function must be uncompiled. Passing a compiled theme will result in an error.

### Theme Compiling

Theme compilation is something performed automatically by the ThemeProvider. You can optionally compile a theme yourself and pass it to the ThemeProvider, but there are limited reasons you may want to do this. We recommend letting the ThemeProvider automatically compile the theme for you.

Theme compilation is an essential part of the theme process as it allows the theoretical design level "layers", e.g. colour palettes to foundations to style presets, to be overridden and customised as desired. For example, when passing overrides to the theme creator to override some colours, you could override a palette colour - say `red070` to a new hex value. This would change all uses of the `red070` token to your new value, whether used by an existing token in NewsKit light, or your own base theme. It does not matter in what theme or where it is used in a theme, the change would be reflected in all references to that token. This is why your overrides should reference tokens using a double curly bracket syntax, similar to Mustache templates, like so: `{{colors.red070}}`. All tokens inside those brackets are looked up at compile time and replaced with the final value, in this case a hex colour.

Tokens can also be used as object keys as well as values. As well as this, multiple tokens can be specified in a single field, this is how the spacing presets are created for example - `spaceInsetSquish030: '{{sizing.sizing030}} {{sizing.sizing040}}',`

To make this system as flexible as reasonably possible the compilation lookup process is recursive. This is utilised in NewsKit for example by a button style preset `buttonOutlinedNegative` using `{{colors.inkNegative}}` which in turn uses `{{colors.red070}}` which evaluates to a hex code colour. A recursion depth limit of 5 is in place to avoid recursive loops, if a loop should occur an error will be logged to console and the values will be set to empty strings.

As well as recursion protection the compiler will also log warnings when you reference tokens which it cannot find. This logging behaviour is overridable by passing your own logger function to the `errorLogger` property inside the options (2nd) argument. One useful reason to do this is to unit test your theme. By replacing the logger with an error throwing function or mock, you can ensure your theme is valid as part of your development lifecycle. There is an example of this below.

### Keywords

To allow you to build your theme more effectively, there are a few special "keywords" which can be used as keys or values. Note that they begin with double (2) underscore characters. The functionality of most of these keywords can be written yourself using functions if desired, however by using these keywords, you are able to perform the functionality while in JSON.

Note that the keywords will be removed from the object as they are interpreted. You should not expect to see the keywords in a compiled theme, for example.

Please note as of NewsKit V5, stylePresets are no longer global, instead they are under each component. You will need to import the component to use the style presets.

    1import { Button } from "newskit"

#### \_\_extends

This keyword is used as an object key, where the value is set to an object path in the theme. This will act like a shallow merge and put the values of the object in the token path into the object which `__extends` is specified. For example, to duplicate the buttonSolidPrimary style preset and replace the hover state:

    1export const stylePresets = {
    2  buttonSolidPrimary: Button.stylePresets.buttonSolidPrimary;
    3  buttonLightDarkToggle: {
    4    __extends: '{{stylePresets.buttonSolidPrimary}}',
    5    hover: {color: '{{colors.red010}}'},
    6}
    7  
    

Alternatively, you can also do this:

    1export const stylePresets = {
    2  buttonLightDarkToggle: {
    3    ...Button.stylePresets.buttonSolidPrimary,
    4    hover: {color: '{{colors.red010}}'},
    5  },
    6}
    7 
    

As well as a single token string, the `__extends` also supports an array of token strings. This can be used to merge multiple objects together. The order of the array is respected and is the merge order of the objects.

#### \_\_deepExtends

This keyword is similar to the above `__extends` keyword except it performs a deep merge. This is useful when you wish to merge multiple deep objects together, for example you might need to combine multiple style presets.

    1{
    2  "__deepExtends": [
    3    "{{stylePresets.buttonSolidPrimary}}",
    4    "{{stylePresets.inkContrast}}"
    5  ]
    6}

Note that only the items specified under the `__deepExtends` keyword will be deeply merged. In the example above, if you were to specify a `base` state with some extra properties, those would overrwrite the merged base states of the two style presets specified. Remember to specify another extends keyword inside any deep objects you wish to change, like below.

    1{
    2  "__deepExtends": [
    3    "{{stylePresets.buttonSolidPrimary}}",
    4    "{{stylePresets.inkContrast}}"
    5  ],
    6  "base": {
    7    "__deepExtends": [
    8      "{{stylePresets.buttonSolidPrimary.base}}",
    9      "{{stylePresets.inkContrast.base}}"
    10    ],
    11    "borderRadius": "{{borders.borderRadiusRounded010}}"
    12  }
    13}

#### \_\_delete

This keyword is slightly different to the above and is used as a value, not a key. When the compiler encounters this value the key will be deleted from the object. This can be useful when you wish to simply remove a key rather than override it. It can delete simple string tokens, e.g. a color in a style preset, as well as whole objects such as the cropAdjustments in a typography preset or the hover state in a style preset.

    1{
    2  "__extends": "{{stylePresets.buttonSolidPrimary}}",
    3  "base": {
    4    "__extends": "{{stylePresets.buttonSolidPrimary.base}}",
    5    "borderRadius": "__delete"
    6  },
    7  "hover": "__delete"
    8}

#### \_\_shallow

This keyword is used as an object key with a value of `true`. When used, it dictates that the object it is a key of should be shallow merged rather than deep merged. This is useful if you wish to override an entire object without having to specify all the keys you wish to delete. For example, for a state inside an existing style preset:

    1{
    2  "tagPrimary": {
    3    "base": {
    4      "__shallow": true,
    5      "backgroundColor": "{{colors.interactivePrimary010}}",
    6      "color": "{{colors.inkBase}}"
    7    }
    8  }
    9}

This would be equivalent to the following (where the keys using the `__delete` keyword exist in the base theme):

    1{
    2  "tagPrimary": {
    3    "base": {
    4      "backgroundColor": "{{colors.interactivePrimary010}}",
    5      "color": "{{colors.inkBase}}",
    6      "borderStyle": "__delete",
    7      "borderColor": "__delete",
    8      "borderWidth": "__delete",
    9      "iconColor": "__delete",
    10      "borderRadius": "__delete"
    11    }
    12  }
    13}

The benefit of using the `__shallow` keyword is that should any new keys be added to the base object, you do not need to update your theme to delete them.

This `__shallow` keyword is unique compared to the others as it is functionality of the underlying `deepMerge` function used as part of the theme creator. You can use this utility by importing `deepMerge` from NewsKit.

### Functions as theme values

In certain use cases you may find the need to create a theme value by utilising other parts of the theme. This can be done by setting the value of a key to a function. This function will be called with the uncompiled theme object when it is encountered. Please note that the compiler will call the functions as they are found and execution order is not guaranteed. The uncompiled theme will still contain any other functions or token references (e.g. `{{colors.red070}}` not `#ff0000`).

### Examples

#### Changing the blue colour palette

Shifting all the blue colours used by NewsKit could be done like so:

#### Adding and updating a colour

Adding a new red palette colour and updating a reference to it could be done like so:

#### Changing the default border radius

Changing the default border radius of NewsKit elements, such as buttons, to sharp corners could be done like so:

#### Setting custom font cropping config

For cropping your font you can use Font Metrics, which are the measurements of characters in a particular font. This approach is precise, easy to implement, and takes into account the fontWeight and fontSize of your font.

You can calculate font metrics for a font by loading a font file into the [Capsize docs](https://seek-oss.github.io/capsize/).

As outlined in the link, choose your font (point 1). If you are uploading your own font file, as general approach, start adjusting the font metrics by clicking on the icon highlighted with the red circle (image below). Adjust it so that H is within the capHeight lines and the font has homogeneous space at the top and the bottom of the Em Square(green lines in the image below.)

e.g

![Capsize adjustement suggestions](static/capsize-adustement.png)

Once satisfied, find and retrieve the metrics (point 3).

Font Metrics should be added to the font family objects in your theme under the relevant font weight token. E.g.:

    1{
    2  "fontWeight010": 400,
    3  "fontFamily010": {
    4    "fontFamily": "\"DM Sans\", sans-serif",
    5    "fontMetrics": {
    6      "fontWeight010": {
    7        "capHeight": 700,
    8        "ascent": 992,
    9        "descent": -310,
    10        "lineGap": 0,
    11        "unitsPerEm": 1000
    12      }
    13    }
    14  }
    15}

Generally, adding the fontMetrics in your theme for a weight of 400 is enough for the majority of our users. However, if in your case you see the need to use more precise metrics for different font weights you can specify them; 400 will be always the fallback.

#### Using a function as a value

#### Adding a style preset

#### Adding a typography preset

#### Unit testing your theme

#### Overriding an icon

NewsKit comes with [Material Design's Icon](https://material.io/resources/icons/?style=baseline) filled and outline sets included. In some cases, it might be desirable to replace the default icon with a user defined one, for instance if we want to use our own close icon across the system.

Check out the [Icons page](/components/icons/) for detailed explanation on how to create custom NewsKit icon.