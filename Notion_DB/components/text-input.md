Text Input | NewsKit design system

Text Input
==========

Overview
--------

The Text Input component consists of a label, input and assistive text.

Usage
-----

Text Input allows users to enter text into a UI. They typically appear in forms and dialogs.

Email Input Component
---------------------

An Email Input component is also available. The EmailInput component is built on top of the TextInput component and it shares the same defaults and props of TextInput. The email input comes with a set of validation rules. The validation only works if the email input component is inside a Form component. For more information please see the Form component.

Props
-----

Text Input has a number of props to facilitate a variety of uses:

size'small' | 'medium' | 'large' = medium

Optional size of the Text Input: Small, Medium or Large.

labelstring

Label text is used to inform users as to what information is requested for a text input. Every text input field should have a label.

namestring

The name indentifier of the input field. It is required when the input is used inside a Form component.

hideLabelboolean = false

A prop can be set on the Text Input component to visually hide the label. The label should remain readable by screen readers by setting the arial label attribute on the input to the value of the label text.

assistiveTextstring

Assistive text gives context about a field’s input, such as how the input will be used. It will be displayed beneath the text input.

disabledboolean = false

If true, the Text Input will render the disabled state of the style preset.

readOnlyboolean = false

If true, the Text Input will render the read only state of the style preset.

ariaLabelstring

The aria-label attribute for the text input. As stated above, if the label is hidden, the label text will be placed into the aria label attribute of the input However, this can be overridden if the consumer sets aria-label prop.

rulesobject

The text input can take validation rules. The validation only works if the input is inside a Form component. For more information please see the Form component.

iconReactElement<NewsKitIcon>

This prop allows the text input component to take a leading icon, for example, the search icon.

overridesobject

If provided, overrides the respective presets for the component and provided elements.

widthstring

If provided, this sets a fixed width to the text input. This can be a sizing token from the theme, or any CSS length value, e.g. 100% for a full-width element.

inputobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the text input.

spaceInsetMQ<string>

If provided, this overrides the padding of the Text Input. Otherwise, spaceInsetSquish010 or spaceInset030 is used depending on the \`size\` prop.

typographyPresetMQ<string>

If provided, this overrides the type preset applied to the text input. Otherwise, utilityBody020 or utilityBody030 is used depending on the \`size\` prop.

spaceStackMQ<string>

This is a spacing preset token which is applied as a margin on the bottom of the Block. Use this to space stacking content down the page.

minHeightstring

If provided, this sets a minimum height to the Text Input. This can be a sizing token from the theme, or any CSS length value. By default, sizing060, sizing080 or sizing090 is used depending on the \`size\` prop.

leadingIconobject

iconOffsetMQ<string>

Applies space between the leading icon and left side of the input field.

spaceInsetMQ<string>

This spacing value overrides the padding value (applied by the spaceInset token) on the left of the input when the leading icon is showing. This avoids any input text rendering behind the icon.

validationIconobject

iconOffsetMQ<string>

Applies space between the validation icon and right side of the input field.

spaceInsetMQ<string>

This spacing value overrides the padding value (applied by the spaceInset token) on the right of the input when the validation icon is showing. This avoids any input text rendering behind the icon.

iconSizeMQ<string>

Overrides the iconSize of the validation icon.

inputLabelobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the text input label.

typographyPresetMQ<string>

If provided, this overrides the type preset applied to the text input label. Otherwise, label030 or label040 is used depending on the \`size\` prop.

spaceInlineMQ<string>

This is a spacing preset token which is applied as a margin on the right of the text input label. Use this to space inline content across the page.

spaceStackMQ<string>

This is a spacing preset token which is applied as a margin on the bottom of the text input label. Use this to space stacking content down the page.

assistiveTextobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the assistive text.

typographyPresetMQ<string>

If provided, this overrides the type preset applied to the text input. Otherwise, utilityLabel020 or utilityLabel030 is used depending on the \`size\` prop.

minHeightstring

If provided, this sets a minimum height to the assistive text container. This is used to prevent the layout shift in page when the assistive text shows and hides.

Refer to the defaults below for the object structure:

An error occurred loading this code example.

Playground
----------

Label

SizesmallDefault (medium)large

Style PresetDefault

Typography PresetDefaultDifferent presets

Spacing PresetDefaultDifferent presets

Assistive TextUnsetWith Assistive Text

PlaceholderDefaultCustom Placeholder

Hide LabelTrueFalse

WidthDefaultFull-widthFix-width

DisabledTrueFalse

Read-onlyTrueFalse

    1import React from 'react';
    2import { TextInput } from 'newskit';
    3
    4export default () => (
    5  <TextInput
    6    size="medium"
    7    overrides={{ label: {}, input: {}, assistiveText: {} }}
    8    placeholder="Placeholder"
    9  />
    10);
    11
    

Edit on CodeSandbox