import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    # Slice the series into windows 
    for i in range(window_size, len(series)):
        X.append(series[i-window_size:i])
        y.append(series[i])

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    # given - fix random seed - so we can all reproduce the same results on our default time series
    np.random.seed(0)


    # build an RNN to perform regression on our time series input/output data
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size,1)))
    model.add(Dense(1))


    # build model using keras documentation recommended optimizer initialization
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)

    # run your model!
    model.fit(X_train, y_train, epochs=1000, batch_size=50, verbose=1)

    # generate predictions for training
    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    uniques = sorted(set(text))
    print("Characters in the original text:")
    print(uniques)

    # remove as many non-english characters and character sequences as you can 

    # get all valid characters (lowercase letters, punctuation, space)
    import string
    valid_characters = list(string.ascii_lowercase)
    valid_characters = valid_characters + list([' ', '!', '"', '&', "'", '(', ')', ',', '-', '.', ':', ';', '?'])
    valid_characters = sorted(valid_characters)
    print("Characters considered to be valid:")
    print(valid_characters)

    # determine characters to be removed
    invalid_characters = set(uniques).difference(valid_characters)
    print("Characters considered to be invalid which will be removed from the text:")
    print(invalid_characters)
    for c in invalid_characters:
        text = text.replace(c, '')
        
    # shorten any extra dead space created above
    text = text.replace('  ',' ')

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    # Slice the series into windows 
    for i in range(window_size, len(text), step_size):
        inputs.append(text[i-window_size:i])
        outputs.append(text[i])

    return inputs,outputs
    