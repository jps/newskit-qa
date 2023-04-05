Component defaults | NewsKit design system

Creating and using themes

Component defaults
==================

A preselected option that is applied to a component to define its appearance or behaviour.

Overview
--------

Each NewsKit component has default design tokens (component defaults) applied to define its default appearance, or behaviour.  
  
As part of the component defaults functionality, there is a consistent `overrides` prop on all components. This prop takes an object which mirrors the structure of the component defaults. Each component documents the structure of its component defaults on its respective documentation page.  
  
Component defaults can be overridden at either the theme level or at a component level.

Carefully consider if the desired impact of changing a component default is to change a specific instance of a component or multiple components. For example, changing the size used by all [button](/components/button/) components at a theme level, or changing the size of a specific instance of a button at a component level.

* * *

Overriding component defaults at a theme level
----------------------------------------------

To override at the theme level, update a theme or [create a theme](/theme/theming/creating-a-theme/) with the changes under the overrides property (similar to changing other areas of the theme). Components or interface elements that are utilising the updated property will reflect these changes.

### Example

Here is an example of overriding the component defaults for the medium-sized [button](/components/button/) component, changing the default [typography presets](/theme/presets/typography-presets/) and [style presets:](/theme/presets/style-presets/)

    1import {createTheme} from 'newskit';
    2
    3const theme = createTheme({
    4  name: 'newskit-component-defaults-change',
    5  overrides: {
    6    componentDefaults: {
    7      button: {
    8        medium: {
    9          typographyPreset: 'utilityButton010',
    10          stylePreset: 'buttonOutlinedPrimary',
    11        },
    12      },
    13    }
    14  },
    15});

Some components, like the button, will have variants in their component defaults such as size.

* * *

Overriding component defaults at the component level
----------------------------------------------------

### Example

    1import {Button} from 'newskit';
    2
    3// Overrides:
    4<Button
    5  size="medium"
    6  overrides={{
    7    typographyPreset: 'utilityButton010',
    8    stylePreset: 'buttonOutlinedPrimary',
    9  }}
    10>
    11  Content
    12</Button>;
    13
    14
    

These overrides will only apply to that specific instance of the component.

The variant (in this case, “medium”) is not included in the overrides. Variants are not specified in the component overrides prop, only the theme. Some components which are built using multiple components may have a nested structure to their component defaults.

The example below shows overriding the [button](/components/button/) component appearance:

    1// Component Defaults:
    2byline: {
    3  stylePreset: 'inkSubtle',
    4  typographyPreset: 'utilityMeta020',
    5  spaceStack: 'space020',
    6  link: {
    7    stylePreset: 'bylineLink',
    8    typographyPreset: 'utilityMeta020',
    9  },
    10  divider: {
    11    stylePreset: 'bylineDivider',
    12    spaceInline: 'space020',
    13  },
    14},
    15
    16// Overrides
    17<Byline
    18  overrides={{
    19    stylePreset: 'bylineCustom',
    20    typographyPreset: 'bylineCustom',
    21    spaceStack: 'space030',
    22    link: {
    23      stylePreset: 'bylineLinkCustom',
    24      typographyPreset: 'bylineLinkCustom',
    25    },
    26    divider: {
    27      stylePreset: 'bylineDividerCustom',
    28      spaceInline: 'space030',
    29    },
    30  }}
    31/>

* * *

### Breakpoint behaviour in component defaults

Part of the functionality of the defaults and overrides system, enables overriding of design tokens at specific breakpoints. For example, setting different typography presets at different breakpoints, can make the text larger on bigger devices than on smaller devices.  
  
Properties that support this are documented as using the generic `MQ` type, i.e. `MQ<string>`. This means passing a single string token to be used at all times, or a combination at breakpoints.

    1typographyPreset: {
    2    xs: 'editorialHeadline010',
    3    md: 'editorialHeadline010',
    4    lg: 'editorialHeadline010',
    5  }

* * *

NewsKit Account
===============

Complete account package with customer information and subscription management.

[Read more](/patterns/solutions/account/)

NewsKit Account
===============

Complete account package with customer information and subscription management.

[Read more](/patterns/solutions/account/)