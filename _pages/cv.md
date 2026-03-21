---
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

Education
======
* Add your education here

Work Experience
======
* Add your work experience here

Skills
======
* Add your skills here

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
