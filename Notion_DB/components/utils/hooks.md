Hooks | NewsKit design system

Hooks
=====

useMediaQueryObject
-------------------

The `userMediaQueryObject` hook handles scenarios where you want to render components based on media query breakpoints. This hook also responds to viewport resizing and returns the appropriate breakpoint for the viewport.

`useMediaQueryObject` returns the value for the current breakpoint from the provided media query object. `MQ<T>`

Media Query hooks require a **NewsKitProvider** or **MediaQueryProvider** as an ancestor of the component in which they are used.

Media Query hooks work only on client-side code in the browser.  
During server-side rendering, hooks will always return the **XS** breakpoint.

### Example

A common use case for using `useMediaQueryObject` is when you want to change component property based on media query. In the example below, the `<Card />` component changes its layout depending on screen the size.

    1const mqLayout = {
    2    xs: 'vertical',
    3    sm: 'vertical',
    4    md: 'horizontal',
    5    lg: 'horizontal',
    6    xl: 'horizontal',
    7}
    8const layout = useMediaQueryObject(mqLayout);
    9<Card layout={layout} /> 

Note: In theory `useMediaQueryObject` could be used with any `MQ<T>`, however, we recommend using it only for props that don't accept `MQ<T>` as a value. Most CSS-based props and overrides already support `MQ<T>` objects. When you create your own components and want to apply responsive behaviour you should try to use [getters](/components/utils/get-from-theme/) and [defaults](/components/utils/get-defaults/) functions.

DO NOT DO THIS:

    1const stylePresets = {
    2    xs: 'dividerPrimary',
    3    md: 'horizontal',
    4}
    5const dividerStylePreset = useMediaQueryObject(stylePresets);
    6<Divider overrides={{stylePreset: dividerStylePreset}} />

useBreakpointKey
----------------

`useBreakpointKey` has a similar utility as `useMediaQueryObject`, it's intended usage is where you want to know the currently active breakpoint key `xs | sm | md | lg | xl`.

### Example

    1const breakpointKey = useBreakpointKey();
    2// return XL when screen has width XL ( 1440px and above )

`<Card />` component use case

    1const breakpointKey = useBreakpointKey();
    2  const layout == breakpointKey === 'xs || breakpointKey === 'sm' ? 'vertical' : 'horizontal';
    3<Card layout={layout} />
    4// the <Card will render verticaly on XS and SM screens and Horizontaly on the rest of breakpoints

useMediaQuery
-------------

`useMediaQuery` is a custom hook used to help detect whether a single media query matches.

Learn more about the API and background ([https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia))

### Example

    1import {useMediaQuery} from 'newskit';
    2const reduceMotion = useMediaQuery('(prefers-reduced-motion: reduce)');
    3// return true when reduce motion is detected

useControlled
-------------

`useControlled` is a custom hook used to allow any component handle controlled and uncontrolled modes, and provide control over its internal state. Most NewsKit components use the useControlled for seamlessly managing both controlled or uncontrolled state scenarios.

With useControlled, you can pass an initial state (using defaultValue) implying the component is uncontrolled, or you can pass a controlled value (using controlledValue) implying the component is controlled.

### Example

useIntersection
---------------

`useIntersection` is a custom hook that detects visibility of a component on the viewport using the IntersectionObserver API ([https://developer.mozilla.org/en-US/docs/Web/API/Intersection\_Observer\_API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)) natively present in the browser.

It is currently being used in the lazy-loading of our image component.

It takes optionally `rootMargin` and `disabled` arguments and returns the full IntersectionObserver's entry object.

### Example

useResizeObserver
-----------------

`useResizeObserver` is a custom hook that utilizes the resizeObserver API ([https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)) to return an element's size.

It takes a ref and returns the width and the height from the observed element.

It also takes an optional callback which allows you to access the full DOMRect object if required.

### Example

useKeypress
-----------

`useKeypress` is a custom hook that detects when the user is pressing one single key or multiple keys.

It takes a key or an array of keys, a call back function and some optional arguments like `enabled`, `eventType`, `target` and `preventDefault`;

This hook is currently being used in the audio player, modal & drawer.

### Example