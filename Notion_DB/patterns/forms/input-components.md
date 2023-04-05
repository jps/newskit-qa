Input components | NewsKit design system

Forms

Input components
================

Use the right component for the type of data you’re collecting.

Introduction
------------

Forms can be split out into data entry types, each will have their own patterns and best practice that is outlined below. You should use an appropriate input type for the data you collect. Providing the right type of input field for requested data will help users enter information in the right format and avoid mistakes, making the process as easy and efficient as possible. Eg. use a Password Input Field for users to input their password.

* * *

Text Field
----------

Text Fields are the simplest and most common form of data entry, allowing users to enter freeform text. This format should be used when the data that is required is open and not something the user can select from a predefined list.

### Considerations

The vast majority of the time, text input will be single line input, however you should consider allowing multiple line entry if the data needed requires it.  
  
The width of the Text Field should be consistent with other Text Fields on the page, unless the data required is a set short number of characters such as postcode (See best practice above).  
  
In some cases the format of the field can be restricted i.e numbers or email address. But this should be considered in error messaging.

#### Text Field usage examples

*   Name
    
*   Email address
    
*   Password
    
*   Date of birth
    
*   Telephone number
    
*   Address
    

* * *

Radio Group - Single selection
------------------------------

A [Radio Group](/components/radio-button/) should be used when there is a predefined list of options for a user to choose from. These should always be a single selection option and should be used for a lower number of options so as not to take up too much space on the page i.e between 2 and 10.

### Considerations

Options should be stacked on top of each other.  
  
You should offer a default selection for Radio Buttons. Radio Buttons always have one option selected so should therefore not be displayed without a default selection.  
  
There may need to be an ‘Other’ option where the user enters an answer that isn’t displayed e.g gender.  
  
If there are a higher number of radio options required it may be necessary to split out the relevant question onto its own page to reduce cognitive load and keep focus on the question.

#### Radio Button usage examples

*   Gender
    
*   Payment type
    
*   Poll
    

* * *

Checkbox - Multiple selection
-----------------------------

If there is a requirement to allow users to select multiple options from a shorter list, then a [Checkbox](/components/checkbox/) can be used. There should still be a limit to the number of options listed so that the page isn’t dominated with options. Similar to Radio Buttons, if there are more than a certain number of options, a [Select](/components/select/) should be used i.e more than 10.

### Considerations

*   Checkboxes should only be displayed vertically, stacked for consistent alignment and positioning across different breakpoints.
    
*   You should not pre-select an option for the user
    
*   There may need to be an ‘Other’ option where the user enters an answer that isn’t displayed e.g interests.
    
*   If there are a higher number of Checkbox options required it may be necessary to split out the relevant question onto its own page to reduce cognitive load and keep focus on the question.
    
*   If there is a maximum/minimum number of responses required, this should be made clear to the user upfront.
    
*   Avoid placing Labels to the left (start) of Checkboxes when there are multiple Checkboxes grouped together to avoid layout misalignment. Instead place Labels to the right (end) so that when used together in forms, Checkbox inputs align vertically, which makes them easier to find, especially for users of screen magnifiers.
    
*   Avoid using Checkboxes in a horizontal orientation to avoid issues with alignment and legibility when there are multiple Checkboxes grouped together.
    

### Checkbox usage example

*   Customer survey
    

* * *

Select - Single or multiple selection
-------------------------------------

A ‘Select’ should be used for a larger number of options than a Radio Group or Checkbox as the options can then be displayed in their own scrollable panel, with focus, rather than on page.  
  
A ‘Select’ can be used for selecting one or multiple options from a predefined list.

### Considerations

*   Consider if a Select is necessary or if a Text Field can be used. Selects can be cumbersome if there are a lot of options for users to scroll through.
    
*   You should not pre-select an option for the user.
    
*   In general all valid options should be displayed within the Select so an ‘Other’ option isn’t needed.
    
*   If there is a more likely/default option, this should be displayed at the top of the drop down to save most users scrolling through every option e.g United Kingdom.
    
*   Options should be displayed in alphabetical order so they are easier to scan/find.
    

### Select usage example

*   Country code (If not using text input).
    

* * *

Combo box
---------

A Combo Box is a combination of a Text Input and a Select. A Combo Box should be used for looking up and selecting an option based on the user's entry to the Text Input. i.e Address lookup.

### Considerations

*   Consider giving the user the option to add their entry manually. Sometimes lookup doesn’t give the required answer so manually typing the response is easier.
    
*   Give clear instructions as to what the user has to type into the text input and what they then have to do i.e ‘Enter your postcode and select your address from the list provided’.
    
*   Allow users to change their entry if a mistake has been made or they decide on a different entry i.e different postcode.
    
*   Select results should be displayed as the user types their text entry rather than waiting for users to select a CTA to submit as this reduces time and effort for the user. There should still however be an option to tap/type the return key on a keyboard or select a CTA to submit.
    

* * *

NewsKit input component links
-----------------------------

### Text Field

Text Fields allow users to enter and edit text content into a UI. They typically appear in Forms.  
  
[View the Text Field component](/components/text-field/)

### Radio Button

Radio Buttons are selection controls that are typically used in forms. They are used for exclusive selection - allowing users to select one of multiple options in a Radio Group.  
  
[View the Radio Button component](/components/radio-button/)

### Checkbox

Checkboxes are selection controls that allow users to select one or multiple items From a group of options. They typically appear in forms.  
  
[View the Checkbox component](/components/checkbox/)

### Select

Select components allow users to select one option from a list. They typically appear in Forms.  
  
[View the Select component](/components/select/)

* * *

Help improve this page
----------------------

To help make sure this page is as useful as it can be, relevant and kept up to date with industry best practices, please get in touch to share your research findings, and contribute to this page.  
  
[Propose a change or contribution by suggesting a feature request.](https://github.com/newscorp-ghfb/newskit/issues/new/choose)

* * *

Overview
========

Forms are used to collect customer’s data.

[Learn more about forms](/patterns/forms/overview/)

Overview
========

Forms are used to collect customer’s data.

[Learn more about forms](/patterns/forms/overview/)