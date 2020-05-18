# page_spider
simple web page spider


```bash
$ python3 page_spider.py -h
usage: page_spider.py [-h] -db DATABASE -i INPUT [-n TOP_N]

optional arguments:
  -h, --help            show this help message and exit
  -db DATABASE, --database DATABASE
                        SQLite File Name
  -i INPUT, --input INPUT
                        File containing urls to read
  -n TOP_N, --top_n TOP_N
                        List Top N word usage Max 15, Min 1
```

Who its work just run it like below example: 

```
$ python3 page_spider.py -i input.txt -db words.db -n 4
[!]  Database working with: words.db
[!]  URL file to Scan: input.txt
[!]  Reading https://en.wikipedia.org/wiki/HTTP/3
[!]  Database save completed!
	[*] the         736
	[*] to          544
	[*] of          416
	[*] retrieved   416
```
