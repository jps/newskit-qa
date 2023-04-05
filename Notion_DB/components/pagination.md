Pagination | NewsKit design system

Navigation

Pagination
==========

Pagination lets users navigate through multiple pages.

Status
======

Supported

* * *

Introduced
==========

[v7.1.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v7.1.0)

* * *

[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-pagination--story-default)[View Design](https://www.figma.com/file/MkU4xtY2yPcCpfhzQCuSnK/v5.0-%F0%9F%9F%A2-NewsKit-component-library?node-id=13255%3A179266&t=YHF77CaB2nhMe5VH-0)

* * *

Anatomy
-------

The pagination contains 3 required elements and 5 optional elements.

Item

Name

Description

Component

Optional

* * *

Options
-------

The pagination has options that can be used to provide an appropriate experience for different use cases.

### First and last pagination item

Links to the first and last item.

### Truncation

Truncation can be applied when there are more items than the width allows. Ellipsis are used to indicate additional items. Double truncation is applied when the current item is separated from both the first and last item.

### Siblings

The main pagination items.

### Boundaries

Pagination items to the left and right of the siblings.

### Size

There are three sizes of pagination: small, medium, and large. The default is medium.

### First and last pagination item

Links to the first and last item.

### Truncation

Truncation can be applied when there are more items than the width allows. Ellipsis are used to indicate additional items. Double truncation is applied when the current item is separated from both the first and last item.

### Siblings

The main pagination items.

### Boundaries

Pagination items to the left and right of the siblings.

### Size

There are three sizes of pagination: small, medium, and large. The default is medium.

* * *

States
------

Pagination has the following states:

### Base

The default style before the user interacts with the pagination.

### Focus

Communicates that a user has highlighted a pagination item (e.g. via keyboard or voice).

### Hover

The pagination item changes style to let the user know it’s interactive.

### Active

The pagination item changes style to provide feedback to the user that it has been interacted with.

### Selected

The pagination item changes style to let the user know it is the current item that has been selected.

### Disabled

Communicates that a pagination item exists, but isn’t available in that scenario. Applies when the user has reached the first or last pagination item.

* * *

Usage
-----

The following guidance describes how and when to appropriately use the pagination component.

* * *

Use pagination when there are more than 25 results

This helps reduce cognitive load as the user is not overwhelmed with information.

* * *

Don’t split pagination over multiple lines

This can make pagination difficult for users to understand.

* * *

Do position pagination in a consistent place on each page

Pagination should appear in close proximity to the content, typically beneath the search results or listing.

* * *

Accessibility considerations
----------------------------

The Pagination has the following accessibility considerations:  
  

*   Pagination is structured using an unordered list. The nav element is labeled ‘pagination’, making it a navigation landmark so that it is easy to locate using assistive tools.
    

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

Pagination

The Pagination container component holds React content for its children

Props

Overrides

Name

Type

Default

Description

Required

From the Pagination props, it is possible to derive lastPage and selected props. This is something we do in the PaginationProviderContext that child components of Pagination can access. See [Storybook examples](https://storybook.newskit.co.uk/?path=/docs/components-pagination--story-default) for how to use the usePaginationContext hook in your custom components.  
  
For reference, these are all the values it returns. In practice, you would only need a few of them:  
`const { size, changePage, page, lastPage, pageSize, totalItems, buildHref } = usePaginationContext();`  
  
Most of these properties are also passed, for convenience, in the itemButton and itemDescription overrides that PaginationItems supports (to avoid the need to call the hook).  
  
If writing a custom input component, lastPage can be used to validate that an input page number is within a valid range and selected can be used to just override the selected item button.

Attribute

Type

Default

Description

Pagination items

The PaginationItems child component shows pagination item links with numbers. Override icon if you want to change the appearance of the truncation icon. Override itemButton/itemDescription if you want to change/extend the appearance of the generated buttons.

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

Pagination navigation items

The PaginationItemFirst, PaginationItemPrev, PaginationItemNext and PaginationItemLast child components all take no props and the same set of overrides. Override icon if you want to change the appearance of the navigation icon. The defaults for paginationfirstItem, paginationPrevItem, paginationNextItem and paginationLastItem all reference the paginationItem stylePreset.

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

Please refer to the [Button](/components/button/#component-api) page for full set of props that can be used as overrides for PaginationFirstItem, PaginationLastItem, PaginationNextItem and PaginationPrevItem.

Pagination list item

The PaginationListItem is a styled LI element that should be used inside any custom Pagination components you write.

Name

Type

Default

Description

Required

Pagination button

The PaginationButton is default item button implementation. It is based on the Button component, as that supports a lot of styling options. These props do not need to be supplied manually, they will be provided in the props of the itemButton function. Overrides passed into PaginationItems get turned into standard Button props before being passed into this component.

Name

Type

Default

Description

Required

Please refer to the [Button](/components/button/#component-api) page for the other props.  
  
The default PaginationButton can be overridden, or added to, by using the itemButton render prop in PaginationItems' overrides. Go to [Storybook examples](https://storybook.newskit.co.uk/?path=/docs/components-pagination--story-default) for code examples. The Variations in Input / Buttons with Input for Selected Item story is an advanced customisation example. It uses the itemButton function to render a custom component for selected items only. The normal items use the default PaginationButton.

Truncation icon defaults

Default overrides used by the truncation icon.

Attribute

Type

Default

Description

Pagination item description defaults

Default overrides used by the TextBlock-based itemDescription override in PaginationItems. It uses utilityBody instead of utilityButton fonts, to match the lighter weight of text inside input/dropdown custom components.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Unordered List



](/components/unordered-list/)

Unordered lists make blocks of related text easier to read, structuring information of equal value into manageable bulleted items.

[

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)