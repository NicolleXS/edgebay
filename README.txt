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

The form does a plain POST to FormSubmit (their documented flow) and the
visitor lands on /thank-you afterwards. An earlier AJAX version was
dropped: it kept the visitor on the page but made delivery failures
invisible, which is the wrong trade for a lead form.

The form posts to FormSubmit's endpoint id
3b673ecd1a4559d5bd2236870bc46c29, which is tied to office@edgebayintl.com.
Using the id instead of the address keeps the mailbox out of the page
source, away from spam harvesters. To change the destination address,
create a new endpoint on formsubmit.co and replace FORM_ID in
build_pages.py (and in index.html).

The endpoint was activated on 4 Sep 2026. If submissions ever stop
arriving, check the spam folder first — FormSubmit sends from its own
servers with the visitor's address as Reply-To, which some filters
dislike. Adding formsubmit.co to the mailbox's allow list fixes it.

Editing basics
--------------
- Phone / WhatsApp / email / social links are constants at the top of
  build_pages.py (and repeated in index.html).
- Brand colors are defined once at the top of css/style.css (:root).
