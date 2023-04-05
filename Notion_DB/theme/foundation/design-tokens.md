Design tokens | NewsKit design system

Foundation

Design tokens
=============

Design tokens are NewsKit’s design decisions. They maintain a scalable and consistent experience for users.

Overview
--------

Design tokens are named entities that store visual and functional information. They take the place of hardcoded values, such as hex values for colour or pixel values for spacing.

* * *

Literal vs contextual tokens
----------------------------

### Literal tokens

Literal tokens add a layer of abstraction to hardcoded values. Rather than reference a colour directly (e.g.`#5E44E4`) you can ‘tokenise’ it to `purple050`.  
  
Now, if you need to change the shade of purple, rather than finding everywhere you’ve used the hex code, you can update it all in one place by changing the value of `purple050`.

### Contextual tokens

Contextual tokens add a further layer of abstraction and assign the token a specific purpose. In the example above, you can give `purple050` token context - say, it should be used in typography as the brand colour - by assigning it the inkBrand token.  
  
Contextual tokens let you do things like customise the way components look product-wide. When deciding between a contextual or literal token, consider: would you want the value you’re using to change if you changed the theme? If yes, use a contextual token.

* * *

Naming convention
-----------------

Tokens follow a camelCase naming convention (e.g. lineHeight) to ensure they’re clear, flexible and extensible.  
  
Where the token maps to a numerical series, three digits (in increments of 10) are added as a suffix. Tokens follow the naming convention: {Property}{Series}

### For example:

body010,  
body020,  
fontWeight010,  
fontWeight020,  
header010,  
header020,  
inkBrand010,  
inkBrand020,  

* * *

Presets
-------

When constructing components, you can group design tokens into [presets](/theme/presets/style-presets/). This creates a simple way to customise particular aspects of a component.

* * *

Fonts
=====

Fonts establish styles for content such as headlines and paragraphs.

[Learn more about fonts](/theme/foundation/fonts/)

Fonts
=====

Fonts establish styles for content such as headlines and paragraphs.

[Learn more about fonts](/theme/foundation/fonts/)