Consent Settings Link | NewsKit design system

Consent Settings Link
=====================

Overview
--------

The consent settings link is a component utilising the [Link](/components/link/) component which on click will open the Sourcepoint CMP (Content Management Platform) privacy manager. This allows users to review or edit their privacy settings after they have submitted the initial privacy consent message.

Prerequisites
-------------

To utilise this component you will need to have added the [Consent](/components/consent/) component added to the head of the page. You will also need to obtain your site id and privacy manager id from Sourcepoint, these are different from the account id used with the [Consent](/components/consent/) component.

Usage
-----

Props
-----

The consent settings link supports any prop valid on the [Link](/components/link/) component. If click event is passed to this component, it can handle it along with the opening of the Sourcepoint CMP privacy manager.

Custom and required props are detailed below:

privacyManagerIdstring

Your privacy manager id.

siteIdstring

Your Sourcepoint site id. This is used for the legacy TCFv1 sourcepoint script.  
  
The legacy TCFv2 script only needs privacy manager id.

gdprboolean

If you're using the unified Sourcepoint script for GDPR.

ccpaboolean

If you're using the unified Sourcepoint script for CCPA.

tabToOpen'purposes' | 'vendors' | 'features' | 'purposes-li' | 'vendors-li'

If you're using the unified Sourcepoint script for GDPR, you can choose the opening view of the modal.

childrenReactNode = Manage Consent

The content of the link. Can be undefined and left to default text.

[See tabToOpen options](https://docs.sourcepoint.com/hc/en-us/articles/4402697202323)