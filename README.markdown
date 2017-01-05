# Language Modeling in Tensorflow

Language Modeling with Dynamic Recurrent Neural Networks, in Tensorflow.


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
