def average_temp(data):
    eu=[] #eu only
    euc=[] #eu and coast
    c=[] #coast only
    n=[] #neither
    for i in data.index:
        if data['coastline'][i]=='yes' and data['EU'][i]=='no':
            c.append(data['temperature'][i])
        elif data['EU'][i]=='yes' and data['coastline'][i]=='no':
            eu.append(data['temperature'][i])
        elif data['coastline'][i]=='yes' and data['EU'][i]=='yes':
            euc.append(data['temperature'][i])
        elif data['coastline'][i]=='no' and data['EU'][i]=='no':
            n.append(data['temperature'][i])
    for i in data.index:
        if math.isnan(data['temperature'][i]):
            if data['coastline'][i]=='yes' and data['EU'][i]=='no':
                data['temperature'][i]=round(np.nanmean(np.array(c)),2)
            elif data['EU'][i]=='yes' and data['coastline'][i]=='no':
                data['temperature'][i]=round(np.nanmean(np.array(eu)),2)
            elif data['coastline'][i]=='yes' and data['EU'][i]=='yes':
                data['temperature'][i]=round(np.nanmean(np.array(euc)),2)
            elif data['coastline'][i]=='no' and data['EU'][i]=='no':
                data['temperature'][i]=round(np.nanmean(np.array(n)),2)
    data.to_csv("EuCitiesTemperatures.csv", columns=data.columns)
average_temp(data)
