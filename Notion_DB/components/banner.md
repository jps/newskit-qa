Banner | NewsKit design system

Feedback & Status

Banner
======

Banners communicate essential information. They’re positioned at the top of the screen to be noticeable and require user action to disappear.

Status
======

Supported

* * *

Introduced
==========

v3.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/banner)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-banner--story-banner-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2163%3A45665&t=FbJDxZalohOA9JXM-0)

* * *

Interactive demo
----------------

This demo lets you preview the banner component, its variations and configuration options.

Banner title

Banner message will display in this space

Banner title

Banner message will display in this space

IntentInformativeNoticeNegative

IconWith IconUnset

Title

Message

ActionsUnsetWith Actions

Close buttonUnsetWith close button

    1import React from 'react';
    2import { Banner } from 'newskit';
    3
    4export default () => (
    5  <Banner
    6    overrides={{ stylePreset: 'bannerInformative' }}
    7    icon="your icon here"
    8    title="Banner title"
    9    actions="your actions here"
    10  >
    11    Banner message will display in this space
    12  </Banner>
    13);
    14
    

Edit on CodeSandbox

* * *

Anatomy
-------

The banner component contains one required element and three optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The banner has options for different use cases:

### Orientation

Display banners horizontally or vertically to best use the space available on a screen. When vertical, stack content and make buttons full-width.

### Intent

A banner has three intents: informative, notice and negative. Each communicates a specific tone to the user.

### Icon

Display an icon as a visual cue and help users with colour blindness discern the message tone.

### Title

Give the banner a title to provide extra context.

### Actionable

Add a call-to-action (CTA) button with a contextual message as a starting point in a user journey.

### Dismissible

Add a close button to let users dismiss the banner.

### Orientation

Display banners horizontally or vertically to best use the space available on a screen. When vertical, stack content and make buttons full-width.

### Intent

A banner has three intents: informative, notice and negative. Each communicates a specific tone to the user.

### Icon

Display an icon as a visual cue and help users with colour blindness discern the message tone.

### Title

Give the banner a title to provide extra context.

### Actionable

Add a call-to-action (CTA) button with a contextual message as a starting point in a user journey.

### Dismissible

Add a close button to let users dismiss the banner.

* * *

Behaviours
----------

Here’s how the banner behaves:

### Text overflow wrap

When the title and/or message in the banner is too long for the available horizontal space, it wraps to form another line.

### Text overflow wrap

When the title and/or message in the banner is too long for the available horizontal space, it wraps to form another line.

* * *

Usage
-----

Here’s how and when to use the banner:

* * *

Do use banners for essential, system-level information

Examples include internet connection issues, expirations of subscriptions, payment failures or major product changes. For confirmations of actions or promotional messages, use another feedback component (e.g. toast) instead.

* * *

Don’t show multiple banners at the same time

Banners should appear in order of importance.

* * *

Do add an action to help users solve the issue

Whenever possible, add an action in the banner so the user can quickly resolve the issue.

* * *

Don’t have more than one action in a banner

Having more than one action to choose from can make it difficult for users to decide what to do next. This doesn’t include the close button.

* * *

Do position below the navigation header

Banners should be positioned at the top of a page, below the navigation header.

* * *

Don’t let banners time out

Banners should only disappear on user interaction (dismissing or completing a task) or when the information is no longer relevant (e.g. updating failed payment details).

* * *

Do convey tone with the right intent

Use the appropriate intent to convey the tone of the banner message. If the tone is neutral, use the informative intent banner.

* * *

Do display again if unresolved

If a user dismisses a banner without resolving the issue, display it again at the next possible occasion, without overwhelming the user (e.g. the next time session).

* * *

Accessibility considerations
----------------------------

The banner meets the latest WAI-ARIA banner specifications.

Focus order

Order

Element

Role

WAI-ARIA

Element

Attribute

Value

Description

User supplied

* * *

SEO considerations
------------------

There are no SEO considerations for the banner.

* * *

API
---

The banner has a range of props to define the experience in different use cases.

Banner

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

### Toast



](/components/toast/)

A Toast communicates confirmation of an action or a low-priority message that does not need to completely interrupt the user experience.

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