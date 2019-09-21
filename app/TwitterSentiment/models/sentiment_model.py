import pickle
import os
import numpy as np
import sys
from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM
from TwitterSentiment.utilities.callbacks import MetricsCallback, PlottingCallback
from TwitterSentiment.utilities.data_preparation import get_labels_to_categories_map, get_class_weights2, onehot_to_categories
from TwitterSentiment.sklearn.metrics import f1_score, precision_score
from TwitterSentiment.sklearn.metrics import recall_score
from TwitterSentiment.data.data_loader import DataLoader
from TwitterSentiment.models.nn_models import build_attention_RNN
from TwitterSentiment.utilities.data_loader import get_embeddings, Loader, prepare_dataset

np.random.seed(1337)

def Sentiment_Analysis(WV_CORPUS, WV_DIM, max_length, PERSIST,  FINAL=True, GOLD=True):
    """
    ##Final:
    - if FINAL == False,  then the dataset will be split in {train, val, test}
    - if FINAL == True,   then the dataset will be split in {train, val}.
    Even for training the model for the final submission a small percentage
    of the labeled data will be kept for as a validation set for early stopping
    
    ##SEMEVAL_GOLD:
    If True, the SemEval gold labels will be used as the testing set

    ##PERSIST
    # set PERSIST = True, in order to be able to use the trained model later
    """
    best_model = lambda: "model.hdf5"
    best_model_word_indices = lambda: "model_word_indices.pickle"


    ############################################################################
    # LOAD DATA
    ############################################################################
    
    embeddings, word_indices = get_embeddings(corpus=WV_CORPUS, dim=WV_DIM)

    if PERSIST:
        pickle.dump(word_indices, open(best_model_word_indices(), 'wb'))

    loader = Loader(word_indices, text_lengths=max_length)

    if FINAL:
        print("\n > running in FINAL mode!\n")
        training, testing = loader.load_final()
    else:
        training, validation, testing = loader.load_train_val_test()

    if GOLD:
        print("\n > running in Post-Mortem mode!\n")
        gold_data = DataLoader().get_gold()
        gX = [obs[1] for obs in gold_data]
        gy = [obs[0] for obs in gold_data]
        gold = prepare_dataset(gX, gy, loader.pipeline, loader.y_one_hot)

        validation = testing
        testing = gold
        FINAL = False

    print("Building NN Model...")
    
    ############################################################################
    # NN MODEL
    ############################################################################
    
    nn_model = build_attention_RNN(embeddings, classes=3, max_length=max_length,
                                unit=LSTM, layers=2, cells=150,
                                bidirectional=True,
                                attention="simple",
                                noise=0.3,
                                final_layer=False,
                                dropout_final=0.5,
                                dropout_attention=0.5,
                                dropout_words=0.3,
                                dropout_rnn=0.3,
                                dropout_rnn_U=0.3,
                                clipnorm=1, lr=0.001, loss_l2=0.0001,)

    # nn_model = cnn_simple(embeddings, max_length)

    # nn_model = cnn_multi_filters(embeddings, max_length, [3, 4, 5], 100,
    #                              noise=0.1,
    #                              drop_text_input=0.2,
    #                              drop_conv=0.5, )

    print(nn_model.summary())
    """
    ############################################################################
    # APPLY CLASS WEIGHTS
    ############################################################################
    
    class_weights = get_class_weights2(onehot_to_categories(training[1]),
                                    smooth_factor=0)
    print("Class weights:",
        {cat_to_class_mapping[c]: w for c, w in class_weights.items()})

    history = nn_model.fit(training[0], training[1],
                        validation_data=validation if not FINAL else testing,
                        epochs=15, batch_size=50,
                        class_weight=class_weights, callbacks=_callbacks)

    pickle.dump(history.history, open("hist.pickle", "wb"))
    nn_model.save_weights(os.path.join("/home/pszmelcz/Desktop/TwitterSentimentAnalysis", "bi_model_weights_1.h5"))
    """