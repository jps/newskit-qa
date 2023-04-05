Switch | NewsKit design system

Actions & Inputs

Switch
======

Switches let users turn a setting on or off.

Status
======

Supported

* * *

Introduced
==========

[v5.4.6](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.4.6)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/switch)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-switch--story-switch-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=1801%3A344142)

* * *

Anatomy
-------

The switch component contains two required elements and five optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The switch has options for different use cases:

### Size

The switch comes in small, medium (default) and large.

### Thumb & track (size & icons)

Change the thumb and track sizes to match a platform's visual style (e.g. Android, iOS).  
  
Add an icon inside the thumb, and two icons within the track (e.g. 'on' and 'off' icons).

The track icon sizes depend on the size of the track and the thumb (i.e. they cannot be bigger than the thumb or they won’t be covered when the thumb slides over them). The thumb icon size depends on the size of the thumb.

### Feedback

The feedback element is non-interactive and appears in the background behind the switch thumb for visual feedback on hover.

### Label

Add a label to the right (end) of the switch to provide context.

You can add a label on the left (start) of a switch using the `labelPosition` prop.

### Size

The switch comes in small, medium (default) and large.

### Thumb & track (size & icons)

Change the thumb and track sizes to match a platform's visual style (e.g. Android, iOS).  
  
Add an icon inside the thumb, and two icons within the track (e.g. 'on' and 'off' icons).

The track icon sizes depend on the size of the track and the thumb (i.e. they cannot be bigger than the thumb or they won’t be covered when the thumb slides over them). The thumb icon size depends on the size of the thumb.

### Feedback

The feedback element is non-interactive and appears in the background behind the switch thumb for visual feedback on hover.

### Label

Add a label to the right (end) of the switch to provide context.

You can add a label on the left (start) of a switch using the `labelPosition` prop.

* * *

States
------

The switch has the following states:

### Base

The default style before the user interacts with the switch.

### Hover

The switch changes style to let the user know it’s interactive.

### Focus

Communicates that the user has highlighted a switch (e.g. via keyboard or voice).

### Focus hover

Communicates that the user has highlighted and hovered over a switch (e.g. via keyboard or voice).

### Checked

The switch input changes style to let the user know the switch is checked. The style of the label remains the same.

### Checked hover

The switch input changes style to let the user know the switch is checked and hovered over. The style of the label remains the same.

### Checked focus

Communicates that a user has highlighted a switch (e.g. via keyboard or voice).

### Checked focus hover

Communicates that a user has highlighted and hovered over a switch (e.g. via keyboard or voice).

### Disabled

Communicates that a switch exists, but isn't available in that scenario. When the user hovers over a switch in a disabled state, the cursor shows as 'not allowed'.  
  
Disabled switches maintain layout consistency and communicate that a switch may become available if another condition is met. The style of the label (colour) changes to indicate that the switch is disabled.

### Checked disabled

Communicates that a switch exists, but isn't available in that scenario. When the user hovers over a switch in a checked disabled state, the cursor shows as 'not allowed'.  
  
Checked disabled switches maintain layout consistency and communicate that a switch may become available if another condition is met. The style of the label (colour) changes to indicate that the switch is checked and disabled.

The feedback element becomes visible (configurable) on state change (e.g. hover).

* * *

Behaviours
----------

Here’s how the switch behaves:

### Checked vs unchecked

Switches can be checked or unchecked.  
  
A switch in a checked state is indicated with the thumb on the right.  
  
A switch in an unchecked state is indicated with the thumb on the left.

### Label overflow wrap

When a label is too long for the available horizontal space, it wraps to form another line.

### Clickable area

The switch feedback element indicates the minimum clickable area for the switch input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the switch. The associated label is also clickable.

### Focusable area

The switch input and label are both interactive, and a user can hover over either, but only the switch thumb is focusable (e.g. via keyboard or voice).

### Checked vs unchecked

Switches can be checked or unchecked.  
  
A switch in a checked state is indicated with the thumb on the right.  
  
A switch in an unchecked state is indicated with the thumb on the left.

### Label overflow wrap

When a label is too long for the available horizontal space, it wraps to form another line.

### Clickable area

The switch feedback element indicates the minimum clickable area for the switch input (also known as hit area or touch target area). The size of the clickable area changes according to the size of the switch. The associated label is also clickable.

### Focusable area

The switch input and label are both interactive, and a user can hover over either, but only the switch thumb is focusable (e.g. via keyboard or voice).

* * *

Usage
-----

Here’s how and when to use the switch:

* * *

Do communicate activation

Use switches for communicating activation (e.g. on/off states).

* * *

Don’t use to communicate selection

Avoid using switches for communicating selection (e.g. multiple table rows). In these cases, use a [checkbox.](/components/checkbox/) instead.

* * *

Do give switches a label

Switches should have an associated label to give users context.

* * *

Don’t require users to press a button

Switches shouldn’t require users to press a button to apply settings.

* * *

Accessibility considerations
----------------------------

The switch has the following accessibility considerations:

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

References: [WAI-ARIA Authoring Practices.](https://www.w3.org/WAI/ARIA/apg/patterns/switch/)

* * *

API
---

Switch

The switch has a range of props to define the experience in different use cases.

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

### Checkbox



](/components/checkbox/)

Checkboxes are selection controls that allow users to select one or multiple items from a group of options. They typically appear in forms.

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