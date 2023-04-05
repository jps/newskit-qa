Text Area | NewsKit design system

Actions & Inputs

Text Area
=========

Text areas allow users to enter and edit multi-line text. They typically appear in forms.

Status
======

Supported

* * *

Introduced
==========

[v6.1.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v6.1.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/blob/main/src/text-area/text-area.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-text-area--text-area-sizes)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components)

* * *

Interactive demo
----------------

This demo allows you to preview the text area component, its variations, and configuration options.

SizeDefaultSmallMediumLarge

StateDefaultValidInvalidDisabled

ResizesNoneVerticalHorizontalBoth

OverridesDefaultCustom StyleFixed widthFixed height

    1import React from 'react';
    2import { TextArea } from 'newskit';
    3
    4export default () => (
    5  <TextArea resize="none" overrides={{ width: '300px' }} />
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

Text areas contain three required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The text area has options that can be used to provide an appropriate experience for different use cases.

### Size

There are three sizes of text area: small, medium, and large. The label, input container, placeholder/input text, and assistive text change size.

### Width

The width of a text area can be customised appropriately for its context, using full-width or a fixed-width value.

### Height

The height of the text area input container is vertically scrollable when the set maxHeight or height is exceeded and a user inputs more information.

### Resize handle

Text areas are resizable with a handle at the bottom right corner of the input container.

The resize handle can be `disabled` in instances where the size of the input container is fixed.

### Character count

Text Areas can use [the character count component](https://newskit.co.uk/components/character-count/) which lets users know how much text they can enter, displaying the number of characters available as a user types. The character limit is configurable.

### Placeholder text

Placeholder text can be displayed to provide the user with a short hint that describes the content that is expected to be inputted by the user (e.g. a sample value or a short description of the expected format).  
  
The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible; use assistive text when providing instructions on completing a text area for clarity.

### Autocomplete

The text area supports native HTML autocomplete functionality that provides a visual hint to users if enabled.  
  
[For more information, please refer to the HTML autocomplete attribute.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

### Max and min length

The text area supports native HTML max and min length value functionality that sets a maximum or minimum length of the number of characters entered, and is indicated to users via the character count.  
  
[For more information, please refer to the HTML input attribute types.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)

### Handling multiple text areas

Selection controls (inputs), such as the FormInput TextArea, can be grouped together with other selection controls, labels, and assistive text together in a fieldset. The fieldset has a caption that gives a title attributed to the elements that appear in the fieldset, called a legend.  
  
The fieldset can also support other selection controls (inputs) such as the [formInput RadioButton](/components/radio-button/), and [formInput checkbox.](/components/checkbox/)

### Size

There are three sizes of text area: small, medium, and large. The label, input container, placeholder/input text, and assistive text change size.

### Width

The width of a text area can be customised appropriately for its context, using full-width or a fixed-width value.

### Height

The height of the text area input container is vertically scrollable when the set maxHeight or height is exceeded and a user inputs more information.

### Resize handle

Text areas are resizable with a handle at the bottom right corner of the input container.

The resize handle can be `disabled` in instances where the size of the input container is fixed.

### Character count

Text Areas can use [the character count component](https://newskit.co.uk/components/character-count/) which lets users know how much text they can enter, displaying the number of characters available as a user types. The character limit is configurable.

### Placeholder text

Placeholder text can be displayed to provide the user with a short hint that describes the content that is expected to be inputted by the user (e.g. a sample value or a short description of the expected format).  
  
The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible; use assistive text when providing instructions on completing a text area for clarity.

### Autocomplete

The text area supports native HTML autocomplete functionality that provides a visual hint to users if enabled.  
  
[For more information, please refer to the HTML autocomplete attribute.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

### Max and min length

The text area supports native HTML max and min length value functionality that sets a maximum or minimum length of the number of characters entered, and is indicated to users via the character count.  
  
[For more information, please refer to the HTML input attribute types.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)

### Handling multiple text areas

Selection controls (inputs), such as the FormInput TextArea, can be grouped together with other selection controls, labels, and assistive text together in a fieldset. The fieldset has a caption that gives a title attributed to the elements that appear in the fieldset, called a legend.  
  
The fieldset can also support other selection controls (inputs) such as the [formInput RadioButton](/components/radio-button/), and [formInput checkbox.](/components/checkbox/)

* * *

States
------

The text area has the following states. They can be displayed with both placeholder content or user-inputted content:

### Base

Text areas have a base state. This is the base style of the input before it has been interacted with by a user.

### Hover

Text areas have a hover state. The style of the input changes to visually communicate and provide feedback to the user that the text area is an interactive element.

### Focus

Text areas have an active state. The style of the input changes to visually communicate and provide feedback to the user that the text area has been interacted.

### Selected

Text areas have a selected state. The style of the input changes and a caret element in the input is also visible to visually communicate and provide feedback to the user that the text area has been selected and they can input content.

### Valid

Text areas in a valid state change style and can display a valid icon when the inputted entry conforms to a specific format.  
  
The input style change and validation icon can appear as soon as a user types a valid entry in the input or on submit.  
  
The [form](/components/form/) component is used to define this validation behaviour.

### Valid focus

Text areas in a valid focus state change style when the inputted entry conforms to a specific condition or format, while focused.

### Valid hover

Text areas in a valid hover state change style when the inputted entry conforms to a specific condition or format while hovering.

### Invalid

Text areas in an invalid state change style and can display an invalid icon when the inputted entry doesn’t conform to a specific format.  
  
The input style change and validation icon can appear as soon as a user types a valid entry in the input or on submit.  
  
The [form](/components/form/) component is used to define this validation behaviour.

### Invalid focus

Text areas in an invalid focus state change style when the inputted entry doesn’t conform to a specific condition or format, while focused.

### Invalid hover

Text areas in an invalid hover state change style when the inputted entry doesn’t conform to a specific condition or format while hovering.

### Disabled

Text areas in a disabled state show that an input exists, but is not available to the user in that scenario. When a user’s cursor hovers over a text area in a disabled state the cursor shows as not-allowed.  
  
Disabled text areas are often used to maintain layout consistency and communicate that the input may become available if another condition has been met, e.g. selecting a previous option in a form.  
  
Content and data in disabled text areas can not be submitted in a form.

### Read-only

Text areas in a read-only state communicate to the user that an input exists, but cannot be modified in that scenario (however, a user can tab to it, highlight it, and copy the text from it).  
  
Read-only text areas are often used to maintain layout consistency and communicate that the input may become available if another condition has been met, e.g. selecting a previous option in a form.  
  
Content and data in read-only text areas can be submitted in a form.

* * *

Behaviours
----------

The following guidance describes how the text area component behaves.

### Input text overflow wrap and truncation

When the input text is too long for the available horizontal space, it wraps to another line when text is inputted.

Truncation in the form of `text-overflow: elipsis` (…) is not supported for the text area.

### Validation

The text area validation rules can be defined for onSubmit or onBlur, for both the initial validation and re-validation using the [form component.](/components/form/)

Validation only works if the FormInput TextArea uses the form component.

### Input text overflow wrap and truncation

When the input text is too long for the available horizontal space, it wraps to another line when text is inputted.

Truncation in the form of `text-overflow: elipsis` (…) is not supported for the text area.

### Validation

The text area validation rules can be defined for onSubmit or onBlur, for both the initial validation and re-validation using the [form component.](/components/form/)

Validation only works if the FormInput TextArea uses the form component.

* * *

Usage
-----

Here’s how and when to use the text area:

* * *

Do use propotional heights

The height of the text area input container should be proportional to the amount of text the user is expected to enter. This can be set via the `maxHeight` property.

* * *

Don't use text areas for single line inputs

Avoid using text areas if you need to let users enter shorter answers no longer than a single line. In this case, you should use the [text field component.](/components/text-field/)

* * *

Do allow users to copy and paste text

Allow users to copy and paste text into the text area input container.

* * *

Don't use text areas to capture multiple pieces of information

Avoid using text areas to capture multiple pieces of information from users, as this increases cognitive load. Instead, consider using multiple text areas, or text fields.

* * *

Do provide a label for context

Text areas should have a [label](/components/form/) associated to give users context of what the text area represents.

* * *

Don't block a user from entering information

Avoid limiting the number of characters users can enter unless there is a specific requirement for doing so.

* * *

Accessibility considerations
----------------------------

The text area has the following accessibility considerations:

Focus order

Order

Element

Role

Keyboard Interactions

Command

Description

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

API
---

The text area has a range of props that can be used to define an appropriate experience for different use cases.

There are two components exported from the package, one for use within the [NewsKit form component](/components/form/), and one for use as a controlled component.

FormInput TextArea

The FormInput TextArea has a range of props that can be used to define an appropriate experience for different use cases. Use this component within the [NewsKit form component.](/components/form/)

Props

Overrides

Name

Type

Default

Description

Required

In React, a <textarea> uses a `value` attribute. This way a form using a <textarea> can be written very similarly to a form that uses a single-line input. The <textarea> does not support the `value` attribute.

In addition to the props that come with the text area component, [native text area attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea#attributes) are also supported by passing them down to the text area component.

The `name` & `rules` props are set on the form input level. If you want to add validation rules or set the name of this component, [please refer to the form component.](/components/form/)

Native attributes `rows` & `cols` can be used by passing unset width and height down to the text area component.

Attribute

Type

Default

Description

Text area

The text area has a range of props that can be used to define an appropriate experience for different use cases. Use this component as a controlled component, for instance where you have a custom validation mechanism.

Props

Overrides

Name

Type

Default

Description

Required

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Form



](/components/form/)

The form component allows users to enter and edit information into a UI using form controls; based on React Hook Form.

[

### Text Field



](/components/text-field/)

Text Fields allow users to enter and edit text content into a UI. They typically appear in forms.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)