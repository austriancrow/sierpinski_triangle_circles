import pygame
import time


def draw_circles(surf, pos, radius, use_radius = False, depth = 1, steps=10, screen=(0,0)):
  (x, y) = pos
  if 0 < x and x < screen[0] and 0 < y and y < screen[1]:
    pygame.draw.circle(surf, (255, 255, 255), pos, radius if use_radius else 1, width=1)
  if radius - depth*steps > 1: 
    new_dist = radius
    draw_circles(surf, (x + new_dist, y), radius/2, use_radius, depth, steps/2, screen)
    draw_circles(surf, (x - new_dist, y), radius/2, use_radius, depth, steps/2, screen)
    draw_circles(surf, (x, y + new_dist), radius/2, use_radius, depth, steps/2, screen)
    #draw_circles(surf, (x, y - new_dist), radius/2)


def main(screen_width, screen_height):
  pygame.init()
  screen = pygame.display.set_mode([screen_width, screen_height])
  steps = 100
  running = True
  screen.fill((0,0,0))
  use_circles = True
  depth = 10
  surf = pygame.Surface([screen_width, screen_height])
  radius = screen_width
  pos = (screen_width/2, 0)
  draw_circles(surf, pos, radius, use_circles, depth, steps, (screen_width, screen_height))
  surf_center = (
    (screen_width - surf.get_width()) / 2,
    (screen_height - surf.get_height()) / 2
  )

  updated = True
  while running:
    # capture events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        elif event.key == pygame.K_c:
          use_circles = not use_circles
        elif event.key == pygame.K_MINUS:
          radius -= steps
          depth -= 1
        elif event.key == pygame.K_PLUS:
          radius += steps
          depth += 1
        updated = True
    if updated:    
      surf.fill((0, 0, 0))
      draw_circles(surf, pos, radius, use_circles, depth, steps, (screen_width, screen_height))
    
      screen.blit(surf, surf_center)
      pygame.display.update()
      updated = False
        
      

      # pygame.draw.rect(
      #   screen,
      #   (255, 255, 255),
      #   (
      #     mouse_pos1[0],
      #     mouse_pos1[1],
      #     w_length,
      #     h_length
      #   )
      # )
    

    
    # fill background white
    

    # draw circle
    # pygame.draw.circle(screen, color[curColor%3], (width/2, height/2), 75)

    # create surface and get rectangle
    # surf = pygame.Surface((50,50))
    # surf.fill(color[curColor])
    # rect = surf.get_rect()
    # surf_center = (
    #   (screen_width-surf.get_width())/2,
    #   (screen_height-surf.get_height())/2
    # )

    # screen.blit(surf, surf_center)

    # #flip display (updates whole screen)
    # pygame.display.flip()



if __name__ == '__main__':
  main(1920, 1080)