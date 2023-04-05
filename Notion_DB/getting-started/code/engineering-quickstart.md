Engineering quickstart | NewsKit design system

Guides

Engineering quickstart
======================

Start building digital products with NewsKit.

Requirements
------------

To use NewsKit components in your project, you’ll need:

*   [Node.js](https://nodejs.org/en/download/) v14 or newer.
    
*   A project to install NewsKit into. If you need to create a new one try [Next.js](https://nextjs.org/learn/basics/create-nextjs-app) or [Create React App](https://create-react-app.dev/docs/getting-started/).
    

We recommend [typescript](https://www.typescriptlang.org/), but NewsKit works with vanilla javascript too.

* * *

Install the package
-------------------

Install the NewsKit package using a package manager like [npm](https://docs.npmjs.com/cli/v8/commands/npm) or [yarn](https://classic.yarnpkg.com/lang/en/).

    1npm install newskit @emotion/react @emotion/styled

  

or

  

    1yarn add newskit @emotion/react @emotion/styled

  

Please note that newskit is using [emotion](https://emotion.sh/docs/introduction) as styling engine, that is why you also need to install`@emotion/react` and`@emotion/styled`.

* * *

Set up an app
-------------

NewsKit components can be used like any [React components](https://reactjs.org/docs/components-and-props.html). They need to be descendants of a `NewsKitProvider` which provides a single wrapper to configure your application. It adds a [ThemeProvider](/theme/theming/using-a-theme/), [MediaQueryProvider](/components/utils/hooks/#usemediaqueryobject), [InstrumentationProvider](/getting-started/code/instrumentation/) and a LayerOrganizer to handle theming, media queries, instrumentation and stacking context in the application.  
  
Here's the "Hello World!" example of using a NewsKit [Tag component](/components/tag/) with the NewsKitProvider.

    1import {NewsKitProvider, Tag, newskitLightTheme} from 'newskit';
    2import React from 'react';
    3export default class App extends React.Component {
    4  render() {
    5    return (
    6      <NewsKitProvider 
    7        theme={newskitLightTheme}
    8        instrumentation={'instrumentation provider props'}
    9        layer={'layer organizer props'}
    10        >
    11        <Tag
    12          href="http://example.com"
    13          size="medium">
    14            Tag Content
    15        </Tag>
    16      </NewsKitProvider>
    17    )
    18  }
    19}

* * *

What’s next?
------------

[

### Creating a theme



](/theme/theming/creating-a-theme/)

Theme NewsKit components to match your brand.

[

### Using a theme



](/theme/theming/using-a-theme/)

Render NewsKit components using an available theme.

* * *

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)