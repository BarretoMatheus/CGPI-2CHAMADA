import cairo
import math

surface=cairo.ImageSurface(cairo.FORMAT_ARGB32, 512,256)
c=cairo.Context(surface)

c.set_source_rgb(1,1,0)
c.paint()

c.set_source_rgb(0,1,1)
c.set_line_width(4)
c.rectangle(200,50,100,50)
c.stroke()

c.set_source_rgb(1,1,1)
c.arc(100,80,40,0,2*math.pi)
c.fill_preserve()
c.set_line_width(4)

c.set_source_rgb(1,0,0)

c.stroke()

surface.write_to_png('formas.png')