Radio Button | NewsKit design system

Actions & Inputs

Radio Button
============

Radio buttons let users make a single selection from multiple options in a radio group. They typically appear in forms.

Status
======

Supported

* * *

Introduced
==========

[v5.3.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.3.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/radio-button)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-radio-button--story-radio-button-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=5918%3A132664)

* * *

Anatomy
-------

The radio button component contains one required element and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The radio button has options for different use cases:

### Size

The radio button input and feedback element both come in small, medium (default) and large.  
  
The icon that appears within the radio button input changes at all three sizes of radio button but can be overridden.

### Icon

Override the icon within the radio button input for different states.

### Feedback

The feedback element is non-interactive and appears in the background behind the radio button input on hover.

### Label

Add a label to the right (end) of the radio button to provide context.

You can add a label on the left (start) of a radio button using the `labelPosition` prop.

### Radio group

Use the radio group to group radio buttons.

### Fieldset

Group selection controls (e.g. form input, radio button and checkbox) together in a [fieldset](/components/fieldset/), along with labels and assistive text. Add a title to the grouped elements using the legend.

### Size

The radio button input and feedback element both come in small, medium (default) and large.  
  
The icon that appears within the radio button input changes at all three sizes of radio button but can be overridden.

### Icon

Override the icon within the radio button input for different states.

### Feedback

The feedback element is non-interactive and appears in the background behind the radio button input on hover.

### Label

Add a label to the right (end) of the radio button to provide context.

You can add a label on the left (start) of a radio button using the `labelPosition` prop.

### Radio group

Use the radio group to group radio buttons.

### Fieldset

Group selection controls (e.g. form input, radio button and checkbox) together in a [fieldset](/components/fieldset/), along with labels and assistive text. Add a title to the grouped elements using the legend.

* * *

States
------

The radio button has the following states:

### Base

The default style before the user interacts with the radio button.

### Hover

The radio button changes style to let the user know it’s interactive. The style of the label remains the same. Users can interact with (hover) the label to check the radio button.

### Focus

Communicates that a user has highlighted a radio button (e.g. via keyboard or voice).

### Focus hover

Communicates that a user has highlighted and hovered over a radio button (e.g. via keyboard or voice).

### Checked

The radio box input changes style to let the user know the radio box is checked. The style of the label remains the same.

### Checked hover

The radio box input changes style to let the user know the radio box is checked and hovered over. The style of the label remains the same.

### Checked focus

Communicates that a user has highlighted a radio button (e.g. via keyboard or voice).

### Checked focus hover

Communicates that a user has highlighted and hovered over a radio button (e.g. via keyboard or voice).

### Invalid

The radio button changes style when radio button selection doesn’t conform to a specific format (e.g. attempting to proceed without selecting a required radio button in a form). Use the form component to validate behaviour. The style of the label remains the same.

### Invalid focus

Communicates that a user has highlighted an invalid radio button (e.g. via keyboard or voice).

### Invalid hover

The radio button changes style to let the user know the radio button is in an invalid state and hovered over. The style of the label remains the same.

### Invalid focus hover

Communicates that a user has highlighted and hovered over an invalid radio button (e.g. via keyboard or voice).

### Checked invalid

The radio button input changes style to let the user know the radio button is checked and in an invalid state. The style of the label remains the same.

### Checked invalid focus

Communicates that a user has highlighted a checked, invalid radio button (e.g. via keyboard or voice).

### Checked invalid hover

The radio button input changes style to let the user know the radio button is checked, in an invalid state and hovered over. The style of the label remains the same.

### Checked invalid focus hover

Communicates that a user has highlighted and hovered over a checked, invalid radio button (e.g. via keyboard or voice).

### Valid

The radio button changes style when radio button selection conforms to a specific format (e.g. updating preferences in a form). Use the form to validate behaviour. The style of the label remains the same.

### Valid focus

Communicates that a user has highlighted a valid radio button (e.g. via keyboard or voice).

### Valid hover

The radio button input changes style to let the user know the radio button is in a valid state and hovered over. The style of the label remains the same.

### Valid focus hover

Communicates that a user has highlighted and hovered over a valid radio button (e.g. via keyboard or voice).

### Checked valid

The radio button input changes style to let the user know the radio button is checked and in a valid state. The style of the label remains the same.

### Checked valid focus

Communicates that a user has highlighted a checked, valid radio button (e.g. via keyboard or voice).

### Checked valid hover

The radio button input changes style to let the user know the radio button is checked, in a valid state and hovered over. The style of the label remains the same.

### Checked valid focus hover

Communicates that a user has highlighted and hovered over a valid radio button (e.g. via keyboard or voice).

### Disabled

Communicates that a radio button exists, but isn’t available in that scenario. When the user hovers over a radio button in a disabled state, the cursor shows as ‘not allowed’.  
  
Disabled radio buttons maintain layout consistency and communicate that a radio button may become available if another condition is met. The style of the label (colour) changes to indicate that the radio button is disabled.

### Checked disabled

Communicates that a radio button exists, but isn’t available in that scenario. When the user hovers over a radio button in a checked disabled state, the cursor shows as ‘not allowed’.  
  
Disabled checked radio buttons maintain layout consistency and communicate that a radio button may become available if another condition is met. The style of the label (colour) changes to indicate that the radio button is checked and disabled.

The feedback element becomes visible (configurable) on state change (e.g. hover).

* * *

Behaviours
----------

Here’s how the radio button behaves:

### Label overflow wrap

When a label is too long for the available horizontal space, it wraps to form another line.

### Clickable area

The radio button feedback element indicates the minimum clickable area for the radio button input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the radio button. The associated label is also clickable.

### Focusable area

The radio button input and label are both interactive, and a user can hover over either, but only the radio button input is focusable (e.g. via keyboard or voice).

### Validation

Use the form to choose whether the radio button validates onSubmit or onBlur, for both the initial validation and re-validation. See the form page for more.  
  

Validation only works if the form input radio button uses the form component.

### Exclusive selection

Checking a radio button in a radio group will uncheck all other radio buttons in that group.

### Autofocus

You can auto-focus on the radio button on page load (when mounted).

### Default checked

The radio button's initial state can be set to checked or unchecked by default (controlled or uncontrolled).  
  
Add checked to the native HTML element to select the radio button by default.  
  
Screen readers will read the radio button aloud to the user and let them know it’s selected.

### Label overflow wrap

When a label is too long for the available horizontal space, it wraps to form another line.

### Clickable area

The radio button feedback element indicates the minimum clickable area for the radio button input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the radio button. The associated label is also clickable.

### Focusable area

The radio button input and label are both interactive, and a user can hover over either, but only the radio button input is focusable (e.g. via keyboard or voice).

### Validation

Use the form to choose whether the radio button validates onSubmit or onBlur, for both the initial validation and re-validation. See the form page for more.  
  

Validation only works if the form input radio button uses the form component.

### Exclusive selection

Checking a radio button in a radio group will uncheck all other radio buttons in that group.

### Autofocus

You can auto-focus on the radio button on page load (when mounted).

### Default checked

The radio button's initial state can be set to checked or unchecked by default (controlled or uncontrolled).  
  
Add checked to the native HTML element to select the radio button by default.  
  
Screen readers will read the radio button aloud to the user and let them know it’s selected.

* * *

Usage
-----

Here’s how and when to use the radio button:

* * *

Do use radio buttons for selecting one option

Use radio buttons when a user can select only one option from a list.

* * *

Don't use radio buttons for selecting multiple options

If users can select multiple options from a list, use checkboxes instead.

* * *

Do give radio buttons a label

Radio buttons should have an associated label to give users context.

* * *

Do put labels on the right of the radio buttons

When grouping multiple radio buttons, put the label on the right. This makes them easier to find, especially for users of screen magnifiers.

* * *

Do display radio buttons vertically

Radio buttons should be displayed vertically, and stacked for consistent alignment and positioning across different breakpoints.

* * *

Do provide context with assistive text

Use assistive text to provide context to the radio button group (e.g. why a selection is required.)

* * *

Accessibility considerations
----------------------------

Group radio buttons

Group radio buttons and related elements (such as labels and assistive text) together using the fieldset component with a title attributed to the elements called a legend.  
  
A fieldset groups related form controls, making them easier to understand. It can also allow users to focus on smaller and more manageable chunks, rather than trying to grasp the entire form at once.

Focus order

Order

Element

Role

Keyboard interactions

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

This package exports three components: a form input radio button for use within the [form component](/components/form/) a radio button for use as a controlled component (e.g. where you have a custom validation mechanism) and the radio group for grouping radio buttons together.  
  
All have a range of props to define the experience in different use cases.

Form input radio button

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

Radio button

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

RadioGroup

Name

Type

Default

Description

Required

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