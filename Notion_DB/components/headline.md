Headline | NewsKit design system

Component

Headline
========

Headline is used to highlight the main point or category of the following text.

Status
======

Supported

* * *

Introduced
==========

v0.19.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/headline)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-headline--story-headline-default)

* * *

Interactive demo
----------------

This demo allows you to preview the headline component, its variations, and configuration options.

Kicker

Headline
========

Headline

Kicker

Heading as

Kicker as

    1import React from 'react';
    2import { Headline } from 'newskit';
    3
    4export default () => (
    5  <Headline
    6    kickerText="Kicker"
    7    headingAs="h1"
    8    kickerAs="span"
    9  >
    10    Headline
    11  </Headline>
    12);
    13
    

Edit on CodeSandbox

* * *

Anatomy
-------

The headline component contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The headline has options for different use cases.

### Heading level

The heading can be rendered as a different section heading level, as well as `<span>`.

### Kicker

Optional content can appear before the heading text and serve as an introduction.

### Heading level

The heading can be rendered as a different section heading level, as well as `<span>`.

### Kicker

Optional content can appear before the heading text and serve as an introduction.

Styling of both the heading and kicker elements of the headline component can be decoupled from the underlying `<h1>` to `<h6>` heading level.

* * *

Usage
-----

Here's how and when to use the headline:

* * *

Do use headlines to create a page hierarchy

Headlines should be used to create various levels of hierarchies between text on a page.

* * *

Accessibility considerations
----------------------------

### Correct heading level

Headings help define the main page structure and are necessary for screen reader users. It’s essential to set heading levels appropriately with this in mind.  
  
You should avoid the following practices:

*   Avoid skipping a heading level, e.g. having `<h1>` but missing `<h1>` on the same page. For example, if there are multiple cards on the same page, ensure you pass headings e.g. `As="h1"`, heading, `As="h2"`, heading,`As="h3"`, etc.
    
*   Avoid using multiple `<h1>` elements on one page or nesting multiple`<h1>` elements as this is not considered best practice semantically.
    

* * *

SEO
---

*   Heading text should be set at the correct semantic level (eg [`<h1> to <h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)) to enable crawlers to better index the page.
    
*   Kicker content text appears before the heading and so doesn’t get announced by screen reader devices with it not being included as part of the heading tag.
    

* * *

API
---

Headline

The headline has a range of props to define the experience in different use cases.

Props

Overrides

Name

Type

Default

Description

Required

The headline has a range of props to define the experience in different use cases.

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

[

### Byline



](/components/byline/)

A small line of text which lists the authors of an article, along with their titles if provided.

[

### Caption



](/components/caption/)

A sentence often added to an image or video to describe or explain what the image or video is showing.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)