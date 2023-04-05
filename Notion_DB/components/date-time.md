Date Time | NewsKit design system

Text

Date Time
=========

The date time component is a styled, HTML5 time element for displaying date and time.

Status
======

Supported

* * *

Introduced
==========

v0.18.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/date-time)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-date-time--story-date-time-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2057%3A5&t=iP77Jd8O6cCJYM4p-1)

* * *

Interactive demo
----------------

This demo lets you preview the date time component, its variations, and configuration options.

Updated: July 1 2017, 2:32pm, The Times

Date

Date format

Date Time Prefix

Suffix

Date Time StylePresetDefaultinkBrand010inkPositive

Date Time TypographyPresetDefaultutilityMeta010

Prefix StylePresetDefaultinkBrand010inkPositive

Prefix TypographyPresetDefaultutilityMeta010

Suffix StylePresetDefaultinkBrand010inkPositive

Suffix TypographyPresetDefaultutilityMeta010

    1import React from 'react';
    2import { DateTime } from 'newskit';
    3
    4export default () => (
    5  <DateTime
    6    date="2017-07-01T14:32:00.000Z"
    7    dateFormat="MMMM d yyyy, h:mmaaaaa'm'"
    8    prefix="Updated: "
    9    suffix="The Times"
    10    overrides={{ prefix: {}, suffix: {} }}
    11  />
    12);
    13
    

Edit on CodeSandbox

* * *

Anatomy
-------

Date time contains one required element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The date time has options for different use cases:

### Prefix

Text placed in front of the date and time, separated by a space.

### Suffix

Text placed after the date and time, separated by a comma and a space.

### Date and time format

Specify a format for displaying the date and time. See [date-fns docs](https://date-fns.org/v2.6.0/docs/format)for the available settings.

### Prefix

Text placed in front of the date and time, separated by a space.

### Suffix

Text placed after the date and time, separated by a comma and a space.

### Date and time format

Specify a format for displaying the date and time. See [date-fns docs](https://date-fns.org/v2.6.0/docs/format)for the available settings.

* * *

Usage
-----

Here’s how and when to use the date time component:

* * *

Do consider the appropriate format for your users

In British English, the month follows the day. In American English, the month precedes the day.

* * *

Accessibility considerations
----------------------------

The Date Time component is wrapped in an [HTML5 time](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time) element. The date prop provided is passed into its `datetime` attribute to make the date displayed fully accessible.

* * *

API
---

Date Time

Props

Overrides

Date time has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

Date Time has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Text Block



](/components/text-block/)

Text block provides a simple way to display text. It supports text cropping, style presets, and typography presets.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)