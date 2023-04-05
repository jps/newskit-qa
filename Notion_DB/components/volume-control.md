Volume Control | NewsKit design system

Volume Control
==============

Overview
--------

### Usage

The VolumeControl component utilises the [Slider](/components/slider/) component, for controlling audio player volume level. The slider has a step of 0.1 and changes a volume number between 0 and 1. The min label is also a clickable mute/unmute button which will set the volume to 0 or back to its previous value on click. The onChange function prop can be used to pass the volume value to the relevant audio player instance, along with also passing the value back down to the VolumeControl.

Props
-----

volumenumber

The volume value, a number between 0 and 1. This value must be updated when onChange is called.

onChange(volume: number) => void

The onChange function receives the new volume value whenever it is changed. Passing this value back into the volume prop is essential to make the slider interactive.

verticalboolean

If true, the volume control is rendered vertically rather than horizontally. The volume control will have a height of 100% in vertical mode. To ensure the slider renders as expected, your container must have a height set.

overridesobject

sliderSliderOverrideProps

If provided overrides the styles of the slider that builds the VolumeControl. The slider overrides structure can be found in the [slider documentation page](/components/slider/).

buttonobject

stylePresetMQ<string>

Overrides the stylePreset of the min (mute) and max control buttons.

iconSizestring

Overrides the iconSize of the min (mute) and max control buttons.

size'small' | 'medium' | 'large'

Overrides the size of the min (mute) and max control buttons.

Refer to the defaults below for the full object structure:

An error occurred loading this code example.

Playground
----------

Use the arrow keys to adjust volume

VerticalUnsettrue

    1import React from 'react';
    2import { StatefulVolumeControl } from 'newskit';
    3
    4export default () => <StatefulVolumeControl />;
    5
    

Edit on CodeSandbox