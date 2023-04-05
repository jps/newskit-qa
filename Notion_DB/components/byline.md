Byline | NewsKit design system

Text

Byline
======

A byline is a line of text that lists the authors of an article, with options to add author’s title, location and link.

Status
======

Supported

* * *

Introduced
==========

v0.18.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/byline)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-byline--story-byline-default)

* * *

Interactive demo
----------------

This demo lets you preview the byline component, its variations, and configuration options.

[Alex Lowe](https://www.thetimes.co.uk/profile/alex-lowe), Deputy Rugby Correspondent|

[Tom Knowles](https://www.thetimes.co.uk/profile/tom-knowles), West Coast Technology Reporter, London|

[David Aaronovitch](https://www.thetimes.co.uk/profile/david-aaronovitch), Columnist

Byline Data

author

href

title

author

href

title

location

author

href

title

Typography Preset OverridesDefaultutilityButton020

Style Preset OverridesDefaultinkPositiveinkNegative

    1import React from 'react';
    2import { Byline } from 'newskit';
    3
    4export default () => (
    5  <Byline
    6    bylineData={[
    7      {
    8        author: 'Alex Lowe',
    9        href:
    10          'https://www.thetimes.co.uk/profile/alex-lowe',
    11        title: 'Deputy Rugby Correspondent',
    12      },
    13      {
    14        author: 'Tom Knowles',
    15        href:
    16          'https://www.thetimes.co.uk/profile/tom-knowles',
    17        title: 'West Coast Technology Reporter',
    18        location: 'London',
    19      },
    20      {
    21        author: 'David Aaronovitch',
    22        href:
    23          'https://www.thetimes.co.uk/profile/david-aaronovitch',
    24        title: 'Columnist',
    25      },
    26    ]}
    27    overrides={{
    28      typographyPreset: 'utilityMeta020',
    29      link: { typographyPreset: 'utilityMeta020' },
    30      stylePreset: 'inkBase',
    31    }}
    32  />
    33);
    34
    

Edit on CodeSandbox

* * *

Anatomy
-------

The byline contains one required element and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The byline has options for different use cases:

### Author’s title

Option to add the author’s title, following their name.

### Author’s location

Option to add the author’s location, following their name and title.

### Divider

A vertical divider between each author allows visual separation.

### Link

If supplied, adds a link to the author’s name. This typically goes to the author’s page.  
  
If the link is external, the external link trailing icon is shown.

### Author’s title

Option to add the author’s title, following their name.

### Author’s location

Option to add the author’s location, following their name and title.

### Divider

A vertical divider between each author allows visual separation.

### Link

If supplied, adds a link to the author’s name. This typically goes to the author’s page.  
  
If the link is external, the external link trailing icon is shown.

* * *

Behaviours
----------

The following guidance describes how the byline behaves.

### Breaks responsively

When viewed responsively, the byline breaks onto a new line for each author.

### Breaks responsively

When viewed responsively, the byline breaks onto a new line for each author.

* * *

Accessibility considerations
----------------------------

The byline has the following accessibility considerations:

Focus order

Order

Element

Role

Keyboard Interactions

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

The byline has a range of props that can be used to define an appropriate experience for different use cases.

Byline

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