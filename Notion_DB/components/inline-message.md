Inline Message | NewsKit design system

Feedback & Status

Inline message
==============

Inline messages communicate contextual information. They’re positioned inline, close to the element they’re adding context to.

Status
======

Supported

* * *

Introduced
==========

v3.3.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/inline-message)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-inline-message--story-inline-message-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=3826%3A144444&t=ysdLVMGI1BOxtCPo-0)

* * *

Interactive demo
----------------

This demo lets you preview the inline message component, its variations and configuration options.

InlineMessage title

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Intentinformativenegative

IconUnsetWith Icon

Title

Message

    1import React from 'react';
    2import { InlineMessage } from 'newskit';
    3
    4export default () => (
    5  <InlineMessage
    6    overrides={{ stylePreset: 'inlineMessageInformative' }}
    7    icon="your icon here"
    8    title="InlineMessage title"
    9  >
    10    InlineMessage's message will display here
    11  </InlineMessage>
    12);
    13
    

Edit on CodeSandbox

* * *

Anatomy
-------

The inline message component contains one required element and two optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The inline message has options for different use cases:

### Intent

An inline message has two intents: informative and negative. Each communicates a specific tone to the user.

### Icon

Display an icon as a visual cue and help users with colour blindness discern the message tone.

### Title

Give the inline message a title to provide more context.

### Intent

An inline message has two intents: informative and negative. Each communicates a specific tone to the user.

### Icon

Display an icon as a visual cue and help users with colour blindness discern the message tone.

### Title

Give the inline message a title to provide more context.

* * *

Behaviours
----------

Here’s how the inline message behaves:

### Text overflow wrap

When the title and/or message in the inline message is too long for the available horizontal space, it wraps to form another line.

### Text overflow wrap

When the title and/or message in the inline message is too long for the available horizontal space, it wraps to form another line.

* * *

Usage
-----

Here’s how and when to use the inline message:

* * *

Do use inline messages to give context

Use an inline message to provide additional context or supporting information to a particular UI element or function (e.g. delivery terms within a delivery address form).

* * *

Don’t use for critical messages

Avoid using inline messages for critical system-level messages such as errors (e.g. loss of functionality). For critical messages, a component that partially or fully interrupts the user experience is more appropriate (e.g. banner or modal).

* * *

Don’t use to add context to a single input

Avoid using inline messages to add context to a single input (e.g. text input). Use assistive text instead.

* * *

Don't use multiple inline messages on a screen

Think carefully before including more than one inline message per screen, as they can increase a user’s cognitive load and become less effective in drawing attention to content.

* * *

Accessibility considerations
----------------------------

The inline message meets accessibility best practices from the W3C guidelines.

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

API
---

The inline message has a range of props and overrides to define the experience in different use cases, and a range of predefined elements and attributes that you can override to define its appearance.

Inline message

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

### Banner



](/components/banner/)

Communicates essential information without blocking an experience.

[

### Flag



](/components/flag/)

A flag is a non-interactive visual indicator used to communicate status.

[

### Toast



](/components/toast/)

A Toast communicates confirmation of an action or a low-priority message that does not need to completely interrupt the user experience.

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