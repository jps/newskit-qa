Progress indicator | NewsKit design system

Progress indicator
==================

Overview
--------

The progress indicator shows the progression of a system operation such as downloading, uploading, processing, etc. in a visual way.

Behaviour
---------

The progress indicator displays progress by animating the indicator along the length of the track. The progress indicator fills the circular track with colour, as it moves from 0 to 360 degrees over a quicker duration and repeats the animation until the action has been completed.

Usage
-----

The progress indicator displays progress by animating an indicator along an invisible circular track in a clockwise direction. It can be applied to buttons, inputs or other elements.

Don't show more than one progress indicator as the user is likely to become overwhelmed! If more than one piece of content is processing, stick to a large for the whole screen and consider skeleton loading or linear progress indicators.

### Theming

Props
-----

overridesobject

If provided, overrides the respective presets for the component and provided elements.

stylePresetMQ<string>

If provided, this overrides the style preset applied to the ProgressIndicator.

sizeMQ<string> = iconSize020

If provided, this overrides the size token applied to the ProgressIndicator.

Refer to the defaults below for the object structure:

An error occurred loading this code example.

Playground
----------

SizeDefault(iconsSize020)iconSize010iconSize030iconSize040iconSize050

Indicator StylePresetDefault(inkBase)inkNonEssentialinkBrand010

    1import React from 'react';
    2import { IndeterminateProgressIndicator } from 'newskit';
    3
    4export default () => (
    5  <IndeterminateProgressIndicator overrides={{}} />
    6);
    7
    

Edit on CodeSandbox