"""
Name: Hangliang Ren

This program provides a series of plotting methods, both 2d and 3d plotting.
Through these methods, you can easily make plots relevant to manifold learning,
from original shape to subplots of all manifold learning results.
"""
import itertools
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


def plot_3d_shape_single(datapoints, colors, title, figsize=(10, 10), set_division=False, save_path=False, show_plot=True):
    """
    parameters
        "datapoints": Dataset used to draw the shape.
        "colors": Dataset used to color the shape; can be None.
        "title": Name of the shape.
        "figsize": size of plot, 10 * 10 as default value.
        "set_division": Choose whether set division in each axis scale;
        False as default value; if wanna set division, input real value.
        "save_path": The path for saving the plot; False as default value;
        if wanna to save plot, input absolute path for saving.
        "show_plot": Whether you want to display the generated plot;
        True as default value.
    post
        Display and save the plotted shape, generated by input dataset.
    """
    fig = plt.figure(figsize=figsize)  # set figure size
    ax = fig.add_subplot(projection='3d')

    ax.scatter(datapoints.T[0], datapoints.T[1], datapoints.T[2], c=colors)
    plt.title(title, fontsize=20)

    # rotate figure
    #ax.view_init(azim=-60, elev=9)
    
    if set_division != False:
        # set division in each axis scale
        ax.xaxis.set_major_locator(ticker.MultipleLocator(set_division))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(set_division))
        ax.zaxis.set_major_locator(ticker.MultipleLocator(set_division))
    
    if save_path != False:
        plt.savefig(save_path)
    
    if show_plot:
        plt.show()


def plot_3d_shape_all(datapoints, colors, title, figsize=(20, 20), set_division=False, save_path=False, show_plot=True):
    """
    parameters
        "datapoints": Dataset used for plotting.
        "colors": Dataset used to color the shape; can be None.
        "title": Name of the shape.
        "figsize": size of plot, 20 * 20 as default value.
        "set_division": Choose whether set division in each axis scale;
        False as default value; if wanna set division, input real value.
        "save_path": The path for saving the plot; False as default value;
        if wanna to save plot, input absolute path for saving.
        "show_plot": Whether you want to display the generated plot;
        True as default value.
    post
        Plot and save all 3d shapes; each shape is plotted by combining first and
        other two columns in "datapoints".
    """
    indices = [i for i in range(1, datapoints.shape[-1])]
    combinations = list(itertools.combinations(indices, 2))
    num_of_plots = len(combinations)
    fig = plt.figure(figsize=figsize)
    
    i = 1
    for combination in combinations:
        sub_data = datapoints[:, [0,combination[0],combination[1]]]
        x, y, z = sub_data.T
        ax = fig.add_subplot(math.ceil(num_of_plots/5), 5, i, projection='3d')
        ax.scatter(x, y, z, c=colors)
        ax.set_title("v0, v" + str(combination[0]) + ", v" + str(combination[1]))

        if set_division != False:
            # set division in each axis scale
            ax.xaxis.set_major_locator(ticker.MultipleLocator(set_division))
            ax.yaxis.set_major_locator(ticker.MultipleLocator(set_division))
            ax.zaxis.set_major_locator(ticker.MultipleLocator(set_division))
        
        i += 1
    
    plt.suptitle(title, fontsize=20)
    if save_path != False:
        plt.savefig(save_path)
        
    if show_plot:
        plt.show()


def plot_2d_shape_single(datapoints, colors, title, figsize=(10, 10), marker_size=20, set_division=False, save_path=False,
                         show_plot=True):
    """
    parameters
        "datapoints": Dataset used to draw the shape, a matrix with 2 columns,
        returned from sklearn manifold learning methods.
        "colors": Dataset used to color the shape; can be None.
        "title": Name of the shape.
        "figsize": size of plot, 10 * 10 as default value.
        "marker_size": size of marker, 20 as default value.
        "set_division": Choose whether set division in each axis scale;
        False as default value; if wanna set division, input real value.
        "save_path": The path for saving the plot; False as default value;
        if wanna to save plot, input absolute path for saving.
        "show_plot": Whether you want to display the generated plot;
        True as default value.
    post
        Plot and save the 2d shape, through data in "datapoints".
    """
    x, y = datapoints.T
    plt.figure(figsize=figsize)
    plt.scatter(x, y, c=colors, s=20, alpha=0.8)
    plt.title(title, fontsize=20)

    if set_division != False:
        # set division in each axis scale
        ax.xaxis.set_major_locator(ticker.MultipleLocator(set_division))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(set_division))

    if save_path != False:
        plt.savefig(save_path)
    
    if show_plot:
        plt.show()


def plot_2d_shape_all(datapoints, colors, title, figsize=(20, 20), marker_size=2, set_division=False, save_path=False,
                      show_plot=True):
    """
    parameters
        "datapoints": Returned matrix from sklearn manifold learning methods, for plotting.
        "colors": Dataset used to color each shape; can be None.
        "title": Name of the plot.
        "figsize": size of plot, 20 * 20 as default value.
        "marker_size": size of marker, 2 as default value.
        "set_division": Choose whether set division in each axis scale;
        False as default value; if wanna set division, input real value.
        "save_path": The path for saving the plot; False as default value;
        if wanna to save plot, input absolute path for saving.
        "show_plot": Whether you want to display the generated plot;
        True as default value.
    post
        Plot and save all 2d shapes; each shape is plotted by combining first and
        another column in "datapoints".
    """
    num_of_plots = datapoints.shape[-1] - 1
    fig = plt.figure(figsize=figsize)
    
    for i in range(1, num_of_plots+1):
        sub_data = datapoints[:, [0,i]]
        x, y = sub_data.T
        ax = fig.add_subplot(math.ceil(num_of_plots/2), 2, i)
        ax.scatter(x, y, s=2, c=colors)
        ax.set_title("v0, v"+str(i))

        if set_division != False:
            # set division in each axis scale
            ax.xaxis.set_major_locator(ticker.MultipleLocator(set_division))
            ax.yaxis.set_major_locator(ticker.MultipleLocator(set_division))
    
    plt.suptitle(title, fontsize=20)
    if save_path != False:
        plt.savefig(save_path)
    if show_plot:
        plt.show()