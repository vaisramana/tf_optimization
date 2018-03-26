import tensorflow as tf
import sys

print "read from ", sys.argv[1]
with tf.Session() as sess:
    with open(sys.argv[1], 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        print graph_def
