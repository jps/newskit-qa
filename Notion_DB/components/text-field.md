Text Field | NewsKit design system

Actions & Inputs

Text Field
==========

Text fields let users enter and edit text. They typically appear in forms.

Status
======

Supported

* * *

Introduced
==========

v3.13.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/blob/develop/src/text-field/text-field.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-text-field--story-text-field-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=4897%3A131265)

* * *

Anatomy
-------

The text field component contains four required elements and two optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The text field has options for different use cases:

### Size

The text field comes in small, medium and large. The label, input container, placeholder/input text, start/end enhancers and assistive text change size. Text inputs should match the height of the button when used together.

### Width

Customise the width of a text field using full-width or a fixed-width value.

### Placeholder text

Use placeholder text to give the user a short hint about what they need to input (e.g. a sample value or a short description of the expected format).  
  
The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible. Use assistive text to give instructions to the user when they’ve completed a text field.

### Start enhancer

Add a component to the start of the input container (e.g. an icon).

### End enhancer

Add a component to the end of the input container (e.g. a button).

### Autocomplete

The text field supports native HTML autocomplete functionality that provides a visual hint to users if enabled.  
  
[Learn more about HTML autocomplete at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

### Max length

The text field supports native HTML max length value functionality that sets a maximum length of the number of characters entered.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#maxlength)

### Min length

The text field supports native HTML max length value functionality that sets a minimum length of the number of characters entered.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#minlength)

### Pattern

The text field supports native HTML regex pattern functionality that the value of the input must match to be valid.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#pattern)

### Type

The text field supports type functionality that sets the type of text field to render to the user. The types supported include 'text' (default for the text field), 'email', 'password', 'tel' and 'number'.  
  
[Learn more about HTML input types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#type)

### Input mode

The text field supports input mode functionality that hints at the type of data that might be entered by the user while editing the element or its contents. Supported input modes include 'text', 'email', 'tel' and 'numeric'.  
  
[Learn more about HTML input mode attribute types at HTML Living Standard.](https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-inputmode-attribute)

### Handling multiple text fields

You can group together selection controls (inputs), such as formInput, radio button and checkbox, as well as labels and assistive text, in a [fieldset](/components/fieldset/). Add a title caption to the grouped elements using the legend.

### Size

The text field comes in small, medium and large. The label, input container, placeholder/input text, start/end enhancers and assistive text change size. Text inputs should match the height of the button when used together.

### Width

Customise the width of a text field using full-width or a fixed-width value.

### Placeholder text

Use placeholder text to give the user a short hint about what they need to input (e.g. a sample value or a short description of the expected format).  
  
The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible. Use assistive text to give instructions to the user when they’ve completed a text field.

### Start enhancer

Add a component to the start of the input container (e.g. an icon).

### End enhancer

Add a component to the end of the input container (e.g. a button).

### Autocomplete

The text field supports native HTML autocomplete functionality that provides a visual hint to users if enabled.  
  
[Learn more about HTML autocomplete at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete)

### Max length

The text field supports native HTML max length value functionality that sets a maximum length of the number of characters entered.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#maxlength)

### Min length

The text field supports native HTML max length value functionality that sets a minimum length of the number of characters entered.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#minlength)

### Pattern

The text field supports native HTML regex pattern functionality that the value of the input must match to be valid.  
  
[Learn more about HTML input attribute types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#pattern)

### Type

The text field supports type functionality that sets the type of text field to render to the user. The types supported include 'text' (default for the text field), 'email', 'password', 'tel' and 'number'.  
  
[Learn more about HTML input types at MDN Web Docs.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#type)

### Input mode

The text field supports input mode functionality that hints at the type of data that might be entered by the user while editing the element or its contents. Supported input modes include 'text', 'email', 'tel' and 'numeric'.  
  
[Learn more about HTML input mode attribute types at HTML Living Standard.](https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-inputmode-attribute)

### Handling multiple text fields

You can group together selection controls (inputs), such as formInput, radio button and checkbox, as well as labels and assistive text, in a [fieldset](/components/fieldset/). Add a title caption to the grouped elements using the legend.

* * *

States
------

The text field has the following states. They can be displayed with both placeholder content or user-inputted content:

### Base

The default style before the user interacts with the text field.

### Hover

The select changes style to let the user know it’s interactive.

### Active

The text field changes style to let the user know they’ve interacted with it.

### Selected (focus)

The text field changes style, and a caret element in the input is also visible, to let the user know the text field has been selected and they can input content.

### Valid

The text field changes style, and can display a valid icon, when the inputted entry conforms to a specific format (e.g. email address, credit card number, password requirements).  
  
The input style change and validation icon can appear as soon as a user types a valid entry in the input or on submit.  
  
Use the form for validation.

### Valid focus

The text field changes style when the inputted entry conforms to a specific condition or format, while focused.

### Valid hover

The text field changes style when the inputted entry conforms to a specific condition or format, while hovering.

### Invalid

The text field changes style and can display an invalid icon when the inputted entry doesn't conform to a specific format (e.g. email address, credit card number, password requirements).  
  
The input style change and validation icon can appear as soon as a user types a valid entry in the input or on submit.  
  
Use the form for validation.

### Invalid focus

The text field changes style when the inputted entry doesn’t conform to a specific condition or format, while focused.

### Invalid hover

The text field changes style when the inputted entry doesn’t conform to a specific condition or format, while hovering.

### Disabled

Communicates that a text field exists, but isn't available in that scenario. When the user hovers over a text field in a disabled state, the cursor shows as 'not allowed'.  
  
Disabled text fields maintain layout consistency and communicate that an input may become available if another condition is met (e.g. selecting a previous option in a form).  
  
You can’t submit content and data in a disabled text field in a form.

### Read-only

Communicates that an input exists, but cannot be modified in that scenario (however, a user can tab to it, highlight it and copy the text from it).  
  
Read-only text fields maintain layout consistency and communicate that an input may become available if another condition is met (e.g. selecting a previous option in a form).  
  
You can submit content and data in a read-only text field in a form.

* * *

Behaviours
----------

Here’s how the text field behaves:

### Input text overflow truncation

When the text field text is too long for the available horizontal space, the text truncates when text is inputted.  
  
Truncation is visually indicated using `text-overflow: elipsis` via the style presets.

### Validation

The text field validation rules can be defined for on submit or on blur, for both the initial validation and re-validation using the form.  
  

Validation only works if the form input text field uses the form component.

### Validation icon

Indicates if the text field is in a valid or invalid state. Use the form to validate.

### Input text overflow truncation

When the text field text is too long for the available horizontal space, the text truncates when text is inputted.  
  
Truncation is visually indicated using `text-overflow: elipsis` via the style presets.

### Validation

The text field validation rules can be defined for on submit or on blur, for both the initial validation and re-validation using the form.  
  

Validation only works if the form input text field uses the form component.

### Validation icon

Indicates if the text field is in a valid or invalid state. Use the form to validate.

* * *

Usage
-----

Here’s how and when to use the text field:

* * *

Do consider text field width

The width of the text field should be proportional to the expected user input.

* * *

Don’t capture multiple pieces of information in one field

Avoid using a single text field to capture multiple pieces of information from users, as this increases cognitive load. Use an individual text field for each input.

* * *

Do use an appropriate input type for the data you collect

Use the appropriate input field to help users enter information in the right format and avoid mistakes (e.g. use a password input field for users to input their password).

* * *

Don’t truncate or wrap input label text

Input label text shouldn't be truncated or wrap over two or more lines. Keep it short, clear and fully visible.

* * *

Do provide a label for context

Text fields should have a label associated to give users context of what the text area represents.

* * *

Don’t validate prematurely

Avoid prematurely validating the input (e.g. avoid setting the input to invalid before the user has finished typing).

* * *

Accessibility considerations
----------------------------

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

This package exports two components: a form input text field for use within the form component, and a text field for use as a controlled component (e.g. where you have a custom validation mechanism).  
  
Both have a range of props to define the experience in different use cases.

Form input text field

Props

Overrides

Name

Type

Default

Description

Required

The `name` & `rules` props are set on the form input level. To add validation rules, or set the name, [see the form component](/components/form/)

The form input text field supports different native HTML attributes (e.g. defining the input type as password or email).

Attribute

Type

Default

Description

Text field

Props

Overrides

Name

Type

Default

Description

Required

The text field supports different [native HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types)(e.g. defining the input type as password or email).

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

[

### Text Area



](/components/text-area/)

Text areas allow users to enter and edit multi-line text. They typically appear in forms.

[

### Form



](/components/form/)

The form component allows users to enter and edit information into a UI using form controls; based on React Hook Form.

[

### Select



](/components/select/)

Select components allow users to select one option from a list.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)