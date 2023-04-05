Checkbox | NewsKit design system

Actions & Inputs

Checkbox
========

Checkboxes let users select one or multiple items from a group of options. They typically appear in forms.

Status
======

Supported

* * *

Introduced
==========

v4.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/blob/develop/src/checkbox/checkbox.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-checkbox--story-checkbox-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=3712%3A75609)

* * *

Anatomy
-------

The checkbox component contains one required element and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The checkbox has options for different use cases:

### Size

The checkbox input and feedback element both come in small, medium (default) and Large.

### Icon

Override the icon within the checkbox input for different checkbox states.

### Feedback

The feedback element is non-interactive and appears in the background behind the checkbox input on hover.

### Label

Add a label to the right (end) of the checkbox to provide context.

You can add a label on the left (start) of a checkbox using the `labelPosition` prop.

### Fieldset

Group together selection controls (e.g. for input, radio button and checkbox) in a [fieldset](/components/fieldset/) , along with labels and assistive text. Add a title to the grouped elements using the legend.

### Size

The checkbox input and feedback element both come in small, medium (default) and Large.

### Icon

Override the icon within the checkbox input for different checkbox states.

### Feedback

The feedback element is non-interactive and appears in the background behind the checkbox input on hover.

### Label

Add a label to the right (end) of the checkbox to provide context.

You can add a label on the left (start) of a checkbox using the `labelPosition` prop.

### Fieldset

Group together selection controls (e.g. for input, radio button and checkbox) in a [fieldset](/components/fieldset/) , along with labels and assistive text. Add a title to the grouped elements using the legend.

* * *

States
------

The Checkbox has the following states:

### Base

The default style before the user interacts with the checkbox.

### Hover

The checkbox changes style to let the user know it’s interactive. The style of the label remains the same. Users can interact with (hover) the label to check the checkbox.

### Focus

Communicates that the user has highlighted a checkbox (e.g. via keyboard or voice).

### Focus Hover

Communicates that the user has highlighted and hovered over a checkbox (e.g. via keyboard or voice).

### Checked

The checkbox input changes style to let the user know the checkbox is checked. The style of the label remains the same.

### Checked Hover

The checkbox input changes style to let the user know the checkbox is checked and hovered over. The style of the label remains the same.

### Checked Focus

Communicates that the user has highlighted a checkbox (e.g. via keyboard or voice).

### Checked Focus Hover

Communicates that the user has highlighted and hovered over a checkbox (e.g. via keyboard or voice).

### Invalid

The checkbox changes style when checkbox selection doesn’t conform to a specific format (e.g. attempting to proceed without selecting a required checkbox in a form). Use the form component to validate behaviour. The style of the label remains the same.

### Invalid Focus

Communicates that the user has highlighted an invalid checkbox (e.g. via keyboard or voice).

### Invalid Hover

The checkbox input changes style to let the user know the checkbox is in an invalid state and hovered over. The style of the label remains the same.

### Invalid Focus Hover

Communicates that the user has highlighted and hovered over an invalid checkbox (e.g. via keyboard or voice).

### Checked Invalid

The checkbox input changes style to let the user know the checkbox is checked and in an invalid state. The style of the label remains the same.

### Checked Invalid Focus

Communicates that the user has highlighted an invalid checkbox (e.g. via keyboard or voice).

### Checked Invalid Hover

The checkbox input changes style to let the user know the checkbox is checked, in an invalid state and hovered over. The style of the label remains the same.

### Checked Invalid Focus Hover

Communicates that the user has highlighted and hovered over an invalid checkbox (e.g. via keyboard or voice).

### Valid

The checkbox changes style when checkbox selection criteria are met (e.g. updating preferences in a form). Use the form component to validate behaviour. The style of the label remains the same.

### Valid Focus

Communicates that the user has highlighted a valid checkbox (e.g. via keyboard or voice).

### Valid Hover

The checkbox input changes style to let the user know the checkbox is in a valid state and hovered over. The style of the label remains the same.

### Valid Focus Hover

Communicates that the user has highlighted and hovered over a valid checkbox (e.g. via keyboard or voice).

### Checked Valid

The checkbox input changes style to let the user know the checkbox is checked and in a valid state. The style of the label remains the same.

### Checked Valid Focus

Communicates that the user has highlighted a valid checkbox (e.g. via keyboard or voice).

### Checked Valid Hover

The checkbox input changes style to let the user know the checkbox is checked, in a valid state and hovered over. The style of the label remains the same.

### Checked Valid Focus Hover

Communicates that the user has highlighted and hovered over a valid checkbox (e.g. via keyboard or voice).

### Disabled

Communicates that a checkbox exists, but isn’t available in that scenario. When the user hovers over a checkbox in a disabled state, the cursor shows as ‘not allowed’.  
  
Disabled checkboxes maintain layout consistency and communicate that a checkbox may become available if another condition is met. The style of the label (colour) changes to indicate that the checkbox is disabled.

### Checked Disabled

Communicates that a checkbox exists, but isn’t available in that scenario. When the user hovers over a checkbox in a checked disabled state, the cursor shows as ‘not allowed’.  
  
Disabled checked checkboxes maintain layout consistency and communicate that a checkbox may become available if another condition is met. The style of the label (colour) changes to indicate that the checkbox is checked and disabled.

The feedback element becomes visible (configurable) on state change (e.g. hover).

* * *

Behaviours
----------

The following guidance describes how the Checkbox component behaves.

### Checked vs unchecked

Checkboxes can be checked or unchecked. An icon appears in the centre of the checkbox to indicate the checked state.

### Label overflow wrap

When a Label is too long for the available horizontal space, it wraps to form another line.

### Transition

When the checkbox is checked, the ‘check’ icon fades up in the centre of the checkbox and `backgroundColor` and `borderColor` transition simultaneously.

### Clickable area

The checkbox feedback element indicates the minimum clickable area for the checkbox input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the checkbox. The associated label is also clickable.

### Focussable area

The checkbox input and label are both interactive, and a user can hover over either, but only the checkbox input is focussable (e.g. via keyboard or voice).

### Validation

Use the form to choose whether the checkbox validates on submit or on blur, for both the initial validation and re-validation.  

Note

Validation only works if the form input checkbox uses the form component.

### Autofocus

You can auto-focus on the checkbox on page load (when mounted).

### Default checked

The checkbox’s initial state can be set to checked or unchecked by default (controlled or uncontrolled).

### Checked vs unchecked

Checkboxes can be checked or unchecked. An icon appears in the centre of the checkbox to indicate the checked state.

### Label overflow wrap

When a Label is too long for the available horizontal space, it wraps to form another line.

### Transition

When the checkbox is checked, the ‘check’ icon fades up in the centre of the checkbox and `backgroundColor` and `borderColor` transition simultaneously.

### Clickable area

The checkbox feedback element indicates the minimum clickable area for the checkbox input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the checkbox. The associated label is also clickable.

### Focussable area

The checkbox input and label are both interactive, and a user can hover over either, but only the checkbox input is focussable (e.g. via keyboard or voice).

### Validation

Use the form to choose whether the checkbox validates on submit or on blur, for both the initial validation and re-validation.  

Note

Validation only works if the form input checkbox uses the form component.

### Autofocus

You can auto-focus on the checkbox on page load (when mounted).

### Default checked

The checkbox’s initial state can be set to checked or unchecked by default (controlled or uncontrolled).

* * *

Usage
-----

Here’s how and when to use the checkbox:

* * *

Do use checkboxes for up to 7 options

If you have more than 7 checkboxes in a group, use a select.

* * *

Do use checkboxes for selecting multiple options

Use checkboxes either for selecting multiple options from a list, or to check or uncheck a control. If users can only select a single option, use the radio button instead.

* * *

Do give checkboxes a label

Checkboxes should have an associated label to give users context.

* * *

Do put labels on the right of grouped checkboxes

Align checkbox inputs vertically. This makes them easier to find, especially for users of screen magnifiers.

* * *

Do display checkboxes vertically

Align checkbox inputs vertically. This makes them easier to find, especially for users of screen magnifiers.

* * *

Don't check options by default

Avoid default checked options. Users might not realise they’ve missed a question and submit an unintended answer.

* * *

Do make error text clear and simple

Error text should be clear, concise and written in complete sentences - and it should tell the user how to resolve the issue.

* * *

Accessibility considerations
----------------------------

The Checkbox has the following accessibility considerations:

Grouping Checkboxes

Group checkboxes and related elements (e.g. labels and assistive text) together using the fieldset component with a title attributed to the elements called a legend.  
  
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

The Checkbox has a range of props that can be used to define an appropriate experience for different use cases.

This package exports two components: a form input checkbox for use within the [form](/components/form/) component, and a checkbox for use as a controlled component (e.g. where you have a custom validation mechanism). Both have a range of props to define the experience in different use cases.

Form input checkbox

The form input checkbox has a range of props that can be used to define an appropriate experience for different use cases. Use this component within the [form](/components/form/) component.

Props

Overrides

Name

Type

Default

Description

Required

Note

The `name` & `rules` props are set on the form input level. To add validation rules, or set the name of this component, see the [form](/components/form/) page

Attribute

Type

Default

Description

Checkbox

The Checkbox has a range of props that can be used to define an appropriate experience for different use cases. Use this component as a controlled component, for instance where you have a custom validation mechanism.

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

### Form



](/components/form/)

The form component allows users to enter and edit information into a UI using form controls; based on React Hook Form.

[

### Radio Button



](/components/radio-button/)

Radio Buttons are selection controls that are typically used in forms

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