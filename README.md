# tamsen
センサーデバイスからの値を簡単にグラフ化できる https://ambidata.io/ 向けのライブラリです。
使用するためには https://ambidata.io/ でのユーザー登録が必要です。

非公式です。

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

# サンプル
Raspberry PiのCPUの温度を送信

~~~
import tamsen
import sys

channelID = xxx
writeKey = "xxxxxxxxxx"

fn = open('/sys/class/thermal/thermal_zone0/temp', 'r')
for line in fn:
  CPU_TEMP = int(line) / float(1000)

print(tamsen.sendData(channelID,writeKey,d1 = CPU_TEMP))
~~~
