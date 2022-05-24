from shapes import Paper, Triangle, Rectangle, Oval
# we are using given code in shapes to create a piece of paper which we can draw objects on such as
# triangles rectangles and ovals. These are all examples of objects, they have attributes such as width, height
# and colour.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def task1():
    paper = Paper()
    rect1 = Rectangle()
    rect2 = Rectangle()

    rect1.set_width(200)
    rect1.set_height(100)
    rect1.set_color('blue')

    rect2.set_width(50)
    rect2.set_height(150)
    rect2.set_color('yellow')

    # when we crate two rectangles and draw them both they do not overlap instead sit next to each other
    # we can place them were we want using the method set_y and set_x

    rect1.set_x(100)
    rect1.set_y(20)
    rect2.set_x(200)
    rect2.set_y(300)

    rect1.draw()
    rect2.draw()
    paper.display()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def task2():
    # if we read the shapes document we can find all the methods and attributes of each shape
    paper = Paper()
    oval1 = Oval()
    tri = Triangle(5,5, 100,5, 100,200)
    # to create a triangle you need to sate the three corner coordinates

    oval1.randomize(20,200)
    # the randomize method randomize all the attributes of the oval such as colour, size and where
    # it is placed on the paper
    oval1.draw()

    tri.set_color('black')
    tri.draw()

    paper.display()

if __name__ == '__main__':
    task1()
    task2()