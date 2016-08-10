---
layout: archive
permalink: "/0xff-beat/"
author_profile: true
title: "0xff beat Podcast"
excerpt: "Sharing the <3 for Drum Machines and Bass Culture."
header: 
  overlay_image: 0xff-beat-banner.jpg
  cta_label: "Follow on Mixcloud"
  cta_url: https://www.mixcloud.com/sergioagostinho/
---

{% include base_path %}

{% include 0xff-beat-subscribe.html %}

<br>

<div class="grid__wrapper" style="display:inline-block;">
  {% for post in site.0xff-beat reversed %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
