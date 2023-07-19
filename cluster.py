""" kmeans clustering simulation """
import pygame
import sys
import numpy as np
from objects import Ball
from time import sleep
from typing import List, Tuple
from sklearn.datasets import make_blobs

# PARAMS
BACKGROUND: Tuple = (0, 0, 0)

WINSIZE: Tuple = (1000, 800)

FRAMES: int = 60
# PYGAME PARAMS
pygame.init()

pygame.display.set_caption('K-means clustering simulator')

screen: pygame.Surface = pygame.display.set_mode((WINSIZE[0], WINSIZE[1]))

clock: pygame.time.Clock = pygame.time.Clock()


n_samples: int = 2000
n_components: int = 5
factor: int = 80

X, y_true = make_blobs(n_samples = n_samples,
                       centers = n_components,
                       cluster_std = 0.55)

X  = np.abs(X)

centroids: List = list()

for k in range(n_components):

    centroids.append(Ball(ball_type = f"centroid-{k}",
                          screen = screen,
                          position = X[np.random.randint(len(X) + 5)],
                          radius = 10,
                          color = (np.random.randint(255),
                                   np.random.randint(255),
                                   np.random.randint(255)),
                          factor = factor))

data_points: List = list()

for pos in X:

    data_points.append(Ball(ball_type = "point",
                            screen = screen,
                            position = pos,
                            radius = 2,
                            color = (255,255,255),
                            factor = factor))
    

dists = np.zeros(shape = (X.shape[0],n_components))

def run():

    while True:

        screen.fill(BACKGROUND)

        keys = pygame.key.get_pressed()

        for point in data_points:

            point.draw_ball()

        for centroid in centroids:

            centroid.draw_ball()

            if keys[pygame.K_SPACE]:

                for i, value in enumerate(data_points):

                    for j, k in enumerate(centroids):

                        dists[i,j]  = np.sqrt(np.sum((value.position - k.position)**2))

                points = np.array([np.argmin(i) for i in dists])   

                for idx in range(n_components):

                    update_centroid = X[points == idx].mean(axis=0) 

                    centroids[idx].position = update_centroid 

                    for i, k in enumerate(points):

                        if idx == k:

                            data_points[i].color = centroids[idx].color

                sleep(0.1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()


        pygame.display.update()

        clock.tick(FRAMES)


if __name__ == "__main__":

    run()