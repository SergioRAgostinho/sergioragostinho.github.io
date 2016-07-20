---
layout: archive
author_profile: true
permalink: tags/
---

{% include base_path %}


{% assign tag_array = "" | split:"|"  %}
{% for post in site.posts %}
  {% for tag in post.tags %}
   {% assign tag_array = tag_array | push: tag %}
  {% endfor %}
{% endfor %}

{% assign tag_array = tag_array | sort | uniq %}
{% for tag in tag_array %}
  <h2 id="{{ tag | slugify }}">{{ tag | capitalize }}</h2>
  <ul style="list-style-type:none;">
  {% for post in site.tags[tag] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
