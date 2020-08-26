import pygame
import random
pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption('Sorting visualizer')

array=[0]*300
color_array=[(255,255,255)]*300
color=[(50,20,40),(255,0,0),(0,255,0),(0,0,0)]

def generate_array():
    for i in range(300):
        color_array[i]=color[0]
        array[i]=random.randint(1,500)

generate_array()

def fill():
    screen.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(5)

def fill2():
    screen.fill((255,255,255))
    drawins()
    pygame.display.update()
    pygame.time.delay(20)

def mergesort(array,l,r):
    mid=(l+r)//2
    if(l<r):
        mergesort(array,l,mid)
        mergesort(array,mid+1,r)
        merge(array,l,mid,mid+1,r)

def merge(array,x1,y1,x2,y2):
    i=x1
    j=x2
    temp=[]
    while i<=y1 and j<=y2:
        color_array[i]=color[1]
        color_array[j]=color[1]
        fill()
        color_array[i]=color[0]
        color_array[j]=color[0]
        if array[i]<array[j]:
            temp.append(array[i])
            i+=1
        else:
            temp.append(array[j])
            j+=1
    while i<=y1:
        color_array[i] = color[1]
        fill()
        color_array[i] = color[0]
        temp.append(array[i])
        i+=1
    while j<=y2:
        color_array[j] = color[1]
        fill()
        color_array[j] = color[0]
        temp.append(array[j])
        j+=1
    j=0
    for i in range(x1,y2+1):
        pygame.event.pump()
        array[i]=temp[j]
        j+=1
        color_array[i]=color[2]
        fill()
        if y2 - x1 == len(array) - 2:
            color_array[i] = color[3]
        else:
            color_array[i] = color[0]


def draw():
    c1=3
    c2=2
    for i in range(1,300):
        pygame.draw.line(screen,color_array[i],(c1*(i-3),0),(c1*(i-3),array[i]),2)

running =True

while(running):
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    mergesort(array, 1, len(array) - 1)
    draw()
    pygame.display.update()
