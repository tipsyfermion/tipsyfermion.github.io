---
layout: archive
title: "Talks and Presentations"
permalink: /talks/
author_profile: true
---

{% if site.talks %}
  {% include base_path %}
  {% for post in site.talks reversed %}
    {% include archive-single-talk.html %}
  {% endfor %}
{% endif %}
