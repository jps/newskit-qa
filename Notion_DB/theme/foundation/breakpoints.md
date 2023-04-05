Breakpoints | NewsKit design system

Foundations

Breakpoints
===========

Breakpoints set a visual point on a screen to adapt the design of content (responsive design), ensuring a consistent, optimised experience across different screen widths.

Overview
--------

Choose from five different breakpoints. You can customise the breakpoint range, margins and gutters. The default values are:

Token

Breakpoint

Range

Usage

You can override default breakpoints in the theme:

    1import {createTheme} from 'newskit';
    2
    3const theme = createTheme({
    4  name: 'theme-with-custom-breakpoints',
    5  overrides: {
    6      breakpoints: {
    7          xs: 0, // 0-359
    8          sm: 360,
    9          md: 540,
    10          lg: 720,
    11          xl: 1080,
    12      }
    13  },
    14});

All breakpoints are fluid until the maximum grid width of 1920px (default). At this point, the grid becomes fixed.

### Fluid

Fluid layouts are calculated to their relative size, and stretch as the screen (viewport) is resized. For example, if you set layout width to 100%, each column will only be calculated to its relative size, and will stretch as the browser is resized.

### Fixed

Fixed layouts don’t respond to the size of the viewport but remain at a fixed width at a specific numerical value (e.g. 1920px).

### Fluid

Fluid layouts are calculated to their relative size, and stretch as the screen (viewport) is resized. For example, if you set layout width to 100%, each column will only be calculated to its relative size, and will stretch as the browser is resized.

### Fixed

Fixed layouts don’t respond to the size of the viewport but remain at a fixed width at a specific numerical value (e.g. 1920px).

You can override max-width defaults in the [Grid & Cell component.](/components/grid/)

* * *

How to use breakpoints
----------------------

You can change the appearance and behaviour of UI elements at different breakpoints.

In the codebase, use the [component overrides and defaults system](/theme/theming/component-defaults/) to override design tokens at specific breakpoints. For example, set different typography presets at different breakpoints to make text bigger on larger devices than on smaller devices.  
  
Properties that support this are specified in the Props sections of the component documentation as using the generic `MQ` type, i.e. `MQ<string>`.  
  
This works by passing either a single string token to be used across all breakpoints, or an object for a combination of multiple breakpoints - consisting of breakpoint keys and token values.

### Code example

Here’s an example of different typography presets at different breakpoints:

    1
    2  typographyPreset: {
    3      xs: 'editorialHeadline010',
    4      md: 'editorialHeadline020',
    5      lg: 'editorialHeadline030',
    6    }
    7  
    

* * *

Colours
=======

Colours express brand identity and convey meaning.

[Learn more about colours](/theme/foundation/colours/)

Colours
=======

Colours express brand identity and convey meaning.

[Learn more about colours](/theme/foundation/colours/)