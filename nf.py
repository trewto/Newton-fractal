import pygame
import random
# Pygame initialization
pygame.init()

# Constants
SCREEN_SIZE = (700, 700)
# how many points ? 
p = 10 ; 
# that means -50 to +50 coordinate
CELL_SIZE =  SCREEN_SIZE[0] / (2 * p ); 


def coordinate_to_color(x, y,b=100):
    p = 10
    # Normalize x and y to be in the range of 0 to 1
    normalized_x = (x + p) / (2 * p)
    normalized_y = (y + p) / (2 * p)

    # Map normalized coordinates to RGB values (0-255)
    r = int(normalized_x * 255)
    if r >255:
        r = 255
    elif r<0 :
        r =0
    g = int(normalized_y * 255)
    if g > 255:
        g = 255
    elif g<0:
        g= 0
     # Constant blue value

    return r, g, b  # Return the RGB color tuple



# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
step = 1
points = []  # Store points' initial positions







def draw_c(x, y, radius):
    # Since each cell in the grid is CELL_SIZE, simply multiply the coordinate by CELL_SIZE
    # and add the screen center offset to get the correct pixel position
    coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    pygame.draw.circle(screen, BLACK, coord, radius)
def draw_with_color(x, y, radius):
    coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    pygame.draw.circle(screen, coordinate_to_color(x,y), coord, radius)
def draw_with_colorr_back_to_inital(x, y,p,q, radius):
    coord = (x * CELL_SIZE + SCREEN_SIZE[0] // 2, -y * CELL_SIZE + SCREEN_SIZE[1] // 2)
    pygame.draw.circle(screen, coordinate_to_color(p,q), coord, radius)


def newrph(p, q):
    z = complex(p, q)
    if z == 0:  # Check if z is zero to avoid division by zero
        return z
    else:
        # here will be the equation
        result = z - (z**5 - 16) / (5 * z**4)
        return result

for _ in range(50000):  # Generate  random points
        COORDINATE_RANGE = 10 ; 
        x = random.uniform(-COORDINATE_RANGE, COORDINATE_RANGE)
        y = random.uniform(-COORDINATE_RANGE, COORDINATE_RANGE)
        color = 1; 
        points.append((x, y,x,y))

#points = [(i, j,i,j) for i in range(-50, 50, 2) for j in range(-50, 50, 2)]
#points  = [(6,7,6,7)]
itarate= 0 
m=1
j=20;
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            step += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            itarate += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            step -= 1
       

    if step == 1:
      
        #print(points)
        #for point in points:
        #    draw_c(point[0], point[1], 3)

        # Draw x and y axis lines
        pygame.draw.line(screen, BLACK, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        step = 1

    elif step == 2:
        for point in points:
            draw_c(point[0], point[1], 2)


        # Draw x and y axis lines
        pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        
        #please disable it 

        if j>0:
            itarate= 1; 
            j = j-1;
        
        if  itarate  ==1:
            itarate = 0 ; 
            i = 0; 
            for point in points:

                ita = newrph(point[0],point[1])
                nx = ita.real 
                ny = ita.imag
                points[i] = (nx,ny , point[2],point[3])
                print(i)
                i+= 1 

    elif step ==3:
        pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        for point in points:
            draw_with_color(point[0], point[1], 2)

    elif step==4:
        pygame.draw.line(screen, RED, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
        pygame.draw.line(screen, RED, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)
        for point in points:
            draw_with_colorr_back_to_inital(point[2], point[3],point[0], point[1], 2)
        #print(points)    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
