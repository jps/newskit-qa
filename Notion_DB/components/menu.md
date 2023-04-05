Menu | NewsKit design system

Navigation

Menu
====

A menu displays a list of navigational items. They are displayed either at the top of a screen, or at the side where space allows.

Status
======

Supported

* * *

Introduced
==========

v3.3.0

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/menu)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-menu--story-menu-default)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=2984%3A966&t=eurTjmEaa1UxGH2d-0)

* * *

Interactive demo
----------------

This demo lets you preview the menu component, its variations and configuration options.

Sizesmallmediumlarge

verticalTrueFalse

Aligncenterstartend

Space InlineDefaultspace050

    1import React from 'react';
    2import { Menu } from 'newskit';
    3
    4export default () => (
    5  <Menu size="medium" align="center" overrides={{}} />
    6);
    7
    

Edit on CodeSandbox

* * *

Anatomy
-------

Menu

The menu contains one required element and three optional elements.

Item

Name

Description

Component

Optional

Sub menu

The sub menu contains three required elements and one optional element.

Item

Name

Description

Component

Optional

* * *

Options
-------

The menu has options for different use cases:

### Orientation

Display the menu and sub menu horizontally or vertically.

### Title

Add a title to a menu item group to categorise its menu items. Only available when the menu is in a vertical orientation.

### Divider

Add a divider between menu items, or as the last element between menu groups.

### Icons (leading & trailing)

Add an icon to a menu item, sub menu item, or menu item group title. Icons can be positioned either before (leading) or after (trailing) the label.

### Alignment

*   Center: Centres the menu item and sub menu item label and icon
    
*   Start: Aligns the menu item and sub menu item label and icons to the left
    
*   End: Aligns the menu item and sub menu item label and icons to the right
    

Default value depends on the vertical prop. When set to ‘true’, the value is set to MenuItemAlign.Start. When set to ‘false’, the value is set to MenuAlign.Center.

### Size

Menu items and sub menu itms come in small, medium and large. Labels, icons and the menu container change size. The menu matches the heights of the three button sizes, so they align when used together.

### Style

There are three default styles based on the menus orientation and application:

*   menuItemVertical is the default style applied when the menu is in a vertical orientation
    
*   menuItemHorizonal is the default style applied when the menu is in a horizontal orientation
    
*   menuItemHorizontalInverse is the default style applied when the menu is in a horizontal orientation on contrasting background colour
    

### Sub menu trigger

A sub menu can be triggered to be open or closed via click.

### Orientation

Display the menu and sub menu horizontally or vertically.

### Title

Add a title to a menu item group to categorise its menu items. Only available when the menu is in a vertical orientation.

### Divider

Add a divider between menu items, or as the last element between menu groups.

### Icons (leading & trailing)

Add an icon to a menu item, sub menu item, or menu item group title. Icons can be positioned either before (leading) or after (trailing) the label.

### Alignment

*   Center: Centres the menu item and sub menu item label and icon
    
*   Start: Aligns the menu item and sub menu item label and icons to the left
    
*   End: Aligns the menu item and sub menu item label and icons to the right
    

Default value depends on the vertical prop. When set to ‘true’, the value is set to MenuItemAlign.Start. When set to ‘false’, the value is set to MenuAlign.Center.

### Size

Menu items and sub menu itms come in small, medium and large. Labels, icons and the menu container change size. The menu matches the heights of the three button sizes, so they align when used together.

### Style

There are three default styles based on the menus orientation and application:

*   menuItemVertical is the default style applied when the menu is in a vertical orientation
    
*   menuItemHorizonal is the default style applied when the menu is in a horizontal orientation
    
*   menuItemHorizontalInverse is the default style applied when the menu is in a horizontal orientation on contrasting background colour
    

### Sub menu trigger

A sub menu can be triggered to be open or closed via click.

* * *

States
------

The menu has the following states. By default, a menu has one menu item in a selected state.

### Base

The default style before the user interacts with the menu.

### Hover

The menu changes style to let the user know it’s interactive.

### Active

The menu item changes style to let the user know they’ve interacted with it.

### Disabled

Communicates that a menu item exists, but isn’t available in that scenario. When the user hovers over a menu item in a disabled state, the cursor shows as ‘not allowed’.  
  
Disabled menu items maintain layout consistency and communicate that a menu item may become available if another condition is met.

### Focus

Communicates that a user has highlighted a menu item (e.g. via keyboard or voice).

### Selected

The menu item changes style to let the user know they’ve selected it.

* * *

Behaviours
----------

Here’s how the menu behaves:

### Width and Height

A menu is 100% width and height, therefore if a specific width or height is required a parent container will control this.

### Transitions

When the user hovers over a menu item, the style transitions from one state to another.

### Selected

The user can only select one menu item at a time.

### Label Overflow

When the label in a menu item or menu item group title is too long for the available horizontal space, it wraps to form another line.

### Sub menu item toggle

Menu items with a sub menu attributed to them toggle the sub menu open or closed.  
  
The sub menu is opened by a script when the user activates the top-level item and closed when the focus leaves the sub menu.

### Width and Height

A menu is 100% width and height, therefore if a specific width or height is required a parent container will control this.

### Transitions

When the user hovers over a menu item, the style transitions from one state to another.

### Selected

The user can only select one menu item at a time.

### Label Overflow

When the label in a menu item or menu item group title is too long for the available horizontal space, it wraps to form another line.

### Sub menu item toggle

Menu items with a sub menu attributed to them toggle the sub menu open or closed.  
  
The sub menu is opened by a script when the user activates the top-level item and closed when the focus leaves the sub menu.

* * *

Usage
-----

Here’s how and when to use the menu:

* * *

Do use sentence case for labels

Write menu item labels in sentence case to help with scannability and legibility.

* * *

Do use for top-level sections and subsections

Use a menu for navigating to different top-level sections or subsections.

* * *

Do limit the number of items in a menu

Think carefully about the number of items in a menu. Too many items can hurt readability and increase the user’s cognitive load.

* * *

Do use sub menus for multi-level navigation

Use a sub menu to display multiple levels of navigation items.

* * *

Accessibility considerations
----------------------------

The menu implements the latest [WAI-ARIA Menu specifications.](https://www.w3.org/WAI/tutorials/menus/)  
  
Indicate navigation menu items with sub menus visually and using markup.

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

SEO considerations
------------------

The rendered menu is built using a native HTML nav element so information can be crawled and indexed by search engines. Give navigational items clear, descriptive titles to allow crawlers to correctly identify content.

* * *

API
---

There are props on the four components that combine to form the menu component (menu item group, sub menu, menu item, and menu divider).

Menu

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

Menu item group

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

Menu item

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

Menu Divider

Attribute

Type

Default

Description

Sub menu

Props

Overrides

Name

Type

Default

Description

Required

Please refer to the menu item for details of the props and other overrides.

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

### Tabs



](/components/tabs/)

Allows users to alternate between views within the same context.

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