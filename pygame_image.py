import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False)

    images=list()
    
    kton_img= pg.image.load("ex01/fig/3.png")
    kton_img= pg.transform.flip(kton_img, True, False) 
    kton2_img= pg.transform.rotozoom(kton_img, 3, 1.0)
    kton3_img= pg.transform.rotozoom(kton_img, 6, 1.0)
    kton4_img= pg.transform.rotozoom(kton_img, 9, 1.0)
    kton5_img= pg.transform.rotozoom(kton_img, 6, 1.0)
    kton6_img= pg.transform.rotozoom(kton_img, 3, 1.0) 
   


    images.append(kton_img)
    images.append(kton2_img)
    images.append(kton3_img)
    images.append(kton4_img)
    images.append(kton5_img)
    images.append(kton6_img)
    

    tmr = 0

    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [x, 0])
        screen.blit(bg2_img,[1600+x,0])
        screen.blit(images[tmr%6],[300,200])
        pg.display.update()
        tmr += 1 
        x -= 1
        if(x+1600==0):
            x = 0

        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()