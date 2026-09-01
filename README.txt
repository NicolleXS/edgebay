EDGEBAY INTERNATIONAL — WEBSITE
================================

Contents
--------
index.html          The homepage
css/style.css       All styling (colors, layout, responsive rules)
images/             Hero photo, US route map (SVG), icons, favicon
                    truck-cutout.jpg is a spare brand asset for future pages

How to publish
--------------
Upload the whole folder to any web host (cPanel public_html, Netlify,
Vercel, GitHub Pages...). No build step needed — it is plain HTML/CSS.

Quote form
----------
The form currently shows a confirmation message on submit but does not
send data anywhere. To receive submissions, connect it to a service like
Formspree/Basin or your own endpoint: in index.html, find the
"quote-form" script block at the bottom and replace it with a POST to
your endpoint (or add action="https://formspree.io/f/YOUR_ID"
method="POST" to the <form> tag and delete the script block).

Editing basics
--------------
- Phone number appears in 3 places in index.html (header, CTA, footer).
- Brand colors are defined once at the top of css/style.css (:root).
- The © year in the footer is at the very bottom of index.html.
