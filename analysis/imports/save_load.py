import pickle
def save_data(data,fn):
    fn = fn[:-4]+'.p'
    pickle.dump(data,open(fn,'wb'))

def load_data(fn):
    fn = fn[:-4] + '.p'
    return pickle.load(open(fn,'rb'))
