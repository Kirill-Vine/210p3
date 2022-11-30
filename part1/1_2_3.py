def pophist(data):
    countriespop=Series(data['population'].values, index=list(data['country']))
    countriespop = (countriespop.reset_index().drop_duplicates(subset='index', keep='last').set_index('index').sort_index())
    countriespop.hist(bins=5)
pophist(data)
