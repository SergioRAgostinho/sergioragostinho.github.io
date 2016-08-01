---
title: Dear FuseNet, paraphrasing and quoting are not the same thing
date: 2016-07-30
tags: [news, media, fusenet]
categories: [posts]
excerpt: "Hi everyone. Today's post is meant to bring your attention to a problem that occasionally happens when people give interviews or are requested to provide testimonies. It is not rare to hear stories about how the original content got completely mangled and twisted by the authors that produced the final article/story."
---

**Edit:**
*FuseNet, unpublished the [page][post]. Something is happening. Let's hope for the best.*

Hi everyone. Today's post is meant to bring your attention to a problem that occasionally happens when people give interviews or are requested to provide testimonies. It is not rare to hear stories about how the original content got completely mangled and twisted by the authors that produced the final article/story. Today, I found out I was a victim of this unfortunate lack of professionalism.

From 20th to the 23rd of June, I attended the [Crash Course on Parallel Computing for Fusion - 24h Técnico.Ulisboa][course], hosted by the  [Instituto de Plasmas e Fusão Nuclear][ipfn] (IPFN), at [Instituto Superior Técnico][ist]. The workshop was organized by IPFN and was advertised on [FuseNet][fusenet].

The program covered introductory exercises on [CUDA][cuda], [OpenMP][omp] and [OpenMPI][mpi], all of them technologies I have interest in. The quorum was pretty much full, and since I was the only one not coming from a physics background, I was asked to provide a testimony about my experience: why had I decided to attend the workshop, what was covered, my general opinion about it, etc...  I was told that it was going to be published at some point on FuseNet's website and therefore I gladly accepted the task, since in the end it was free outreach. It came with steep price. 

Below, I present both the content that was published on FuseNet and the testimony I handed them to be published. What you'll notice is that the author paraphrased me, although conveying the idea that it is in fact a quote, and to make it worse, he used a somewhat awful unimaginative macaronic english.

![facepalm](https://upload.wikimedia.org/wikipedia/commons/3/3b/Paris_Tuileries_Garden_Facepalm_statue.jpg)
*Picture by [Alex E. Proimos](https://www.flickr.com/photos/proimos/)*

I'm hoping to see this issue cleared, the post amended and to receive a written apology from its author. Make me proud FuseNet, I'm waiting. Time to spam the social networks.

# The FuseNet post

The post can be checked [here][post]. I took a [snapshot](/images/posts/fusenet-post.png) of the page, just in case it (hopefully) gets edited at some point, so that this rant doesn't lose its context. Nevertheless, let's focus on what was published **as my own words**. I took the liberty to highlight in bold some of the blatant editorials.

> Especially those courses, were the main reason for Sérgio Agostinho, a Portuguese PhD student at the Signal Processing Group of the Instituto de Sistemas e Robótica (affiliated with IST), to sign up for the workshop. "Both, CUDA and OpenMP, are currently very popular for many exciting and different applications", Sérgio says. "A combination of both programming frameworks provides a very powerful toolset for developing **codes**. Having some experience with both of them, could help me develop a very efficient implementation of the algorithms on which I will be working during the course of my PhD." Sérgio is doing his PhD in the field of Computer Vision (CV), **focussing** on Structure from Motion. "Furthermore, for my job as maintainer of the Point Cloud Library (PCL), a popular library in CV, it is also very useful to be familiar with CUDA and OpenMP, since many of the contributions to the **PCDL-library** are made with those techniques."



# My testimony

Here's the [original file](/assets/pdf/sagostinho_testimony.pdf) I handed for being published. The content is shown underneath with my typos in bold, to be equally fair.

> My name is Sérgio Agostinho, a PhD student working in Computer Vision (CV), focused in Structure from Motion, and I attended the Crash Course on Parallel Computing for Fusion at Instituto Superior Técnico (IST) in Lisbon, from June 20th – 23rd 2016. I work at IST, where I'm part of the Signal Processing Group at Instituto de Sistemas e Robótica.
> 
> I decided to **enrol** in this course because it covered CUDA and OpenMP. CUDA became a prominent framework over this past decade enabling the many exciting applications in many topics of CV, but more recently, driving astonishing results in Deep Learning, by empowering popular frameworks like TensorFlow and Caffe. OpenMP became popular for allowing developers to take full advantage of the now standard multicore architectures, with very minimal effort. Expertise on both constitutes a powerful toolset for developing very efficient implementations of the algorithms I'll be working on, over the course of my PhD.
>
> Besides being a PhD student, I'm also a maintainer for a popular library in CV called Point Cloud Library (PCL). PCL is a library focused on manipulating 3D point clouds, and it provides a lot of functionalities to work with this particular data structure. Many of the operations over point clouds, can be parallelized and as such, the library has a number of implementations making use of OpenMP and CUDA e.g.: normal estimation and kinfu (an open source implementation of the Kinect Fusion algorithm), respectively. As a maintainer, I'm responsible for reviewing contributions to the library made by the community and fixing bugs, some of them made with CUDA and OpenMP.
> 
> What I found most useful about the course was that it provided a hands-on introduction on three different types of frameworks which cover most needs, in terms of parallelization, a developer might have. CUDA is great when having to perform vectorized operations over high dimensional data, OpenMP allows to easily fully exploit the multicore architectures, and if the problem is too big to be handled by a single machine, that's where MPI comes in and helps approach it from a multi-machine/cluster perspective.
> 
> In this day and age, where parallel computational devices are ubiquitous, this course should be considered mandatory for any entry level developer looking to work in highly intensive computing applications. I you have the opportunity to take it, don't miss the chance.




[course]: http://www.fusenet.eu/node/1095
[cuda]: http://www.nvidia.com/object/cuda_home_new.html
[ipfn]: http://www.ipfn.ist.utl.pt/
[ist]: https://tecnico.ulisboa.pt/pt/
[fusenet]: http://www.fusenet.eu/
[mpi]: http://www.open-mpi.org/
[omp]: http://openmp.org/wp/
[post]: http://www.fusenet.eu/node/1146
