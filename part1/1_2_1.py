def showregions(data):
    regions=['Coast','EU','EU and coast','Neither']
    ceu=0 #counter eu only
    ceuc=0 #counter eu and coast
    cc=0 #counter coast only
    cn=0 #counter neither
    for i in data.index:
        if data['coastline'][i]=='yes' and data['EU'][i]=='no':
             cc+=1
        elif data['EU'][i]=='yes' and data['coastline'][i]=='no':
             ceu+=1
        elif data['coastline'][i]=='yes' and data['EU'][i]=='yes':
             ceuc+=1
        elif data['coastline'][i]=='no' and data['EU'][i]=='no':
            cn+=1
    cities=[cc,ceu,ceuc,cn]
    plt.bar(regions,cities)
    plt.show()
showregions(data)
