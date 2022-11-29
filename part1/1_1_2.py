def subset(data):
    cities=[]
    countries=list(data['country'].values)
    countries1=list()
    for i in data.index:
        if data['latitude'][i]>=40 and data['latitude'][i]<=60 and data['longitude'][i]>=15 and data['longitude'][i]<=30:
            cities.append(data['city'][i])
        else:
            countries1.append(countries[i])
            countries[i]=0
    lst = [i for i in countries if i != 0]
    maximalc=list()
    for i in lst:
        if i not in countries1:
            if i not in maximalc:
                maximalc.append(i)
    return cities, maximalc #list of cities that lie between latitudes 40 to 60 and longitudes 15 to 30, and a list countries have the maximal number of cities in this geographical band
subset(data)
