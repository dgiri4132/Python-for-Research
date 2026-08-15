import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

languages=['JavaScript','Ruby','C','Java','Perl']
Urls = []
all_languages={}
for language in languages:
    URL = 'https://api.github.com/search/repositories?q=language:'+str(language)+'&sort=star'
    r = requests.get(URL)
    print("Status code: ", r.status_code)
    Urls.append(URL)
    response_dict = r.json()
    print("Total repositories: ", response_dict['total_count'])
    repo_dicts = response_dict['items']
    all_languages[language]=repo_dicts



for language, repo_dicts in all_languages.items():
    names, plot_dicts = [], []
    for repo_dict in repo_dicts[:10]:
        names.append(repo_dict['name'])
        plot_dict = {
            'value' : repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink' : repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
    my_style = LS('#333366', base_style = LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style = my_style)
    chart.title = 'Most-Starrted '+str(language)+' Projects on Github'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_in_browser()