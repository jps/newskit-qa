Icons | NewsKit design system

Icons
=====

Overview
--------

Icons are small SVG shapes, ranging from basic UI shapes to brand logos. NewsKit provides utility functions to create themably icons from SVG files or [emotion-icons](https://emotion-icons.dev/).

### Usage

Icons can be used to enhance other elements and content, as well as used inside links or buttons when space is limited.

Importing Emotion icons
-----------------------

Breaking Change

From version 6 we do not export emotion icons as part of newskit library.

In order to continue using icons from Emotion, you will need to import them directly from the `emotion-icons` package and convert them to NewsKit icons using the toNewsKitIcon utility function.

You can find the list of available icons on the [emotion-icons.dev](https://emotion-icons.dev/) page.

The following example shows how to convert an emotion icon to a NewsKit icon:

    1
    2    import {toNewsKitIcon} from 'newskit';
    3    import {AccountTree} from '@emotion-icons/material/AccountTree';
    4    const IconFilledAccountTree = toNewsKitIcon(AccountTree);
    5  
    

Creating NewsKit icons
----------------------

With the help of the [`customToNewsKitIcon`](/components/utils/custom-to-newskit-icon/) util function, each SVG icon can be easily turned into a Newskit icon that works well with theme tokens and [`getFromTheme`](/components/utils/get-from-theme/) util functions. The only requirement is to wrap the SVG markup within an `Svg` component and pass props to it.

With the help of the [`customToNewsKitIcon`](/components/utils/custom-to-newskit-icon/) util function, each SVG icon can be easily turned into a Newskit icon that works well with theme tokens and [`getFromTheme`](/components/utils/get-from-theme/) functions. The only requirement is to wrap the `SVG` markup within an Svg component and pass props to it.

The following example shows how the SVG component should be used:

    1
    2  <Svg {...props} viewBox="0 0 429 422">
    3    <g fill="none" fillRule="evenodd" transform="translate(-77.000000, -1738.000000) translate(77.000000, 1738.500000)">
    4      <circle cx="250.5" cy="242.5" r="178" style="mix-blend-mode:multiply"/>
    5      <circle cx="195" cy="195" r="195" style="mix-blend-mode:multiply"/>
    6    </g>
    7  </Svg>
    8 
    

Use `customToNewsKitIcon` utility function to make the svg icon compatible with NewsKit:

    1
    2export const IconFilledFacebook = customToNewsKitIcon(
    3  'IconFilledFacebook',
    4  props => (
    5    <Svg {...props} viewBox="0 0 24 24">
    6      <path
    7        fillRule="nonzero"
    8        d="M13.0784931,22.2595724 L13.0784931,13.1365112 L16.2002321,13.1365112 L16.6676019,9.5811424 L13.0784931,9.5811424 L13.0784931,7.31114568 C13.0784931,6.28180493 13.3699223,5.58025387 14.8748197,5.58025387 L16.7941176,5.57938466 L16.7941176,2.39951562 C16.4620261,2.35634473 15.3227937,2.25957241 13.9973813,2.25957241 C11.2301818,2.25957241 9.33569472,3.916388 9.33569472,6.9592112 L9.33569472,9.58123898 L6.20588235,9.58123898 L6.20588235,13.1366078 L9.33559627,13.1366078 L9.33559627,22.2595724 L13.0784931,22.2595724 Z"
    9      />
    10    </Svg>
    11  ),
    12);
    13 
    

Props
-----

Icons must have a size specified, and some also support an optional colour override.

titlestring

This optional prop adds title to the svg image in order to make it accessible and visible for screen readers. If your icon is just decorative and not part of the content this prop can be ommited, otherwise it should be passed.

overridesobject

If provided, overrides the respective presets for the component and provided elements.

stylePresetMQ<string>

If provided, this overrides the style preset applied to the svg.

sizeMQ<string>

If provided, this overrides the size of the icon.

marginInlineMQ<string>

Takes one space token to specify the logical inline start and end margin of the container. Can be used on breakpoints

marginInlineStartMQ<string>

Takes one space token to specify the logical inline start margin of the container. Can be used on breakpoints

marginInlineEndMQ<string>

Takes one space token to specify the logical inline end margin of the container. Can be used on breakpoints

marginBlockMQ<string>

Takes one space token to specify the logical block start and end margin of the container. Can be used on breakpoints

marginBlockStartMQ<string>

Takes one space token to specify the logical block start margin of the container. Can be used on breakpoints

marginBlockEndMQ<string>

Takes one space token to specify the logical block end margin of the container. Can be used on breakpoints

Rationale
---------

### Accessibility

Where icon colour can be overidden, the icon must have a 3:1 minimum contrast ratio with its background.