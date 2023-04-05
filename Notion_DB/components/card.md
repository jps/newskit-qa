Card | NewsKit design system

Card
====

Overview
--------

Cards group content that allows users to browse a collection of related items and actions in a modular, easy-to-read way. There are three main areas to the card component: Media, Content and Action area.

### Usage

Cards are used to display a summary of content and will reveal more details upon interaction.

### Variants

There are two card variants - card without inset `<Card/>` card with inset `<CardInset/>`

Props
-----

hrefstring | BaseLinkProps

If provided, the Card will render with an anchor. Both `string` and `BaseLinkProps` are supported,`BaseLinkProps` is derived from `React.AnchorHTMLAttributes`, providing access to all anchor props. For more details check the Interactivity section below.  
  
**NOTE:** If href prop is not provided the card will omit all interactive states (hover and active) from the style presets applied to the inner card containers.

layoutMQ<'vertical' | 'horizontal' | 'horizontal-reverse'> = vertical

The card supports three layouts:  
  

*   `vertical` - The card is stacked vertically, displaying top to bottom: media, content and action items.
    
*   `horizontal` - The card is laid out horizontally, media on the left and content stacked above action items on right.
    
*   `horizontal-reverse` - The card is laid out horizontally, content stacked above action items on left with media on the right.
    

mediaImageProps | React.ComponentType

If this parameter is provided as `ImageProps` object (see [Image documentation](/components/image/)), it will render the media as an image.  
If this is provided as a custom React component, it will render the React component directly.

mediaInteractiveboolean = false

Removes the card media from link area. This prop only matters when the card is used as a link and when custom media or video components are passed as cardMedia so the user can interact with the video (play, pause, etc...) without navigation to occur.  
  
**NOTE:** If necessary, make sure your media element is tabbable by adding `tabindex` to it.

childrenExclude<React.ReactNode, 'undefined'>

This is the body of the Card. A card requires to have at least a heading. Each element of the body content should be wrapped within a [Block](/components/block/) component which is responsible for the spacing between the elements. Refer to the examples below.

actionsReact.ComponentType

If provided, the Card will render the React component being passed to the actions. This could be buttons, tags and/or links. The actions section is typically placed at the bottom of the card and would only be clickable if the child components would be.  
If there are multiple items, it is advised to use the Stack component to display the items. Refer to the examples below.  

overridesobject

If provided, overrides the respective presets for the component and provided elements.

stylePresetMQ<string>

If provided, this overrides the style preset of the card.

horizontalRatiostring = 1:1

If provided, this sets the ratio between the MediaContainer and TeaserAndActionsContainer on a Card with horizontal layout. The ratio consists of two integers with a colon separating them (1:1), where the first value is applied to the left side and the second value is applied to the right side of the card, regardless if the layout is horizontal or horizontal-reverse.  
If 'none' is passed, we don't apply any ratio.  
If an invalid value is passed, the ratio will default to what is defined in component defaults  
  
**NOTE:** This prop works for `horizontal` and `horizontal-reverse` layouts only.

mediaContainerobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the passed media container.

spaceInlineMQ<SpacingPresetKeys>

If provided, this overrides the space between the media container and the container that holds the content and actions area.

paddingInlineMQ<string>

It can take one space token to specify the logical inline start and end padding of the container. This space token can also be used on breakpoints.

paddingInlineStartMQ<string>

It can take one space token to specify the logical inline start padding of the container. This space token can also be used on breakpoints.

paddingInlineEndMQ<string>

It can take one space token to specify the logical inline end padding of the container. This space token can also be used on breakpoints.

paddingBlockMQ<string>

It can take one space token to specify the logical block start and end padding of the container. This space token can also be used on breakpoints.

paddingBlockStartMQ<string>

It can take one space token to specify the logical block start padding of the container. This space token can also be used on breakpoints.

paddingBlockEndMQ<string>

It can take one space token to specify the logical block end padding of the container. This space token can also be used on breakpoints.

teaserContainerobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the teaser container.

paddingInlineMQ<string>

It can take one space token to specify the logical inline start and end padding of the container. This space token can also be used on breakpoints.

paddingInlineStartMQ<string>

It can take one space token to specify the logical inline start padding of the container. This space token can also be used on breakpoints.

paddingInlineEndMQ<string>

It can take one space token to specify the logical inline end padding of the container. This space token can also be used on breakpoints.

paddingBlockMQ<string>

It can take one space token to specify the logical block start and end padding of the container. This space token can also be used on breakpoints.

paddingBlockStartMQ<string>

It can take one space token to specify the logical block start padding of the container. This space token can also be used on breakpoints.

paddingBlockEndMQ<string>

It can take one space token to specify the logical block end padding of the container. This space token can also be used on breakpoints.

actionsContainerobject

stylePresetMQ<string>

If provided, this overrides the style preset applied to the actions container.

minHeightstring

If provided, this sets a minimum height to the actions container. This can be a sizing token from the theme, or any CSS length value.

paddingInlineMQ<string>

It can take one space token to specify the logical inline start and end padding of the container. This space token can also be used on breakpoints.

paddingInlineStartMQ<string>

It can take one space token to specify the logical inline start padding of the container. This space token can also be used on breakpoints.

paddingInlineEndMQ<string>

It can take one space token to specify the logical inline end padding of the container. This space token can also be used on breakpoints.

paddingBlockMQ<string>

It can take one space token to specify the logical block start and end padding of the container. This space token can also be used on breakpoints.

paddingBlockStartMQ<string>

It can take one space token to specify the logical block start padding of the container. This space token can also be used on breakpoints.

paddingBlockEndMQ<string>

It can take one space token to specify the logical block end padding of the container. This space token can also be used on breakpoints.

paddingInlineMQ<string>

Takes one space token to specify the logical inline start and end padding of the container. Can be used on breakpoints

paddingInlineStartMQ<string>

Takes one space token to specify the logical inline start padding of the container. Can be used on breakpoints

paddingInlineEndMQ<string>

Takes one space token to specify the logical inline end padding of the container. Can be used on breakpoints

paddingBlockMQ<string>

Takes one space token to specify the logical block start and end padding of the container. Can be used on breakpoints

paddingBlockStartMQ<string>

Takes one space token to specify the logical block start padding of the container. Can be used on breakpoints

paddingBlockEndMQ<string>

Takes one space token to specify the logical block end padding of the container. Can be used on breakpoints

marginInlineMQ<string>

Takes one space token to specify the logical inline start and end margin of the container. Can be used on breakpoints

marginInlineStartMQ<string>

Takes one space token to specify the logical inline start margin of the container. Can be used on breakpoints

marginInlineEndMQ<string>

Takes one space token to specify the logical inline end margin of the container. Can be used on breakpoints

marginBlockMQ<string>

Takes one space token to specify the logical block start and end margin of the container. Can be used on breakpoints

marginBlockStartMQ<string>

Takes one space token to specify the logical block start margin of the container. Can be used on breakpoints

marginBlockEndMQ<string>

Takes one space token to specify the logical block end margin of the container. Can be used on breakpoints

Refer to the defaults below for the object structure:

An error occurred loading this code example.

  
  
**NOTE:** The `headline` object represent the defaults that will be applied to the`Headline` component used inside the card.  
  

*   `card.headline.nonInteractive` - will be applied by default to the headline when there is **no href** property
    
*   `card.headline.interactive` - will be applied by default to the headline when **href** property is provided
    

You are still able to override the default `Headline` styles by passing the overides directly to the [Headline](/components/headline/) as shown on the examples below.

  
**NOTE:** Card Props extends `React.HTMLAttributes` so that you can pass any valid HTML attribute like onClick.

### Examples

#### Vertical card

##### Card without inset

![Card Media](static/placeholder-3x2.png)

IMAGE

[

CROWDS HEAD

outdoors as bank holiday temps soar above 20 degrees
====================================================



](#)

The bank holiday weekend has seen some mixed weather, but as the sun emerged, many in the UK took the opportunity to make the most of the lockdown easing.

[News](#)

[Sport](#)

##### Card with inset

![Card Media](static/placeholder-3x2.png)

IMAGE

[

CROWDS HEAD

outdoors as bank holiday temps soar above 20 degrees
====================================================



](#)

The bank holiday weekend has seen some mixed weather, but as the sun emerged, many in the UK took the opportunity to make the most of the lockdown easing.

[News](#)

[Sport](#)

#### Horizontal card

##### Card without inset

![Card Media](static/placeholder-1x1.png)

IMAGE

[

CROWDS HEAD

outdoors as bank holiday temps soar above 20 degrees
====================================================



](#)

The bank holiday weekend has seen some mixed weather, but as the sun emerged, many in the UK took the opportunity...

[News](#)

[Sport](#)

**NOTE:** When you use non-inset card without actions you will need to provide additional spacing to the teaser. Otherwise clipping (overflowing) on the last row might occur due to Line Height Cropping. For more information check [this article on medium](https://medium.com/eightshapes-llc/cropping-away-negative-impacts-of-line-height-84d744e016ce)

### Interactivity

When the Card component has a `href` property (making it interactive), it is recommended to pass the [Headline](/components/headline/) as a child, inside of the card content area. In this case the Headline will have a link applied to it, which will have various interactive states (hover, visited, avtive) and the Headline will have new component-defaults applied out of the box - `card.headline.interactive` (listed in the card defaults above), you can also pass your own custom overrides to the Headline.

For this implementation, we use a z-index property in order to exclude the actions area and the media area (when we have mediaInteractive = true) from the link area.

**NOTE:** It is not mandatory for the headline component to be direct child of the card content. It can be nested inside a structure, but make sure it does not have any parents with `position: relative` style applied as it will break the clickable area of the link.

**NOTE:** Passing styled component created from the Headline to the card content would not work correctly when the card is used as a link. Instead use the Headline overrides to modify its styles. Otherwise, the interactivity of the link will not work as expected.

### Accessibility

*   Always pass an `alt` prop to the card image regardless of whether you use the built in or a custom image component.
*   When creating a tab order for the different parts of the card, remember to put the headline before the image or media so that screen-reader users get the context before the image alt tag.
*   When passing custom interactive component (i.e. video) as card media remember to take care of making the media component visible for screen readers by adding tabindex if necessary.
*   Add aria-label prop to allow a user to describe the action that will be performed when the user interacts with the card. By default, this could be the headline text.
*   When nesting other components of the card, always follow those components' accessibility guidelines.