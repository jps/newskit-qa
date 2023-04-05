Fieldset | NewsKit design system

Layout

Fieldset
========

Fieldsets provide contextual information around a group of form controls in a web form.

Status
======

Supported

* * *

Introduced
==========

[v5.0.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.0.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/fieldset)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-fieldset--story-fieldset-default)

* * *

Anatomy
-------

The fieldset contains two required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The fieldset has options for different use cases:

### Legend

Title the group of elements in the fieldset with a caption.

### Size

The fieldset legend comes in small, medium and large. The default is medium.

You can customise the size of the legend, and any [form](/components/form/) selection controls, labels and assistive text, as required.

### Legend

Title the group of elements in the fieldset with a caption.

### Size

The fieldset legend comes in small, medium and large. The default is medium.

You can customise the size of the legend, and any [form](/components/form/) selection controls, labels and assistive text, as required.

* * *

States
------

The fieldset has the following states:

### Base

The default state.

### Disabled

Communicates that the grouped form selection controls exist, but aren’t available in that scenario. Disabled fieldsets maintain layout consistency in a form, and communicate that a form selection control may become available if another condition is met. The style of the legend (colour) changes to indicate that the form selection controls grouped with the fieldset are disabled.

* * *

Form structure
--------------

The diagram below shows how to use the fieldset to group form controls and wrap them with the form to apply validation:

* * *

Accessibility considerations
----------------------------

The fieldset has the following accessibility considerations:

Legend

The legend is a caption for a group of form controls. Use it to explain the function or purpose of the form controls.

Legends are important for users with screen readers. Screen readers will repeat the legend for each form control within a fieldset.

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

SEO
---

If you’re including an image inside the fieldset, ensure alt text is applied.

* * *

API
---

Fieldset

Props

Overrides

The fieldset has a range of props and overrides to define the experience in different use cases, and a range of predefined elements and attributes that you can override to define their appearance.

Name

Type

Default

Description

Required

The fieldset has a range of props and overrides to define the experience in different use cases, and a range of predefined elements and attributes that you can override to define their appearance.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Stack



](/components/stack/)

A low-level foundational component used to layout items in a horizontal or vertical stack.

[

### Structured List



](/components/structured-list/)

The Structured List is a layout component that groups similar or related content.

[

### Visibility



](/components/visibility/)

A pair of components which can be used to show and hide content at different breakpoints.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)