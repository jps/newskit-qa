Instrumentation setup | NewsKit design system

Guides

Instrumentation setup
=====================

Set up instrumentation on NewsKit components.

Overview
--------

NewsKit components are built to emit events "out of the box" via the provided NewsKit event instrumentation system. This requires a small amount of setup in your project so emitted events can reach your desired tag manager.  
  
Events fired via the provided instrumentation system can be forwarded to as many handlers as desired. NewsKit provides two handlers:  

*   A console handler that outputs the fired events to the browser console
    
*   A Tealium handler that forwards the event onto the Tealium tag manager (Tealium must be present on the page for this handler to work)
    

The handlers are exported under `instrumentationHandlers`. You can also create your own handlers (e.g. if you need to forward events to a different tag manager).

For more information, users with the relevant access can read the internal RFC which lead to this implementation. This can be found on [Github.](https://github.com/newsuk/nuk-rfcs)

* * *

Setup
-----

The event instrumentation system is part of NewsKit, so the install you have for other components works here, too.  
  
Create the event instrumentation by calling the function `createEventInstrumentation`. This takes two arguments:

*   an array of event handler functions; an event handler function simply takes an array of events and returns the same. There are two handlers provided by NewsKit, a console and Tealium handler (exported under `instrumentationHandlers`), but you can also pass your own custom handlers.
    
*   An event context object; this is an optional, but recommended, object of contextual data relevant to the page the events are being fired from. It might contain, for example, the page URL and a user identifier.
    

This function will return an object containing the context passed to it and the `fireEvent` function. This is the function used internally by NewsKit components to fire events to your handlers.

### Instrumentation provider

Similar to the way you may use the [ThemeProvider](/theme/theming/using-a-theme/) to set the components theme, NewsKit provides a React context component called `InstrumentationProvider` to wrap the React DOM of your project and provide the required event instrumentation down to NewsKit components.  
  
The props required for this component match the object output from the `createEventInstrumentation` function. As a result, the object can simply be destructured into the props of the provider.

Keep in mind that `NewsKitProvider` already contains `InstrumentationProvider` so only use it when you want to create a new context for part of your application.

    1import {
    2  instrumentationHandlers,
    3  createEventInstrumentation,
    4  InstrumentationProvider,
    5  Link,
    6} from 'newskit';
    7
    8const handlers = [
    9  instrumentationHandlers.createConsoleHandler(),
    10  instrumentationHandlers.createTealiumHandler(),
    11  instrumentationHandlers.createTealiumTrackHandler(),
    12];
    13
    14const contextObject = {
    15  pageUrl: 'www.my-amazing-website.com',
    16};
    17
    18const instrumentation = createEventInstrumentation(handlers, contextObject);
    19
    20const MyPage = (
    21  <InstrumentationProvider {...instrumentation}>
    22    <Link href="example.com">My Amazing Link</Link>
    23  </InstrumentationProvider>
    24);

In this example, the link component, and any other NewsKit instrumentation enabled components, emit events to the browser's console. This could look something like this:

    1{
    2  "originator": "link",
    3  "trigger": "click",
    4  "context": {
    5    "url": "www.my-amazing-website.com"
    6  }
    7}

InstrumentationProvider components can be nested if you wish to extend the context object to add extra data. See below for more information and examples.

### Middleware

NewsKit contains a middleware composition system to allow for operations on events before they reach a handler. For example, if you want to filter events to forward only a specific set to a tag manager, perform some event data transformations or batch the events reaching a handler.  
  
Instrumentation middleware functions have the same signature as handlers. They take in an array of events and must return an array of events. The returned array can be a different length - or even empty, if necessary - though it's recommended that middleware functions are pure and do not mutate the array or events.  
  
The example below uses filter middleware to pass only specific events to specific handlers:

    1import {
    2  instrumentationHandlers,
    3  composeInstrumentationMiddleware,
    4  instrumentationMiddleware,
    5  EventTrigger,
    6  createEventInstrumentation,
    7} from 'newskit';
    8
    9const consoleHandler1 = composeInstrumentationMiddleware(
    10  instrumentationHandlers.createConsoleHandler('Click event:'),
    11  instrumentationMiddleware.filterByTrigger(EventTrigger.Click),
    12);
    13
    14const consoleHandler2 = composeInstrumentationMiddleware(
    15  instrumentationHandlers.createConsoleHandler('Swipe event:'),
    16  instrumentationMiddleware.filterByTrigger(EventTrigger.Swipe),
    17);
    18
    19const consoleHandler3 = instrumentationHandlers.createConsoleHandler(
    20  'Some other event:',
    21);
    22
    23const tealiumHandler = composeInstrumentationMiddleware(
    24  instrumentationHandlers.createTealiumHandler(),
    25  instrumentationMiddleware.filterByTrigger(EventTrigger.Load),
    26)
    27
    28const handlers = [consoleHandler1, consoleHandler2, consoleHandler3, tealiumHandler];
    29
    30const instrumentation = createEventInstrumentation(handlers, {
    31  url: 'www.my-amazing-website.com',
    32});

### Custom Event Firing

You shouldn't need to add instrumentation event firing to NewsKit components, as this is already provided. But there may be a case where you have pre-existing custom components and wish to use the single NewsKit event instrumentation. You can do this in two ways:

*   Use the NewsKit HOC `withInstrumentation`. This wraps the component argument in the instrumentation context and passes a `fireEvent` prop to the component.
    
*   Use the NewsKit React hook `useInstrumentation`. This returns an object containing the `fireEvent` function.
    

You can call this function with your custom instrumentation event as necessary, so long as it meets event requirements.  
  
Event objects must contain an event `originator` (the name of the component firing the event) and an event`trigger` from the `EventTrigger` enum listed below (this can be used as a JS object or the direct string values in non-TS projects).  
  
Events can also contain a `context` object, which can be any JSON-serializable structure.

    1import {withInstrumentation, EventTrigger} from 'newskit';
    2
    3export interface MySpecialCustomButtonProps {
    4  buttonText: string;
    5}
    6
    7export const MySpecialCustomButton: React.FC<
    8  MySpecialCustomButtonProps
    9> = withInstrumentation(({fireEvent, buttonText}) => (
    10  <button
    11    onClick={() =>
    12      fireEvent({
    13        originator: 'my-special-custom-button',
    14        trigger: EventTrigger.Click,
    15        context: {
    16          buttonText,
    17        },
    18      })
    19    }
    20  >
    21    {buttonText}
    22  </button>
    23));

Key

Value

### Nested Instrumentation Providers & Contexts

It is possible to build up and extend the context of an event by nesting instances of the `InstrumentationProvider`. Each provider can take a context object which will be shallow-merged onto the parent when an event is fired.  
  
This can be useful to build up event information that is specific to a particular component instance - without that component needing to know anything outside its own scope. For example, a button can fire a click event, but the layers of context can provide the information on what the button is for and where it is on the page.

    1import React from 'react';
    2
    3import {
    4  InstrumentationProvider,
    5  instrumentationHandlers,
    6  createEventInstrumentation,
    7  ThemeProvider,
    8  newskitLightTheme,
    9  EventTrigger,
    10  useInstrumentation,
    11} from 'newskit';
    12
    13const rootContext = {
    14  pageUrl: 'www.my-amazing-website.com',
    15};
    16
    17const instrumentation = createEventInstrumentation(
    18  [instrumentationHandlers.createConsoleHandler()],
    19  rootContext,
    20);
    21
    22const RailItem: React.FC<{itemId: number}> = ({itemId, ...props}) => {
    23  const {fireEvent} = useInstrumentation();
    24  return (
    25    <button
    26      {...props}
    27      onClick={() => {
    28        fireEvent({
    29          originator: 'button',
    30          trigger: EventTrigger.Click,
    31        });
    32      }}
    33    >
    34      {itemId}: A really great item!
    35    </button>
    36  );
    37};
    38
    39const Rail: React.FC<{
    40  railName: string;
    41}> = ({railName}) => (
    42  <div>
    43    <InstrumentationProvider
    44      context={{
    45        pageArea: 'rail',
    46        railName,
    47      }}
    48    >
    49      <h3>{railName}</h3>
    50      <RailItem itemId={1} />
    51      <RailItem itemId={2} />
    52    </InstrumentationProvider>
    53  </div>
    54);
    55
    56const App = () => (
    57  <NewsKitProvider theme={newskitLightTheme} instrumentation={instrumentation}>
    58    <Rail railName="Some great rail" />
    59  </NewsKitProvider>
    60);

In this example, we have a root `NewsKitProvider` providing the page URL. Inside the `Rail` component, we have `InstrumentationProvider` - this provides any child events with rail specifics, like the rail name. The `RailItem` contains a button that fires a click event.  
  
This is the resulting click event:

    1{
    2  "context": {
    3    "pageUrl": "www.my-amazing-website.com",
    4    "pageArea": "rail",
    5    "railName": "Some great rail"
    6  },
    7  "originator": "button",
    8  "trigger": "click"
    9}

It is important to remember that in the example above, the `fireEvent` function is scoped to the context of the parent provider (the one which wraps the `RailItem`).  
  
This means if we wanted to add more context to the event inside the `RailItem`, doing the following would NOT work as expected. The `railItemId` we are adding to the context would NOT appear in the event context.

    1const RailItem: React.FC<{itemId: number}> = ({itemId, ...props}) => {
    2const {fireEvent} = useInstrumentation();
    3return (
    4  <InstrumentationProvider
    5    context={{
    6      // THIS WON'T BE INCLUDED! The fireEvent above is outside the scope of this provider!
    7      railItemId: itemId,
    8    }}
    9  >
    10    <button
    11       {...props}
    12       onClick={() => {
    13         fireEvent({
    14           originator: 'button',
    15           trigger: EventTrigger.Click,
    16         });
    17       }}
    18     >
    19      {itemId}: A really great item!
    20    </button>
    21  </InstrumentationProvider>
    22 );
    23};

This would produce the following event (for rail item 1) as expected:

    1const RailItem: React.FC<{itemId: number}> = ({itemId, ...props}) => {
    2  const {fireEvent} = useInstrumentation();
    3  const eventContext = {
    4    railItemId: itemId,
    5  };
    6  return (
    7    <button
    8      {...props}
    9      onClick={() => {
    10        fireEvent({
    11          originator: 'button',
    12          trigger: EventTrigger.Click,
    13          context: eventContext,
    14        });
    15      }}
    16    >
    17      {itemId}: A really great item!
    18    </button>
    19  );
    20};

Instead, you can add context to the event directly (or we must put the button into a separate component and get the `fireEvent`function at that scope level).  
  
Passing context information via the `fireEvent` function is the simpler option:

    1{
    2  "context": {
    3    "pageUrl": "www.my-amazing-website.com",
    4    "pageArea": "rail",
    5    "railName": "Some great rail",
    6    "railItemId": 1
    7  },
    8  "originator": "button",
    9  "trigger": "click"
    10}

* * *

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)