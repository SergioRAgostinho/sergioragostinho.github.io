---
title: Setting up a multi user and system wide Anaconda installation
location: Lisbon, Portugal
toc: true
toc_label: "Contents"
tags: [sysadmin, anaconda]
---

Create group add all your desired users there

Install on /opt/anaconda3 as root

chgrp humans -R /opt/anaconda3
chmod g+s -R /opt/anaconda3


whatever file is created inside will always be visible and accessible by the group and it will be created with assugned to the group humans by default

