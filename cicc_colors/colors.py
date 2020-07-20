"""
CICC WM colors for slides, reports and tables.
"""

class Color:
    """This class is used to represent color.  Components red, green, blue
    are in the range 0 to 255"""

    def __init__(self, r=0, g=0, b=0, a=255):
        "Initialize with red, green, blue, alpha in range [0-255]"
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

    def __repr__(self):
        return "Color({},{},{},{})".format(self.red, self.green, self.blue, self.alpha)

    @property
    def __key__(self):
        return self.red, self.green, self.blue, self.alpha

    def __hash__(self):
        return hash(self.__key__)

    def __comparable__(self,other):
        return isinstance(other,Color)

    def rgb(self):
        "Returns a three-tuple of components"
        return (self.red, self.green, self.blue)

    def rgba(self):
        "Returns a four-tuple of components"
        return (self.red, self.green, self.blue, self.alpha)

    def normal_rgb(self):
        "Returns a three-tuple of components, range 0-1"
        return tuple([x/255 for x in self.rgb()])

    def normal_rgba(self):
        "Returns a four-tuple of components, range 0-1"
        return tuple([x/255 for x in self.rgba()])

    def hex(self):
        return ('#%02x%02x%02x' % self.rgb()).upper()

    def hexa(self):
        return ('#%02x%02x%02x%02x' % self.rgba()).upper()

    @property
    def normalizedAlpha(self):
        return self.alpha/255

def RGB2Hex(red, green, blue):
    return Color(red,green,blue).hex()

def Hex2RGB(hexstr):
    red = int(hexstr[1:3], 16)
    green = int(hexstr[3:5], 16)
    blue = int(hexstr[5:], 16)
    return Color(red,green,blue).rgb()

"""
colors from ppt template, repersent the position of each color.
"""
#新图表色
ppt_1_1 = Color(203,170,123)
ppt_1_2 = Color(190,192,194)
ppt_1_3 = Color(199,103,75)
ppt_1_4 = Color(138,144,165)
ppt_1_5 = Color(223,151,83)
ppt_1_6 = Color(222,201,172)
ppt_1_7 = Color(229,230,231)
ppt_1_8 = Color(213,141,120)
ppt_1_9 = Color(177,181,195)
ppt_1_10 = Color(231,177,126)

#新核心色
ppt_2_1 = Color(222,206,166)
ppt_2_2 = Color(236,236,236)
ppt_2_3 = Color(231,177,126)
ppt_2_4 = Color(155,53,25)

#新其他文本填充色
ppt_3_1 = Color(180,162,141)
ppt_3_2 = Color(205,193,179)
ppt_3_3 = Color(216,191,154)
ppt_3_4 = Color(216,217,218)
ppt_3_5 = Color(229,185,173)
ppt_3_6 = Color(223,216,230)
ppt_3_7 = Color(99,107,135)
ppt_3_8 = Color(207,183,123)
ppt_3_9 = Color(185,65,30)
ppt_3_10 = Color(215,125,40)

#线条色
ppt_4_1 = Color(115,30,0)
ppt_4_2 = Color(189,140,70)
ppt_4_3 = Color(60,70,105)
ppt_4_4 = Color(127,127,127)
ppt_4_5 = Color(0,112,192)
ppt_4_6 = Color(155,105,255)
ppt_4_7 = Color(215,125,40)
ppt_4_8 = Color(130,100,65)