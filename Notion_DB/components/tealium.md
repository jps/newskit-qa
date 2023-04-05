Tealium | NewsKit design system

Tealium
=======

Overview
--------

The Tealium component is a non-visual component for the injection of the Tealium 3rd party scripts.

Prerequisites
-------------

To utilise this component you will need to have the relevant Tealium account details to form the correct script url; an account id, profile id and environment.

Usage
-----

Props
-----

accountIdstring

Your Tealium account id.

profileIdstring

Your Tealium profile id.

envstring

Your Tealium env, e.g. dev.

reactHelmetreact-helmet Helmet Component

By default the Consent component will inject its scripts by rendering script tags. However, if your project is using \[React Helmet\](https://www.npmjs.com/package/react-helmet) you can pass the Helmet component in and the scripts will render using that component.