---
title: Automating the Change Log for your Project
location: Ulm, Germany
excerpt: Put something here later
date: 2018-10-07
tags: [github, change-log, changelog, releases]
categories: [tutorials]
toc: true
toc_label: "Contents"
---

## Introduction

Today I will be talking about one important aspect of maintaining an community driven open source project which is keeping a change log. The change log is a useful tool for your users, as it quickly provides them with a summary of important changes that occurred in your project. However, keeping track of changes on an relatively sized open source project which is understaffed can quickly become a laborious task which will soon be hated by your project's maintainers. This is something I've personally experienced while maintaining [Point Cloud Library](http://pointclouds.org/) (PCL). Updating the change log is something we only do prior to a release and to make matters worse, our release cycle tends to be very long. When the time comes to update the change log, the list of merged pull requests (PR) is so extensive that this task turns into something painfully time consuming and monotonous. Since it is a monotonous task, no one wants to pick it up,  the release gets delayed, more PRs are merged and more items need to be added to the change log, prolonging a potentially endless cycle.

After realizing PCL is far from meeting optimal standards in terms of what an open source library should be, the issues of the long release cycle and the tracking of changes quickly rose to the top as one of the first problems to address.

## Goals

The goal was simple: to have an easy and quick way to update the change log, while ensuring it still provides useful information to PCL's users. The answer the first part was definitely *automation*, but to meet the goal of the second we got inspiration somewhere else. At a certain point in the development cycle of this new change log tool, my fellow PCL maintainer [Sergey Alexandrov](https://github.com/taketwo) brought up [https://keepachangelog.com/](https://keepachangelog.com/). I believe their motto says it all:
> Don’t let your friends dump git logs into changelogs.

In their website, they identify six category which are definitely relevant to have.


Types of changes

    Added for new features.
    Changed for changes in existing functionality.
    Deprecated for soon-to-be removed features.
    Removed for now removed features.
    Fixed for any bug fixes.
    Security in case of vulnerabilities.

PRs are naturally groupings of commits all about the same topic.

Occasionally grouping more PR might be worth it. Still needs to be implemented.