#!/usr/bin/env python3
"""Generates the Edgebay interior pages with shared header/footer."""

PHONE = "(310) 634-1017"
TEL = "tel:+13106341017"
WA_NUMBER = "+1 (727) 654-9418"
WA = "https://wa.me/17276549418?text=Hi%20Edgebay%2C%20I%27d%20like%20a%20quote%20for%20shipping%20my%20vehicle."
EMAIL = "office@edgebayintl.com"
FB = "https://www.facebook.com/profile.php?id=61573226470889"
IG = "https://www.instagram.com/edgebay.intl"
TT = "https://www.tiktok.com/@edgebayintl"
YEAR = "2026"

BADGE = '''<svg class="logo-badge" viewBox="0 0 54 62" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="1.5" y="1.5" width="51" height="59" rx="5" stroke="#0642a0" stroke-width="2.6"/>
        <g stroke="#0642a0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M15 10.5h24"/><rect x="15.5" y="14" width="23" height="11" rx="1.5"/>
          <path d="M15.5 25v12M38.5 25v12"/><path d="M11 18.5h4.5M38.5 18.5H43"/><path d="M11 18.5v8M43 18.5v8"/>
          <rect x="19.5" y="28" width="15" height="9" rx="1"/>
          <path d="M22.5 30.5h9M22.5 33h9M22.5 35.5h9" stroke-width="1.3"/>
          <path d="M10.5 40.5h33v4.5a1.5 1.5 0 0 1-1.5 1.5H12a1.5 1.5 0 0 1-1.5-1.5z"/>
          <path d="M13.5 43.5h5M35.5 43.5h5" stroke-width="1.4"/>
        </g>
        <text x="27" y="55.5" text-anchor="middle" font-family="Montserrat, sans-serif" font-weight="800" font-size="6.2" letter-spacing="1.6" fill="#0642a0">EDGEBAY</text>
      </svg>'''

FBADGE = BADGE.replace('stroke="#0642a0" stroke-width="2.6"', 'FOO').replace('#0642a0', '#01204a').replace(
    '<rect x="1.5" y="1.5" width="51" height="59" rx="5" FOO/>',
    '<rect x="1" y="1" width="52" height="60" rx="6" fill="#ffffff"/>')

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
PIN_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
MAIL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>'
CLOCK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="{c}"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'

FB_SVG = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M14 8.5h3V5h-3c-2.2 0-4 1.8-4 4v2.5H7.5V15H10v7h3.5v-7h2.7l.55-3.5H13.5V9.5c0-.6.4-1 1-1z" transform="translate(-0.5 -1)"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="0.6" fill="#ffffff" stroke="none"/></svg>'
TT_SVG = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M12.53.02C13.84 0 15.14.01 16.44 0c.08 1.53.63 3.09 1.75 4.17 1.2 1.11 2.89 1.62 4.51 1.8v4.03c-1.52-.05-3.05-.37-4.43-1.02-.6-.27-1.16-.62-1.71-.98-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'

CHECK = '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="11" fill="#e2ebfa"/><path d="m7.6 12.3 2.9 2.9 6-6.2" stroke="#0642a0" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CAR_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/></svg>'
GARAGE_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M12 2.5 2.5 9v12.5h4V13h11v8.5h4V9L12 2.5zM8.2 15h7.6c.4 0 .76.24.92.6l.78 1.9v3a.5.5 0 0 1-.5.5h-.5a.5.5 0 0 1-.5-.5v-.5H8v.5a.5.5 0 0 1-.5.5H7a.5.5 0 0 1-.5-.5v-3l.78-1.9c.16-.36.52-.6.92-.6zm.05 1.5-.55 1.4h8.6l-.55-1.4h-7.5z"/></svg>'
US_ICON = '<img src="images/us-icon.png" alt="" aria-hidden="true">'
BOLT_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M13 2 3.5 14H10l-1 8 9.5-12H12l1-8z"/></svg>'
MOTO_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="5.3" cy="16.8" r="3"/><circle cx="18.7" cy="16.8" r="3"/><path d="M5.3 16.8 8.6 10h2.6l2.2 3.4h3l2.3 3.4"/><path d="M8.6 10 7.4 7.8H5.2"/><path d="M13.4 13.4 15 9h2.4"/></svg>'
SHIELD_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M12 1.8 3.5 5v6.4c0 5.35 3.55 9.86 8.5 11.1 4.95-1.24 8.5-5.75 8.5-11.1V5L12 1.8zm-1.55 14.15-3.3-3.3 1.4-1.4 1.9 1.9 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>'
BOAT_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M4 15.2 5.6 10.5h13L20.2 15c-1.1.7-2.2 1-3.3 1-1.4 0-2.4-.7-3.7-.7s-2.3.7-3.7.7c-1.2 0-2.3-.3-3.5-.8zM7.6 9.5V6h4.3l2.6 3.5H7.6z"/><path d="M2 18.6c1.3.8 2.6 1.2 3.9 1.2 1.4 0 2.4-.7 3.7-.7s2.3.7 3.7.7 2.4-.7 3.7-.7 2.3.7 3.7.7c1.3 0 2.6-.4 3.9-1.2v-1.8c-1.3.8-2.6 1.2-3.9 1.2-1.4 0-2.4-.7-3.7-.7s-2.3.7-3.7.7-2.4-.7-3.7-.7-2.3.7-3.7.7c-1.3 0-2.6-.4-3.9-1.2z" opacity=".85"/></svg>'
RV_ICON = '<svg viewBox="0 0 24 24" fill="#ffffff"><path d="M2 7.5A2.5 2.5 0 0 1 4.5 5H16l4.6 4.6H21a1 1 0 0 1 1 1V16a1 1 0 0 1-1 1h-1.3a2.7 2.7 0 0 1-5.2 0H9.5a2.7 2.7 0 0 1-5.2 0H3a1 1 0 0 1-1-1zM5.3 7.8v3.4h4.2V7.8zm6.2 0v3.4h4.9l-3.4-3.4z"/><circle cx="6.9" cy="17" r="1.4" fill="#0642a0"/><circle cx="17.1" cy="17" r="1.4" fill="#0642a0"/></svg>'

SERVICES = [
    ('open-transport.html', 'Open Transport'),
    ('enclosed-transport.html', 'Enclosed Transport'),
    ('door-to-door.html', 'Door-to-Door Service'),
    ('expedited-shipping.html', 'Expedited Shipping'),
    ('motorcycle-transport.html', 'Motorcycle Transport'),
    ('boat-transport.html', 'Boat Transport'),
    ('rv-motorhome-transport.html', 'RV &amp; Motorhome Transport'),
]


def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
</head>
<body>
'''


def nav_links(cls):
    drop = '\n'.join(f'          <a href="{h}">{n}</a>' for h, n in SERVICES)
    mob = '\n'.join(f'      <a href="{h}">{n}</a>' for h, n in SERVICES)
    return drop, mob


def header(active):
    def cls(k):
        return ' class="active"' if k == active else ''
    drop, mob = nav_links(cls)
    return f'''<!-- ================= HEADER ================= -->
<header class="site-header site-header--solid">
  <div class="container header-inner">
    <a href="index.html" class="logo" aria-label="Edgebay International — Home">
      {BADGE}
      <span class="logo-text">
        <span class="logo-line1">EDGEBAY</span>
        <span class="logo-line2">INTERNATIONAL</span>
      </span>
    </a>
    <nav class="main-nav" aria-label="Main navigation">
      <a href="index.html"{cls('home')}>Home</a>
      <span class="nav-drop">
        <a href="services.html"{cls('services')}>Services <span class="nav-caret"></span></a>
        <span class="dropdown-menu"><span class="dropdown-inner">
          <a href="services.html" class="all">All Services</a>
{drop}
        </span></span>
      </span>
      <a href="how-it-works.html"{cls('how')}>How It Works</a>
      <a href="about.html"{cls('about')}>About Us</a>
      <a href="faq.html"{cls('faq')}>FAQ</a>
      <a href="contact.html"{cls('contact')}>Contact Us</a>
    </nav>
    <a class="header-phone" href="{TEL}">
      <span class="phone-icon-circle">{PHONE_SVG.format(c='#ffffff', w='2')}</span>
      <span>
        <span class="phone-number">{PHONE}</span>
        <span class="phone-hours">Mon - Fri: 9AM - 6PM EST</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span><span></span><span></span></button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation">
    <a href="index.html"{cls('home')}>Home</a>
    <a href="services.html"{cls('services')}>Services</a>
    <div class="mobile-sub">
{mob}
    </div>
    <a href="how-it-works.html"{cls('how')}>How It Works</a>
    <a href="about.html"{cls('about')}>About Us</a>
    <a href="faq.html"{cls('faq')}>FAQ</a>
    <a href="contact.html"{cls('contact')}>Contact Us</a>
    <a class="mobile-call" href="{TEL}">Call {PHONE}</a>
  </nav>
</header>
'''


def banner(title, crumb):
    return f'''<section class="page-banner">
  <div class="container">
    <h1>{title}</h1>
    <p class="breadcrumb"><a href="index.html">Home</a><span class="sep">/</span>{crumb}</p>
  </div>
</section>
'''


CTA_BAND = f'''<!-- ================= CTA ================= -->
<section class="cta-band">
  <div class="container">
    <h2>Ready to Ship Your Vehicle?</h2>
    <p>Get your free, no-obligation quote today — it only takes a minute.</p>
    <div class="actions">
      <a href="index.html#quote" class="btn btn-white">Get a Free Quote</a>
      <a href="{TEL}" class="btn btn-red">Call {PHONE}</a>
    </div>
  </div>
</section>
'''

FOOTER_SERVICE_LINKS = '\n'.join(f'        <li><a href="{h}">{n}</a></li>' for h, n in SERVICES)

FOOTER = f'''<!-- ================= FOOTER ================= -->
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <div class="flogo">
        {FBADGE}
        <span>
          <span class="logo-line1">EDGEBAY</span>
          <span class="logo-line2">INTERNATIONAL</span>
        </span>
      </div>
      <p>A trusted, licensed auto transport broker based in Atlanta, Georgia, coordinating safe and reliable vehicle transport across all 50 states.</p>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="how-it-works.html">How It Works</a></li>
        <li><a href="about.html">About Us</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Our Services</h4>
      <ul class="footer-links">
{FOOTER_SERVICE_LINKS}
      </ul>
    </div>
    <div>
      <h4>Contact Info</h4>
      <ul class="footer-contact">
        <li>{PHONE_SVG.format(c='#7f9ecb', w='1.8')}<a href="{TEL}">{PHONE}</a></li>
        <li>{WA_SVG.format(c='#7f9ecb')}<a href="{WA}" target="_blank" rel="noopener">WhatsApp {WA_NUMBER}</a></li>
        <li>{MAIL_SVG.format(c='#7f9ecb', w='1.8')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{PIN_SVG.format(c='#7f9ecb', w='1.8')}<span>Atlanta, Georgia, USA</span></li>
        <li>{CLOCK_SVG.format(c='#7f9ecb', w='1.8')}<span>Mon - Fri: 9AM - 6PM EST</span></li>
      </ul>
    </div>
    <div>
      <h4>Stay Connected</h4>
      <div class="social-row">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a>
        <a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok">{TT_SVG}</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>&copy; {YEAR} Edgebay International. All Rights Reserved.</span>
      <span><a href="privacy-policy.html">Privacy Policy</a><span class="sep">|</span><a href="terms-of-service.html">Terms of Service</a></span>
    </div>
  </div>
</footer>

<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_SVG.format(c='#ffffff')}</a>

<script>
  (function () {{
    var header = document.querySelector('.site-header');
    var toggle = document.querySelector('.nav-toggle');
    if (!header || !toggle) return;
    toggle.addEventListener('click', function () {{
      var open = header.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }});
  }})();
</script>
</body>
</html>
'''

FORM_SCRIPT = f'''<script>
  (function () {{
    var form = document.getElementById('quote-form');
    if (!form) return;
    var btn = form.querySelector('.btn-submit');
    var ok = document.getElementById('form-success');
    var err = document.getElementById('form-error');
    form.addEventListener('submit', function (e) {{
      e.preventDefault();
      var data = {{}};
      new FormData(form).forEach(function (v, k) {{ data[k] = v; }});
      if (data._honey) return;
      data.customer_email = data.email || '';
      data._subject = 'New quote request from ' + (data.name || 'website');
      data._template = 'table';
      btn.disabled = true; var label = btn.textContent; btn.textContent = 'Sending...';
      ok.hidden = true; err.hidden = true;
      fetch('https://formsubmit.co/ajax/{EMAIL}', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json', 'Accept': 'application/json' }},
        body: JSON.stringify(data)
      }}).then(function (r) {{ return r.json().then(function (j) {{ return {{ okStatus: r.ok, body: j }}; }}); }})
        .then(function (res) {{
          if (res.okStatus && (res.body.success === 'true' || res.body.success === true)) {{
            ok.hidden = false; form.reset(); btn.textContent = 'Request Sent \\u2713';
          }} else {{ throw new Error('bad'); }}
        }})
        .catch(function () {{ err.hidden = false; btn.disabled = false; btn.textContent = label; }});
    }});
  }})();
</script>'''


def quote_form():
    return f'''      <form id="quote-form" class="form-grid" autocomplete="on">
        <div class="field"><input type="text" name="name" placeholder="Full Name" required></div>
        <div class="field"><input type="email" name="email" placeholder="Email Address" required></div>
        <div class="field"><input type="tel" name="phone" placeholder="Phone Number" required></div>
        <div class="field">
          <select name="vehicle_type" required>
            <option value="" disabled selected hidden>Vehicle Type</option>
            <option>Sedan</option><option>SUV</option><option>Pickup Truck</option><option>Van</option>
            <option>Motorcycle</option><option>Boat</option><option>RV / Motorhome</option><option>Other</option>
          </select>
          <span class="field-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></span>
        </div>
        <div class="field"><input type="text" name="pickup" placeholder="Pick Up Location" required></div>
        <div class="field"><input type="text" name="delivery" placeholder="Delivery Location" required></div>
        <div class="field full">
          <input type="text" name="date" placeholder="Preferred Pick Up Date" onfocus="this.type='date'" onblur="if(!this.value)this.type='text'">
          <span class="field-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></span>
        </div>
        <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="display:none">
        <button type="submit" class="btn-submit full">Get My Free Quote</button>
        <p class="secure-note full">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          Your information is secure and will never be shared.
        </p>
        <p class="secure-note full" id="form-success" hidden style="color:#1a7f37;font-weight:500;">Thank you! Your quote request has been received — we'll get back to you shortly.</p>
        <p class="secure-note full" id="form-error" hidden style="color:#b42318;font-weight:500;">Something went wrong. Please call us at {PHONE} or email {EMAIL}.</p>
      </form>'''


def checks(items):
    lis = '\n'.join(f'        <li>{CHECK}<span>{i}</span></li>' for i in items)
    return f'      <ul class="check-list">\n{lis}\n      </ul>'


def info_cards(cards):
    out = '\n'.join(
        f'      <div class="info-card"><h3>{t}</h3><p>{p}</p></div>' for t, p in cards)
    return f'    <div class="info-cards">\n{out}\n    </div>'


def other_svcs(exclude):
    links = '\n'.join(
        f'        <a href="{h}">{n}</a>' for h, n in SERVICES if h != exclude)
    return f'''    <div class="other-svcs">
      <h3>Explore our other services</h3>
      <div class="chip-row">
{links}
      </div>
    </div>'''


MAP_FRAME = '''    <div class="photo-frame map-frame">
      <div class="map-card">
        <img src="images/us-map.svg" alt="Map of the United States with a transport route from the West Coast to the East Coast">
        <span class="map-tag">''' + PIN_SVG.format(c='#0642a0', w='2') + ''' Door to door, all 50 states</span>
      </div>
    </div>'''


def photo_frame(img, alt, badge):
    return f'''    <div class="photo-frame">
      <img src="images/photos/{img}.jpg" alt="{alt}" loading="lazy">
    </div>'''


def gallery(items, title='On the Road with Edgebay', intro='A look at the kinds of vehicles our carrier network moves every day.'):
    if not items:
        return ''
    cols = ' cols-2' if len(items) == 2 else ''
    figs = '\n'.join(
        f'''      <figure class="gallery-item">
        <img src="images/photos/{img}.jpg" alt="{alt}" loading="lazy">
        <figcaption class="cap">{alt}</figcaption>
      </figure>''' for img, alt in items)
    return f'''
<section class="page-section">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">{title}</h2>
    <div class="center-bar"></div>
    <p class="gallery-intro">{intro}</p>
    <div class="gallery-grid{cols}">
{figs}
    </div>
  </div>
</section>
'''


def service_page(fname, nav_title, h1, title, desc, icon, intro_h2, paras, checklist, cards,
                 hero_photo=None, hero_alt='', hero_badge='Real Edgebay shipment', gal=None, map_visual=False):
    body = head(title, desc) + header('services') + banner(h1, f'<a href="services.html">Services</a><span class="sep">/</span>{nav_title}')
    paras_html = '\n'.join(f'      <p class="content-p">{p}</p>' for p in paras)
    if map_visual:
        visual = MAP_FRAME
    elif hero_photo:
        visual = photo_frame(hero_photo, hero_alt, hero_badge)
    else:
        visual = f'    <div class="illus-panel"><div class="big-icon">{icon}</div></div>'
    body += f'''
<section class="page-section">
  <div class="container two-col">
    <div>
      <h2>{intro_h2}</h2>
{paras_html}
{checks(checklist)}
    </div>
{visual}
  </div>
</section>

<section class="page-section alt">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">Good to Know</h2>
    <div class="center-bar"></div>
{info_cards(cards)}
{other_svcs(fname)}
  </div>
</section>
{gallery(gal or [])}
''' + CTA_BAND + FOOTER
    open(f'/root/edgebay/{fname}', 'w').write(body)


# ----------------------------------------------------------------- services
service_page(
    'open-transport.html', 'Open Transport', 'Open Transport',
    'Open Auto Transport — Edgebay International',
    'Cost-effective open carrier auto transport across all 50 states. Get a free quote from Edgebay International, a licensed Atlanta-based broker.',
    CAR_ICON,
    'The Smart, Affordable Standard',
    ["Open transport is the most popular way to ship a vehicle in the United States — the same method dealerships and manufacturers use every day. Your car travels securely strapped onto an open multi-car carrier, handled by a vetted, fully insured professional driver.",
     "Because open carriers move more vehicles per trip, this is the most economical option, with the widest choice of pickup dates on virtually every route."],
    ["The most cost-effective transport option", "Fastest carrier availability nationwide",
     "Ideal for sedans, SUVs, pickups, and vans", "Full carrier insurance included during transit",
     "Door-to-door pickup and delivery included"],
    [("Best For", "Daily drivers, family cars, SUVs, and any vehicle where value and reliability matter more than white-glove handling."),
     ("Pricing Factors", "Distance, vehicle size and weight, route popularity, and season all shape your rate. Popular routes cost less thanks to steady carrier availability."),
     ("Timing", "Most pickups happen within a few days of booking. Cross-country runs typically deliver in 7–10 days; regional moves much faster.")],
    hero_photo='open-carrier-suv', hero_alt='Open multi-car carrier loaded with SUVs on the highway',
    gal=[('open-carrier-porsche', 'Open carrier loaded with Porsche and Audi sports cars'),
         ('open-carrier-mercedes', 'Brand-new Mercedes SUVs on an open carrier'),
         ('exotic-ferrari-flatbed', 'Ferrari loaded on an open flatbed carrier')])

service_page(
    'enclosed-transport.html', 'Enclosed Transport', 'Enclosed Transport',
    'Enclosed Auto Transport — Edgebay International',
    'Enclosed trailer transport for luxury, classic, and exotic vehicles. Maximum protection, coordinated by Edgebay International.',
    GARAGE_ICON,
    'Maximum Protection for Special Vehicles',
    ["When the vehicle is irreplaceable, enclosed transport is the answer. Your car rides inside a fully enclosed trailer, shielded from weather, road debris, and prying eyes from pickup to delivery.",
     "Enclosed carriers typically move only a few vehicles at a time, use soft tie-down systems and liftgates where needed, and are operated by drivers who specialize in high-value vehicles."],
    ["Complete protection from weather and road debris", "Soft straps and low-clearance loading available",
     "Higher cargo insurance coverage than open transport", "Discreet transport for high-value vehicles",
     "Preferred for luxury, classic, exotic, and show cars"],
    [("Best For", "Luxury, classic, exotic, and collector cars — or any vehicle you want treated with extra care, including brand-new purchases."),
     ("Pricing Factors", "Enclosed transport typically costs more than open due to limited capacity and specialized equipment. Value protection usually outweighs the difference."),
     ("Timing", "Enclosed carriers are fewer on the road, so allow a little more flexibility on pickup dates — we plan the schedule with you.")],
    hero_photo='enclosed-ferrari', hero_alt='Ferrari secured inside an enclosed transport trailer',
    gal=[('enclosed-porsche', 'Porsche GT2 RS loaded in an enclosed trailer'),
         ('enclosed-mclaren', 'McLaren inside a fully enclosed carrier'),
         ('enclosed-sportscar', 'Open-top sports car secured in an enclosed trailer')])

service_page(
    'door-to-door.html', 'Door-to-Door Service', 'Door-to-Door Service',
    'Door-to-Door Auto Transport — Edgebay International',
    'Convenient door-to-door vehicle pickup and delivery anywhere in the USA, coordinated by Edgebay International.',
    US_ICON,
    'From Your Driveway to the Destination',
    ["No terminals, no extra trips: with door-to-door service, the carrier picks up your vehicle as close to your address as legally and safely possible, and delivers it the same way at the destination.",
     "It works at homes, offices, dealerships, and auctions across all 50 states. If a street is too narrow for a 75-foot carrier, your driver arranges a convenient nearby spot — a parking lot or wide crossroad."],
    ["Pickup and delivery at or near your address", "Available with both open and enclosed transport",
     "Live coordination with your driver by phone", "Works for homes, offices, dealerships, and auctions",
     "Serving all 50 states, including rural areas"],
    [("Best For", "Anyone who values convenience — busy relocations, remote purchases, snowbird moves, and corporate transfers."),
     ("Access Considerations", "Low-hanging trees, gated communities, or tight streets may require meeting the driver nearby. We confirm all details before pickup day."),
     ("Preparation", "Have your vehicle accessible, keys ready, and about a quarter tank of fuel. You or a representative sign the inspection report at both ends.")],
    map_visual=True,
    gal=[('exotic-lamborghini', 'Lamborghini delivered by flatbed right at the destination'), ('exotic-ferrari-red', 'Ferrari picked up on a flatbed at a residential address'),
         ('open-carrier-mercedes', 'Multi-car delivery on an open carrier')])

service_page(
    'expedited-shipping.html', 'Expedited Shipping', 'Expedited Shipping',
    'Expedited Auto Transport — Edgebay International',
    'Need your car moved fast? Expedited vehicle shipping with priority carrier assignment from Edgebay International.',
    BOLT_ICON,
    'When Time Is the Priority',
    ["Sometimes the schedule can't wait — a job that starts Monday, a vehicle sold at auction with storage fees running, a last-minute relocation. Expedited shipping puts your vehicle at the front of the line.",
     "We prioritize your load with our carrier network, target the tightest realistic pickup window, and keep you updated at every stage so you always know where your vehicle is."],
    ["Priority carrier assignment on your route", "Tightest realistic pickup windows — often 24–48 hours",
     "Proactive status updates throughout transit", "Available for both open and enclosed transport",
     "Ideal for auctions, relocations, and deadlines"],
    [("Best For", "Auction purchases with storage deadlines, urgent relocations, dealer trades, and anyone who simply can't wait for standard scheduling."),
     ("Pricing Factors", "Expedited service carries a premium — it buys your spot at the front of the carrier queue. We always quote it transparently up front."),
     ("Honest Expectations", "We commit to realistic windows, not fantasy promises. Weather and traffic still exist — but your load gets priority treatment the whole way.")],
    hero_photo='exotic-ferrari-red', hero_alt='Ferrari loaded on a dedicated flatbed for expedited delivery',
    gal=[('exotic-lamborghini', 'Dedicated flatbed delivery of a Lamborghini'),
         ('exotic-ferrari-flatbed', 'Ferrari on a single-vehicle carrier'),
         ('open-carrier-porsche', 'Priority load on an open carrier')])

service_page(
    'motorcycle-transport.html', 'Motorcycle Transport', 'Motorcycle Transport',
    'Motorcycle Transport — Edgebay International',
    'Safe, specialized motorcycle shipping nationwide — cruisers, sport bikes, and customs — coordinated by Edgebay International.',
    MOTO_ICON,
    'Specialized Care for Two Wheels',
    ["Motorcycles need more than a strap and a ramp. We match your bike with carriers equipped for powersports: wheel chocks, soft tie-downs, and drivers who know how to load and secure two wheels properly.",
     "From cruisers and sport bikes to customs and vintage machines, your motorcycle travels secured upright and protected, with enclosed options available for maximum care."],
    ["Carriers equipped with chocks and soft tie-downs", "Enclosed transport available for full protection",
     "Crated and palletized options for long distances", "Door-to-door pickup and delivery included",
     "Insurance coverage throughout transit"],
    [("Best For", "Relocations, bike purchases from out of state, rally season transport, and seasonal moves south or north."),
     ("Preparation", "Clean the bike for inspection, remove loose accessories, check for leaks, and leave about a quarter tank of fuel."),
     ("Pricing Factors", "Distance, bike size and weight, open vs. enclosed, and seasonality. Enclosed is recommended for high-value and vintage bikes.")],
    hero_photo='motorcycle-flatbed', hero_alt='Motorcycle secured with soft tie-downs on a flatbed carrier',
    gal=[('motorcycle-highway', 'Sport bike strapped down and on the road'),
         ('motorcycle-flatbed', 'Dual-sport motorcycle secured on a flatbed')])

service_page(
    'boat-transport.html', 'Boat Transport', 'Boat Transport',
    'Boat Transport — Edgebay International',
    'Nationwide boat and watercraft hauling on trailers or specialized carriers, coordinated by Edgebay International.',
    BOAT_ICON,
    'Coast to Coast, Lake to Lake',
    ["Whether it's a bass boat, a center console, a pontoon, or a jet ski, we arrange safe overland transport for your watercraft — on your own trailer or on a carrier's hydraulic boat trailer if you don't have one.",
     "We match your boat's length, beam, and height with the right hauler, handle route planning around permit requirements for wide loads, and keep you informed from the ramp to the driveway."],
    ["Trailered boats, jet skis, and pontoons up to oversize dimensions", "Carrier-supplied boat trailers available",
     "Route planning for wide or tall loads, permits handled", "Door-to-door, marina, and dealer pickups",
     "Cargo insurance coverage throughout transit"],
    [("Best For", "Seasonal relocations, out-of-state boat purchases, marina-to-marina moves, and dealer deliveries anywhere in the 50 states."),
     ("Preparation", "Drain fuel to about a quarter tank, remove loose gear and electronics, secure hatches and covers, and note the exact length, beam, and height when requesting a quote."),
     ("Pricing Factors", "Distance, boat dimensions and weight, whether you supply the trailer, and permit needs for oversize loads. We quote it all transparently.")],
    hero_photo='boat-yacht-lowboy', hero_alt='Cabin cruiser strapped down on a lowboy trailer, hauled by a semi truck')

service_page(
    'rv-motorhome-transport.html', 'RV &amp; Motorhome Transport', 'RV &amp; Motorhome Transport',
    'RV & Motorhome Transport — Edgebay International',
    'Motorhome, camper, and travel trailer transport across the USA — driven or towed by vetted professionals, coordinated by Edgebay International.',
    RV_ICON,
    'Your Home on Wheels, Delivered',
    ["From Class A motorhomes to fifth wheels, travel trailers, and camper vans, we coordinate the right method for your RV: professional drive-away for drivable units, or towing and flatbed hauling for trailers and non-running vehicles.",
     "Every driver in our network is vetted, insured, and experienced with large recreational vehicles — including the permits and routing that tall or long units require."],
    ["Drive-away service for motorhomes and camper vans", "Towing for fifth wheels and travel trailers",
     "Flatbed and lowboy options for non-running units", "Oversize permits and routing handled for you",
     "Door-to-door, dealer, and campground deliveries"],
    [("Best For", "Snowbird seasonal moves, RV purchases from out of state, dealer transfers, and relocations where you'd rather not drive the rig yourself."),
     ("Preparation", "Secure all interior items, empty tanks, retract slides and awnings, disconnect propane, and document the exterior with photos before pickup."),
     ("Pricing Factors", "Distance, RV length and height, whether it's drivable or needs to be towed, and any permit requirements for oversize dimensions.")],
    hero_photo='rv-hymer-flatbed', hero_alt='Hymer motorhome loaded on a flatbed carrier for transport', hero_badge='Motorhome on a flatbed carrier')

# ----------------------------------------------------------------- services overview
tiles = [
    ('open-transport.html', CAR_ICON, 'Open Transport', 'The cost-effective standard — your vehicle on a secure open carrier, the way most cars move across America.'),
    ('enclosed-transport.html', GARAGE_ICON, 'Enclosed Transport', 'Full protection in an enclosed trailer for luxury, classic, or high-value vehicles.'),
    ('door-to-door.html', US_ICON, 'Door-to-Door Service', 'Pickup and delivery as close to your addresses as possible — no terminals, no extra trips.'),
    ('expedited-shipping.html', BOLT_ICON, 'Expedited Shipping', 'Priority carrier assignment and the tightest realistic pickup windows when time is short.'),
    ('motorcycle-transport.html', MOTO_ICON, 'Motorcycle Transport', 'Specialized equipment and careful handling for cruisers, sport bikes, and customs.'),
    ('boat-transport.html', BOAT_ICON, 'Boat Transport', 'Trailered boats, jet skis, and pontoons hauled safely between marinas, dealers, and homes.'),
    ('rv-motorhome-transport.html', RV_ICON, 'RV &amp; Motorhome Transport', 'Drive-away, towing, or flatbed hauling for motorhomes, fifth wheels, and campers.'),
    ('contact.html', SHIELD_ICON, 'Fully Insured, Always', 'Every shipment we coordinate is covered by carrier cargo insurance. Questions? Talk to us.'),
]
tiles_html = '\n'.join(
    f'''      <a class="svc-tile" href="{h}">
        <div class="service-icon">{i}</div>
        <h3>{t}</h3>
        <p>{p}</p>
        <span class="more">Learn more &#8594;</span>
      </a>''' for h, i, t, p in tiles)

svc = head('Auto Transport Services — Edgebay International',
           'Open, enclosed, door-to-door, expedited, motorcycle, boat and RV transport across all 50 states. Explore Edgebay International services.')
svc += header('services') + banner('Our Auto Transport Services', 'Services')
svc += f'''
<section class="page-section">
  <div class="container two-col">
    <div>
      <h2>Every Vehicle. Every Route.<br>The Right Way to Ship It.</h2>
      <p class="content-p">Edgebay International coordinates vehicle transport across all 50 states through a network of licensed, insured, and performance-vetted carriers. Whatever you drive and wherever it needs to go, there's a service built for it.</p>
      <p class="content-p">Not sure which option fits? Call us at <a href="{TEL}" style="color:var(--blue);font-weight:600;">{PHONE}</a> or <a href="{WA}" target="_blank" rel="noopener" style="color:var(--blue);font-weight:600;">message us on WhatsApp</a> — we'll recommend the right one in minutes.</p>
    </div>
{photo_frame('open-carrier-porsche', 'Open carrier loaded with sports cars coordinated by Edgebay', 'Real Edgebay shipment')}
  </div>
</section>

<section class="page-section alt">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">Choose Your Service</h2>
    <div class="center-bar"></div>
    <div class="svc-tiles">
{tiles_html}
    </div>
  </div>
</section>
{gallery([('open-carrier-suv', 'SUVs on an open carrier'), ('enclosed-mclaren', 'McLaren in an enclosed trailer'), ('exotic-lamborghini', 'Lamborghini delivered by flatbed'),
          ('motorcycle-flatbed', 'Motorcycle secured on a flatbed'), ('enclosed-porsche', 'Porsche loaded in an enclosed carrier'), ('exotic-ferrari-red', 'Ferrari on a dedicated flatbed')],
         title='Vehicles We Move', intro='From daily drivers to exotics and motorcycles — a few examples of what our carrier network handles.')}
''' + CTA_BAND + FOOTER
open('/root/edgebay/services.html', 'w').write(svc)

# ----------------------------------------------------------------- how it works
hiw = head('How It Works — Edgebay International',
           'Shipping your car in four simple steps: quote, booking, transport, and delivery. See how Edgebay International works.')
hiw += header('how') + banner('How It Works', 'How It Works')
hiw += f'''
<section class="page-section">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">Ship Your Vehicle in Four Simple Steps</h2>
    <div class="center-bar"></div>
    <div class="steps-grid">
      <div class="step">
        <div class="step-num">1</div>
        <h3>Request Your Quote</h3>
        <p>Fill out our quick form or call us. Tell us the vehicle, the route, and your dates — you'll get a clear, no-obligation quote.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h3>Book Your Pickup</h3>
        <p>Happy with the price? We assign a vetted, insured carrier from our network and confirm your pickup window and details.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h3>Pickup &amp; Transport</h3>
        <p>The driver inspects your vehicle with you, documents its condition on the Bill of Lading, loads it, and hits the road. We keep you updated throughout.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <h3>Delivery at Your Door</h3>
        <p>At the destination, you inspect the vehicle against the pickup report, sign off, and you're done. Simple as that.</p>
      </div>
    </div>
  </div>
</section>

<section class="page-section alt">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">What to Expect Along the Way</h2>
    <div class="center-bar"></div>
{info_cards([
    ("What You'll Need", "The vehicle's year, make and model, pickup and delivery ZIP codes, your preferred dates, and whether it runs. That's all it takes to quote."),
    ("Stay Informed", "From carrier assignment to delivery day, we keep you posted with timely updates — and you can always call, email, or WhatsApp us for status."),
    ("Real People, Real Support", "You get a dedicated point of contact who knows your shipment, Monday through Friday, 9AM–6PM EST. No phone mazes."),
])}
  </div>
</section>

''' + CTA_BAND + FOOTER
open('/root/edgebay/how-it-works.html', 'w').write(hiw)

# ----------------------------------------------------------------- about
about = head('About Us — Edgebay International',
             'Edgebay International is a licensed, FMCSA-compliant auto transport broker based in Atlanta, Georgia, serving all 50 states.')
about += header('about') + banner('About Edgebay International', 'About Us')
about += f'''
<section class="page-section">
  <div class="container two-col">
    <div>
      <h2>Nationwide Auto Transport,<br>Made Simple.</h2>
      <p class="content-p">Edgebay International is a licensed auto transport broker based in Atlanta, Georgia. We exist for one reason: shipping a vehicle should be simple, transparent, and stress-free — and too often it isn't.</p>
      <p class="content-p">As a broker, we don't just book a truck. We match your shipment with the right carrier from our vetted network, negotiate a fair rate, handle the paperwork, and stay on top of your shipment until the keys are back in your hand.</p>
      <p class="content-p">We operate in full compliance with FMCSA regulations and treat every vehicle like our own — and every customer like family.</p>
    </div>
{photo_frame('enclosed-porsche', 'Porsche loaded in an enclosed trailer by an Edgebay carrier', 'Real Edgebay shipment')}
  </div>
</section>

<section class="page-section alt">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">Licensed, Registered, Accountable</h2>
    <div class="center-bar"></div>
    <div class="stats-grid">
      <div class="stat-tile"><span class="stat-value">50</span><span class="stat-label">States Served</span></div>
      <div class="stat-tile"><span class="stat-value">DOT #3906150</span><span class="stat-label">USDOT Registration</span></div>
      <div class="stat-tile"><span class="stat-value">MC #1450201</span><span class="stat-label">Motor Carrier Number</span></div>
      <div class="stat-tile"><span class="stat-value">100%</span><span class="stat-label">Insured Shipments</span></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">What We Stand For</h2>
    <div class="center-bar"></div>
{info_cards([
    ("Transparent Pricing", "Clear quotes with no hidden fees and honest expectations about routes, timing, and options — before you commit to anything."),
    ("Vetted Carriers Only", "Every carrier we work with is checked for licensing, insurance coverage, and a track record of on-time, damage-free deliveries."),
    ("A Real Point of Contact", "From first quote to final delivery, you talk to a person who knows your shipment — by phone, email, or WhatsApp."),
])}
  </div>
</section>

''' + CTA_BAND + FOOTER
open('/root/edgebay/about.html', 'w').write(about)

# ----------------------------------------------------------------- faq
faqs = [
    ("How much does it cost to ship a car?",
     "Rates depend on distance, vehicle size and weight, transport type (open or enclosed), route popularity, and season. Popular routes with lots of carrier traffic cost less. The fastest way to know is our free quote — it takes a minute and there's no obligation."),
    ("How long will my transport take?",
     "Coast-to-coast shipments typically deliver within 7–10 days of pickup; shorter regional routes often take 1–5 days. Pickup itself is usually scheduled within a few days of booking. Need it faster? Ask about our expedited service."),
    ("Should I choose open or enclosed transport?",
     "Open transport is the affordable standard used for most vehicles, including by dealerships. Enclosed transport costs more but fully shields the vehicle from weather and road debris — the right call for luxury, classic, exotic, or high-value cars."),
    ("Is my vehicle insured during transport?",
     "Yes. Every carrier we assign holds active cargo insurance that covers your vehicle during transit, and we verify that coverage before the carrier is confirmed. The driver also documents your vehicle's condition at pickup and delivery on the Bill of Lading."),
    ("Do you ship boats, RVs, and motorcycles too?",
     "Yes. Beyond cars and trucks we coordinate motorcycle transport, trailered boats and jet skis, and motorhomes, fifth wheels, and campers — driven, towed, or hauled on a flatbed depending on the unit. Just tell us the dimensions when you request a quote."),
    ("Can I leave personal items in the car?",
     "Light personal items (generally up to about 100 lbs, in the trunk) are usually tolerated, but they aren't covered by the carrier's insurance and add weight. Never leave valuables, electronics, or documents in the vehicle."),
    ("My car doesn't run — can you still ship it?",
     "In most cases, yes. Inoperable vehicles need a carrier with a winch and extra clearance, which adds some cost. Just tell us the vehicle's condition when you request your quote so we assign the right equipment."),
    ("How should I prepare my vehicle for pickup?",
     "Wash it (so the inspection is accurate), remove valuables and toll tags, disable the alarm, leave about a quarter tank of fuel, and photograph the vehicle. Have a set of keys ready for the driver."),
    ("Do I need to be present at pickup and delivery?",
     "You or someone you trust (18+) must be present at both ends to walk the inspection with the driver and sign the Bill of Lading. That document protects you — it's the official record of your vehicle's condition."),
    ("When and how do I pay?",
     "Your advisor confirms the payment schedule and accepted methods together with your quote, before you book — so there are never surprises. You'll know exactly what's due and when."),
    ("Are you a carrier or a broker?",
     "We're a licensed broker (DOT #3906150, MC #1450201). That works in your favor: instead of being limited to one truck's schedule, we match your shipment against an entire network of vetted carriers to get the right equipment, route, and price."),
]
faq_html = '\n'.join(
    f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-body">{a}</div>
      </details>''' for q, a in faqs)

faq = head('FAQ — Edgebay International',
           'Answers to the most common auto transport questions: pricing, timing, insurance, preparation, and more.')
faq += header('faq') + banner('Frequently Asked Questions', 'FAQ')
faq += f'''
<section class="page-section">
  <div class="container">
    <h2 class="content-h2" style="text-align:center;">Everything You Need to Know</h2>
    <div class="center-bar"></div>
    <div class="faq-list">
{faq_html}
    </div>
    <p style="text-align:center;margin-top:34px;font-size:15px;">Didn't find your answer? <a href="contact.html" style="color:var(--blue);font-weight:600;">Contact us</a> or call <a href="{TEL}" style="color:var(--blue);font-weight:600;">{PHONE}</a>.</p>
  </div>
</section>

''' + CTA_BAND + FOOTER
open('/root/edgebay/faq.html', 'w').write(faq)

# ----------------------------------------------------------------- contact
contact = head('Contact Us — Edgebay International',
               'Get in touch with Edgebay International: free quotes, phone, email, and WhatsApp. Based in Atlanta, serving all 50 states.')
contact += header('contact') + banner('Contact Us', 'Contact Us')
contact += f'''
<section class="page-section">
  <div class="container contact-grid">
    <div>
      <h2 class="content-h2">Let's Get Your Vehicle Moving</h2>
      <p class="content-p" style="margin-bottom:28px;">Questions, quotes, or a shipment already on the road — reach us any way you like. A real person answers.</p>

      <div class="contact-card">
        <span class="cta-icon">{PHONE_SVG.format(c='#0642a0', w='1.9')}</span>
        <span><span class="label">Call Us</span><a class="value" href="{TEL}">{PHONE}</a></span>
      </div>
      <div class="contact-card">
        <span class="cta-icon" style="background:#e3f8ec;">{WA_SVG.format(c='#1eb356')}</span>
        <span><span class="label">WhatsApp</span><a class="value" href="{WA}" target="_blank" rel="noopener">{WA_NUMBER}</a></span>
      </div>
      <div class="contact-card">
        <span class="cta-icon">{MAIL_SVG.format(c='#0642a0', w='1.9')}</span>
        <span><span class="label">Email</span><a class="value" href="mailto:{EMAIL}">{EMAIL}</a></span>
      </div>
      <div class="contact-card">
        <span class="cta-icon">{CLOCK_SVG.format(c='#0642a0', w='1.9')}</span>
        <span><span class="label">Business Hours</span><span class="value">Mon – Fri: 9AM – 6PM EST</span></span>
      </div>
      <div class="contact-card">
        <span class="cta-icon">{PIN_SVG.format(c='#0642a0', w='1.9')}</span>
        <span><span class="label">Based In</span><span class="value">Atlanta, Georgia — serving all 50 states</span></span>
      </div>
      <div class="social-row" style="margin-top:22px;">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook" style="background:var(--blue);">{FB_SVG}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram" style="background:var(--blue);">{IG_SVG}</a>
        <a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok" style="background:var(--blue);">{TT_SVG}</a>
      </div>
    </div>

    <div class="quote-card">
      <h3>Get Your Free Quote</h3>
{quote_form()}
    </div>
  </div>
</section>

''' + FOOTER.replace('</body>', FORM_SCRIPT + '\n</body>')
open('/root/edgebay/contact.html', 'w').write(contact)

# ----------------------------------------------------------------- legal pages
def legal_page(fname, h1, title, desc, sections, updated='September 2026'):
    body = head(title, desc) + header(None) + banner(h1, h1)
    secs = ''
    for heading, parts in sections:
        secs += f'      <h2>{heading}</h2>\n'
        for p in parts:
            if isinstance(p, list):
                secs += '      <ul>\n' + ''.join(f'        <li>{li}</li>\n' for li in p) + '      </ul>\n'
            else:
                secs += f'      <p>{p}</p>\n'
    body += f"""
<section class="page-section">
  <div class="container">
    <div class="legal-content">
      <p class="updated">Last updated: {updated}</p>
{secs}      <div class="note">Questions about this document? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE}.</div>
    </div>
  </div>
</section>

""" + FOOTER
    open(f'/root/edgebay/{fname}', 'w').write(body)


legal_page('privacy-policy.html', 'Privacy Policy', 'Privacy Policy — Edgebay International',
    'How Edgebay International collects, uses, and protects your personal information.',
    [
     ("Who We Are", [
        "Edgebay International (\"Edgebay\", \"we\", \"us\") is a licensed auto transport broker based in Atlanta, Georgia (USDOT #3906150, MC #1450201). This Privacy Policy explains what information we collect through our website and services, how we use it, and the choices you have."]),
     ("Information We Collect", [
        "We collect information you provide directly to us, for example when you request a quote, contact us by phone, email, or WhatsApp, or book a shipment:",
        ["Contact details: your name, email address, and phone number.",
         "Shipment details: vehicle type, year, make and model, pickup and delivery locations, preferred dates, and vehicle condition.",
         "Communications: the content of messages you send us and notes from our conversations with you."],
        "We also receive limited technical information automatically when you visit our website, such as your IP address, browser type, pages viewed, and the date and time of your visit, through our hosting provider's standard server logs."]),
     ("How We Use Your Information", [
        ["To prepare and send you a quote and respond to your requests.",
         "To arrange and manage your shipment, including assigning a carrier and keeping you informed of its status.",
         "To communicate with you about your shipment, our services, and customer support.",
         "To comply with legal, regulatory, and insurance requirements applicable to auto transport.",
         "To maintain the security and performance of our website."]]),
     ("How We Share Information", [
        "We do not sell your personal information. We share it only as needed to provide our services:",
        ["With the licensed carrier assigned to your shipment, so they can pick up and deliver your vehicle and contact you about scheduling.",
         "With service providers who help us operate, such as our website hosting provider and the service that delivers quote-form submissions to our inbox. These providers process data only on our behalf.",
         "When required by law, regulation, legal process, or to protect the rights, property, or safety of Edgebay, our customers, or others."]]),
     ("Cookies and Analytics", [
        "Our website does not currently use advertising cookies. If we add analytics or similar tools in the future, we will update this policy accordingly. You can control cookies through your browser settings."]),
     ("Data Retention", [
        "We keep quote requests and shipment records for as long as needed to provide our services and to meet our legal, accounting, and insurance obligations, after which we delete or anonymize them."]),
     ("Your Choices and Rights", [
        "You may request access to, correction of, or deletion of the personal information we hold about you by emailing us. You may also opt out of marketing communications at any time. Depending on where you live, you may have additional rights under applicable privacy laws; we will honor valid requests in accordance with those laws."]),
     ("Security", [
        "We use reasonable administrative and technical safeguards to protect your information. However, no method of transmission over the internet is completely secure, and we cannot guarantee absolute security."]),
     ("Children", [
        "Our services are intended for adults. We do not knowingly collect personal information from children under 18."]),
     ("Changes to This Policy", [
        "We may update this Privacy Policy from time to time. The date at the top of the page shows when it was last revised. Continued use of our website or services after a change means you accept the updated policy."]),
    ])

legal_page('terms-of-service.html', 'Terms of Service', 'Terms of Service — Edgebay International',
    'The terms and conditions that apply to quotes, bookings, and vehicle transport coordinated by Edgebay International.',
    [
     ("Agreement to These Terms", [
        "These Terms of Service (\"Terms\") govern your use of the Edgebay International website and the vehicle transport brokerage services we provide. By requesting a quote, booking a shipment, or using our website, you agree to these Terms."]),
     ("Our Role as a Broker", [
        "Edgebay International is a licensed transportation broker (USDOT #3906150, MC #1450201). We arrange the transport of your vehicle with independent, licensed and insured motor carriers. We do not own trucks or physically transport vehicles ourselves. The carrier assigned to your shipment is responsible for the pickup, transport, and delivery of the vehicle."]),
     ("Quotes and Booking", [
        "Quotes are estimates based on the information you provide, including vehicle type, condition, route, and dates. Inaccurate or incomplete information (for example, an inoperable vehicle, modifications, oversized dimensions, or added cargo) may change the price or the equipment required. A booking is confirmed when we send you a booking confirmation, which will state the agreed price, pickup window, and payment terms."]),
     ("Pickup and Delivery Windows", [
        "Pickup and delivery dates are estimated windows, not guarantees. Transit times can be affected by weather, traffic, road conditions, mechanical issues, and other circumstances beyond our control. We will keep you informed of any significant changes."]),
     ("Your Responsibilities", [
        ["Provide accurate vehicle and shipment information and keep us informed of any changes.",
         "Have the vehicle ready at the agreed time: accessible, with about a quarter tank of fuel, alarms disabled, and keys available.",
         "Remove personal belongings and valuables. Personal items left in the vehicle are not covered by carrier insurance and are transported at your own risk.",
         "Ensure you or an authorized adult (18+) is present at pickup and delivery to inspect the vehicle and sign the Bill of Lading."]]),
     ("Inspection, Bill of Lading, and Claims", [
        "At pickup, the carrier inspects the vehicle with you and records its condition on the Bill of Lading. At delivery, inspect the vehicle again before signing. Any new damage must be noted on the Bill of Lading at the time of delivery; damage not noted at delivery may not be eligible for a claim. Claims are handled under the assigned carrier's cargo insurance, and we will assist you in the process."]),
     ("Insurance", [
        "Every carrier we assign is required to maintain active cargo and liability insurance, which we verify before confirming the carrier. Coverage applies to the vehicle itself during transit, subject to the carrier's policy terms and exclusions."]),
     ("Payment", [
        "Payment amounts, methods, and timing are stated in your booking confirmation. Prices may be adjusted if the shipment details differ materially from what was quoted (for example, a vehicle that is inoperable, larger, or heavier than declared)."]),
     ("Cancellations and Changes", [
        "You may cancel or change a booking by contacting us as early as possible. Any applicable cancellation terms, including for cancellations after a carrier has been dispatched, are stated in your booking confirmation."]),
     ("Limitation of Liability", [
        "To the fullest extent permitted by law, Edgebay International's liability arising from our brokerage services is limited to the brokerage fees you paid to us for the shipment in question. We are not liable for indirect, incidental, or consequential damages, including loss of use, delays, or lost profits. Nothing in these Terms limits liability that cannot be limited under applicable law."]),
     ("Website Use", [
        "The content of this website is provided for general information and is owned by or licensed to Edgebay International. You may not copy, reproduce, or use it for commercial purposes without our written permission."]),
     ("Governing Law", [
        "These Terms are governed by the laws of the State of Georgia, USA, and applicable federal transportation regulations, without regard to conflict-of-law principles."]),
     ("Changes to These Terms", [
        "We may update these Terms from time to time. The date at the top of the page shows when they were last revised. Continued use of our website or services after a change means you accept the updated Terms."]),
    ])

# expose pieces for index.html patching
if __name__ == '__main__':
    open('/root/edgebay/_form_script.html', 'w').write(FORM_SCRIPT)
    open('/root/edgebay/_quote_form.html', 'w').write(quote_form())
    print("generated pages")
