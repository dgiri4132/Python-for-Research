import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'Python Projects'
chart.x_labels = ['yt-dlp','markitdown','skills']
plot_dicts = [
{'value': 184315, 'label': 'Description of yt-dlp.'},
{'value': 173599, 'label': 'Description of mark-it-down.'},
{'value': 169048, 'label': 'Description of skills.'},
]

chart.add('', plot_dicts)
chart.render_in_browser()
