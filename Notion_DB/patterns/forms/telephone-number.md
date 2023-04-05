Telephone number | NewsKit design system

Forms

Telephone number
================

Ask for a user’s telephone number when there is a clear business requirement.

* * *

How to ask for a user’s telephone number
----------------------------------------

Telephone numbers are sensitive information. Be clear about why it is being collected.

### Labelling

This should be labelled as ‘Contact telephone number’ and you should only ask for it once. Some users will not have a home phone number so you should not ask for this separately unless there is a business requirement to do so.  
  
Similarly, not all users will have a mobile number so you should not be specific about the type of telephone number you require unless there is a business need for one type over the other i.e needing to be able to text customers.

### International numbers

You will need to allow for international telephone numbers. The simplest way to do this is to allow users to select their country code from a select list.  
  
The select list should:  
  

*   Default on the relevant country your business/customers are based.
    
*   Display the relevant country code in the text field i.e +44.
    
*   Display the most likely selected countries to the top of the select list. (If relevant)
    

  
Although displaying the country code negates the need for the user to enter a ‘0’ at the start of their phone number, you should still accept telephone numbers where the ‘0’ is added to reduce customer error and the need for confusing error messaging.

#### Do

*   Be clear as to why we are collecting the user's telephone number.
    
*   Allow users to include spaces and hyphens in their telephone number.
    
*   Allow autofill so the user can easily fill out this form based on saved personal data on their device.
    
*   Validate telephone numbers so you can let users know if they have entered one incorrectly. [Google’s libphonenumber library](https://github.com/google/libphonenumber) can validate telephone numbers from most countries.
    
*   Default on number entry for mobile devices.
    
*   Default country code on the relevant country your business/users are based.
    

#### Don’t

*   Make the user scroll unnecessarily through the country dropdown. Country code drop downs can be fiddly and involve a lot of list items to scroll through.
    
*   Display telephone numbers as links on devices that cannot make calls.
    

### Error states

Please enter your telephone number (If left empty).  
  
Please enter a valid telephone number (If too long).  
  
Please enter a telephone number in the correct format (If in incorrect format).

* * *

Help improve this page
----------------------

To help make sure this page is as useful as it can be, relevant and kept up to date with industry best practices, please get in touch to share your research findings, and contribute to this page.  
  
[Propose a change or contribution by suggesting a feature request.](https://github.com/newscorp-ghfb/newskit/issues/new/choose)

* * *

Input components
================

Use the right component for the type of data you’re collecting.

[Choose the right input component](/patterns/forms/input-components/)

Input components
================

Use the right component for the type of data you’re collecting.

[Choose the right input component](/patterns/forms/input-components/)