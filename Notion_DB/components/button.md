Button | NewsKit design system

Actions & Inputs

Button
======

Buttons let users make choices and take action.

Status
======

Supported

* * *

Introduced
==========

v0.2.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/develop/src/button)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-button--story-button-size)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=1817%3A8822)

* * *

Anatomy
-------

Button

The button component contains two required elements and one optional element.

Item

Name

Description

Component

Optional

Icon Button

The icon button contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The button has options for different use cases.

### Appearance

There are three button styles by default: solid, outlined and minimal.

Note

Use inverse buttons on darker backgrounds.

### Intent

The button has four intents: primary, secondary, positive and negative. Each communicates a specific tone to the user.

### Size

The button comes in small, medium (default) and large.

### Border radius and width

Override the button’s [border](/theme/foundation/borders/) radius and border width, and apply them to the theme.

### Icons (leading & trailing)

Add an icon to a button either before (leading) or after (trailing) the label.

### Label

Add a label to a button to give users more context about what the button does.

### Icon Button

The icon button has the same options, behaviours and properties as the button, but with a single icon in the centre of the container.

### Button as a link

Render buttons as [links.](/components/link/) The link is styled like a button but behaves like a link.

### Appearance

There are three button styles by default: solid, outlined and minimal.

Note

Use inverse buttons on darker backgrounds.

### Intent

The button has four intents: primary, secondary, positive and negative. Each communicates a specific tone to the user.

### Size

The button comes in small, medium (default) and large.

### Border radius and width

Override the button’s [border](/theme/foundation/borders/) radius and border width, and apply them to the theme.

### Icons (leading & trailing)

Add an icon to a button either before (leading) or after (trailing) the label.

### Label

Add a label to a button to give users more context about what the button does.

### Icon Button

The icon button has the same options, behaviours and properties as the button, but with a single icon in the centre of the container.

### Button as a link

Render buttons as [links.](/components/link/) The link is styled like a button but behaves like a link.

* * *

States
------

The Button has the following states:

### Base

The default style before the user interacts with the button.

### Hover

The button changes style to let the user know it’s interactive.

### Focus

Communicates that a user has highlighted a button (e.g. via keyboard or voice).

### Active

The button changes style to let the user know they’ve interacted with it.

### Disabled

Communicates that a button exists, but isn’t available in that scenario. When the user hovers over a button in a disabled state, the cursor shows as ‘not allowed.  
  
Disabled buttons maintain layout consistency and communicate that a button may become available if another condition is met.

### Loading

Communicates that an action will become available when loading is complete, or that an action is being completed.  
  
The background colour of the button changes and a loading indicator is displayed.

* * *

Behaviours
----------

Here’s how the button behaves:

### Fixed and full width

Buttons can be either fixed width or full width. Consider how they’ll respond and react to containers around them:  
  
Fixed width - size dependant on content (e.g. label or icon)  
  
Full width - size responsive to container

Note

Use full width buttons on smaller screen sizes, or in components (e.g. [cards](/components/card/)), where the width is restricted.

### Transition

When the user hovers over a button, or a button is active, the backgroundColor and/or borderColor transitions.

### Clickable area

Buttons have a minimum clickable area (also known as hit area or touch target area). The size of the clickable area changes according to the size of the button.

### Fixed and full width

Buttons can be either fixed width or full width. Consider how they’ll respond and react to containers around them:  
  
Fixed width - size dependant on content (e.g. label or icon)  
  
Full width - size responsive to container

Note

Use full width buttons on smaller screen sizes, or in components (e.g. [cards](/components/card/)), where the width is restricted.

### Transition

When the user hovers over a button, or a button is active, the backgroundColor and/or borderColor transitions.

### Clickable area

Buttons have a minimum clickable area (also known as hit area or touch target area). The size of the clickable area changes according to the size of the button.

* * *

Usage
-----

Here’s how and when to use the button:

* * *

Do allow a sufficient hit area

When placing two or more buttons inline, make sure they are a sufficient size or have spacing between them to avoid users accidentally hitting the wrong button.

* * *

Don’t use full width buttons in wide containers

Full width buttons are more appropriate for small devices or contained components.

* * *

Do consider button width

When deciding between a fixed or full width button, consider how it will respond and react to the containers around it.

* * *

Don’t separate related buttons

Place related buttons next to each other so associated actions are relative, and to reduce cognitive load.

* * *

Don’t stack buttons unnecessarily

Avoid stacking buttons when there’s enough space to place them side by side.

* * *

Don’t have more than one primary button

Avoid having more than one primary (high emphasis) button on a screen to help guide the user to the primary action.

* * *

Accessibility considerations
----------------------------

The button has the following accessibility considerations:

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

The button supports native [HTML](https://www.w3.org/TR/html-aria/#docconformance) and [aria attributes](https://www.w3.org/TR/wai-aria-1.1/#button).

* * *

SEO
---

Ensure icons have alt text applied.

* * *

API
---

Button

Props

Overrides

The button has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The button has a range of props that can be used to define an appropriate experience for different use cases.

Attribute

Type

Default

Description

Icon Button

Props

Overrides

The icon button has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The icon button has a range of props that can be used to define an appropriate experience for different use cases.

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