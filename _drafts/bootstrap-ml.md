---
title: An insiders review of the first Bootstrap ML workshop session
location: Lisbon, Portugal
toc: true
toc_label: "Contents"
tags: [bootstrap-ml, workshop]
---

Two weeks have passed since the first (and currently only) session of the [Bootstrap ML](/bootstrap-ml) workshop took place. It was my first experience developing a workshop from scratch with the aggravated challenge of being about Machine Learning. I thought about sharing some thoughts behind the entire process. The goods and the bads, the expectations versus what was actually accomplished.

If you're curious on having a take from the participant's perspective you should definitely check out this [blog post](https://medium.com/hugo-ferreiras-blog/basics-of-machine-learning-and-a-simple-implementation-of-the-naive-bayes-algorithm-80c1e67a2e8a) by Hugo Ferreira. It's a wonderful summary of the content I presented at the workshop.

## The Invitation

The entire thing started at the end of February, with an invitation from a former student I had while working as teaching assistant for a Machine Learning course. The goal was to come up with an introductory level workshop in Machine Learning aimed at math undergraduate students, as a way to capture their interest in the field. One could argue the media is doing a great job at that already but that's beside the point. The workshop was thought as having a theoretical introduction followed by real problem for the participants to address, all of this spanning a total duration of two hours.

It was the first time I was invited for such a thing, so after pondering on the invitation for a couple of days, I decided to challenge myself and accept it.

## Open Source and Collaborative

It's no secret I'm an open source endorser. I had a clear goal from the beginning which was to make all content publicly available, but things did not exactly stop there.

Having a single person doing all the material and also proof read it, is bound to have a number of mistakes. The over exposure and simple saturation of looking at the same content multiple times, sometimes lowers the attention levels to unimaginable heights. So there were going the be mistakes for sure and I needed to provide a mechanism for people to flag and submit corrections. But what if one wanted to extend the material on its own and contribute back?

At this point it was blatantly obvious that I wanted all the traditional mechanisms of an open source coding project. Well, that's what [GitHub](https://github.com/) is for.

## Free and Version Control Friendly

I had a way for everyone to interact with the workshop material, but also to submit corrections, comments and feedback. Great! However, in order to really leverage GitHub and implicitly version control functionalities, the content needed to be all prepared in a text friendly format. Whatever example was going to developed for the practical part of the session was meeting this requirement by default, after all it was going to be code. But what about the presentation content of the theoretical part? This one posed a problem.

Every time the word "presentation" comes to my mind, it is usually followed by the word "PowerPoint". It was clear from the start that PowerPoint was not an option: the file format it produces is a zipped version of the content and it would be impossible to analyze incremental differences and easily understand what was changed. Also, although commonly widespread, PowerPoint is still a paid tool and placing such an entry barrier just to be able to visualize and edit the content, defeated the whole purpose of being free and open source. Powerpoint, Keynote and others we're out of the race. Using open tools was more important than having clear diff reports so for a while I considering dropping the latter goal.

As time went by the decision boiled down to either using [Google Slides](https://www.google.com/slides/about/) or using the [Beamer](https://www.sharelatex.com/learn/Beamer) class in LaTex. There were of course pros and cons to this.

After trying a number of web presentation tools, I personally believe that Google Slides is the most flexible and powerful one I've tried so far. When vendors create web versions of their (fully featured) presentation oriented desktop applications, they only implement the most basic feature set, which honestly suits the majority of use cases. I'm convinced this happens as an incentive for power users to actually buy the desktop client applications, just to get to get those extra features. It's not that I consider myself one, but I tend to enjoy having a modern clean look and feel to my presentations, which normally means I start with blank theme and ending up creating one from scratch. So as long as one has a Google account, they would be able to edit the content. It was still not optimal but better.

The second in line was the Beamer class for LaTeX. I honestly feel this is a reasonable method to produce content filled slides, which are not really meant to be used for a presentation but more for having a person browsing through topics at their own leisure, in private. The LaTeX approach just had some very minor issues: the output would be a PDF file, so whatever type of media I wanted to include, would have to be restricted to text and images; the default templates for the class are nothing "to write home about" and creating a style from scratch in LaTeX tends to be punishing. Once more, not optimal but it was something.

Not being fully satisfied with my choices I reached out for some of my contacts in the development world, to see if there was some new "fancy" framework, developers were using to prepare presentations. If there's one thing I've learned from my year working in web development is that every time someone sneezes, a new JavaScript framework is born. Web development is very fast paced world and so web devs tend to be savvy in knowing all the new trends. Et voilá, let [Reveal.js](https://revealjs.com/#/) enter the room.

Reveal.js had everything, it's based on a HTML/CSS/JavaScript combo meaning it is super flexible to present whatever type of content one might need. Most importantly, it was definitely text based, so a person can visualize the slides as long as they have a (modern) browser and edit things with any text editor. One can embed videos, gifs, audio and even full web pages from other places, the possibilities are basically endless as a result of the major push in technology to have very content rich and flexible web pages. Two round it all off, Reveal.js fully supports using LaTeX math notation with MathJax and the default themes were simple and and yet modern looking enough for my taste. I was (and am) completely sold to it.

It was time to start preparing content!

## How to "Machine Learn" in 1 Hour

Yep, it sounds like bogus and honestly it is. The session was planned to span a duration of 2 hours, split between two parts, one theoretical and one practical. Assuming they both had the same time allocation, it meant I had one hour. This was going to be hard. To help you understand the level of challenge here assume I ask you to teach me your specialty in 1 hour. What would you talk about?

To top things of, the way the human mind learns new concepts was definitely not in my favor. I don't remember who exactly I'm exactly paraphrasing here but the idea is that for most people, at any point in time their brains are prepared to handle a single obstacle which they need to work in order to overcome. This obstacle can be a problem one needs to solve, a new concept one is trying to master, etc... I was going to "bombard" my students with a number of concepts they ever hear of, relying on my assumption of their existing past knowledge in Linear Algebra and Statistics. The odds of one retaining anything from the session seemed awfully low right from the start.

The objectives needed to be tailored appropriately. I started asking myself "What is utterly fundamental that these people retain from this workshop?" and as it turned out, the answer came fairly quickly. Provided the description of a real life problem, which can potential be solved resorting to Machine Learning, anyone attending this workshop should be able to appropriately understand what type of Task needs to solved, what type of Experience our algorithm will subject to and have a rough guess of which Performance metric to use in order to train the algorithm.

I'm already employing some of the technical (provide links to presentation slides)

Tried with my father 

The algorithms:
overall interest in deep learning means that neural networks need to appear at some point


Underestimated
a topic which by now feels very familiar to me but yet it still is quite dense to the common person who hears about the terms and wonders about it

## Coming up with examples

if you actually check the commented the slides I originally even thought I would have time to talk about Generative Adversarial Networks. Insane.

Thankful for the sign of trust


I blame 

Not to confuse clean twith basic 

Inspiration from the TED Talks
