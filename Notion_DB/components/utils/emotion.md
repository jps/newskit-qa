Emotion | NewsKit design system

Emotion
=======

Overview
--------

NewsKit exports out some of the most commonly used Emotion functions/types/components to help consumers build custom components where needed.

CSS
---

The css function in Emotion accepts styles as a template literal, object, or array of objects and returns a class name. It is the foundation of emotion. The primary way to style elements with emotion is the `css` prop. It provides a concise and flexible API to style your components.

Styled Components
-----------------

`styled` is a way to create React components that have styles attached to them. It’s available from @emotion/styled. `styled` is very similar to `css` except you call it with an HTML tag or React component and then call that with a template literal for string styles or a regular function call for object styles. NewsKit uses `styled` in both the components and the documentation site. Here is the official Emotion documentation for [Styled Components](https://emotion.sh/docs/styled).

CSSObject
---------

The `css` prop accepts object styles (`CSSObject`) directly and does not require an additional import. Object styles (`CSSObject`) are especially useful with the css prop because you don’t need a css call like with string styles. Object styles can also be used with `styled`. Here is the official Emotion documentation for [Object Styles](https://emotion.sh/docs/css-prop)

SerializedStyles
----------------

To pass string styles(`SerializedStyles`), you must use css which is exported by @emotion/core, it can be used as a tagged template literal. Here is the official Emotion documentation for [String Styles](https://emotion.sh/docs/css-prop).

Global
------

Global component (`Global`) injects styles into the global scope and is useful for applications such as css resets or font faces. It accepts a styles prop which accepts the same values as the css prop except it inserts styles globally. Global styles are also removed when the styles change or when the Global component unmounts. In NewsKit, we use `Global` to apply font faces to our documentation site pages. Here is the official Emotion documentation for [Global Styles](https://emotion.sh/docs/globals).

Theming
-------

Theming is included in the @emotion/react package. Emotion's theming API provide us with `ThemeProvider`，`withTheme` and `useTheme`, which are widely used in NewsKit components and the documentation site. You can read about their usage [here](/theme/theming/using-a-theme/) or on Emotion's official documentation site [Theming](https://emotion.sh/docs/theming#api).