Form | NewsKit design system

Actions & Inputs

Form
====

Forms let users enter and edit information using form controls. Based on [React Hook Form.](https://react-hook-form.com/)

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/form)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-form--story-form-default)

* * *

Interactive demo
----------------

This demo lets you preview the form component, its variations and configuration options.

Email

Submit

Validation ModeDefault (onSubmit)onBlur

ReValidation ModeDefault (onBlur)onSubmit

    1import React from 'react';
    2import { Form } from 'newskit';
    3
    4export default () => <Form />;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

Form

The form component contains two required elements and no optional elements.

Item

Name

Description

Component

Optional

Form input components

These are the form input components available for use with the form:

Item

Name

Description

Component

Optional

* * *

Options
-------

Form input components have options for different use cases:

### FormInputLabel

When wrapped inside the `FormInput` component, the state can be passed down to the `FormInputLabel` component if the user desires.

Note

Ensure screen readers can read labels by setting the aria-label attribute to the label text’s value.

### FormInputAssistiveText

When wrapped inside the `FormInput`, the state can be passed down to the`FormInputAssistiveText` component, depending on if validation is a success or error state.  
  
`FormInputAssistiveText` can also display a character count to let users know how much text they can enter, when there is a limit set on the number of characters on a [text field](/components/text-field/#component-api) or text area.

### FormInputTextArea

When wrapped inside the `FormInput` the state can be passed down to the `FormInputTextField` component, depending on if validation is a success or error state. [Text area documentation.](/components/text-area/#component-api)

### FormInputTextField

When wrapped inside the `FormInput` the state can be passed down to the `FormInputTextField` component, depending on if validation is a success or error state. [Text field documentation.](/components/text-field/#component-api)

### FormInputSelect

When wrapped inside the `FormInput` the state can be passed down to the `FormInputSelect` component, depending on if validation is a success or error state. [Select documentation.](/components/select/#component-api)

### FormInputCheckbox

When wrapped inside the `FormInput` the state can be passed down to the`FormInputCheckbox` component, depending on if validation is a success or error state. [Checkbox documentation.](/components/checkbox/#component-api)

### FormInputRadioButton

When wrapped inside the `FormInput` the state can be passed down to the`FormInputRadioButton` component, depending on if validation is a success or error state. Multiple can be grouped together using the radioGroup component. [Radio Button documentation.](/components/radio-button/#component-api)

### Fieldset

Selection controls (inputs), such as the `FormInputRadioButton`, and`FormInputCheckbox`, can be grouped together with other selection controls, labels and assistive text together in a fieldset. The fieldset has a caption that gives a title attributed to the elements that appear in the fieldset, called a legend. [Fieldset documentation.](/components/fieldset/)

### FormInputLabel

When wrapped inside the `FormInput` component, the state can be passed down to the `FormInputLabel` component if the user desires.

Note

Ensure screen readers can read labels by setting the aria-label attribute to the label text’s value.

### FormInputAssistiveText

When wrapped inside the `FormInput`, the state can be passed down to the`FormInputAssistiveText` component, depending on if validation is a success or error state.  
  
`FormInputAssistiveText` can also display a character count to let users know how much text they can enter, when there is a limit set on the number of characters on a [text field](/components/text-field/#component-api) or text area.

### FormInputTextArea

When wrapped inside the `FormInput` the state can be passed down to the `FormInputTextField` component, depending on if validation is a success or error state. [Text area documentation.](/components/text-area/#component-api)

### FormInputTextField

When wrapped inside the `FormInput` the state can be passed down to the `FormInputTextField` component, depending on if validation is a success or error state. [Text field documentation.](/components/text-field/#component-api)

### FormInputSelect

When wrapped inside the `FormInput` the state can be passed down to the `FormInputSelect` component, depending on if validation is a success or error state. [Select documentation.](/components/select/#component-api)

### FormInputCheckbox

When wrapped inside the `FormInput` the state can be passed down to the`FormInputCheckbox` component, depending on if validation is a success or error state. [Checkbox documentation.](/components/checkbox/#component-api)

### FormInputRadioButton

When wrapped inside the `FormInput` the state can be passed down to the`FormInputRadioButton` component, depending on if validation is a success or error state. Multiple can be grouped together using the radioGroup component. [Radio Button documentation.](/components/radio-button/#component-api)

### Fieldset

Selection controls (inputs), such as the `FormInputRadioButton`, and`FormInputCheckbox`, can be grouped together with other selection controls, labels and assistive text together in a fieldset. The fieldset has a caption that gives a title attributed to the elements that appear in the fieldset, called a legend. [Fieldset documentation.](/components/fieldset/)

* * *

Behaviours
----------

Here’s how the form input components behave:  
  

Form input validation

Define FormInput validation rules for onSubmit or onBlur, for both the initial validation and re-validation using the form. Learn more about validation rules with [React Hook Form.](https://react-hook-form.com/get-started/#Applyvalidation)  
  
For validation to work, you need to individually wrap each form input component (e.g. FormInputTextField) in the form component. For example:

    1<Form onSubmit={onSubmit}>
    2  <FormInput
    3    name="checkbox"   
    4    rules={{
    5      required: 'Required field',
    6    }}
    7  >
    8    <FormInputCheckbox value="tc" />
    9  </FormInput> 
    10  <FormInput
    11        name="select"
    12        rules={{
    13          required: 'Required field',
    14        }}
    15      >
    16    <FormInputSelect>
    17      <SelectOption value="Option 1">Option 1</SelectOption>
    18      <SelectOption value="Option 2">Option 2</SelectOption>
    19    </FormInputSelect>
    20  </FormInput>
    21  <Button type="submit">Submit</Button>
    22</Form>

  
  

Form yup schema

The form supports schema validation with external validation libraries. To use `Yup`, for example, pass `yupResolver(schema)`to the resolver prop. Learn more about schema validation with [React Hook Form.](https://react-hook-form.com/get-started/#SchemaValidation)

    1import {yupResolver} from '@hookform/resolvers/yup';
    2import * as yup from 'yup';
    3
    4const schema = yup.object().shape({
    5  email: yup.string().email().required(),
    6  username: yup.string().required(),
    7});
    8
    9<Form onSubmit={onSubmit} resolver={yupResolver(schema)}>
    10  <FormInput name="email">
    11    <FormInputLabel>E-mail</FormInputLabel>
    12    <FormInputTextField type="email" />
    13    <FormInputAssistiveText>Enter your email</FormInputAssistiveText>
    14  </FormInput>
    15  <FormInput name="username">
    16    <FormInputLabel>Username</FormInputLabel>
    17    <FormInputTextField />
    18    <FormInputAssistiveText>Enter username</FormInputAssistiveText>
    19  </FormInput>
    20  <Button type="submit">
    21    Submit
    22  </Button>
    23</Form>;
    24
    

### Assistive text minimum height

Apply a minimum height to the assistive text container to stop the layout of the page shifting when the assistive text shows and hides.

### Assistive text overflow wrap

When the assistive text is too long for the available horizontal space, it wraps to form another line.

### Assistive text minimum height

Apply a minimum height to the assistive text container to stop the layout of the page shifting when the assistive text shows and hides.

### Assistive text overflow wrap

When the assistive text is too long for the available horizontal space, it wraps to form another line.

* * *

Usage
-----

Here’s how and when to use the form:  
  
For best practices to follow when creating a form, see the [forms patterns guidance.](/patterns/forms/overview/)

* * *

Do keep forms clear and simple

Clear, simple forms help prevent users from getting confused and submitting wrong information.

* * *

Don't include questions that aren't essential

Ask yourself if each FormInput is necessary.

* * *

Do wrap FormInput components that need validation

Ensure each FormInput component that needs validation is wrapped in a form.

* * *

Don’t validate prematurely

Avoid prematurely validating a FormInput (e.g. avoid setting text fields to invalid before the user has finished typing).

* * *

Do use onBlur validation

Where possible, validate using onBlur (i.e. when the user clicks out of a FormInput, it’s validated).

* * *

Do make error text clear and helpful

Error text should be clear, concise and written in complete sentences - and it should tell the user how to resolve the issue.

* * *

Do use sentence case for labels and assistive text

Write labels and assistive text in sentence case to help with scannability and legibility.

* * *

Don't truncate or wrap labels

Keep labels short, clear and fully visible.

* * *

Do keep labels and assistive text close to FormInput

Labels and assistive text should be in close proximity to their FormInput components to provide context for users.

* * *

Do use assistive text for instructions

Use assistive text for instructions on completing an input or to communicate requirements.

* * *

Do swap assistive text with error text or character count

Swap assistive text with error text or character count as required. Once the input is valid, show the assistive text or character count again.

* * *

Do nest FormInput components

FormInput components don't need to be direct children of the form component and can be nested inside other elements.

* * *

Tutorial
--------

Learn how to use the form component effectively using the tutorial below.

[

### Form tutorial



](/getting-started/code/form-step-by-step/)

Tutorial for engineers to build a form using the form sub components.

[

### Form tutorial



](/getting-started/code/form-step-by-step/)

Tutorial for engineers to build a form using the form sub components.

* * *

Form structure
--------------

This diagram shows how to use form input components inside a [fieldset](/components/fieldset/), which you can then use to create a full form:

* * *

Accessibility considerations
----------------------------

The form has the following accessibility considerations:

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

Form

The form has a range of props to define the experience in different use cases.

Name

Type

Default

Description

Required

Form input

The form input has a range of props to define the experience in different use cases.

Name

Type

Default

Description

Required

Form input assistive text

The `FormInputAssistiveText` component has a range of props to define the experience in different use cases. Use within the form component.\`,

Props

Overrides

Name

Type

Default

Description

Required

Note

Props and overrides for the assistive text component are the same as the form input assistive text component, as listed above.

Attribute

Type

Default

Description

Form input label

The `FormInputLabel` has a range of props to define the experience in different use cases. Use within the form.

Props

Overrides

Name

Type

Default

Description

Required

Note

Props and overrides for the label component are the same as the FormInputLabel component, as listed above. For details of props and overrides:

*   [FormInputTextField](/components/text-field/#component-api)
    
*   [FormInputSelect](/components/select/#component-api)
    
*   [FormInputCheckbox](/components/checkbox/#component-api)
    
*   [FormInputRadioButton](/components/radio-button/#component-api)
    

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Checkbox



](/components/checkbox/)

Checkboxes are selection controls that allow users to select one or multiple items from a group of options. They typically appear in forms.

[

### Text Field



](/components/text-field/)

Text Fields allow users to enter and edit text content into a UI. They typically appear in forms.

[

### Radio Button



](/components/radio-button/)

Radio Buttons are selection controls that are typically used in forms

[

### Text Area



](/components/text-area/)

Text areas allow users to enter and edit multi-line text. They typically appear in forms.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)