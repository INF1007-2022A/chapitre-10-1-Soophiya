#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    #un array de 64 valeurs entre -1.3 et 2.5
    return np.linspace(-1.3, 2.5, num = 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    #une fonction qui convertit une liste de coordonées cartésiennes en coordonées polaires
    x = cartesian_coordinates[0]
    y = cartesian_coordinates[1]
    r = np.sqrt(x**2 + y**2)
    
    if x == 0:
        theta = np.pi/2
    else:
        theta = np.arctan(y/x)
    
    return np.array([r, theta])

def find_closest_index(values: np.ndarray, number: float) -> int:
    #une fonction qui trouve l'index de la valeur la plus proche d'un nombre
    return np.argmin(np.abs(values - number))


def graph250():
    #un graphique de f(x) = x**2 *sin(1/(x**2))+ x de 250 points entre [-1,1]

    x = np.range(-1, 1, 250)
    y = x**2 * np.sin(1/(x**2)) + x
    plt.title("graphique de f(x) = x**2 *sin(1/(x**2))+ x de 250 points entre [-1,1]")
    plt.xlabel('axe des x')
    plt.ylabel('axe des y')
    plt.plot(x, y)
    plt.show()
    return None

if __name__ == '__main__':
    linear_values()
    coordinate_conversion(np.array([1, 1]))
    find_closest_index(np.array([1, 2, 3, 4, 5]), 3.2)

    pass
