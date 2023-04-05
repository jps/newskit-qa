Best practice | NewsKit design system

Forms

Best practice
=============

Help users to fill in forms quickly and accurately by following these industry best practices.

Introduction
------------

Following best practices ensures that the user understands what data is being collected and why, is not overwhelmed by the information we are requesting, and knows the data they have entered is valid.

* * *

Structure & Layout
------------------

Consider if your form should be displayed in a single step or split into multi-steps. Some short forms can be displayed on one page, meaning that the user can see all the information that needs to be entered.

### Single step vs multi step

If you have a lot of information to collect, it’s worth considering breaking the form into sensible steps e.g. personal details, billing etc. This may reduce cognitive load for users so they can focus on one type of data at a time. This also allows for customer data, such as email addresses, to be captured early in the process, meaning they can contact users who drop out of the registration process.  
  
It’s always advisable to test each layout with your users and, ideally, run experiments to understand which structure has the best conversion.  
  
More information and insight on single step vs multi step can be found [here.](https://wpmanageninja.com/single-step-form-vs-multi-step-form-which-one-is-the-best-and-why/)

### Tip

If your form is split into several steps, there should be an easy way for the user to go back to the previous step. Data should be autosaved when they go backwards/forwards through the steps.

### Keep the number of fields to a minimum

The more personal data you ask for, the more likely users will drop out of the funnel. Therefore, you should only ask for information that is genuinely required.

[WSJ](https://www.wsj.com/) saw a 1.8% conversion lift for each field that was reduced, so keeping fields to a minimum is likely to have a positive impact.

### Layout

#### Do

*   [Forms](/components/form/) should be displayed in a single column layout. This means the user’s focus is on one data input type at a time and there is less cognitive load searching the page for what data to enter.
    

### Text field width

#### Do

*   Most [Text fields](/components/text-field/) should be proportional to the expected user input - no longer than a single line, such as their name or phone number.  
      
    For example, Text Fields that have a set short number of characters should have a proportional width i.e year of birth or postcode.
    

#### Don’t

*   You should avoid using the Text Field if you need to let users enter longer answers that might span multiple lines. Consider using an alternative, such as Text Area.
    

* * *

Progress & abandonment
----------------------

The user's progress should be highlighted, so they understand where they are in the relevant journey, what step is coming next and how long the process will be. These can be given a visual treatment so it's apparent to the user which steps are 'to be done', 'doing' and 'done'.

### Tip

The user should be able to easily go back through each step and edit their data, in case a mistake has been made.

### Abandonment capture

If users attempt to abandon a form or registration process by navigating away from a window, you can prompt them to stay on the page and continue their journey. This can be done natively via the user’s browser or via a bespoke experience that we can manage/control.

* * *

Labels
------

Using best practice when displaying labels on a Form is vital to ensure the user knows what data they need to enter and that data is entered in the correct format.

### Display

#### Do

*   Labels should be displayed above the required field and left aligned so that the user can still see the requested data format when their cursor is active within the field.
    
*   Input labels and placeholder text should be in sentence case, whereby only the first word of a sentence and proper nouns are capitalised, with the rest of the words in lowercase. This helps with scannability and legibility.
    

#### Don’t

*   Input label text should not be truncated or wrapped over two or more lines. Keep it short, clear, and fully visible.
    

### Placeholder text

#### Do

*   Placeholder text can be displayed to provide the user with a short hint that describes the content that is expected to be inputted by the user (e.g. a sample value or a short description of the expected format).
    
*   Once a value is entered, the placeholder text is no longer visible. Assistive Text is the preferred way to communicate this information.
    

#### Don’t

*   The short hint is displayed in the input container before the user enters a value. However, placeholders should not be used as a replacement for labels.
    
*   Don't put instructions on completing an input or requirements into placeholder text as it cannot be read by a screenreader and is therefore not accessible.
    

### Assistive text

#### Do

*   If needed, Assistive Text should be used to hint at the action the user is being asked to do, for example, ‘Select all that apply’.
    
*   In terms of placement of Assistive Text - if it's attributed to a single input like a text field then it typically appears below. If there are multiple text fields in a group [(Fieldset for example)](/components/fieldset/) then it may make sense to sit above the inputs so assistive text/error messages are in a consistent place.
    
*   If there are a lot of [Text Fields](/components/text-field/) in a group, then the Assistive Text would be pushed to the end of the group, so it’s worth considering placement depending on the number of inputs in a group.
    

### Float labels

It has become more common to use ‘float labels’ whereby the Label sits within the text field initially and then moves above the Text Field once the Text Field becomes in focus. Whilst this is an interesting way of displaying Labels, before implementing, you should consider if there is any benefit to the user. It uses up space for hint text within the field, distracts the user and offers little benefit in terms of spacing as space needs to be given for the Label above the field either way.  
  
You can find a more detailed breakdown on why float labels may not be appropriate on the [UX Movement.](https://uxmovement.com/forms/infield-top-aligned-labels-floating-labels/)

### Single underline text entry field

In 2017, Google changed their [Material Design guidelines](https://material.io/design/introduction) to recommend single underline text entry fields. Due to this they have become a lot more popular when designing forms. However, it’s worth noting that since then Google have updated their guidelines as they found that:

*   Some users didn’t know that they could interact with the text field.
    
*   It looked like an empty box.
    
*   The line affordance under the old text fields was not clear to some users.
    
*   The line was confused with a divider.
    
*   The label and input were confused with body text, especially in dense compositions.
    

### Tip

There is more on this and the research they carried out [here.](https://medium.com/google-design/the-evolution-of-material-designs-text-fields-603688b3fe03) They have since changed the guideline to add a box for the text field as well as an underline so just displaying an underline for text entry should be avoided.

### Mandatory/Optional

Only optional fields should be highlighted. You should only be asking for customer data that we need as part of the business requirements so the vast majority will be mandatory.

* * *

Validation & Error messages
---------------------------

Validation and error messaging goes hand in hand to ensure you are capturing customer data accurately. This informs the user when they have entered data correctly, as well as clearly highlighting when an error has occurred.

### Validation

Displaying a tick next to data that has been entered correctly means the user can confidently move onto the next data entry point.  
  
However, consider if this is always needed. Validation is only useful if information needs to be in a certain format or meet specific criteria e.g password.

### Tip

Validation should be displayed ‘On blur’ (Once the user has tabbed out of the field), not summarised on submission of data. More information on validation states can be found [here.](https://www.w3schools.com/jsref/event_onblur.asp)  
  
You can toggle between both options in NewsKit [here.](/components/form/)

### Error messages

Error messaging should clearly inform the user an error has occurred, highlight where that error has occurred and what the user has to do to address the error.  
  
Within NewsKit, error messages are displayed in the place of Assistive Text. Once the error has been addressed then the Assistive Text is shown again.

### Best practice

*   Errors and validation should be displayed ‘On blur’ (once the user has tabbed out of the field) not as the user is entering their information.
    
*   Write error text that communicates a solution. Error text should be written in a few clear, concise and complete sentences. More guidance on error text can be found [here.](https://design-system.service.gov.uk/components/error-message/)
    
*   Space for error messaging below the Text Field should be catered for to stop the page jumping up and down when errors are shown/addressed. Within NewsKit you can apply min heights to text fields.
    
*   If an error is being addressed, the relevant error message should not be displayed when the field is active, however a check should still be done when the user tabs out of the field to ensure the error has been addressed.
    
*   When the user has addressed the error it should no longer appear.
    
*   If there are a number of data inputs on a page, consider whether to add a summary of errors panel so the user can see all errors listed in one place. More information on error summaries can be found [here.](https://design-system.service.gov.uk/components/error-summary/)
    
*   Errors and validation should be based on the previous fields the user has engaged with, not the whole form, unless they are submitting the Form. (See below)
    

### Tip

Further guidance on the display of errors and visual feedback within form fields has been outlined [here.](https://www.nngroup.com/articles/errors-forms-design-guidelines/)  
  
Credit: Nielsen Norman Group.

* * *

Call to actions/buttons
-----------------------

Having consistency across your site as to where call to actions appear means that users are comfortable with the action they are selecting and not making mistakes when submitting a form.

### Tip

Labeling call to actions effectively and contextually means that users understand the action they are taking or where they will be taken on selection of the CTA. (See example, if the user is midway through several steps, ‘Continue’ should be used rather than ‘Submit’ which feels like the end of a journey.)  
  
Contextual labelling also gives screen reader users confidence that they are performing the intended action.

### Positioning

[Buttons](/components/button/) should be displayed in order of importance from right to left, with the primary button on the right.  
  
However, avoid multiple submit buttons on forms whenever possible. If the form must have multiple submit buttons the primary action should come first (i.e: Primary: Continue/Submit, Secondary: Back/Cancel)  
  
There might be some cases where a support/help action is needed, it should be put as a tertiary action with a link button styling.  
  
On mobile, buttons should be centered and go full width, the ordering would then change from right to left to top to bottom.

This behaviour is already built into NewsKit as part of the button group component. When the button group is used in mobile breakpoints, the buttons become full width, change order and are fixed at the bottom of the viewport with a background to separate them from the page content.

### Visual treatment

Primary and secondary buttons should have a clear visual treatment to clearly differentiate their importance to the user. Tertiary buttons should be text links to avoid having 3 call to actions in a similar style.  
  
Different styles can also be applied to buttons when used in the right context to give visual aid for critical actions, for example, destructive flows like confirming cancellation, deleting account, revoking access, etc.

* * *

Auto - On focus
---------------

Automatically auto-focus the first field in your form. This makes it clear to the user which field they need to fill out first and also reduces the number of clicks/effort it takes to start filling out the form. There should also be a clear focus state so the user understands where their cursor is and what data they need to enter.

* * *

Accessibility
-------------

All forms should adhere to accessibility guidelines to ensure they are usable by all. There should be a visible label on each data entry type as well as hard coded instructions for users with screen readers.  
  
Any restrictions on data entry such as password credentials should be displayed on the page upfront, not once data has been entered.  
  
Full, up to date guidance on accessibility when designing forms can be found on the [WCAG website.](https://www.w3.org/WAI/tutorials/forms/)

* * *

Security & CAPTCHA
------------------

Security when capturing user data is imperative, however you still need to consider the user’s experience. CAPTCHA is a commonly used security feature whereby users have to enter text that’s displayed on screen or select required images to prove that they are not a robot.  
  
However there are simpler, more user friendly options that don’t disrupt the user experience as much and potentially lead to drop off. reCAPTCHA is a simpler form of security whereby a user just has to select a check box next to ‘I am not a robot’. This is much less disruptive to their experience so it is recommended.

### Tip

Consider placement. It’s important that reCAPTCHA is displayed at the end of a form and not half way. Displaying this randomly disrupts the flow of the form and can look like it’s not part of your site. Some login platforms such as Auth0 display the reCaptcha widget half way through the form as default and this should be avoided. (See example)

* * *

Help improve this page
----------------------

To help make sure this page is as useful as it can be, relevant and kept up to date with industry best practices, please get in touch to share your research findings, and contribute to this page.  
  
[Propose a change or contribution by suggesting a feature request.](https://github.com/newscorp-ghfb/newskit/issues/new/choose)

* * *

Address
=======

Use this pattern to collect a user's address.

[Learn more about address data capture](/patterns/forms/address/)

Address
=======

Use this pattern to collect a user's address.

[Learn more about address data capture](/patterns/forms/address/)