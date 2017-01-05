import sms_data as data
import char_rnn

if __name__ == '__main__':
    # fetch metadata dictionaries
    X, Y, idx2ch, ch2idx = data.load_data()

    # build the model
    num_classes = len(idx2ch)
    net = char_rnn.CharRNN(seqlen= 1,
                           num_classes= num_classes,
                           num_layers= 2,
                           state_size= 128,
                           epochs= 0,
                           learning_rate= 0.1,
                           batch_size= 1, 
                           ckpt_path= 'ckpt/',
                           model_name= 'sms_lm')

    # generate 100 characters for each char in our vocabulary
    #  and let's write it to a file!
    with open('data/sms_results.txt', 'w') as f:
        for ch in idx2ch:
            char_indices = net.generate_characters(
                    num_chars= 100, init_char_idx= ch2idx[ch])
            msg = ''.join([ idx2ch[chidx] for chidx in char_indices ])
            print('________________________________________________')
            print(msg)
            f.write('\n' + msg + '\n')

