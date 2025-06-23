import tensorflow as tf


print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU'))) 

if tf.test.is_gpu_available(): 

    print("GPU is available.") 

else: 

    print("GPU is not available.")