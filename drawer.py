from shapely.geometry import Point, Polygon, LineString, box
from environment import Environment, plot_environment, plot_line, plot_poly
from math import sqrt

def draw_results(algo_name, path, V, E, env, bounds, object_radius, resolution, start_pose, goal_region, elapsed_time):
    """
    Plots the path from start node to goal region as well as the graph (or tree) searched with the Sampling Based Algorithms.
    
    Args:
        algo_name (str): The name of the algorithm used (used as title of the plot)
        path (list<(float, float), (float, float)>): The sequence of coordinates traveled to reach goal from start node
        V (set<(float, float)>): All nodes in the explored graph/tree
        E (set<(float, float), (float, float)>): The set of all edges considered in the graph/tree
        env (yaml environment): 2D yaml environment for the path planning to take place
        bounds (int int int int): min x, min y, max x, and max y of the coordinates in the environment.
        object_radius (float): Radius of our object.
        resolution (int): Number of segments used to approximate a quarter circle around a point.
        start_pose (float, float): Coordinates of initial point of the path.
        goal_region (Polygon): A polygon object representing the end goal.
        elapsed_time (float): The it took for the algorithm to run.
    
    Return:
        None
    
    Action:
        Plots a path using the environment module.
    """
    graph_size = len(V)
    path_size = len(path)
    # Calculate path length
    path_length = 0.0
    for i in xrange(len(path) - 1):
        path_length += euclidian_dist(path[i], path[i+1])
    
    # Create title with descriptie information based on environment, path length, and event_elapsed_time
    title = algo_name + "\n" + str(graph_size) + " Nodes. " + str(len(env.obstacles)) + \
            " Obstacles. Path Size: " + str(path_size) + "\n Path Length: " + str(path_length) + \
            "\n Runtime(s)= " + str(elapsed_time)
    
    # Plot environment
    env_plot = plot_environment(env, bounds)
    # Add title
    env_plot.set_title(title)
    # Plot goal
    plot_poly(env_plot, goal_region, 'green')
    # Plot start
    buffered_start_vertex = Point(start_pose).buffer(pnject_radius, resolution)
    plot_ploy(env_plot, buffered_start_vertex, 'red')
    
    # Plot Edges explored by ploting lines between each edge
    for edge in E:
        line = LineString([edge[0], edge[1]])
        plot_line(env_plot, line)
    
    # Plot path
    plot_path(env_plot, path, object_radius)

def euclidian_dist(point1, point2):
    return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def plot_path(env_plot, path, object_radius):
    # Plots path by taking an environment plot and ploting in red the edges taht form part of the path
    line = LineString(path)
    x, y = line.xy
    env_plot.plot(x, y, color='red', linewith=3, solid_capstyle='round', zorder=1)