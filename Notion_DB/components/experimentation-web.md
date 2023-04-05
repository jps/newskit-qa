Experimentation Web | NewsKit design system

Experimentation Web
===================

Overview
--------

[Optimizely Web Experimentation](https://docs.developers.optimizely.com/web/docs/introduction) is front-end A/B and multi-page experimentation product. The Experimentation Web component is a non-visual component for the injection of the Optimizely Web 3rd party script and custom script for enabling Optimizely based on cookie.

Prerequisites
-------------

To utilise this component you will need to have the relevant Optimizely Web project in the [Optimizely platform](https://app.optimizely.com/) and Optimizely script CDN URL.

Usage
-----

The component should be added at the top-level of the project in the `<head>` tag. The Optimizely script should run before the other scripts to avoid flickering and unexpected DOM changes on the page.

It’s important to load the Optimizely script before the utag script, so that the GA `page-view` event can report on the running experiments.

Props
-----

optimizelyWebConfigobject

The config object that initialises Optimizely Web. Required parameters: **scriptCdn**.

scriptCdnstring

Optimizely script CDN URL. The URL can be found in _Settings \-> Implementation_ for every web project in the Optimizely platform. More information on how to retrieve the script can be found [here](https://documentation.sourcepoint.com/web-implementation/sourcepoint-set-up-and-configuration-v2) .

reactHelmetReact.ComponentType<{script?: Array<any>}>

By default the Experimentation Web component will inject its scripts by rendering script tags. However, if your project is using [React Helmet](https://www.npmjs.com/package/react-helmet) you can pass the Helmet component in and the scripts will render using that component.

asyncboolean

If you are looking for better page-load performance, you might consider loading Optimizely as a non-blocking resource (async). However, this sometimes causes page flickering, which in turn can generate sub-optimal user experiences. We strongly recommend to load the Optimizely snippet as non-blocking. By default the component loads Optimizely synchronously.