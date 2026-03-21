---
layout: archive
title: "Blog Posts"
permalink: /year-archive/
author_profile: true
---

{% include base_path %}

{% assign grouped_posts = site.posts | group_by_exp: "post", "post.date | date: \"%Y\"" %}
{% for group in grouped_posts %}
  <h2 id="{{ group.name }}-ref">{{ group.name }}</h2>
  <ul>
    {% for post in group.items %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
