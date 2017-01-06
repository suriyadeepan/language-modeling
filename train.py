import data
import utils
import char_rnn

import sys


if __name__ == '__main__':
    # get cmd line args from user <- config file
    if len(sys.argv) > 1:
        # get configuration
        g = utils.get_config(sys.argv[1])
        # check if we need to process text file
        if g['data_file'] and utils.isEmpty(g['ckpt_path']):
            # check if folder exists, if not create folder
            utils.assert_dir(g['data_path'])
            data.process_data(filename= g['data_file'],
                    path= g['data_path'])
        # check if checkpoint path exists
        utils.assert_dir(g['ckpt_path'])

        try:
            # fetch dataset
            X, Y, idx2ch, ch2idx = data.load_data(path=g['data_path'])
        except:
            print('\n>> Is the folder {} empty?'.format(g['ckpt_path']))
            print('Shouldn\'t it be?')
            sys.exit()

        # training set batch generator
        trainset = utils.rand_batch_gen(X, Y, batch_size= g['batch_size'])

        # build the model
        num_classes = len(idx2ch)
        net = char_rnn.CharRNN(seqlen= X.shape[-1], 
                               num_classes= num_classes,
                               num_layers= g['num_layers'],
                               state_size= g['state_size'],
                               epochs= 100000000,
                               learning_rate= g['learning_rate'],
                               batch_size= g['batch_size'],
                               ckpt_path= g['ckpt_path'],
                               model_name= g['model_name']
                               )

        # train on trainset
        net.train(trainset)

    else:
        print('\nUsage')
        print(':: python3 train.py config_file.ini')
