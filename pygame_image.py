import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    images=list()
    
    kton_img= pg.image.load("ex01/fig/3.png")
    kton_img= pg.transform.flip(kton_img, True, False) 
    kton2_img= pg.transform.rotozoom(kton_img, 10, 1.0)
    kton3_img= pg.transform.rotozoom(kton_img, 15, 1.0)
    kton4_img= pg.transform.rotozoom(kton_img, 20, 1.0)
    kton5_img= pg.transform.rotozoom(kton_img, 25, 1.0)
    kton6_img= pg.transform.rotozoom(kton_img, 30, 1.0) 
    kton7_img= pg.transform.rotozoom(kton_img, 35, 1.0)
    kton8_img= pg.transform.rotozoom(kton_img, 40, 1.0)
    kton9_img= pg.transform.rotozoom(kton_img, 45, 1.0)
    kton10_img= pg.transform.rotozoom(kton_img, 50, 1.0)


    images.append(kton_img)
    images.append(kton2_img)
    images.append(kton3_img)
    images.append(kton4_img)
    images.append(kton5_img)
    images.append(kton6_img)
    images.append(kton7_img)
    images.append(kton8_img)
    images.append(kton9_img)
    images.append(kton10_img)

    tmr = 0

    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img,[1600+x,0])
        screen.blit(images[tmr%10],[300,200])
        pg.display.update()
        tmr += 1 
        x -= 1
        if(x+1600==0):
            x = 0

        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()