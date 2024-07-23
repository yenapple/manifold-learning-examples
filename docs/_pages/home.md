---
layout: single
title: Welcome to the Manifold Learning Examples project!
permalink: / 
header:
 image: /assets/images/other-figures/header_home.jpg


distortion_example:
  - url: /assets/images/other-figures/ethanoltorsion2.png
    image_path: /assets/images/other-figures/ethanoltorsion2.png
    alt: "Distortion at corners"
    title: "Distortion at corners"
  - url: /assets/images/T-SNE/n=10000, d2=10, n_neighbors=100.png
    image_path: /assets/images/T-SNE/n=10000, d2=10, n_neighbors=100.png
    alt: "Filaments artifact"
    title: "Filaments artifact"
  - url: /assets/images/other-figures/galaxy_1_2.png
    image_path: /assets/images/other-figures/galaxy_1_2.png
    alt: "Horseshoe artifact"
    title: "Horseshoe artifact"

---



What this site is about
------------------------

**Manifold Learning (ML) algorithms** -- also called **Embedding algorithms** -- can help us interpret data with many dimensions (such as a cloud of word embeddings or of configurations of a molecule) by mapping it to 2D or to 3D where **we can see** it. But is what we are seeing the **real shape** of the data? Almost always, ML algorithms *distort the shape*. Sometimes the distortions are unimportant, but sometimes they can make us see *clusters, "arms", holes, and "horseshoes"* (what we will call **artefacts**) that are not properties of the data, but just effects of the algorithm and parameter choices. 

This project illustrates some of the most common effects and artefacts you will encounter, as you start using Embedding algorithms for your  real data. The artefacts are *not* symptoms of "too little data" -- most of them persist even when the data size _n_ goes to infinity! We chose simple artificial examples as the most common effects are present even with the simplest data. 

The good news is that once you are aware of their presence, the artefacts and distorions can be recognized and methods exist to circumvent or to correct them. 

{% include gallery id = "distortion_example"  layout = third %}

What is in this site
-------------------------

You may navigate this site through the categories on the upper navigation bar. (In each category, there is a side navigation bar directing through each content.)

- [Tutorials](/tutorials/) include short tutorial posts on manifolds and manifold learning, longer tutorial videos, review paper and related recent talks.  
- [Articles](/articles/) include a series of short articles, illustrating significant but less widely known counterintuitive behaviors of manifold learning algorithms. Most of these effects are predictable or documented theoretically, and we include (light) references to the main sources.
- [Software](/software/) include python code examples generating synthetic examples/descriptive plots in both uniform/nonuniform manner. These are mostly based on packages [Sk-learn](https://scikit-learn.org/stable/) and [megaman](https://github.com/mmp2/megaman), for which we also share installation process and experiences on those packages.




How to use this site 
-----------------------

This site is the project page of this [Github repository](https://github.com/mmp2/manifold-learning-examples). 

Feel free to visit the repostory, to use the code, articles and graphics, citing the repository (_please see sidebar_ **About** to obtain citation). Currently, it is a working repository; changes to the code or files are possible.

 Contributors (in alphabetical order)
-------------------------

* [Haoqiang (Murray) Kang](https://github.com/mk322) **original repository creator**, non-uniform density, aspect ratio, t-SNE
* Marina Meila, Professor, concept and scientific leadership
* [Hangliang Ren (Harry)](https://github.com/Harryahh), spectral embedding, non-uniform density, plotting, aspect ratio
* [Qirui Wang](https://github.com/Typhoeus-Wang), UMAP, aspect ratio
* [Yujia Wu](https://github.com/yujiaw3-1933467), data generation, plotting, Local Linear Embedding, aspect ratio