---

permalink: /articles/aspect-ratio

toc: true

gal_horseshoe:
  - url: /assets/images/other-figures/galaxy_1_2.png
    image_path: /assets/images/other-figures/galaxy_1_2.png
    alt: "galaxy spectra v0, v2, with horseshoe"
    title: "galaxy spectra v0, v2, with horseshoe"
  - url: /assets/images/other-figures/umap_kneigh_comp-crop1.png
    image_path: /assets/images/other-figures/umap_kneigh_comp-crop1.png
    alt: "rectangle 7 x 1, horseshoe abd clusters"
    title: "rectangle 7 x 1, horseshoe abd clusters"

gal_nohorseshoe:
  - url: /assets/images/other-figures/galaxy_1_3.png
    image_path: /assets/images/other-figures/galaxy_1_3.png
    alt: "galaxy spectra v0, v2, no horseshoe"
    title: "galaxy spectra v0, v2, no horseshoe"
  - url: /assets/images/other-figures/umap_kneigh_comp-crop2.png
    image_path: /assets/images/other-figures/umap_kneigh_comp-crop2.png
    alt: "rectangle 7 x 1, no horseshoe"
    title: "rectangle 7 x 1, no horseshoe"

sidebar:
  nav: "algorithms"

---

The effect of manifold aspect ratio: seeing "horseshoes" everywhere
====================================================================

> Hangliang Ren, Murray Kang, Qirui Wang, Yujia Wu, Marina Meila

Below is an embedding of a real data set, spectra of galaxies in $D=3750$ dimensions (described <a href="https://arxiv.org/abs/1603.02763">here</a> or <a href="https://www.jmlr.org/papers/v17/16-109.html">here</a>), and embedded by <a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">this paper</a> with DiffusionMaps, into $m=2$ dimensions. Next to it is an embedding of a synthetic data set, a rectangle with length $7\times$ width by UMAP. This paper <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-2/issue-3/Horseshoes-in-multidimensional-scaling-and-local-kernel-methods/10.1214/08-AOAS165.full">Horeshoes in multidimensional scaling and local kernel methods</a> presents an embedding of the <a href="https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records">UCI Congressional voting records data</a> $D=16$ in $m=2$ dimensions with an algorithm called *Multi-Dimensional Scaling (MDS)*. All these embeddings look like horseshoes, but for the last 2 cases *we know* that there is no horseshoe in the data (the congressional data is approximately one-dimensional, with the congressmen ordered by degree of partisanship, plus significant noise). Thus the horseshoe  is an *artefact* of the algorithm used. What is causing it?

{% include gallery id = "gal_horseshoe" layout = half %}


Fortunately, horseshoes are easily recognized. Below we show the simple fix, for a more sophisticated algorithm look at <a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">Selecting the independent coordinates of manifolds with large aspect ratios </a>.

{% include gallery id = "gal_nohorseshoe"  layout = half %}


What is aspect ratio? 
---------------------
Below we see two examples of rectangles with different *aspect ratios*. For the left rectangle, the aspect ratio $a=4/3$, representing its length over  and  for the right rectangle it is $a=8/1.9=4.21$ (we avoid choosing aspect ratios that are integers). 

{% include figure popup=true image_path="https://user-images.githubusercontent.com/91905313/212610533-68ccd0c9-7944-4fe1-bcbe-532bb9b0b889.png" alt="different rectangles with different aspect ratio" caption="different rectangles with different aspect ratio" %}


Below we see data sampled uniformly from these 2 rectangles.

{% include figure popup=true image_path="https://user-images.githubusercontent.com/91905313/212610635-dc128dd0-dde8-4044-aacd-65be9e9de188.png" alt="uniform sample from two rectangles" caption="uniform sample from two rectangles" %}


Aspect ratio can be defined for other simple manifolds, that can be obtained by "rolling up" these rectangles. 

Two Swiss Rolls. The aspect ratio is inherited from the original rectangles (left $a=4/3$, right $a=8/1.9=4.21$ ).

{% include figure popup=true image_path="https://user-images.githubusercontent.com/91905313/212611133-39188188-ee2b-4559-accd-d7dd84e2c7aa.png" alt="two different Swiss roles" caption="two different Swiss roles" %}


Two Tori. A torus is a rectangle that is first rolled up (and glued) into a tube, then rolled again to form a tubular ring. The aspect ratio is then the ratio of the original rectangle, equal to the ratio of the larger and smaller radii of the torus (left $R/r=4/3$, right $R/r=8/1.9=4.21$).

{% include figure popup=true image_path="https://user-images.githubusercontent.com/91905313/212611596-c14a8121-f96f-4025-8e4e-3ffb9032e005.png" alt="two different tori" caption="two different tori" %}

These manifolds all have *intrinsic dimension* $d=2$, because they are obtained by a transformation of a rectangle, which is itself a 2 dimensional manifold. Even though they are 2 dimensional manifold, the torus and swiss roll live in $m=3$ coordinates, and we call $m$ the *embedding dimension*. Of course not all manifolds are obtained from rectangles. Qualitatively, we think of the aspect ratio of a manifold as the aspect ratio of the data, after the manifold is "unfolded" in $d$ dimensions. 

Most real data is not generated from rectangles, but most real data, when unfolded, has aspect ratio $>2$, in other words, not close to 1. The following examples illustrate how this affects the embeddings produced by different embedding algorithms. 

Before embarking on the examples, the readers are invited to take a detour dealing with the question: what is a good embedding? And what isn't?



*a table with links to subsets of results:*

Rectangle
---------

The rectangle is the simplest manifold example. The embedding algorithm will map _input data_  $(x_1,x_2)$ sampled from rectangles to points in $m=2$ with _embedding coordinates_ denoted $(v_0,v_1)$. In other words, we aren't even trying to "reduce dimension", as the data is already "embedded" in 2D. But the algorithms do not know it, and we will have the opportunity to observe their behavior.

The $v$ notation for embedding coordinates is motivated by the fact that most embedding algorithms use the eigenvectors of a matrix as embedding coordinates (Isomap, SpectralEmbedding, LLE). The UMAP algorithm starts with coordinates obtained by eigenvectors, which are then post-processed; t-SNE is the only method that does not use eigendecomposition. 

**Uniform Density**

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
      <th>15.79</th>
    </tr>
  </thead>
  <tbody>
    {% for emb in site.data.imgs.arRectUnif %}
    <tr>
      <td>{{emb.title}}</td>
      {% for em in emb.children %}
      <td><img src = "{{site.baseurl}}{{em.url}}" width="111" height="168"></td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>

*The best single plot for different aspect ratio* **TODO: add a second row with the eigenvectors chosen in each case**

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
      <th>15.79</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UMAP</td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961595-41515ac0-3437-4c6d-b70f-56f964cfb086.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961596-5bb5a029-5743-4b7e-9b19-defbded719a7.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961597-dabfe06d-232b-4c8e-a4b8-fb3956a8b3d3.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961600-de79c4df-037f-4ba4-b8c0-1880f4ef09e6.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961601-d6a0e72b-b835-4ad5-8be8-8752c61022d8.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961602-653e8a59-05d9-4b6a-b26b-ebf6e8443736.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961603-81266b80-536d-4fa3-bfbb-4d89ed1d34c4.jpeg" width="111" height="111"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190961604-d1b06b31-ce45-4ec2-abd2-b242a7c4efd2.jpeg" width="111" height="111"></td>
    </tr>
    <tr>
      <td>Eigenvectors</td>
      <td>the first eigenvector and the second eigenvector</td>
      <td>the first eigenvector and the third eigenvector</td>
      <td>the first eigenvector and the fourth eigenvector</td>
      <td>the first eigenvector and the fifth eigenvector</td>
      <td>the first eigenvector and the sixth eigenvector</td>
      <td>the first eigenvector and the nineth eigenvector</td>
      <td>the first eigenvector and the nineth eigenvector</td>
      <td>the first eigenvector and the tenth eigenvector</td>
    </tr>
  </tbody>
</table>

Swiss roll
----------
A swiss roll is just a rectangle rolled up. So, the embedding algorithms should output the same results as before, since they are getting the essentially same data, right? This pretty much what we observe. (At a more careful examination, we see that one end of the swiss roll is sometimes more stretched than the other. This is an effect of the sampling density, which is *not exaclty uniform*. When we generate our swiss rolls, the dark (blue) points get denser, because they are in the inner part of the spiral, while the light (yellow) points become sparser. As we will discuss in more detail [here --to be written shortly --](variable-density.md), some ML algorithms can be sensitive to the non-uniformity of the samples.)

**Uniform Density**

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
    </tr>
  </thead>
  <tbody>
    {% for emb in site.data.imgs.arSwissUnif %}
    <tr>
      <td>{{emb.title}}</td>
      {% for em in emb.children %}
      <td><img src = "{{site.baseurl}}{{em.url}}" width="125" height="189"></td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>

*The best single plot for different aspect ratio* 

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UMAP</td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962239-ba4b96ec-5b65-4a84-a8f3-f70b3d46bde5.jpeg" width="125" height="189"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962241-9b9ee4ce-ba3a-4327-8d0c-1f4099e9de89.jpeg" width="125" height="189"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962244-b710a3aa-053f-4af2-8d58-f2256d54100d.jpeg" width="125" height="189"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962238-03541129-ef57-4fab-944e-b8c14b988e90.jpeg" width="125" height="189"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962240-619ccf87-f876-414f-9af2-4d81f600c4f5.jpeg" width="125" height="189"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Eigenvectors</td>
      <td>the first eigenvector and the third eigenvector</td>
      <td>the first eigenvector and the fourth eigenvector</td>
      <td>the first eigenvector and the fourth eigenvector</td>
      <td>the first eigenvector and the fourth eigenvector</td>
      <td>the first eigenvector and the seventh eigenvector</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Rectangle with hole
-------------------
Because ML algorithms are "myopic", and only see small neighborhoods around each point, creating a hole in the data complicates their work. Some of the challenges are minor; for example, there are multiple ways to map the data that are approximately the same -- this is what causes Isomap to "round the hole". This effect will disappear gradually with more densely sampled data. Other challenges are more serious: a long rectangle with a hole is in fact *the union of 4 long rectangles*! 

**Uniform Density**

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
      <th>15.79</th>
    </tr>
  </thead>
  <tbody>
    {% for emb in site.data.imgs.arRectHoleUnif %}
    <tr>
      <td>{{emb.title}}</td>
      {% for em in emb.children %}
      <td><img src = "{{site.baseurl}}{{em.url}}" width="111" height="168"></td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>

*The best single plot for different aspect ratio* 

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
      <th>10.53</th>
      <th>15.79</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UMAP</td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962576-5093604c-3e4c-4ad5-a78e-59d1bd10b0ba.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962577-24613454-b43d-489a-b8bd-85d779bfe297.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962578-8dba2f01-3077-4e2b-b0e8-78f192dde5a6.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962579-43019d04-e61a-4027-961d-a69d7bf9c138.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962580-f4000ab3-7f66-4974-8343-8e86405b7347.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962582-d49c09be-abed-43ab-93c1-076e17d818fb.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962586-157a127b-d72e-46bf-b3a1-251c7c844e0e.jpeg" width="111" height="168"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962587-19b65f01-aef4-4186-af6a-6483e03ddc3b.jpeg" width="111" height="168"></td>
    </tr>
    <tr>
      <td>Eigenvectors</td>
      <td>the first eigenvector and the second eigenvector</td>
      <td>the first eigenvector and the second eigenvector</td>
      <td>the first eigenvector and the second eigenvector</td>
      <td>the first eigenvector and the eighth eigenvector</td>
      <td>the first eigenvector and the seventh eigenvector</td>
      <td>the first eigenvector and the eighth eigenvector</td>
      <td>the first eigenvector and the third eigenvector</td>
      <td>the first eigenvector and the sixth eigenvector</td>
    </tr>
  </tbody>
</table>

Torus
-----

**Uniform Density**

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
    </tr>
  </thead>
  <tbody>
    {% for emb in site.data.imgs.arTorusUnif %}
    <tr>
      <td>{{emb.title}}</td>
      {% for em in emb.children %}
      <td><img src = "{{site.baseurl}}{{em.url}}" width="142" height="346"></td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>

*The best single plot for different aspect ratio*

<table>
  <thead>
    <tr>
      <th>ML algo</th>
      <th>1.33</th>
      <th>2.5</th>
      <th>3.16</th>
      <th>4.21</th>
      <th>5.26</th>
      <th>8.42</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>UMAP</td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962979-c6568816-e574-42ad-b8eb-9564c66afad3.jpeg" width="142" height="150"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962983-37b2e8ef-dc1b-4bb6-b5f8-2218c6769e66.jpeg" width="142" height="150"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962985-39688127-a1fa-45fa-bd8c-fb8343d4f8bb.jpeg" width="142" height="150"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962986-f4e05eb9-b00e-4e55-b065-561680dd0a2d.jpeg" width="142" height="150"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962989-d1f6081f-98ff-4064-881b-360bebcb8ba5.jpeg" width="142" height="150"></td>
      <td><img src="https://user-images.githubusercontent.com/81238710/190962990-b72fb3ae-a058-4e87-bae1-78f650581d58.jpeg" width="142" height="150"></td>
    </tr>
    <tr>
      <td>Eigenvectors</td>
      <td>The first eigenvector, the second eigenvector, and the third eigenvector</td>
      <td>The first eigenvector, the second eigenvector, and the sixth eigenvector</td>
      <td>The first eigenvector, the second eigenvector, and the eighth eigenvector</td>
      <td>The first eigenvector, the second eigenvector, and the tenth eigenvector</td>
      <td>The first eigenvector, the second eigenvector, and the tenth eigenvector</td>
      <td>The first eigenvector, the second eigenvector, and the nineth eigenvector</td>
    </tr>
  </tbody>
</table>

+ One good exanple here is that for aspect ratio 1.33, the single best plot generated by UMAP is using the first eigenvector, the second eigenvector, and the third eigenvector. The plot is colored by z-axis based on the original dataset. From the plot, we notice that the plot result does not have any significant parts where points with different color intersects together. 

A manifold with $d=3$ 
---------------------
(brick?, ellipsoid? swiss roll?)

A "cute" manifold
------------------

Explanation, diagnosis, and what to do
---------------------------------------

For all ML algorithms presented here, the $m$ embedding coordinates are eigenvectors of a matrix. We would like each of them to represent an independent coordinate, but, in reality, the picture is more complex. If we compute many more than $m$ eigenvectors, we see that some or the higher order eigenvectors are harmonics of the preceding ones.

[Here, v1, v2 and v5 are harmonics of v0, and v4 is a harmonic of v3](https://github.com/mk322/manifold-learning-examples/blob/main/aspect-ratio-plots/Spectral-megaman/SwissRoll/Swiss_Roll_a10b4_Spectral_phi.jpg)

The larger the aspect ratio, the more harmonics of v0, the first eigenvector, will be found immediately following v0.

If we select harmonics among our embedding coordinate, the observed dimension of the embedding is *smaller than $d$, the intrinsic dimension. This is the main diagnostic that the **Independent Eigenvector Selection** (this is how we call our goal in technical terms) has not succeeded. In fact, if the dimension observed is not equal to $d$ everywhere, the embedding *has failed*. For simple cases, the drop in dimension happens everywhere (see above), for more complicated manifolds, it can happen only on parts of the data.


What to do?
-----------

We must search among the eigenvectors, from lower orders to higher, for a set of $m$ that preserve $d$ everywhere. When the manifold becomes more difficult (thinner, closer to itself) we may *need to increase $m$, the number of embedding coordinates* -- as shown by Johanthan Bates here [The embedding dimension of Laplacian eigenfunction maps](https://arxiv.org/abs/1605.01643).


Further reading and examples with real data 
--------------------------------------------

<a href="https://proceedings.neurips.cc/paper/2019/hash/6a10bbd480e4c5573d8f3af73ae0454b-Abstract.html">Selecting the independent coordinates of manifolds with large aspect ratios </a> discusses the problems in the case of Spectral Embedding (the authors have experimented with other algorithms such as LTSA and UMAP as well, observing similar behaviors) and proposes a solution, while <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-2/issue-3/Horseshoes-in-multidimensional-scaling-and-local-kernel-methods/10.1214/08-AOAS165.full">Horeshoes in multidimensional scaling and local kernel methods</a> does the same for MDS. In [Parsimonious representation of nonlinear dynamical systems through manifold learning: A chemotaxis case study](https://www.sciencedirect.com/science/article/pii/S1063520315000949) describe the aspect ratio problem for ML algorithm, and introduce the name **Independent Eigenvector Selection** and a first algorithm to correct it. 

Contributions
--------------
*MK* ;*MM* concept, main text, references; *HR*; *QW*; *YW* .


