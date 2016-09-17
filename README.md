# tamsen
センサーデバイスからの値を簡単にグラフ化できる https://ambidata.io/ 向けのライブラリです。

# 使い方

~~~
import tamsen

channelID = xxx
writeKey = "xxxxxxxxx"


tamsen.sendData(channelID,writeKey,d1　= 1,d2 = 43 ...d8)
~~~

# インストール方法
~~~
# pip install git+https://github.com/gorakuru/tamsen.git
~~~
