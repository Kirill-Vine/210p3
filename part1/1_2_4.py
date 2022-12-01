def subplots(data):
    fig, axes=plt.subplots(2,2,figsize=(30,30))
    ceu=0 #counter eu only
    ceuc=0 #counter eu and coast
    cc=0 #counter coast only
    cn=0 #counter neither
    for i in data.index:
        if data['coastline'][i]=='yes' and data['EU'][i]=='no':
            if data['temperature'][i]>10:
                color='red'
            elif data['temperature'][i]<6:
                color='blue'
            else:
                color='orange'
            axes[0][0].plot(data['city'][i],data['latitude'][i], 'o', c=color)
            cc+=1
        elif data['EU'][i]=='yes' and data['coastline'][i]=='no':
            if data['temperature'][i]>10:
                color='red'
            elif data['temperature'][i]<6:
                color='blue'
            else:
                color='orange'
            axes[0][1].plot(data['city'][i],data['latitude'][i], 'o', c=color)
            ceu+=1
        elif data['coastline'][i]=='yes' and data['EU'][i]=='yes':
            if data['temperature'][i]>10:
                color='red'
            elif data['temperature'][i]<6:
                color='blue'
            else:
                color='orange'
            axes[1][0].plot(data['city'][i],data['latitude'][i], 'o', c=color)
            ceuc+=1
        elif data['coastline'][i]=='no' and data['EU'][i]=='no':
            if data['temperature'][i]>10:
                color='red'
            elif data['temperature'][i]<6:
                color='blue'
            else:
                color='orange'
            axes[1][1].plot(data['city'][i],data['latitude'][i], 'o', c=color)
            cn+=1
    axes[0][0].set_title('Coastline only')
    axes[0][1].set_title('EU only')
    axes[1][0].set_title('Coastline and EU')
    axes[1][1].set_title('Neither')
    axes[0][0].set_xticks(range(cc))
    axes[0][1].set_xticks(range(ceu))
    axes[1][0].set_xticks(range(ceuc))
    axes[1][1].set_xticks(range(cn))
    axes[0][0].set_xticklabels(range(cc))
    axes[0][1].set_xticklabels(range(ceu))
    axes[1][0].set_xticklabels(range(ceuc))
    axes[1][1].set_xticklabels(range(cn))
    plt.show()
subplots(data)
