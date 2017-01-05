import sms_data as data
import utils
import char_rnn

if __name__ == '__main__':
    # fetch dataset
    X, Y, idx2ch, ch2idx = data.process_data()

    # training set batch generator
    trainset = utils.rand_batch_gen(X, Y, batch_size=128)

    # build the model
    num_classes = len(idx2ch)
    net = char_rnn.CharRNN(seqlen=X.shape[-1], 
                           num_classes = num_classes,
                           state_size = 128,
                           epochs = 50000,
                           learning_rate = 0.1,
                           batch_size=128, ckpt_path= 'ckpt/')

    # train on trainset
    sess, step = net.train(trainset, sess)
