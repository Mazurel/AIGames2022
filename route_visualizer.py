import folium
import numpy as np
from scipy import sparse
import pandas as pd

BOUNDARIES = [(21.9430, -67.5), (55.7765, -135)]
VIL_THRESHOLD_COLORS = [
    (10000, (0.63, 0.0, 0.01, 1.0)),
    (32.32, (0.87, 0.56, 0.0, 1.0)),
    (12.16, (0.95, 0.75, 0.0, 1.0)),
    (7.08, (0.93, 0.95, 0.0, 1.0)),
    (3.53, (0.38, 0.69, 0.0, 1.0)),
    (0.77, (0.63, 0.94, 0.0, 1.0)),
    (0.52, (0.9, 0.9, 0.9, 0.03)),
]
 
 
def _matrix_to_weather_colormap(sparse_matrix: sparse.csr_matrix) -> np.ndarray:
    matrix = sparse_matrix.toarray()
    result = np.zeros(shape=matrix.shape + (4,))
    for thresh, color in VIL_THRESHOLD_COLORS:
        result[matrix <= thresh] = color
    return result
 
 
def _plot_matrix() -> folium.Map:
    fmap = folium.Map(location=[35, -100], zoom_start=6) 
    return fmap
 
 
def load_and_show_vil(points = None) -> folium.Map:
    plot = _plot_matrix()
    if points is not None:
      for point in points:
        folium.Marker(point[0], icon=folium.Icon(color=point[1])).add_to(plot)
    return plot

proper_list = [[(32.897333333333336, -97.03769444444444), 'red'],
                [(32.78270833333333, -96.99513888888889), 'red'],
                [(32.7651, -96.93934166666666), 'red'],
                [(32.768791666666665, -96.83155277777777), 'red'],
                [(32.858775, -96.80919444444444), 'red'],
                [(32.98796111111111, -96.80902499999999), 'red'],
                [(33.451458333333335, -96.96152777777777), 'red'],
                [(34.31742222222223, -96.61986666666667), 'red'], 
                [(35.69325, -95.86595555555554), 'red'],
                [(33.272932170433606, -96.90278797429484), 'blue'],
                [(33.7305232470049, -96.85142430845241), 'blue'],
                [(34.00958816067647, -96.74132083912704), 'blue'],
                [(34.28865307434804, -96.63121736980167), 'blue'],
                [(34.58051229476809, -96.4757014360186), 'blue'],
                [(34.843602367313956, -96.33153620537053), 'blue'],
                [(35.10669243985982, -96.18737097472246), 'blue'],
                [(35.369782512405685, -96.04320574407438), 'blue'],
                [(35.63287258495155, -95.89904051342631), 'blue']]

my_map = load_and_show_vil(proper_list)
my_map.save(f"waypoints_marked.html")
