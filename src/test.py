import gzip, cPickle
f = gzip.open('mnist.pkl.gz', 'rb')
#(x_train, t_train), (x_valid, t_valid), (x_test, t_test)  = cPickle.load(f)
x_train  = cPickle.load(f)
f.close()

print "x_train" 
print x_train
print x_train.shape
#print "t_train"
#print t_train
#print t_train.shape
#print "x_valid"
#print x_valid
#print x_valid.shape
#print "t_valid"
#print t_valid
#print t_valid.shape
#print "x_test"
#print x_test
#print x_test.shape
#print "t_test"
#print t_test
#print t_test.shape
