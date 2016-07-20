---
layout: archive
author_profile: true
permalink: categories/
---

{% include base_path %}


{% assign cat_array = "" | split:"|"  %}
{% for post in site.posts %}
  {% for cat in post.categories %}
   {% assign cat_array = cat_array | push: cat %}
  {% endfor %}
{% endfor %}

{% assign cat_array = cat_array | sort | uniq %}
{% for cat in cat_array %}
  <h2 id="{{ cat | slugify }}">{{ cat | capitalize }}</h2>
  <ul style="list-style-type:none;">
  {% for post in site.categories[cat] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
