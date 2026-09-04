EDGEBAY INTERNATIONAL — WEBSITE
================================

Contents
--------
index.html                 Homepage
services.html              Services overview
open-transport.html        Service pages (one per service)
enclosed-transport.html
door-to-door.html
expedited-shipping.html
motorcycle-transport.html
boat-transport.html
rv-motorhome-transport.html
how-it-works.html, about.html, faq.html, contact.html
css/style.css              All styling (colors, layout, responsive rules)
images/                    Hero photo, US route map (SVG), icons, favicon
images/photos/             Real shipment photos used on the service pages
build_pages.py             Generator for all pages except index.html
                           (edit it, run `python3 build_pages.py`)

How to publish
--------------
The repo is connected to Vercel — every push to `main` redeploys.
No build step: plain HTML/CSS.

URLs are extension-less (/services, /contact, and / for home) thanks to
vercel.json ("cleanUrls": true). Vercel redirects /services.html to
/services automatically, so any old link keeps working. Internal links
and asset paths are root-relative (/css/..., /images/...) — keep them
that way when editing; build_pages.py rewrites them automatically.

Quote form
----------
Both quote forms (homepage + contact) send to office@edgebayintl.com
through FormSubmit (https://formsubmit.co).

The form tries a background (AJAX) submission first, which keeps the
visitor on the page and shows an inline confirmation. If that call is
refused — which is what happens while the address is not activated yet,
and also if a browser blocks the request — it automatically falls back to
a normal form POST, so a request is never lost. After a normal POST the
visitor lands on /thank-you.

The form posts to FormSubmit's endpoint id
3b673ecd1a4559d5bd2236870bc46c29, which is tied to office@edgebayintl.com.
Using the id instead of the address keeps the mailbox out of the page
source, away from spam harvesters. To change the destination address,
create a new endpoint on formsubmit.co and replace FORM_ID in
build_pages.py (and in index.html).

ACTIVATION (one time only): submit the form once on the live site, then
click "Activate Form" in the email FormSubmit sends to
office@edgebayintl.com. If that link reports "Not a valid link", it has
usually already been consumed — just submit the form again and check
whether the request arrives.

Editing basics
--------------
- Phone / WhatsApp / email / social links are constants at the top of
  build_pages.py (and repeated in index.html).
- Brand colors are defined once at the top of css/style.css (:root).
