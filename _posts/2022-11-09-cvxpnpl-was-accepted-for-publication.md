---
title: CvxPnPL was (finally) accepted for publication at the Journal of Mathematical Imaging and Vision
tags: [absolute-pose-estimation, convex-optimization]
location: Munich, Germany
---

After almost two years going back and forth, my paper ["CvxPnPL: A Unified Convex Solution to the Absolute Pose Estimation Problem from Point and Line Correspondences"](/assets/pdf/publications/cvxpnpl.pdf) was finally accepted to the
[Journal of Mathematical Imaging and Vision](https://www.springer.com/journal/10851). This was the last missing piece to finally conclude my PhD and so now it's just a matter of wrapping up the thesis and defending things[^1].

In case you haven't read the paper, CvxPnPL is a Perspective-N-Points-and-Lines method, i.e., it's a [PnP](https://en.wikipedia.org/wiki/Perspective-n-Point) method that can also work with line correspondences. In layman terms, given 2D-3D point and lines correspondences in an image and a previously supplied 3D model, CvxPnPL will estimate an optimal pose for your object with respect to the camera, that can best explain the correspondences you provided as input.
![Image of a couple of pose estimate for the Occlusion dataset](/assets/images/posts/cvxpnpl/real-0777.png)
The beauty of it comes from the fact that the convex formulation used, makes it very simple to verify a posteriori, if the solutions produced are in fact global optima, which is a "nice to have" thing.

If you have a problem where something like this could come in handy, CvxPnPL is readily available through PyPI. Just call
```shell
pip install cvxpnpl
```
from within your python environment and take it for a spin. There are some very simple [examples](https://github.com/SergioRAgostinho/cvxpnpl/tree/master/examples) in the official repo, that show how to use the solver and help to better understand the API expectations.

Feel free to open a new [discussion](https://github.com/SergioRAgostinho/cvxpnpl/discussions) on GitHub in case you have questions.

[^1]: Famous last words.
