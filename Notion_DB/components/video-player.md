Video Player | NewsKit design system

Media

Video Player
============

The video player component allows a user to play and control video content.

Status
======

Supported

* * *

Introduced
==========

[v5.0.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.0.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/video-player)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-video-player-default--story-default-video-player)

* * *

The NewsKit video player component wraps the underlying [Brightcove player](https://player.support.brightcove.com/getting-started/index.html) that can be themed, by using [NewsKit design tokens](/theme/foundation/design-tokens/).

Anatomy
-------

In order to allow NewsKit consumers to display video content, the component is built on top of [Brightcove’s video player.](https://player.support.brightcove.com/getting-started/index.html)  
  
The subcomponents listed below can be enabled in the [Brightcove config file](https://player.support.brightcove.com/general/player-configuration-guide.html) passed to the video player component:

Item

Name

Description

Component

Optional

* * *

Layout examples
---------------

Default player

The following example shows the default video player layout option that can be assembled using the various available subcomponents of the Brightcove player. [View the example in Storybook](https://storybook.newskit.co.uk/?path=/docs/components-video-player-default--story-default-video-player).

Player in card

The video player can be used with other components to create more complex modules, such as a [card](/components/card/) to give context to the video being played. [View the examples in Storybook](https://storybook.newskit.co.uk/?path=/docs/components-video-player-default--story-default-video-player).

Code examples can be viewed in Storybook via the ‘Story’ tab in the addons panel.

For full details of all available Brightcove player subcomponents, and their respective options and behaviours, refer to the [Brightcove documentation](https://player.support.brightcove.com/index.html), and the [playerx GitHub repo](https://github.com/brightcove/playerx).

NewsKit allows users to customise the styling of the subcomponents of the Brightcove player, using [NewsKit design tokens](/theme/foundation/design-tokens/)  
  
Refer to the [Step-by-Step: Player Customization guide from Brightcove](https://player.support.brightcove.com/getting-started/step-step-player-customization.html) for details.

* * *

Accessibility considerations
----------------------------

The video player component meets the standards set out in the [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/) accessibility guidelines.  
  
Refer to the [Brightcove Player accessibility features](https://player.support.brightcove.com/general/brightcove-player-accessibility.html) for more information.

* * *

API
---

Video Player

The video player requires a `config` prop that can be used to define an appropriate experience for different use cases. This will then be passed to the underlying [Brightcove player](https://player.support.brightcove.com/getting-started/step-step-player-customization.html) .

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

### Audio Player



](/components/audio-player/)

The audio player component allows a user to play and control the playback of live and recorded audio content.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)