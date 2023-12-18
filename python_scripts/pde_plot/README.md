# pde_plot
The package `pde` can be used to plot PDEs using matplotlib and seaborn.

See `pde_plot.py` file for examples on how to use.
## Dependencies
* matplotlib
* seaborn
* numpy

## `pde.separated_PDE`
Function to plot a separated 1D-PDE on the finite interval $[0,L]$.
$$
u(x,t)=F(x)G(t)\;\;\; \forall x\in[0,L]
$$

Parameters:
* `F`:          separated function $F(x)$ 
* `G`:          separated function $G(t)$ 
* `L`:          length $L$; $x\in [0,L]$
* `c`:          speed
* `title`:      title of plot
* `timeseries`: times at which $u(x,T)$ will be plotted
* `N`:          plot resolution (N=10: coarse, N=100: medium, N=200: fine)

Return:
## `pde.PDE`
Function to plot a 1D-PDE on the finite interval $[0,L]$.

Parameters:
* `u`:          function $u(x,t)$ 
* `L`:          length $L$; $x\in [0,L]$
* `c`:          speed
* `title`:      title of plot
* `timeseries`: times at which $u(x,T)$ will be plotted
* `N`:          plot resolution (N=10: coarse, N=100 [default]: medium, N=200: fine)
* `t_len`:      time duration [default = 2.5]

## `pde.Laplace`
Function to plot a 2D-Laplace equation on the finite interval $x\in[0,L], y\in[0,M]$.

Parameters:
* `u`:          function $u(x,t)$ 
* `L`:          length $L$; $x\in [0,L]$
* `M`:          length $M$; $y\in [0,M]$
* `c`:          speed
* `title`:      title of plot
* `lines`:      y-positions at which $u(x,Y)$ will be plotted
* `N`:          plot resolution (N=10: coarse, N=100 [default]: medium, N=200: fine)
