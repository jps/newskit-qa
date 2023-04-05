Aspect Ratio | NewsKit design system

Aspect Ratio
============

For more information on how to apply aspect ratio to image, please refer to the [Image component](/components/image/).

Overview
--------

The aspect ratio of an image is the ratio of its width to its height. It is commonly expressed as two numbers separated by a colon, as in 16:9. For an x:y aspect ratio, the image is x units wide and y units high. Widely used aspect ratios include 4:3, 16:9 and 3:2. Regardless of its child's dimensions, the component will maintain the specified aspect ratio or calculate and maintain an aspect ratio based on a provided width and height.

Props
-----

aspectRatiostring

This is a string interpolation of the aspect ratio of the children by \`width:height\`. e.g. \`2:3\` for 2 by 3 ratio.

heightstring = auto

Used in combination with \`width\` to calculate the aspect ratio for the children. Generally supply the height px value if known, if not supply vertical aspect ratio. Both width and aspectRatio should be supplied in a consistent manner. This prop accepts any unit for the height in css, but if one is not provided then it assigns \`px\` as its default unit.

maxHeightstring

Used in combination with \`height\` to set the maximum height of the children despite the height set by the aspect ratio. This is to prevent the aspect ratio being distorted if the dimensions of the children are dynamic and changes after its initial render. This prop accepts any unit for the maxheight in css, but if one is not provided then it assigns \`px\` as its default unit.

widthstring = 100%

Used in combination with \`height\` to calculate the aspect ratio for the children. Generally supply the width px value if known, if not supply horizontal aspect ratio. Both width and aspectRatio should be supplied in a consistent manner. This prop accepts any unit for the maxwidth in css, but if one is not provided then it assigns \`px\` as its default unit.

maxWidthstring

Used in combination with \`width\` to set the maximum width of the children. Same as \`maxHeight\`. This prop accepts any unit for the width in css, but if one is not provided then it assigns \`px\` as its default unit.

Playground
----------

Please note that for the sake of the example in the playground below there is a hypothetical limit for the width and height dimensions. Within the bounds of 600px by 600px the aspect ratio should work correctly, but in the real world it will depend on the dimensions of the parent component.

Insert Children here

Aspect Ratio

children

Height

max height

max width

width

    1import React from 'react';
    2import { AspectRatio } from 'newskit';
    3
    4export default () => (
    5  <AspectRatio
    6    aspectRatio="3:2"
    7    height="200"
    8    maxHeight="200"
    9    maxWidth="300"
    10    width="300"
    11  >
    12    Insert Children here
    13  </AspectRatio>
    14);
    15
    

Edit on CodeSandbox