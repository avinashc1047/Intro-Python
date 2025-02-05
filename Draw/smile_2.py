from designer import *
set_window_color('lightsalmon')
set_window_size(2000,1300)

def smile(x_val:int, y_val:int):
    circle('yellow', 250, x_val, y_val)
    circle('olive', 50, (x_val-100), (y_val-100))
    circle('olive', 50, (x_val+100), (y_val-100))
    arc('olive', 3.7, 5.8, 20, (x_val-145), (y_val-130), 300, 250)
    #(color, start, stop, thick, leftx, topy, width, height)
    return

draw(smile(0, 650), smile(500, 650), smile(1000, 650), smile(1500, 650), smile(2000, 650))
