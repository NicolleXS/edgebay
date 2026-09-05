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
Both quote forms (homepage + contact) post to Web3Forms, which delivers
to office@edgebayintl.com:

  action="https://api.web3forms.com/submit"
  access_key = 71df5154-5feb-443c-ae07-0295153b6a6c

The key is public by design (it lives in the page source) and only says
where the message goes. Change the destination address at web3forms.com
and replace WEB3FORMS_KEY in build_pages.py (and in index.html).

A "redirect" field sends the visitor to /thank-you after submitting, and
a hidden "botcheck" checkbox filters bots.

FormSubmit was used first and dropped: it accepted the submissions but
never delivered them, most likely because it sends with the visitor's
address as the sender, which fails SPF/DMARC at the receiving server.

Editing basics
--------------
- Phone / WhatsApp / email / social links are constants at the top of
  build_pages.py (and repeated in index.html).
- Brand colors are defined once at the top of css/style.css (:root).
