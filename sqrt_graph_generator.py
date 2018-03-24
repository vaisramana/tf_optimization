import tensorflow as tf

a = tf.placeholder(tf.float32, name="in")
b = tf.sqrt(a, name="out")


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    graph = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def, ["out"], ["in"])
    tf.train.write_graph(graph, '.', './graph_sqrt.pb', as_text=False)

