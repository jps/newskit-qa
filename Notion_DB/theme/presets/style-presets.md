Style presets | NewsKit design system

Presets

Style presets
=============

A collection of foundational design tokens combined into a preset to define reusable styles for interface elements and their interactive states.

Overview
--------

Style presets define properties such as colour, border radius and text decoration across multiple states. For example, a style preset might contain the styles for all of a button’s states.  
  
Together with [typography presets](/theme/presets/typography-presets/), [sizing](/theme/foundation/sizing/) and [spacing](/theme/foundation/spacing/), style presets provide a component’s visual attributes.

* * *

Style preset properties
-----------------------

Style presets use a combination of the following styles:

Token

Accepted Values

Description

Choose CSS values carefully because of the impact on the theming system.

* * *

Style preset states
-------------------

You can apply the following states to style presets:

Example

State

Description

* * *

Use style presets
-----------------

You can apply style presets to components in several ways. [Learn more about using a theme in code](/theme/theming/using-a-theme/) to better understand the trade-offs of each approach.  
  
For more advanced use cases, access style presets from the theme by calling [getStylePreset](/components/utils/get-defaults/) or Emotion’s [useTheme hook](/components/utils/emotion/).

### Code example

You can declare style presets for the button component by passing it to the `createTheme` function:

    1const buttonSolidPrimary: StylePresetStates = {
    2    base: {
    3        backgroundColor: '{{colors.interactivePrimary030}}',
    4        borderRadius: '{{borders.borderRadiusCircle}}',
    5        color: '{{colors.inkInverse}}',
    6        iconColor: '{{colors.inkInverse}}',
    7    },
    8    hover: {
    9        backgroundColor: '{{colors.interactivePrimary040}}',
    10    },
    11    active: {
    12        backgroundColor: '{{colors.interactivePrimary050}}',
    13    },
    14    disabled: {
    15        backgroundColor: '{{colors.interactiveDisabled010}}',
    16        color: '{{colors.inkNonEssential}}',
    17        iconColor: '{{colors.inkNonEssential}}',
    18    },
    19    loading: {
    20        backgroundColor: '{{colors.interactivePrimary020}}',
    21        color: '{{colors.inkBrand010}}',
    22        iconColor: '{{colors.inkBrand010}}',
    23    },
    24};

* * *

Add custom style presets to the theme
-------------------------------------

See the [creating themes guide](/theme/theming/creating-a-theme/) for more details.

* * *

Transition Presets
==================

A collection of motion attributes combined into a preset to define reusable motion.

[Learn more about transition presets](/theme/presets/transition-presets/)

Transition Presets
==================

A collection of motion attributes combined into a preset to define reusable motion.

[Learn more about transition presets](/theme/presets/transition-presets/)