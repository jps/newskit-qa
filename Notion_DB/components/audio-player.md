Audio Player | NewsKit design system

Media

Audio Player
============

The audio player component allows a user to play and control the playback of live and recorded audio content.

Status
======

Supported

* * *

Introduced
==========

[v5.3.0](https://github.com/newscorp-ghfb/newskit/releases/tag/v5.3.0)

* * *

[View code](https://github.com/newscorp-ghfb/newskit/tree/main/src/audio-player-composable)[View Storybook](https://storybook.newskit.co.uk/?path=/docs/components-audio-player-composable--story-audio-player)[View Design](https://www.figma.com/file/FSbCQa6SzVR3K48ZWLeD77/%F0%9F%9F%A2-NK-Web-Components?node-id=324%3A3)

* * *

Anatomy
-------

Audio player composable

The audio player composable is responsible for maintaining the audio player state, and receiving interactions from subcomponents, and contains the non-visual audio element. It is the wrapper for the subcomponents listed below:

Item

Name

Description

Component

Optional

Volume control

The volume control contains one required element and one optional element.

Item

Name

Description

Component

Optional

Playback speed control

The Playback speed control contains two required elements and no optional elements.

Item

Name

Description

Component

Optional

* * *

Layout examples
---------------

Full player

The following example shows the full audio player layout option that can be assembled using the various available subcomponents. [View examples in Storybook.](https://storybook.newskit.co.uk/?path=/docs/components-audio-player-composable--story-audio-player)

Inline player

Use an inline audio player for simple inline playback e.g. within an article. [View examples in Storybook.](https://storybook.newskit.co.uk/?path=/docs/components-audio-player-composable--story-audio-player)

Player in card

The audio player can be used with other components to create more complex modules, such as a [card](/components/card/), to give context to the track or show being played. [View examples in Storybook.](https://storybook.newskit.co.uk/?path=/docs/components-audio-player-composable--story-audio-player)

Code examples can be viewed in [Storybook](https://storybook.newskit.co.uk/?path=/docs/components-audio-player-composable--story-audio-player) via the ‘Story’ tab in the addons panel.

* * *

Options
-------

The audio player has options that can be used to provide an appropriate experience for different use cases.

### Live

The live functionality is used for streaming live audio content  
  
Live streaming audio can be indicated by providing a [flag](/components/flag/) component with text and icon to communicate this to users.

### Recorded

The recorded functionality is used for streaming recorded audio content. Extended controls allow the user to play, pause, forward, replay, and skip to the next, or the previous track. A seek bar is provided to indicate buffering, duration, and track position. Track position can be further controlled with the [slider](/components/slider/) thumb.

### Autoplay

The audio player can be set to play automatically when audio content is loaded.

Note

This will not work on mobile browsers due to users' data allowance, and it can't happen on page load – the user has to interact with the page the audio player appears on for it to work. Navigating inside a single-page application will work as expected, as there is no page refresh.

### Time display

Can be used to display the current time elapsed, duration of the audio track, or both.

### Forward & replay

Icon buttons for forwarding or replaying the audio track for a determined number of seconds (default 10 seconds).  
  
Custom values can be provided for the number of seconds in the scale, as well as custom icons.

### Playback speed control

Audio speed can be selected on click/tap, changing the pace of the audio track, with the default/normal value set at 1x.  
  
The playback speed control launched in a [modal](/components/modal/) is intended for use on mobile, and a [popover](/components/popover/) is intended for use on desktop.

### Volume Control

The volume control has the option of either being displayed in an expanded or collapsed mode.  
  
The volume slider can be expanded on hover or focus of the mute button in either horizontal or vertical orientations.

### Mute button

The volume control has the option to hide the volume slider for use on mobile devices, with only the mute button visible.

### Live

The live functionality is used for streaming live audio content  
  
Live streaming audio can be indicated by providing a [flag](/components/flag/) component with text and icon to communicate this to users.

### Recorded

The recorded functionality is used for streaming recorded audio content. Extended controls allow the user to play, pause, forward, replay, and skip to the next, or the previous track. A seek bar is provided to indicate buffering, duration, and track position. Track position can be further controlled with the [slider](/components/slider/) thumb.

### Autoplay

The audio player can be set to play automatically when audio content is loaded.

Note

This will not work on mobile browsers due to users' data allowance, and it can't happen on page load – the user has to interact with the page the audio player appears on for it to work. Navigating inside a single-page application will work as expected, as there is no page refresh.

### Time display

Can be used to display the current time elapsed, duration of the audio track, or both.

### Forward & replay

Icon buttons for forwarding or replaying the audio track for a determined number of seconds (default 10 seconds).  
  
Custom values can be provided for the number of seconds in the scale, as well as custom icons.

### Playback speed control

Audio speed can be selected on click/tap, changing the pace of the audio track, with the default/normal value set at 1x.  
  
The playback speed control launched in a [modal](/components/modal/) is intended for use on mobile, and a [popover](/components/popover/) is intended for use on desktop.

### Volume Control

The volume control has the option of either being displayed in an expanded or collapsed mode.  
  
The volume slider can be expanded on hover or focus of the mute button in either horizontal or vertical orientations.

### Mute button

The volume control has the option to hide the volume slider for use on mobile devices, with only the mute button visible.

* * *

Behaviours
----------

The following guidance describes how the Audio Player behaves.

### Buffering

The seek bar indicates audio track duration and buffering, and controls the track position. Also known as an audio ‘scrubber’.

### Skip previous

The skip previous icon button is used to skip to the beginning of the track and if pressed within the first five seconds of a track will skip to the previously played track (if available).  
  
If no previous track is available, the icon button will be disabled for the first 5 seconds of playback.

### Skip next

The skip next icon button is used to skip to the next track (if available).  
  
If there is no next track available, the icon button will be disabled.

### Play pause - live

When audio is playing the play pause icon button will display a stop icon, and a play icon when no audio is playing. Play will resume from the current point in the live stream.

### Play pause - recorded

When audio is playing the play pause icon button will display a pause icon, and a play icon when no audio is playing. Paused content will resume from the track position.

### Mute button

The mute icon button mutes/unmutes the audio track on click/tap, or via the `M` keyboard shortcut.

### Buffering

The seek bar indicates audio track duration and buffering, and controls the track position. Also known as an audio ‘scrubber’.

### Skip previous

The skip previous icon button is used to skip to the beginning of the track and if pressed within the first five seconds of a track will skip to the previously played track (if available).  
  
If no previous track is available, the icon button will be disabled for the first 5 seconds of playback.

### Skip next

The skip next icon button is used to skip to the next track (if available).  
  
If there is no next track available, the icon button will be disabled.

### Play pause - live

When audio is playing the play pause icon button will display a stop icon, and a play icon when no audio is playing. Play will resume from the current point in the live stream.

### Play pause - recorded

When audio is playing the play pause icon button will display a pause icon, and a play icon when no audio is playing. Paused content will resume from the track position.

### Mute button

The mute icon button mutes/unmutes the audio track on click/tap, or via the `M` keyboard shortcut.

* * *

Usage
-----

Here’s how and when to use the audio player:

* * *

Do use a flag for 'live' audio streaming

Use a [flag](/components/flag/) to show users that audio is being live streamed.

* * *

Do adapt the component for different breakpoints

For optimal user experience across breakpoints, it is recommended to display the playback speed control options in a [popover](/components/popover/) for desktop, and in a [modal](/components/modal/) for mobile.

* * *

Do use the expandable volume control when space is limited

Use the expandable volume control when space in an audio player is limited.

* * *

Don’t display on mobile

Avoid displaying the volume control on mobile devices as users can use their native device controls to increase or decrease the volume of the audio track.

* * *

Accessibility considerations
----------------------------

The audio player has the following accessibility considerations:

*   For recorded audio content, it is best practice to provide audio transcription in order to cater to accessibility needs. This is generally provided in [WebVTT format.](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    

Focus order

Focus order depends on how the audio player subcomponents are assembled and ordered in the DOM.

Volume control

Order

Element

Role

Playback speed control

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

Audio player composable

The audio player composable has a range of props that can be used to define an appropriate experience for different use cases.

Name

Type

Default

Description

Required

The audio player requires a source stream to be passed in as using the `src` prop. This will then be loaded into the internal `<audio>` element for playback.

The audio element is non-visual, and as such doesn’t come with predefined elements and attributes that can be overridden to define their appearance.

Play Pause Button

The play pause button has a range of props that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

Please refer to the [Icon Button](/components/button/) component for details of the props and other overrides.

Attribute

Type

Default

Description

Time display

The time display has a range of props that can be used to define an appropriate experience for different use cases.

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

Seek bar

The seek bar has the following overrides that can be used to define an appropriate experience for different use cases.

Attribute

Type

Default

Description

Please refer to the [Slider](/components/slider/) component for details of overrides.

Skip next button

The skip next button has the following overrides that can be used to define an appropriate experience for different use cases.

Attribute

Type

Default

Description

Please refer to the [icon button](/components/button/) component for details of the props and other overrides.

Skip previous button

The skip previous button has the following overrides that can be used to define an appropriate experience for different use cases.

Attribute

Type

Default

Description

Please refer to the [icon button](/components/button/) component for details of the props and other overrides.

Forward Button

The forward button has the following overrides that can be used to define an appropriate experience for different use cases.

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

Please refer to the [icon button](/components/button/) component for details of the props and other overrides.

Replay button

The replay button has the following overrides that can be used to define an appropriate experience for different use cases.

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

Please refer to the [icon button](/components/button/) component for details of props and overrides.

Volume control

The volume control has a range of props that can be used to define an appropriate experience for different use cases.

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

Please refer to the [Popover](/components/popover/) component for details of props and overrides.

Playback Speed Control

The playback speed control has the following overrides that can be used to define an appropriate experience for different use cases.

Props

Overrides

Name

Type

Default

Description

Required

This component should extend the overrides of the [Popover](/components/popover/), [Modal](/components/modal/) components.

Attribute

Type

Default

Description

* * *

Related components
------------------

[

### Button



](/components/button/)

Allows users to take actions, and make choices, with a single tap.

[

### Slider



](/components/slider/)

Allows users to choose a single value or range between min and max values by sliding a thumb.

[

### Modal



](/components/modal/)

A Modal is a layout panel that presents critical information or requests users input without navigating away from the current page.

[

### Popover



](/components/popover/)

A Popover (also known as a Popper) is a layout component that displays non-critical information when a user clicks or taps on a UI element.

* * *

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)

Need Help?
==========

Cant find what you are looking for?

[Get In Touch](/about/contact-us/)