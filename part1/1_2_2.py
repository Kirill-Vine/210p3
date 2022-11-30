def eumap(data):
    countries=data.groupby('country')
    for name, group in countries:
        plt.plot(group.longitude, group.latitude, marker='o', linestyle='', markersize=5, label=name)
eumap(data)
