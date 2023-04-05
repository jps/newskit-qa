Consent | NewsKit design system

Consent
=======

Overview
--------

The consent component is a non-visual component for the consent of the use of 3rd party cookies. It triggers the loading of a Sourcepoint CMP (Content Management Platform) dialog to allow the user to decide what 3rd party cookies they wish to allow or disallow on their browser. Unless you are utilising React Helmet, it must be placed inside the body of the document during server-side rendering.

At the moment this component is supporting three versions of the Sourcepoint config. Versions GDPR TCF V2 and GDPR Non-TCF, these are both legacy implementations (SourcePoint clients implemented before May 5th, 2021 will used these and should be migrated to the Unified Script). The most upto date version is the Unified Script.

Prerequisites
-------------

To utilise this component you will need to have a [Sourcepoint](https://www.sourcepoint.com) account and, if required, a Sourcepoint messaging subdomain set up. For more detailed information please see Sourcepoint [Unified Script or Web Implementation](https://docs.sourcepoint.com/hc/en-us/articles/4405412395667-CMP-web-implementation). For legacy implementations [documentation TCF V2](https://documentation.sourcepoint.com/web-implementation/web-implementation/sourcepoint-gdpr-and-tcf-v2-support/) or [documentation Non-TCF](https://documentation.sourcepoint.com/web-implementation/web-implementation/gdpr-non-tcf-web-implementation).

Usage
-----

Props Unified Script GDPR TCF
-----------------------------

sourcePointConfigUnified

The config object that initialises SourcePoint. See [Sourcepoint documentation](https://docs.sourcepoint.com/hc/en-us/articles/4405412419731) for a full reference.  
  
In order to add Sourcepoint script for GDPR or CCPA you must add at least an empty gdpr or ccpa object (see below).

accountIdnumber

The accountId value associates the property with your organization's Sourcepoint account. Your organization's accountId can be retrieved by contacting your Sourcepoint Account Manager or via the My Account page in your Sourcepoint account.

baseEndpointstring

A single server endpoint that serves the messaging experience. For GDPR TCF, CCPA, GDPR Standard, and Custom Messaging, the baseEndpoint is https://cdn.privacy-mgmt.com.

isSPAboolean

When set to true, will confirm the implementation for a single page application and will show a message only when window.\_sp\_.executeMessaging();is triggered.  
**Note:** `window._sp_.executeMessaging();` is supposed to be called on each (virtual) pageload.

authIdnumber

Allows your organization to pass a consent identifier to Sourcepoint to be used with authenticated consent

authCookiestring

Allows your organization to configure a unique name for Sourcepoint's authId cookie.

campaignEnvstring

When set to stage, the implementation will default to campaigns configured in your stage campaign environment.

joinHrefboolean

When set to true, will ensure that all directory regular expression functionality works in conjunction with the propertyHref parameter.  
  
The joinHref parameter is solely used to test your implementation across different servers while still allowing for URL RegEx matching.  
  
For these reasons, Sourcepoint strongly recommends that joinHref is set to true to ensure full CMP functionality.

targetingParamsobject

Targeting params allow a developer to set arbitrary key/value pairs. These key/value pairs are sent to Sourcepoint servers where they can be used to take a decision within the scenario builder.

propertyHrefstring = false

Maps the implementation to a specific URL as set up in the Sourcepoint account dashboard.

propertyIdnumber

Maps the message to a specific property (website, app, OTT) as set up in Sourcepoint account dashboard.

eventsobject

An array of events that allow Javascript callbacks to be triggered. Please refer to the [Optional Callback](https://documentation.sourcepoint.com/web-implementation/web-implementation/sourcepoint-gdpr-and-tcf-v2-support/optional-callbacks-tcfv2) document to learn more about how to use events as part of your setup configuration.

gdprobject

In order to surface a GDPR message to your clients, you will need to include the gdpr: object in your client configuration script regardless of whether you configure any optional parameters.

consentLanguagestring

Ensure that the purposes or stack names listed in a consent message remain in the same language regardless of an end-user's browser language setting.  
  
Uses ISO 639-1 language codes.

groupPmIdnumber

Allows your organization to use the privacy manager ID for the property group's privacy manager.

targetingParamsobject

Targeting params allow a developer to set arbitrary key/value pairs. These key/value pairs are sent to Sourcepoint servers where they can be used to take a decision within the scenario builder.  
  
targetingParams set within the gdpr object will override overall targetingParams

ccpaobject

In order to surface a CCPA message to your clients, you will need to include the ccpa: object in your client configuration script regardless of whether you configure any optional parameters.

alwaysDisplayDNSboolean

Setting this parameter to true enables use cases where a Sourcepoint Do Not Sell (my data) notification is hardcoded.

groupPmIdnumber

Allows your organization to use the Privacy Manager ID for the property group's Privacy Manager ID.

targetingParamsobject

Targeting params allow a developer to set arbitrary key/value pairs. These key/value pairs are sent to Sourcepoint servers where they can be used to take a decision within the scenario builder.  
  
targetingParams set within the gdpr object will override overall targetingParams

reactHelmetreact-helmet Helmet Component

By default the Consent component will inject its scripts by rendering script tags. However, if your project is using  [React Helmet](https://www.npmjs.com/package/react-helmet)  you can pass the Helmet component in and the scripts will render using that component.

Props GDPR TCF V2
-----------------

sourcePointConfigTCFV2

The config object that initialises SourcePoint. See [Sourcepoint documentation](https://documentation.sourcepoint.com/web-implementation/web-implementation/sourcepoint-gdpr-and-tcf-v2-support/gdpr-and-tcf-v2-setup-and-configuration_v1.1.3) for a full reference.

accountIdnumber

The accountId value associates the property with your organization's Sourcepoint account. Your organization's accountId can be retrieved by contacting your Sourcepoint Account Manager or via the My Account page in your Sourcepoint account.

targetingParamsobject

Targeting params allow a developer to set arbitrary key/value pairs. These key/value pairs are sent to Sourcepoint servers where they can be used to take a decision within the scenario builder.

isSPAboolean

When set to true, will confirm the implementation for a single page application and will show a message only when window.\_sp\_.executeMessaging();is triggered.  
**Note:** `window._sp_.executeMessaging();` is supposed to be called on each (virtual) pageload.

mmsDomainstring

has been replaced by the new `baseEndpoint` parameter for optimization reasons. This change is completely backwards compatible. However, it is recommended that older implementations move to the new parameter to benefit from the optimizations.

wrapperAPIOriginstring

has been replaced by the new `baseEndpoint` parameter for optimization reasons. This change is completely backwards compatible. However, it is recommended that older implementations move to the new parameter to benefit from the optimizations.

propertyHrefboolean

Maps the implementation to a specific URL as set up in the Sourcepoint account dashboard.

baseEndpointstring

is a single server endpoint from where the messaging as well as the GDPR and TCFv2 experience is served. The baseEndpoint can also be changed to a CNAMED 1st party subdomain in order to persist 1st party cookies on Safari web browser (due to Safari’s ITP) by setting cookies through the server with "set-cookie" rather than using "document.cookie" on the page. Changing the baseEndpoint domain is optional but recommended!

groupPmIdnumber

Allows your organization to use the Privacy Manager ID for the property group use of a property group's Privacy Manager ID.  
**Note:** Call `window._sp_.loadPrivacyManagerModal()` without passing a parameter and the Privacy Manager that displays will be that property's version of the groupPmId Privacy Manager.

waitForConsentboolean = false

When true (the default value), the consent component will cause prebid.js to wait for user consent to be provided before it initialises.

eventsobject

An array of events that allow Javascript callbacks to be triggered. Please refer to the [Optional Callback](https://documentation.sourcepoint.com/web-implementation/web-implementation/sourcepoint-gdpr-and-tcf-v2-support/optional-callbacks-tcfv2) document to learn more about how to use events as part of your setup configuration.

consentLanguagestring

If this parameter is not present, stacks and purposes will appear according to the end-user's preferred browser language setting.`consentLanguage: "nl"`

reactHelmetreact-helmet Helmet Component

By default the Consent component will inject its scripts by rendering script tags. However, if your project is using  [React Helmet](https://www.npmjs.com/package/react-helmet)  you can pass the Helmet component in and the scripts will render using that component.

Props GDPR Non-TCF
------------------

SourcePointConfigNonTCFV1

The config object that initialises SourcePoint. See [Sourcepoint documentation](https://documentation.sourcepoint.com/web-implementation/web-implementation/sourcepoint-gdpr-and-tcf-v2-support/gdpr-and-tcf-v2-setup-and-configuration_v1.1.3) for a full reference.

accountIdnumber

The accountId value associates the property with your organization's Sourcepoint account. Your organization's accountId can be retrieved by contacting your Sourcepoint Account Manager or via the My Account page in your Sourcepoint account.

baseEndpointstring

The baseEndpoint can also be changed to a CNAME first-party subdomain in order to persist first-party cookies on Safari web browser (due to Safari’s ITP) by setting cookies through the server with set-cookie rather than using document.cookie on the page.

isSPAboolean

When set to true, will confirm the implementation for a single page application and will show a message only when window.\_sp\_.executeMessaging();is triggered.  
**Note:** `window._sp_.executeMessaging();` is supposed to be called on each (virtual) pageload.

groupPmIdnumber

Allows your organization to use the Privacy Manager ID for the property group use of a property group's Privacy Manager ID.  
**Note:** Call `window._sp_.loadPrivacyManagerModal()` without passing a parameter and the Privacy Manager that displays will be that property's version of the groupPmId Privacy Manager.

propertyHrefstring

Maps the implementation to a specific URL as set up in the Sourcepoint account dashboard.

propertyIdstring

Maps the message to a specific property (website, app, OTT) as set up in the Sourcepoint account dashboard.

targetingParamsobject

Targeting params allow a developer to set arbitrary key/value pairs. These key/value pairs are sent to Sourcepoint servers where they can be used to take a decision within the scenario builder.

eventsobject

[Click here](https://documentation.sourcepoint.com/web-implementation/web-implementation/gdpr-non-tcf-web-implementation/optional-event-callbacks-for-gdpr-non-tcf-web-implementation) for all optional event callbacks that are supported by Sourcepoint for GDPR non-TCF web implementations.

consentLanguagestring

If this parameter is not present, stacks and purposes will appear according to the end-user's preferred browser language setting.`consentLanguage: "nl"`

How to run on localhost
-----------------------

The minimum parameters for the Consent component to run locally are a sourcePointConfig object with accountId and siteHref for TCFV1 and with an accountId and propertyHref for TCFV1. The `siteHref` or `propertyHref` property should be an url that that exists in your account's property group. Contact your sourcepoint account manager.

In a V2 example it would look like this:

    1<Consent
    2    sourcePointConfigTCFV2={{
    3      accountId: accountId,
    4      propertyHref: 'http://newskit.co.uk/'
    5    }}
    6  />

Consent button
--------------

By setting `renderConsentButton` to false the default consent button will be hidden. This component can be use intead. It gives the flexibilty to place anywhere on the page.

settingsButtonTextstring = Privacy Settings

Consent button label text

postPromptUIstring = privacy-settings-prompt

As this prop connects the consent button to the consent component, the value of this prop needs to match with the value provided in the consent component.