# CICC Colors

Library of color palettes for CICC WM slides, reports and tables.
CICC调色板可以用于在使用Python生成图表或报告时，能够匹配CICC的颜色模板。

## Install

`pip install cicc_colors`

## How to Use

1. 直接使用模板颜色,颜色使用 *ppt_x_y* 来标记, *x*, *y* 是CICC PPT模板中色版的位置。

```python
from cicc_colors import colors
colors.ppt_1_1
>>> Color(203,170,123,255)
colors.ppt_1_1.hex()
>>> 'CBAA7B'
colors.ppt_1_1.rgb()
>>> (203,170,123)
colors.ppt_1_1.normal_rgb()
>>> (0.796078431372549, 0.6666666666666666, 0.4823529411764706)
```

2. 自定义颜色，使用 r,g,b 来定义颜色后使用

```python
from cicc_colors import colors
user_color = colors.Color(115,30,0)
>>> Color(115,30,0)
user_color.hex()
>>> '731E00'
user_color.hex(with_hex = True)
>>> '#731E00'
user_color.rgb()
>>> (115, 30, 0)
user_color.normal_rgb()
>>> (0.45098039215686275, 0.11764705882352941, 0.0)
```

3. rgb 转 hex

```python
from cicc_colors import colors
colors.RGB2Hex(203,170,123)
>>> '#CBAA7B'
```

4. hex 转 rgb

```python
from cicc_colors import colors
colors.Hex2RGB('#FF0FF0')
>>> (255, 15, 240)
```

## How to Contribute