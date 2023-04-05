Tabs | NewsKit design system

Navigation

Tabs
====

Tabs let users switch between views within the same context.

Status
======

Supported

* * *

Introduced
==========

v0.20.1

* * *

[View code](https://github.com/newscorp-ghfb/newskit)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-tabs--story-tabs-distribution-start)[View Design](https://github.com/newscorp-ghfb/newskit)

* * *

Interactive demo
----------------

This demo lets you preview the tabs component, its variations and configuration options.

Now playing

Up next

Later

Stories of our Times | One remarkable story, told in depth, each day. Our daily news podcast takes you to the heart of the stories that matter, with exclusive access and reporting. Published for the start of your day and hosted by Manveen Rana and David Aaronovitch.

Red Box | News Podcast of the Year: Matt Chorley presents the best interviews, analysis and panel discussions from his Times Radio show. Listen live 10am-1pm Monday to Thursday.

Stories of our Times | One remarkable story, told in depth, each day. Our daily news podcast takes you to the heart of the stories that matter, with exclusive access and reporting. Published for the start of your day and hosted by Manveen Rana and David Aaronovitch.

Distributionstartgrowequal

Sizesmallmediumlarge

Space InlineDefaultspace040space060

Tab Bar Track WeightDefaultborderWidth030

Tab Bar Indicator WeightDefaultborderWidth030

Tab Bar Indicator sizeDefault75%sizing050

Style preset overridesDefaultcardContainer

dividerTrueFalse

verticalTrueFalse

initialSelectedIndex

Aligncenterstartend

Indicator Positionstartendnone

    1import React from 'react';
    2import { Tabs } from 'newskit';
    3
    4export default () => (
    5  <Tabs
    6    distribution="start"
    7    size="medium"
    8    overrides={{
    9      selectionIndicator: { track: {}, indicator: {} },
    10    }}
    11    initialSelectedIndex={0}
    12    align="center"
    13    indicatorPosition="end"
    14  />
    15);
    16
    

Edit on CodeSandbox

* * *

Anatomy
-------

Tabs contain four required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

Tabs have options for different use cases:

### Size

Tabs come in small, medium and large. Tab labels, icons and the tab container change size. Tabs match the heights of the three button sizes, so they align when used together.

### Icons (leading & trailing)

Add an icon to a tab item. Icons can be positioned either before (leading) or after (trailing) the tab label.

### Label

Add labels to tab items. A label can give more context to the content that will be displayed when the user selects a tab.

### Orientation

Display tabs horizontally or vertically.

### Indicator position

Display the tabs indicator on the bottom of the tab for the horizontal orientation and left or right of the tab for the vertical orientation.

### Indicator size

Change the size of the tab indicator to give more or less prominence, using either: full-width of the tab, fixed-width/fixed-height (based on orientation) or a percentage of the tab height/width (based on orientation).

### Indicator weight

Customise the weight of the tab indicator to give more or less affordance.

### Track weight

Customise the weight of the tab track to give more or less affordance.

### Dividers

Add dividers between tab items. Dividers match the width or height (depending on orientation) of the tab items.

### Distribution

*   Start  Aligns the tab items to the left of the content area for horizontal orientation (default) and to the top for vertical orientation. The width of the tab group is defined by the width of its children.
    
*   Grow Spreads all tab items across the content area, filling the entire available width or height, depending on the orientation. The width of each tab item is defined by its content.
    
*   Equal Spaces each tab item across the content area equally, regardless of the width or height of its children.
    

### Alignment

*   Start Aligns the tab item label and icons to the left.
    
*   Center Centres the tab item label and icons.
    
*   End Aligns the tab item label and icons to the right.
    

The default alignment depends on the orientation. When tabs are vertical it’s Start and when tabs are horizontal it’s Center.

### Size

Tabs come in small, medium and large. Tab labels, icons and the tab container change size. Tabs match the heights of the three button sizes, so they align when used together.

### Icons (leading & trailing)

Add an icon to a tab item. Icons can be positioned either before (leading) or after (trailing) the tab label.

### Label

Add labels to tab items. A label can give more context to the content that will be displayed when the user selects a tab.

### Orientation

Display tabs horizontally or vertically.

### Indicator position

Display the tabs indicator on the bottom of the tab for the horizontal orientation and left or right of the tab for the vertical orientation.

### Indicator size

Change the size of the tab indicator to give more or less prominence, using either: full-width of the tab, fixed-width/fixed-height (based on orientation) or a percentage of the tab height/width (based on orientation).

### Indicator weight

Customise the weight of the tab indicator to give more or less affordance.

### Track weight

Customise the weight of the tab track to give more or less affordance.

### Dividers

Add dividers between tab items. Dividers match the width or height (depending on orientation) of the tab items.

### Distribution

*   Start  Aligns the tab items to the left of the content area for horizontal orientation (default) and to the top for vertical orientation. The width of the tab group is defined by the width of its children.
    
*   Grow Spreads all tab items across the content area, filling the entire available width or height, depending on the orientation. The width of each tab item is defined by its content.
    
*   Equal Spaces each tab item across the content area equally, regardless of the width or height of its children.
    

### Alignment

*   Start Aligns the tab item label and icons to the left.
    
*   Center Centres the tab item label and icons.
    
*   End Aligns the tab item label and icons to the right.
    

The default alignment depends on the orientation. When tabs are vertical it’s Start and when tabs are horizontal it’s Center.

* * *

States
------

Tabs have the following states. By default, tabs have one tab item in a selected state.

### Base

The default style before the user interacts with the tab item.

### Hover

The tab item changes style to let the user know it’s interactive.

### Active

The tab item changes style to let the user know they’ve interacted with it.

### Selected

The tab item changes style to let the user know they’ve selected it.

### Disabled

Communicates that a tab item exists, but isn’t available in that scenario. When the user hovers over a tab item in a disabled state, the cursor shows as ‘not allowed’.  
  
Disabled tab items maintain layout consistency and communicate that a tab item may become available if another condition is met.

### Focus

Communicates that a tab item exists, but isn’t available in that scenario. When the user hovers over a tab item in a disabled state, the cursor shows as ‘not allowed’.

* * *

Behaviours
----------

Here’s how tabs behave:

### Animation

When the user selects a tab item, the indicator slides along the track of the tabs to the newly selected tab item. At the time of selection, the tabs content changes immediately.

### Selected

The user can only select one tab item at a time. This property changes an individual tab item’s selected state.

### Tabs overflow

When there are too many tabs to fit horizontally across the viewport, a scroll component is applied. On desktop, the controls (buttons) are rendered on the scroll.

### Label overflow wrap

When the label in a tab item is too long for the available horizontal space, it wraps to form another line.

### Animation

When the user selects a tab item, the indicator slides along the track of the tabs to the newly selected tab item. At the time of selection, the tabs content changes immediately.

### Selected

The user can only select one tab item at a time. This property changes an individual tab item’s selected state.

### Tabs overflow

When there are too many tabs to fit horizontally across the viewport, a scroll component is applied. On desktop, the controls (buttons) are rendered on the scroll.

### Label overflow wrap

When the label in a tab item is too long for the available horizontal space, it wraps to form another line.

* * *

Usage
-----

Here’s how and when to use tabs:

* * *

Do use tabs to switch between views

Use tabs to let users alternate between views within the same context.

* * *

Don’t truncate tab labels

Tab item labels shouldn’t be truncated. Keep them short, clear and fully visible.

* * *

Do use when there are two or more content views

Use tabs when users have two or more content views to choose from.

* * *

Don’t nest tabs

Avoid nesting tabs as this can cause usability issues. Consider an alternative component (e.g. accordion) or rethink the page structure.

* * *

Do use sentence case for labels

Tab labels should be written in sentence case to help with scannability and legibility.

* * *

Don’t use more than 5 tabs

Avoid using tabs when there are five or more content views. Consider an alternative component (e.g. select) to reduce the user’s cognitive load.

* * *

Do keep tabs in view of the content

Tabs should remain in view of the content. If the content is too large to display with the tabs in the same viewport, make the tabs fixed (sticky).

* * *

Don’t mix tabs with and without icons

Avoid mixing tab items that include an icon with those that don’t include an icon. This helps ensure they have equal importance.

* * *

Do use vertical orientation when space is limited

Use the vertical orientation when there are more than five tabs and horizontal space is limited.

* * *

Don’t use tabs to navigate to different pages

Avoid using tabs to navigate to different pages and anchoring to different sections on a page. Use a navigation component (e.g. link) instead.

* * *

Accessibility considerations
----------------------------

Tabs implement the latest [WAI-ARIA Tabs specifications](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/Tab_Role).

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

By default, aria-label will match the tab text label. Where a tab item text label is not visible on the screen (i.e. if there’s only an icon in a tab item) a string should be passed to the title prop on the icon.

* * *

SEO considerations
------------------

Ensure icons have alt text applied.

* * *

API
---

Tabs have a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define their appearance.

Tabs

Props

Overrides

Name

Type

Default

Description

Required

To support resizing of the selected tab indicator this component uses the ResizeObserver API this is not supported in Internet explorer, if you require support we suggest you add a pollyfill to your application.

Attribute

Type

Default

Description

Tab

A tab has a range of props for different use cases, and a range of predefined elements and attributes that can be overridden to define its appearance.

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

### Accordion



](/components/accordion/)

Accordions show and hide related content. Use them to break up long pages into segmented, prioritised sections.

[

### Link



](/components/link/)

Links allow users to navigate to a new location or to additional information.

[

### Menu



](/components/menu/)

A Menu displays a list of navigational items. They are displayed either at the top of a screen, or at the side where space allows.

[

### Tag



](/components/tag/)

Tags are used to classify content, typically using keywords.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)