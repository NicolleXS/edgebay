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

Quote form
----------
Both quote forms (homepage + contact) send to office@edgebayintl.com
through FormSubmit (https://formsubmit.co). IMPORTANT: the very first
submission triggers a one-time activation email to office@edgebayintl.com —
click "Activate" in that email, after which every request is delivered.

Editing basics
--------------
- Phone / WhatsApp / email / social links are constants at the top of
  build_pages.py (and repeated in index.html).
- Brand colors are defined once at the top of css/style.css (:root).
