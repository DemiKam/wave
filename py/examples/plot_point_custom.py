# Plot / Point / Custom
# No description available.
# ---
import random

from synth import FakeScatter
from telesync import Site, data, ui

site = Site()

page = site['/demo']

n = 40
f = FakeScatter()
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Point, custom',
    data=data('price performance discount', n),
    vis=ui.vis([ui.mark(mark='point', x='=price', y='=performance', size='=discount', size_range='4 30',
                        fill_color='#eb4559', stroke_color='#eb4559', stroke_size=1, fill_opacity=0.3,
                        stroke_opacity=1)])
))
v.data = [(x, y, random.randint(1, 10)) for x, y in [f.next() for _ in range(n)]]

page.sync()