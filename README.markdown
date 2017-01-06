# Language Modeling in Tensorflow

Language Modeling with Dynamic Recurrent Neural Networks, in Tensorflow.


## Training


You can train the model on any data. Just make sure to put the text in a single file and run *train.py* with the file name.

*Sample configuration file*

```ini
[str]
data_path= data/tensorflow/
ckpt_path= ckpt/tensorflow/ 
model_name= tf_lm
data_file= data/tensorflow/tensorflow.txt
[int]
batch_size= 128
num_layers= 2
state_size= 128
[float]
learning_rate= 0.1
```

*train*

```bash
python3 train.py tf_src_code.ini
```

*generate text*

```bash
python3 generate.py tf_src_code.ini d 1000
# start with initial character 'd'
#  generate 1000 characters
```


## SMS data

I gathered the spam messages in my phone's inbox, accumulated over the past 2 years (roughly 2000 messages). Used a 2 layered stacked-LSTM RNN to model it. Generates non-sensical [text](https://gist.github.com/suriyadeepan/d8c59e22b177d13d4141051546cde0d7), which resembles the spam messages.

> [WAP Push] Download App starting from Bangalont koud spepout 899 & 17-1GB D
> Open bit.ly/fontkm.bovk Stapers Prady-100 SMonil Jontal Talk trestroup on !7 6/2 & bear starting so
> Bangy offer OFFV send mang rides. Seb110 ya Details OFFER  Anjonations? Talk Meleare tilp 1051
> FREE Listen & Select) paytmathi Special ABuree Dial Maghone T&C-Jour phase . Men:tipes!    Entreats, 
> http://wap.D20113. on 1503.BSNL TN VAS
> //122.176.201620Bug,220dy today 20MB DHAYS .Use VEERIWN

## Project Madurai

Electronic versions of printed texts (abbreviated as Etexts) of [ancient tamil literary works](http://www.projectmadurai.org/) are important pedagoic and scholarly resources. 

Scraped 4.1 GB worth of text from Project Madurai. The script for scraping is available [here](data/madurai/scrape.py).
