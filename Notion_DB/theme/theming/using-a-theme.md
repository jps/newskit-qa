Using Themes | NewsKit design system

Using Themes
============

Overview
--------

To render NewsKit components you must have a theme available for them to utilise. You can use your own theme, or use one of the two NewsKit defaults - NewsKit light and NewsKit dark. Details on how to create your theme can be found [here](/theme/theming/creating-a-theme/).

Setting a theme
---------------

### NewsKitProvider & ThemeProvider components

NewsKitProvider provides a single wrapper to configure your application which includes ThemeProvider, [MediaQueryProvider](/components/utils/hooks/#usemediaqueryobject), [InstrumentationProvider](/getting-started/code/instrumentation/) and [LayerOrganizer](/components/layer/).

A ThemeProvider utilises a React Context to provide a theme to all NewsKit components descended under it. You pass your theme (or a NewsKit default) to the `theme` prop. This will typically be an uncompiled theme, but you can pass a pre-compiled theme if you wish.

The theme provided is then available to any NewsKit component under it. The theme is also used by any custom styled components created using the `styled` function exported from NewsKit.

ThemeProvider's can also be nested - allowing the child to override the parent theme. This will only cause a shallow merge of the child theme over the parent. To create a sub-theme which inherits from a base theme, see the `createTheme` documentation [here](/theme/theming/creating-a-theme/).

ThemeProvider can be nested, however, we do NOT recommend nesting NewsKitProviders, as it can lead to unexpected behaviour. NewsKitProvider should only be used once per application on a very top level.

  
  
  

Reading a theme
---------------

As the example shows above, reading from a theme inside a styled component works as you would expect from Emotion. However, if you wish to read from the theme outside of a styled component, you have two options - a higher-order component and a React hook.

withTheme higher-order component
--------------------------------

By wrapping your component in `withTheme`, the theme object will be passed into your component as a prop.

### useTheme hook

The `useTheme` hook also allows you to access the theme, but helps avoid the extra "wrapper hell" that higher-order components bring.

Using CSS custom properties (variables)
---------------------------------------

NewsKit provides a way to expose the following tokens as CSS variables: `borders`, `colors`, `overlays`, `motions`, `shadows`, `sizing`, `spacePresets` and `fonts`.

Color tokens have prefix of `color` for example `inkBase` is `--color-inkBase`, the rest of the tokens are keeping their names like `sizing020` is `--sizing020`.

In order to enable that functionality to your project, you need to add a prop `exposeCssVariables` to ThemeProvider, or pass it as themeOptions to NewsKitProvider as the example bellow:

    1<NewsKitProvider theme={yourTheme} themeOptions={{exposeCssVariables: true}}>
    2  Main theme context
    3  <ThemeProvider theme={yourSubTheme} exposeCssVariables>Sub-theme context</ThemeProvider>
    4</NewsKitProvider>

Exposing CSS variables will add aditional **div** element to your HTML