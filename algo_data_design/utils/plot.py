def get_plot_colour_by_index(idx, colours_to_avoid=[]):
    # https://matplotlib.org/stable/gallery/color/named_colors.html
    background = 'w'
    all_colours = ['b', 'g', 'r', 'c', 'y', 'tab:gray', 'tab:pink', 'tab:brown', 'tab:purple', 'tab:orange',
                   'chartreuse', 'm', 'cornflowerblue', 'darkviolet', 'crimson', 'fuchsia', 'salmon', 'indigo', 'k']
    available_colours = []
    for c in all_colours:
        if c not in colours_to_avoid:
            available_colours.append(c)
    return available_colours[(idx % len(available_colours))]
