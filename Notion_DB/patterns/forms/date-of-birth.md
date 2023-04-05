Date of birth | NewsKit design system

Forms

Date of birth
=============

Ask for a user’s date of birth when we need to validate the user’s age. This should not be collected unless you have a need for it to validate a user’s age or benefit them in some way.

* * *

How to ask for a user’s date of birth
-------------------------------------

Date of birth is sensitive information and should only be collected when there is a business need.

### Labelling

Date of birth should be labelled as ‘Date of birth’, not abbreviated to ‘D.O.B’ as this could lead to confusion.  
  
You should clearly state why you are collecting this information as it is not always a requirement so you will need to have a specific reason.

### Data entry format

The preferred format for date of birth is a text entry field per date type i.e day/month/year. This is simpler than scrolling through a drop down and minimises users selecting a random date from the drop down. - See research on [GOV.UK](https://designnotes.blog.gov.uk/2013/12/05/asking-for-a-date-of-birth/)  
  
Date format should be day/month/year i.e 12 - 05 - 1983 as this is the most common format.

### Auto-tab

As there are 3 fields to fill out for date of birth, the field should auto-tab to the next field once the relevant number of digits have been entered. This saves users time and effort selecting each field individually.

#### Do

*   Default to the numeric keyboard when on mobile. (Use using the 'type="number"' attribute).
    
*   Split out each date field, not rely on users entering a forward slash or hyphen.
    
*   Collect 4 digits for the year as year of birth now crosses between 1900’s/2000’s.
    
*   Allow autofill so the user can easily fill out this form based on saved personal data on their device.
    
*   Show hint text so the user understands the date format they need to enter.
    

#### Don’t

*   Use a date picker for date of birth.
    
*   Use a drop down for year of birth.
    
*   Mix text input and drop downs.
    

### Error state variants

Please enter your date of birth (If left empty)  
  
Please enter your full date of birth (If some fields are left empty)  
  
Please enter a valid date of birth (If non-numeric characters are entered on desktop or a date of birth is entered outside of a set criteria)

* * *

Help improve this page
----------------------

To help make sure this page is as useful as it can be, relevant and kept up to date with industry best practices, please get in touch to share your research findings, and contribute to this page.  
  
[Propose a change or contribution by suggesting a feature request.](https://github.com/newscorp-ghfb/newskit/issues/new/choose)

* * *

Date picker
===========

Use a date picker when capturing a date that is in the future like a delivery or a booking.

[Learn more about capturing dates](/patterns/forms/date-picker/)

Date picker
===========

Use a date picker when capturing a date that is in the future like a delivery or a booking.

[Learn more about capturing dates](/patterns/forms/date-picker/)