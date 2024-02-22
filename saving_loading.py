#SAVING THE MODEL
gen.save('pix2.h5')

#LOADING THE MODEL

from tensorflow.keras.models import load_model
loaded_model=load_model('pix2.h5')
from tensorflow.keras.optimizers import Adam

# Define optimizer, loss, and metrics
optimizer = Adam(learning_rate=0.001)
loss = 'binary_crossentropy'
metrics = ['accuracy']

# Compile the model with the specified optimizer, loss, and metrics
loaded_model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
loaded_model.fit(train_dataset, epochs=10,validation_data=test_dataset)
