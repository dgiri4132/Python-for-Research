import pygal_maps_world.maps as mp

wm = mp.World()
wm.title = "Populations of COuntries in North America"
wm.add('North America' , {'ca' : 34126000, 'us': 309349000, 'mx' : 113423000})

wm.render_in_browser()
""" Here we also pass dictionary contrary to the previous one. It helps to highlight the population, darker meaning more populated. """