Grid Layout step-by-step | NewsKit design system

Guides

Grid Layout step-by-step
========================

The grid layout component is a wrapper around CSS grid that maps all CSS grid properties to React props.

Out of the box, all React props support media query objects as values so that you can easily create responsive layouts.

Key benefits:
-------------

*   Support media query objects
    
*   Allows usage for sizing and spacing tokens
    
*   Allows composition when using naming areas
    

* * *

First layout
------------

Let‘s create our first layout.  
  
Consider the following UI element as our end goal:

Following best practices, we’re going to start with a mobile design and gradually move upward to larger screens.

* * *

Creating a component
--------------------

Create a component.

    1// src/components/card.tsx
    2
    3import React from 'react';
    4
    5export const Card = () => <p>Nothing here yet</p>;
    6
    

* * *

Using GridLayout and naming areas
---------------------------------

Next step, let‘s import the [NewsKit grid layout component.](/components/grid-layout/)

    1// src/components/card.tsx
    2
    3import React from 'react';
    4import { GridLayout } from 'newskit';
    5
    6export const Card = () => <p>Nothing here yet</p>;
    7
    8
    

When describing layouts we can split our UI element into areas. Looking at our design, we could have the following areas:

Try to name areas in a meaningful way, and use names like`image`, `content`, and `action` instead of `top`, `middle`, and `bottom`. This is useful when you create responsive layouts and the position of the areas may change.  
  
Let’s create our first areas. We create a string with tree areas and describe their relation and position. Then pass it to the `GridLayout` component.

    1// src/components/card.tsx
    2
    3const mobileAreas = `
    4  image
    5  content
    6  action
    7`;
    8
    9export Card = () => (
    10	<GridLayout areas={mobileAreas}>Nothing yet</GridLayout>
    11);
    12
    

When you use areas prop on `GridLayout` component, it returns React components with names generated from passed areas. Those components are available in the children render function as arguments:

    1// src/components/card.tsx
    2
    3export Card = () => (
    4	<GridLayout areas={mobileAreas}>
    5	{
    6		(Areas) => (
    7			<> // <- notice the React.Fragment wrapper
    8          <Areas.Image>Image</Areas.Image>
    9          <Areas.Content>Content</Areas.Content>
    10          <Areas.Action>Action</Areas.Action>
    11        </>
    12		)
    13	}
    14	</GridLayout>
    15);
    16
    

Now we can render other components inside those area components to make up the desired appearance. We also need to import a few more [components](/components/overview/) from NewsKit. Here‘s an example of what this looks like:

    1// src/components/card.tsx
    2
    3import { Image, Headline, TextBlock, Button, GridLayout } from 'newskit';
    4
    5export Card = ({imageUrl, headline, short, url}) => (
    6	<GridLayout areas={mobileAreas}>
    7	{
    8		(Areas) => (
    9			<>
    10          <Areas.Image>
    11            <Image src={imageUrl} />
    12          </Areas.Image>
    13          <Areas.Content>
    14            <Headline>{headline}</Headline>
    15            <TextBlock>{short}</TextBlock>
    16          </Areas.Content>
    17          <Areas.Action>
    18            <Button url={url}>read more</Button>
    19          </Areas.Action>
    20		</>
    21		)
    22	}
    23	</GridLayout>
    24);
    25
    

* * *

Areas relations
---------------

The areas prop describes the position of the areas inside the grid. When we want to specify things like dimension and spacing between areas we need to add `columns`, `rows`, `columnGap`, and `rowGap`. In the following example, we add space between each row using the `rowGap` prop and passing the space token from NewsKit.

    1// src/components/card.tsx
    2import { Image, Headline, TextBlock, Button, GridLayout } from 'newskit';
    3
    4export Card = ({imageUrl, headline, short, url}) => (
    5	<GridLayout areas={mobileAreas} rowGap="space030">
    6	{
    7		(Areas) => (
    8			/* Same as above... */
    9		)
    10 }
    11</GridLayout>
    12);
    13
    

* * *

Responsive props
----------------

The `GridLayout` component supports responsive props, which means we can have different values for `areas`, `rowGap`, and other props for different breakpoints.  
  
In order to do that, we need to pass objects with values per each breakpoint. In the example below, we specify a different`rowGap` value for mobile, tablet and desktop screens.

    1<GridAres rowGap={{xs: '10px', sm: '15px', md: '20px', lg: '25px', xl: '30px'}}>

We can apply the same principle to our areas prop so that our [card](/components/card/) component changes its layout on a desktop breakpoint and achieves this UI:

    1// src/components/card.tsx
    2
    3const mobileAreas = `
    4  image
    5  content
    6  action
    7`;
    8
    9const desktopAreas = `
    10	image content
    11	image action
    12`;
    13
    14export const Card = ({imageUrl, headline, short, url}) => (
    15	<GridLayout
    16		areas={{xs: mobileAreas, md: desktopAreas}}
    17		rowGap="space030"
    18		columnGap="space030">
    19	{
    20		(Areas) => (
    21			/* Same as above... */
    22		)
    23	}
    24	</GridLayout>
    25);
    26
    

* * *

Summary
-------

Here’s all of the code together:

    1// src/components/card.tsx
    2
    3import React from 'react';
    4import { Image, Headline, TextBlock, Button, GridLayout } from 'newskit';
    5
    6const mobileAreas = `
    7  image
    8  content
    9  action
    10`;
    11
    12const desktopAreas = `
    13	image content
    14	image action
    15`;
    16
    17export const Card = ({imageUrl, headline, short, url}) => (
    18  <GridLayout
    19    areas={{xs: mobileAreas, md: desktopAreas}}
    20    rowGap="space030"
    21    columnGap="space030"
    22  >
    23    {Areas => (
    24      <>
    25        <Areas.Image>
    26          <Image src={imageUrl} />
    27        </Areas.Image>
    28        <Areas.Content>
    29          <Headline>{headline}</Headline>
    30          <TextBlock>{short}</TextBlock>
    31        </Areas.Content>
    32        <Areas.Action>
    33          <Button href={url}>read more</Button>
    34        </Areas.Action>
    35      </>
    36    )}
    37  </GridLayout>
    38);

* * *

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)