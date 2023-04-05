Select | NewsKit design system

Actions & Inputs

Select
======

Selects let users select one option from a list. They typically appear in forms.

Status
======

Supported

* * *

Introduced
==========

v4.3.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/select)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-select--story-select-size)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/NK-Web-Components?node-id=4603%3A124656)

* * *

Anatomy
-------

The select component contains five required elements and two optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The select component has options for different use cases:

### Size

The select component comes in small, medium and large. The input container, placeholder/input text and start/end enhancers change size. Selects should match the height of the button and other inputs (e.g. text field) when used together.

### Select for mobile

Select options can appear in a modal (with overlay). This is intended for long lists of options (e.g. presenting a list of countries to select from in a form).

### Width

Customise the width of a select using full-width or a fixed-width value.

### Min-height

Customise the minimum height of both a select input and the select panel (containing the option items).

### Placeholder text

Use placeholder text to give the user a short hint about what to input (e.g. a sample value or short description of the expected format). The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible. Use assistive text to give instructions to the user when they've completed a select.

### Start enhancer

The select supports start enhancer property that allows for a component to be added to the start of the input container (e.g. an icon).

### End enhancer

Add a component to the end of the input container (e.g. an icon).

### Pre-selected options

Set a pre-selected option on the select. When specified, the option is displayed in the select upon page load.

### Custom selected display

Define the select option item and the select input independently (e.g. you might have a list of countries in text format in the select option items, then, upon user selection, display the selected item as a country flag in the select input).

### Size

The select component comes in small, medium and large. The input container, placeholder/input text and start/end enhancers change size. Selects should match the height of the button and other inputs (e.g. text field) when used together.

### Select for mobile

Select options can appear in a modal (with overlay). This is intended for long lists of options (e.g. presenting a list of countries to select from in a form).

### Width

Customise the width of a select using full-width or a fixed-width value.

### Min-height

Customise the minimum height of both a select input and the select panel (containing the option items).

### Placeholder text

Use placeholder text to give the user a short hint about what to input (e.g. a sample value or short description of the expected format). The short hint is displayed in the input container before the user enters a value.

Placeholder text is not accessible. Use assistive text to give instructions to the user when they've completed a select.

### Start enhancer

The select supports start enhancer property that allows for a component to be added to the start of the input container (e.g. an icon).

### End enhancer

Add a component to the end of the input container (e.g. an icon).

### Pre-selected options

Set a pre-selected option on the select. When specified, the option is displayed in the select upon page load.

### Custom selected display

Define the select option item and the select input independently (e.g. you might have a list of countries in text format in the select option items, then, upon user selection, display the selected item as a country flag in the select input).

* * *

States
------

The select has the following states:

### Base

The default style before the user interacts with the select.

### Hover

The select changes style to let the user know it’s interactive.

### Focus

The select changes style when the element is focussed (e.g. via keyboard or voice).

### Selected

The select changes style when the user’s selection conforms to a specific condition. This is the style of the input when the panel element is visible (open).

### Valid

The select changes style to let the user know the select is in a valid state.  
  
The input style change and validation icon can appear as soon as the user types a valid entry in the input or on submit.  
  
Use the form to validate behaviour.

### Valid focus

The select changes style to communicates that a user has highlighted a valid select.

### Valid hover

The select changes style to let the user know the select is in a valid state, and hovered over.

### Invalid

The select changes style to let the user know the select is in an invalid state.  
  
The input style change and validation icon can appear as soon as a user types a valid entry in the input or on submit.  
  
Use the form component to validate behaviour.

### Invalid focus

The select changes style to communicate that a user has highlighted an invalid select.

### Invalid hover

The select changes style to let the user know the select is in an invalid state, and hovered over.

### Disabled

Communicates to the user that an input exists, but cannot be modified in that scenario.  
  
Disabled selects maintain layout consistency and communicate that an input may become available if another condition is met (e.g. selecting a previous option in a form).

### Read-only

The select in a read-only state communicates to the user that an input exists, but cannot be modified in that scenario (however, a user can tab to it, highlight it and copy the text from it).  
  
Read-only selects are often used to maintain layout consistency and communicate that an input may become available if another condition is met (e.g. selecting a previous option in a form).  
  
Content and data in a read-only select can be submitted in a form.

* * *

Behaviours
----------

Here’s how the select behaves:

### Select input and select option item text-overflow truncation

When the select input text or the select option item text is too long for the available horizontal space, the text truncates.  
  
Truncation is visually indicated using `text-overflow:elipsis` via the style presets.

### Validation

Use the form to choose whether the select validates on submit or on blur, for both the initial validation and re-validation.

Validation only works if the select uses the form component.

### Validation icon

An icon indicates if the select is in a valid or invalid state. Use the form for validation.

### Select input and select option item text-overflow truncation

When the select input text or the select option item text is too long for the available horizontal space, the text truncates.  
  
Truncation is visually indicated using `text-overflow:elipsis` via the style presets.

### Validation

Use the form to choose whether the select validates on submit or on blur, for both the initial validation and re-validation.

Validation only works if the select uses the form component.

### Validation icon

An icon indicates if the select is in a valid or invalid state. Use the form for validation.

* * *

Usage
-----

Here’s how and when to use the select:

* * *

Do use a select for multiple options

Use a select to present multiple options where only one can be selected. If the user can select more than one option, use the checkbox instead.

* * *

Don’t use a select for few options

Don't use a select when you have only a few options and enough space. Use a radio button instead. Selects can cause usability issues due to the number of interactions required. This can increase the likelihood of the user abandoning the task.

* * *

Do use selects for four or more options

Use a select when there are four or more options, and the user can only choose one.

* * *

Don’t have an empty select on page load

If a default option isn’t appropriate, use a placeholder (e.g. ‘select an option’).

* * *

Don’t use selects for adding or removing options

If you want the user to be able to add and remove options, use a text field with tags or a combobox instead.

* * *

Accessibility considerations
----------------------------

The Select component has the following accessibility considerations:

Group selects

Group selects and related elements (e.g. labels and assistive text) together using the fieldset component with a title attributed to the elements called a legend.  
  
A fieldset groups related form controls, making them easier to understand. It can also allow users to focus on smaller and more manageable chunks, rather than trying to grasp the entire form at once.

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

The select component is composed of three key elements. They have a range of props to define the experience in different use cases.

There are two components exported from the package, one for use within the form and one for use as a controlled component.

Form input select

The form input select has a range of props to define the experience in different use cases. Use within the form.

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

Check out the [modal](/components/modal/) for all props and overrides.

Select

The select has a range of props to define the experience in different use cases. Use within the form.

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

Check out the [modal](/components/modal/) for all props and overrides.

SelectOption

The selectOption has a range of props to define the experience in different use cases. Use within the form.

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

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

[

### Checkbox



](/components/checkbox/)

Checkboxes are selection controls that allow users to select one or multiple items from a group of options. They typically appear in forms.

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