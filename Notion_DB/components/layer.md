Layer | NewsKit design system

Layout

Layer
=====

Layers allow for the stacking of components and other elements, giving control over how they interact together and appear to users.

Status
======

Supported

* * *

Introduced
==========

[v6.0.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v6.0.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/layer)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-layer--story-layer-default)

* * *

Overview
--------

Control over how different layers appear and interact together is important when building reusable components, as most modern user interfaces use layers to manage how components and other elements appear to users.  
  
Previously, the NewsKit design system utilised `z-index` to order component and element depth. However, we discovered that this approach did not work effectively when building and working with components due to the lack of control it afforded.  
  
Our solution allows for greater user control via the `LayerOrganizer` and `Layer` components which rely on the [stacking context and stacking order](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context) to achieve the same functionality, rather than the traditional `z-index`.

* * *

Layer organizer
---------------

The layer organizer is a provider-type component that needs to be added at the root level of your application. It creates a new stacking context and adds an extra `div` element to your application which will be used to host rendered layers. For example, the NewsKit [Modal](https://www.newskit.co.uk/components/modal/) , [Drawer](https://www.newskit.co.uk/components/drawer/) , or [Select](https://www.newskit.co.uk/components/select/) components will render inside that div element.  
  
You can nest multiple Layer organizers to create a new stacking context. Be aware that the Layer component will always render in the parent one.  
  

If you use `NewsKitProvider` you do not need to add a `LayerOrganizer` since it is already part of the `NewsKitProvider`.

  
  
  
  

Layer organizer interactive demo
--------------------------------

This demo lets you preview the layer organizer component, its variations and configuration options.

Render red layerTrueFalse

Render green layerTrueFalse

    1import React from 'react';
    2import { LayerOrganizer } from 'newskit';
    3
    4export default () => <LayerOrganizer />;
    5
    

Edit on CodeSandbox

* * *

Layer
-----

The layer component renders its children inside a host using `createPortal`. The host is the parent `LayerOrganizer`.  
  
With layers, there is no need for the [z-index CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) as layers completely rely on the stacking order within a `LayerOrganizer`.  
  
  
  

Layer interactive demo
----------------------

This demo lets you preview the layer component, its variations and configuration options.

Render blue layerTrueFalse

Render orange layerTrueFalse

    1import React from 'react';
    2import { Layer } from 'newskit';
    3
    4export default () => <Layer />;
    5
    

Edit on CodeSandbox

* * *

Usage
-----

The following guidance describes how and when to use layers.  
  

*   In general, try to avoid using `z-index` in your component-based application. If you need to have a `z-index` added to an element, make sure it is within an ordered stacking context. [Refer to MDN for more information on how to create a stacking context.](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context)
    
*   In order to support applications that have stacking contexts with `z-index` set to a value other than auto, `LayerOrganizer` and `NewsKitProvider` accept a `z-index` number. When a `z-index` value is passed, it will set it as a `z-index` value for all the layers within its context.
    
*   When using `LayerOrganizer` you do not need to set a default value. However, in some cases, you might have third-party libraries or components that use `z-index` where you may need to change the default `z-index` value equal to or greater than the highest `z-index` value of all top-level stacking contexts in your application (note this may be not the highest `z-index` value across your application).
    

z-indexes within separate stacking contexts are not compared, and children within a stacking context that goes last will overlay those with a higher `z-index`, but within a separate stacking context that goes earlier in the stacking order.

* * *

API
---

Layer organizer

The layer organizer has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

Layer

The layer has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

* * *

Related components
------------------

[

### Modal



](/components/modal/)

A Modal is a layout panel that presents critical information or requests users input without navigating away from the current page.

[

### Drawer



](/components/drawer/)

A layout panel that slides out the side of the screen revealing content like navigation or filters.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)