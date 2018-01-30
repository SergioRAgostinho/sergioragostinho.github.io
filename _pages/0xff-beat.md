---
layout: archive
permalink: "/0xff-beat/"
author_profile: true
title: "0xff beat Podcast"
excerpt: "Sharing the <3 for Drum Machines and Bass Culture."
header:
  overlay_image: "/assets/images/0xff-beat-banner.jpg"
  cta_label: "Follow on Mixcloud"
  cta_url: https://www.mixcloud.com/0xff-beat/
---

{% include 0xff-beat-subscribe.html %}

<br>

<div class="grid__wrapper">
  {% assign sorted = site.off-beat | reverse %}
  {% for post in sorted %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
