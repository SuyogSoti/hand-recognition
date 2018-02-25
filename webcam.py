import pygame
import pygame.camera

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()

image = image.map_rbg()
print(image.get_buffer())
