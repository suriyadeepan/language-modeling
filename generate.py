import data
import utils
import char_rnn

import sys

if __name__ == '__main__':
    if len(sys.argv) > 3:
        # get configuration
        g = utils.get_config(sys.argv[1])
        # fetch metadata dictionaries
        X, Y, idx2ch, ch2idx = data.load_data(path=g['data_path'])

        # build the model
        num_classes = len(idx2ch)
        net = char_rnn.CharRNN(seqlen= 1,
                               num_classes= num_classes,
                               num_layers= g['num_layers'],
                               state_size= g['state_size'],
                               epochs= 0,
                               learning_rate= 0.1,
                               batch_size= 1, 
                               ckpt_path= g['ckpt_path'],
                               model_name= g['model_name']
                               )

        char_indices = net.generate_characters(
                num_chars= int(sys.argv[3]), init_char_idx= ch2idx[sys.argv[2]])
        msg = ''.join([ idx2ch[chidx] for chidx in char_indices ])
        print(msg)

    else:
        print('\n>> Usage')
        print(':: python3 generate.py config_file.ini <s> <n>')
        print('\t<s> : starting character')
        print('\t<n> : number of characters to generate')
        print('>> example')
        print(':: python3 generate.py tf_src_code.ini d 1000')
