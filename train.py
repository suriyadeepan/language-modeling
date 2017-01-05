PATH = 'data/madurai/'
#PATH = 'data/sms/'

import data
import utils
import char_rnn

if __name__ == '__main__':
    # fetch dataset
    X, Y, idx2ch, ch2idx = data.load_data(path=PATH)

    batch_size = 256

    # training set batch generator
    trainset = utils.rand_batch_gen(X, Y, batch_size= batch_size)

    # build the model
    num_classes = len(idx2ch)
    net = char_rnn.CharRNN(seqlen= X.shape[-1], 
                           num_classes= num_classes,
                           num_layers= 4,
                           state_size= 256,
                           epochs= 1000000,
                           learning_rate= 0.1,
                           batch_size= batch_size,
                           ckpt_path= 'ckpt/madurai/',
                           model_name= 'madurai_lm')

    # train on trainset
    net.train(trainset)
