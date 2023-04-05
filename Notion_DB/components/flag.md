Flag | NewsKit design system

Feedback & Status

Flag
====

A flag is a non-interactive visual indicator used to communicate status.

Status
======

Supported

* * *

Introduced
==========

v0.8.0

* * *

[View code](https://github.com/newscorp-ghfb/ncu-newskit/blob/develop/src/flag/flag.tsx)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-flag--story-flag-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=1952%3A2650)

* * *

Interactive demo
----------------

This demo allows you to preview the flag component, its variations, and configuration options.

Flag Content

Content

Flag SizeDefault (Small)MediumLarge

Style PresetDefaultflagSolidPositiveflagMinimalPositive

Typography PresetDefaultutilityLabel010label020

    1import React from 'react';
    2import { Flag } from 'newskit';
    3
    4export default () => <Flag size="small">Flag Content</Flag>;
    5
    

Edit on CodeSandbox

* * *

Anatomy
-------

The flag contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The flag has options that can be used to provide an appropriate experience for different use cases.

### Appearance

By default, there are two styles of flag; solid and minimal, with colours set in the theme to communicate status to the user, eg. negative (red for high priority), or positive (green for active).

### Size

There are three sizes of flag; small, medium, and large.

### Icons (leading & trailing)

Icons can be displayed in a flag and can be positioned either before (leading) or after (trailing) the label in the flag.

### Appearance

By default, there are two styles of flag; solid and minimal, with colours set in the theme to communicate status to the user, eg. negative (red for high priority), or positive (green for active).

### Size

There are three sizes of flag; small, medium, and large.

### Icons (leading & trailing)

Icons can be displayed in a flag and can be positioned either before (leading) or after (trailing) the label in the flag.

* * *

Usage
-----

Here’s how and when to use the flag:

* * *

Do use flags to draw attention

Use flags to draw attention to a new feature, piece of content, or status change that may be of particular interest to a user.

* * *

Don't use flags for categorisation

Avoid using flags for categorisation other than status. Consider using a [tag](/components/tag/) instead

* * *

Don't make flags interactive

Use flags as a non-interactive status indicator.

* * *

SEO considerations
------------------

*   Ensure icons have alt text applied.
    

* * *

API
---

Flag

Props

Overrides

The flag has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The flag has a range of predefined elements and attributes that can be overridden to define its appearance.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Tag



](/components/tag/)

Tags are used to classify content, typically using keywords.

[

### Toast



](/components/toast/)

A Toast communicates confirmation of an action or a low-priority message that does not need to completely interrupt the user experience.

[

### Banner



](/components/banner/)

Communicates essential information without blocking an experience.

[

### Inline Message



](/components/inline-message/)

An Inline message communicates contextual information. They are positioned inline, in close proximity to the element they are adding context to.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)