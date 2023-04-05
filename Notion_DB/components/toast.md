Toast | NewsKit design system

Feedback & Status

Toast
=====

Toasts communicate confirmation of an action or a low-priority message.

Status
======

Supported

* * *

Introduced
==========

v3.3.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/toast)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-toast--story-toast-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2289%3A310&t=9INLWlTCXpYsQH6O-0)

* * *

Interactive demo
----------------

This demo lets you preview the toast component, its variations and configuration options.

Toast title

Toast message will display here

* * *

undo

Intentneutralinformativenoticepositivenegative

IconUnsetWith Icon

Title

Message

ActionsUnsetWith Actions

    1import React from 'react';
    2import { Toast } from 'newskit';
    3
    4export default () => (
    5  <Toast
    6    icon="your icon here"
    7    title="Toast title"
    8    actions="your actions here"
    9  >
    10    Toast message will display here
    11  </Toast>
    12);
    13
    

Edit on CodeSandbox

* * *

Anatomy
-------

The toast component contains one required element and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The toast has options for different use cases:

### Intent

The toast has five intents: neutral, informative, notice, positive and negative. Each intent communicates a specific tone to the user.

### Icon

Add an icon to the toast to indicate status or intent. This also helps users who are colour blind discern the message tone.

### Title

Add a title to the toast to give the message extra context.

### Actionable

Add a call-to-action (CTA) button with a contextual label to the toast to give the user the option to perform another action relevant to the one just taken (e.g. ‘undo’).

### Auto-hide duration

Increase or decrease how long the toast is displayed before automatically hiding, to give the user an appropriate amount of time to read the message.

### Position

Position the toast to appear and hide from the following positions on the screen: top-left, top-centre, top-right, bottom-left, bottom-centre and bottom-right.

### Offset

Give the toast an offset to create space from the horizontal and/or vertical edge of the screen.

### Intent

The toast has five intents: neutral, informative, notice, positive and negative. Each intent communicates a specific tone to the user.

### Icon

Add an icon to the toast to indicate status or intent. This also helps users who are colour blind discern the message tone.

### Title

Add a title to the toast to give the message extra context.

### Actionable

Add a call-to-action (CTA) button with a contextual label to the toast to give the user the option to perform another action relevant to the one just taken (e.g. ‘undo’).

### Auto-hide duration

Increase or decrease how long the toast is displayed before automatically hiding, to give the user an appropriate amount of time to read the message.

### Position

Position the toast to appear and hide from the following positions on the screen: top-left, top-centre, top-right, bottom-left, bottom-centre and bottom-right.

### Offset

Give the toast an offset to create space from the horizontal and/or vertical edge of the screen.

* * *

Behaviours
----------

Here’s how the toast behaves:

### Text overflow wrap

When the title and/or the message in the toast is too long for the available horizontal space, it wraps to form another line.

### Multi toast

Display multiple toasts at the same time using a queue system (toast provider).

### Persist on interaction

When the toast is in a hover or focus state, it doesn’t auto-hide (pause). When the toast is no longer in a hover or focus state, the timer starts from where it left off (unpause).

### Text overflow wrap

When the title and/or the message in the toast is too long for the available horizontal space, it wraps to form another line.

### Multi toast

Display multiple toasts at the same time using a queue system (toast provider).

### Persist on interaction

When the toast is in a hover or focus state, it doesn’t auto-hide (pause). When the toast is no longer in a hover or focus state, the timer starts from where it left off (unpause).

* * *

Usage
-----

Here’s how and when to use the toast:

* * *

Do use for confirmation and low-priority messages

Use a toast to communicate confirmation of an action or a low-priority message that doesn’t need to completely interrupt the user’s experience.

* * *

Don’t place a toast over navigation

Avoid placing a toast over navigation as this may block user interaction.

* * *

Do avoid clashes with other components

Consider the placement of a toast in relation to other user feedback components (e.g. banners) to avoid clashes.

* * *

Don’t use toasts for multiple actions

Avoid displaying more than one action in a toast. Having more than one action to choose from can make it difficult for the user to decide to do next.

* * *

Do offset from the edge of the screen

Always have offset (space) from the edge of the screen to the toast.

* * *

Don’t show multiple toasts

Avoid displaying more than one toast where possible. Where applicable, update the content of the current toast instead (e.g. “Article saved. ‘Undo’” to “Article removed”).

* * *

Accessibility considerations
----------------------------

The toast meets accessibility best practices from the W3C guidelines.

Focus order

Order

Element

Role

Keyboard interactions

Command

Description

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

API
---

Toast

The toast has a range of props to define the experience in different use cases.

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

ToastProvider

Name

Type

Default

Description

Required

toast() function

Invoke this function to display a toast. Returns a toast ID.

Argument

Type

Default

Description

Required

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

### Inline Message



](/components/inline-message/)

An Inline message communicates contextual information. They are positioned inline, in close proximity to the element they are adding context to.

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