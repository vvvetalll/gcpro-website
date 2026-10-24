# Enquiry forms: decision brief — 24 October 2026

**Recommendation for approval:** one short, single-step Request Service form with **Name, Phone, City or ZIP required**; Service needed defaults to **Not sure** and is optional; brief description and email optional. Contact Us: **Name, Email, Message required**, Phone optional. Do not copy the current long loss questionnaire.

Analysis only. No pages, forms, links, settings or notification recipients changed. No form submitted, company contacted, CAPTCHA solved or real personal information entered.

## Current-form comparison

Inspected current rendered pages in the connected browser, including390px mobile. R = marked required in visible labels/HTML `required`/`aria-required`; O = no such requirement exposed. **Server enforcement, submission success, delivery and callback performance are unverified for every site.** Counts exclude hidden technical fields, honeypots, search/newsletter forms and duplicate responsive forms. All inspected enquiry flows showed one rendered page/step; ATI uses conditional fields, not an observed wizard.

| Site / actual URL / form placement | Current fields and requirement | Button, telephone alternative and stated next step | Mobile / friction observed |
|---|---|---|---|
| **GCPRO Request**, [production](https://gcprochicago.com/service-request/). Dedicated page; long main form exists in DOM but is **hidden**; a separate Footer form is visible. | Hidden long form:23 entry controls/groups (radio choices grouped; address parts/email confirmation separate),11 marked-required subcontrols. Name split, phone, email+confirmation, full address, damage/room questions, materials, insurance carrier, loss date, details, SMS. Visible Footer: name/email/phone/comments R; SMS checkbox not marked required. | Hidden button Request Service; visible Footer button Submit. Large telephone alternative precedes Footer form,847-656-3322. No specific form-follow-up timing observed. | Main wrapper `gform_wrapper_2` remained `display:none` on desktop/mobile; its DOM inventory is **not** proof of an accessible working form. Footer fields stack,50px inputs,120px comments;13px consent checkbox. Two smsConsent IDs exist on this page; visible Footer checkbox lacked associated label in that inspection. No submit validation tested. |
| **GCPRO Contact**, [production](https://gcprochicago.com/contact-us/). Contact details page; form embedded far down in shared Footer. | Name/email/phone/comments R; SMS checkbox not marked required. | Submit. Office number/contact call actions precede form; no specific post-submit expectation. |335px form at390px viewport, four stacked fields. Long intervening page content puts form well below initial viewport; both email and phone compulsory in markup. |
| **Restore Construction**, [Contact](https://restoreconstruction.com/contact-us/). Dedicated Contact page with embedded request form. | Request type, full name, phone, email, ZIP R; brief description O. | Submit Request. Body telephone before form; current observed local number847-321-7294.24/7 availability claimed; no explicit form-reply deadline observed. | Visible labels; tel/email types. ZIP uses number input rather than text. Several misspelled service options; no Not sure, but an Other-like choice.375px form at390px. |
| **ServiceMaster of Lincoln Park**, [Contact](https://servicemasteroflincolnpark.com/contact/). Dedicated Contact page plus separate Footer form. | Main: name/email R; phone/address/subject/message O. Footer differs: name/email/phone R, message O. | Send. Emergency phone773-346-6767 at top. No specific post-submit timing observed. | Some main captions lack associated HTML labels; phone/email pairs remain in narrow columns. Page horizontal overflow observed at390px; cause not isolated. Main/Footer requirements conflict. |
| **ATI**, [Contact](https://atirestoration.com/contact-us/). Dedicated corporate contact page. | Initially first/last name,email,phone,ZIP,reason R; optional marketing/SMS boxes. Choosing New damage reveals required requester-role selection. Further conditional company/title/category/details controls exist; their complete branch visibility was not tested. | Submit.800-400-9353 prominently above form; page claims response within24 hours and directs immediate needs to telephone. That is ATI's claim, not measured performance. |327px form; visible labels. Phone is text input without tel inputmode. Conditional routing increases effort; this corporate/mixed-enquiry model is broader than a simple GCPRO callback. |
| **GoDry Chicago**, [Contact](https://godrychicago.com/contact). Dedicated page, embedded evaluation form. | First/last name,email,phone,ZIP,service,comments. No required markers/HTML requirement exposed; **do not infer server-side optionality**. | Submit.855-662-1744 and call alternatives; on-site response claim, not an observed form-reply commitment. | Form appeared after asynchronous rendering; initial empty observation was not counted as no form.288px form at390px. Mainly placeholder prompts rather than persistent field labels. |
| **Romexterra**, [homepage request section](https://www.romexterra.com/). Embedded form; another responsive/modal form exists. | Name,phone,email,damage type R; description O. Off-screen company_website honeypot excluded. | Send Service Request → on primary form; secondary form says Request Service. Current observed phone312-756-0210. Page distinguishes urgent calls from non-emergency forms and claims one-business-day replies. |335px primary form, stacked controls; labels and tel/email types. Short service choice plus optional description is a useful structural example. Do not transfer its callback/response claims or service capabilities. |
| **ServiceMaster by Zaba**, [Contact](https://www.servicemasterbyzaba.com/contact-us/). Dedicated page, embedded enquiry form. | First/last name,phone,email,ZIP,message R; CAPTCHA present. | Get help now. Chicago773-647-1985 / suburbs847-730-7301 call alternatives. No specific form-reply deadline observed. |335px form,903px measured form height at390px; persistent labels, tel/email types. Mandatory message and both contact channels add effort; CAPTCHA completion not tested. |

These are **observed design choices, not evidence of conversion effectiveness**. No conversion rates, form abandonment rates or ranking claims are available. Current browser observations take precedence over indexed snippets: some phone numbers/button wording differed.

## The two recommended forms

| Field | Request Service | Contact Us | Reason |
|---|---|---|---|
| Name | Required; one field | Required; one field | Enough to identify/greet the person; no first/last split. |
| Phone | Required, native tel | Optional | Callback contact for service requests; avoid forcing it on a person asking an email question. |
| City or ZIP code | Required, plain text | Omit | Initial locality/coverage discussion; not full-address collection or automatic coverage confirmation. |
| Service needed | Optional; default Not sure | Omit | Helpful routing context without forcing a damage diagnosis. Start with approved primary service categories, Other and Not sure; owner confirms routing choices. |
| Brief description | Optional, short textarea | Required Message | Service requester can explain by phone; a general written enquiry needs its actual question. |
| Email | Optional | Required, native email | No verified GCPRO rule requires email before a callback. Contact Us deliberately supports an email reply. |

Request Service has **three required entries**, not a mandatory six-field intake. Keep optional fields visibly marked Optional and use a modest textarea, not a technical questionnaire. No mandatory subject, property type, insurance or photo upload. For someone who wants a call instead of providing email on Contact Us, show the telephone and Request Service route.

**Button:** use **Send Service Request** while handling remains unconfirmed. **Request a Callback** is the preferred intent label once the owner confirms that an operator actually returns these requests. Neither wording promises a deadline or dispatch. Contact: **Send Message**. Do not use Book Now, Dispatch Now or instant-help promises for an unverified workflow.

**Next-step copy, proposed:** explain that submitted details allow the team to follow up about the enquiry, with the existing phone as an alternative. Publish a received confirmation only after successful backend acceptance is demonstrated. Do not promise a callback time, live operator availability, booking, dispatch or an automatic email receipt. Error copy should offer retry and the phone number; input preservation must be tested at implementation.

## What to remove from initial enquiry collection

| Current element | Recommendation |
|---|---|
| First/last split | Replace with one Name field. |
| Required email plus confirmation | Optional single email for Request Service; no confirmation retyping. |
| Street/unit/city/state/ZIP address group | Replace with City or ZIP initially. Obtain/verify full service address before any visit/dispatch, during follow-up. |
| Rooms affected, standing water, damage-level terminology, power, flooring/walls/ceiling, cause addressed, mandatory loss date | Collect relevant details in the operator's follow-up, not as a barrier to contact. Do not ask customers to classify deterioration/materials to request a call. |
| Insurance carrier | Defer. Policy/claim numbers and insurance handling can be discussed when relevant and through approved channels. They are not a verified prerequisite for a callback. |
| Details | Retain as optional service context; required only as the general Contact message. |
| SMS consent | Do not silently carry over as compulsory or equate marketing permission with requesting a phone call. Confirm whether SMS is actually used and obtain approved wording/behavior. |
| Photos / policy numbers | Not observed as fields in the current long DOM form; **do not add** initially. Request later only when needed via a confirmed handling channel. |

## Page and mobile structure

Use existing design tokens/native controls. Request Service: concise H1/intro, clickable847-656-3322 **before the form**, one inset form panel, a brief factual what-happens-next note, usual Footer. Avoid a tall photographic Hero, reviews/logo sections or SEO text between intent and form. Contact: short heading; phone, existing approved email/address/directions; short form. Desktop can pair contact details and form; mobile stacks phone → form → address/directions. Confirm office hours rather than inventing them.

One column on mobile; existing20px page gutters and8px radius, familiar typography/colors. Recommend48px controls,16px input text, persistent associated labels, full-width submit and concise Optional markers. Do not force the entire form into one screen, shrink text or add a wizard. No photographs or insurance upload in phase1. Preserve the existing Footer and approved inset CTA convention. These are proposed layouts, not implemented pages.

## Installed Atomic feasibility — read-only

MCP discovery and live native editor inspection of existing Popup1801/Form51db3f70 establish:

- Atomic input types text/email/number/tel/password/url; textarea, select, label, checkbox/radio, date/time, file upload and submit elements exist. Proposed basic fields need no custom code/plugin. Label input-id and input _cssid support association; required toggles exist. Tel type is **not** proof of phone-number validity checking.
- Select options/default value/multiple/required; textarea rows and min/max length; autocomplete is exposed as a **boolean**, not token-specific name/tel/postal-code choices in the typed schema. Input pattern/inputmode are not exposed there. Generic Attributes controls exist, but their field-level behavior was not tested. Keep City or ZIP permissive rather than inventing a brittle validator.
- Live Actions after submit list: **Email, Email2, Collect submissions, Webhook**. Email controls include recipient, subject/body, From/name, Reply-to, cc/bcc, metadata and HTML/plain format; UI documents [all-fields] and @ field insertion. Their existence does not verify mailbox ownership or delivery. Current editor default recipient is not an approved operator routing decision.
- Native default/success/error states and required success/error containers are available; containers can hold editable native text children. No submission/error/notification runtime test occurred. The existing coverage popup intercepts sending with its authorized local code; it is **not** proof that an enquiry sends successfully.
- No dedicated Atomic CAPTCHA/honeypot widget or form anti-spam property/control was demonstrated. Do not assume legacy Elementor Form reCAPTCHA automatically applies. Native supported spam protection and delivery must be confirmed before launch; do not substitute custom code/install a plugin. No native multistep/conditional-intake behavior was demonstrated or is needed here.

The **field/layout proposal is feasible**; routing, delivery, spam protection and truthful receipt behavior remain launch gates. Email2 auto-replies are unnecessary for the optional-email callback form unless supported empty-email handling is verified. Collect submissions is available, but retention/access policy needs approval.

## Exact owner questions before implementation/launch

1. Which monitored inbox/CRM receives each form, who owns follow-up, and who covers missed/unanswered enquiries?
2. Are these genuinely callback requests? What are staffed handling hours and after-hours/urgent-request instructions? No deadline will be published without confirmation.
3. Is email ever mandatory before first contact? If so, what operational task requires it?
4. Is city or ZIP enough for initial routing; which service categories should reach which operator? Coverage remains address-confirmed, not automatic.
5. Are SMS replies actually used? What approved consent/privacy wording and optionality should apply?
6. Which approved sender/recipient, storage retention/access, native spam protection and controlled delivery-test process will be used? Who approves customer-facing success/error wording?

## Evidence and limitations

Current browser fields/labels/DOM, mobile geometry and installed schemas/UI inspected24 October2026 (America/Chicago); no production/admin writes. Form requirements are annotations, not tested server rules. No competitor submission, empty-submit validation, real personal data, CAPTCHA completion or callback test. Asynchronous forms and hidden GCPRO main form are explicitly distinguished from zero-content pages. Mobile emulation is not a physical-phone keyboard/accessibility audit.

Prior sources: [October22 competitor dossiers](../seo/2026-10-22-deep-competitive-research/COMPETITOR_DOSSIERS.md) identify form/CTA patterns but do not establish current requiredness, validation or conversion; [October24 content-depth competitors](../seo/2026-10-24-content-depth-audit/COMPETITORS.md) supply relevant service competitors; [availability popup record](../components/service-availability-popup.md) describes a local coverage lookup, not an enquiry intake. Current observations were rechecked independently. [Sanitized evidence](2026-10-24-enquiry-forms-evidence.json). Publish button remained disabled when exiting native editor; no save/publish action performed.
