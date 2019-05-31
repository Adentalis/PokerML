import pygame as pg

class HandTestGui:

    def start(self):

     #   pics = [pg.image.load('R1.png')]
        test = pg.image.load('2C.jpg')
        pg.init()
        win = pg.display.set_mode((500, 500))
        pg.display.set_caption("PokerML - HandTest")

        x = 50
        y = 50
        width = 40
        height = 60
        vel = 5
        run = True
        while run:
            pg.time.delay(10)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False


            win.blit(test, (0, 0))
            pg.draw.rect(win, (255, 0, 0), (x, y, width, height))
            pg.display.update()
