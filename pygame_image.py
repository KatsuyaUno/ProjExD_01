import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    kton_img= pg.image.load("ex01/fig/3.png")
    kton_img= pg.transform.flip(kton_img, True, False) 
    #kk_img= pg.transform.rotozoom(kk_img, 10, 1.0)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(kton_img, [100, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()