Character Count | NewsKit design system

Feedback & Status

Character Count
===============

Character count lets users know how much text they can enter in an input container as they type.

Status
======

Supported

* * *

Introduced
==========

[v6.3.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v6.3.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/character-count)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-character-count--character-count-default)

* * *

Anatomy
-------

The character count contains one required element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The character count has options that can be used to provide an appropriate experience for different use cases.

### Character limit

The input and character count text counts down as a user types, and changes to an invalid state when the character limit is exceeded. Users can still input characters if they exceed the set character count. This allows them to edit down their input so it falls within the limit.  
  
The character limit is configurable and is set via native HTML max and min length value functionality.  
  
[For more information, please refer to the HTML input attribute types.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)

### Character limit

The input and character count text counts down as a user types, and changes to an invalid state when the character limit is exceeded. Users can still input characters if they exceed the set character count. This allows them to edit down their input so it falls within the limit.  
  
The character limit is configurable and is set via native HTML max and min length value functionality.  
  
[For more information, please refer to the HTML input attribute types.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)

* * *

States
------

The character count has the following states:

### Base

The character count has a base state. This is the base style of the input before the input has been interacted with by a user.

### Invalid

The character count in an invalid state changes style when the inputted entry doesn’t conform to the limit set on the number of characters.  
  
The [form](https://www.newskit.co.uk/components/form/) component is used to define this validation behaviour.

### Valid

The character count in a valid state changes style when the inputted entry conforms to the limit set on the number of characters.  
  
The [form](https://www.newskit.co.uk/components/form/) component is used to define this validation behaviour.

### Disabled

The character count in a disabled state shows that an input exists, but is not available to the user in that scenario. When a user’s cursor hovers over an input in a disabled state the cursor shows as not-allowed, and the character count state changes.

* * *

Usage
-----

Here’s how and when to use the character count :

* * *

Do display an error message when needed

If a user tries to submit a form with an exceeded character count, display an error message prompting them to reduce the number of characters.

* * *

Don’t restrict users from inputting characters

Don’t restrict users from inputting characters or copying and pasting them even if they exceed the set character count. This allows for editing down their input so it falls within the set limit.  
  
By default, browsers prevent users from entering more, or fewer characters to an input field than allowed by the maxLength and minLength attributes. [Refer to MDN for more information on client-side validation.](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

* * *

Do display a word count when needed

In some cases, it may be more helpful to show a word count. For example, if your question requires a longer answer, you can set data-maxwords in the component markup. E.g. //data-maxwords="100"//.

* * *

Accessibility considerations
----------------------------

The character count has the following accessibility considerations:  
  
Use `aria-live=POLITENESS_SETTING` to set the priority with which the screen reader should treat updates to live regions, allowing for the voiceover to read out loud the remaining characters as the user types.

Code example

This is read out on voiceover first before the user begins to type. Then as the user types, the remaining character count is read out.  
  
you have enter up to 200 chracters ⇒ hidden

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

API
---

The FormInput character count has a range of props that can be used to define an appropriate experience for different use cases. Use this component within [the NewsKit form component.](https://www.newskit.co.uk/components/form/)

FormInput character count

Props

Overrides

Name

Type

Default

Description

Required

The character limit is configurable and is set via [native HTML max and min length value functionality.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#attributes)

Attribute

Type

Default

Description

Character count

The character count has a range of props that can be used to define an appropriate experience for different use cases. Use this component as a controlled component, for instance where you have a custom validation mechanism.

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

### Flag



](/components/flag/)

A flag is a non-interactive visual indicator used to communicate status.

[

### Progress Indicator



](/components/progress-indicator/)

Demonstrates the progress of a system action e.g. waiting for a page to load.

[

### Tooltip



](/components/tooltip/)

A Tooltip is a feedback component that displays a short, informational message when a user hovers over or focuses on a UI element.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)