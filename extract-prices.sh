#!/bin/bash
PATH=/home/goldameir/Garbage:/home/goldameir/anaconda3/bin:/home/goldameir/bin:/home/goldameir/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
{
  wget -O ethereum_price.txt https://ethereumprice.org/
  string1=$(grep '<span id="ep-price' ethereum_price.txt)
  #string1=$(grep "<meta property='og:title' content='ETH/USD" ethereum_price.txt)
  prefix1='<span class="metrics__primary__value"><span class="quote-symbol">$</span><span id="ep-price">'
  foo1=${string1#$prefix1}
  foo1="${foo1%%<*}"
  wget -O litecoin_price.txt https://www.coingecko.com/en/price_charts/litecoin/usd
  string2=$(grep "for today is" litecoin_price.txt)
  prefix2="<b>Litecoin price</b> for today is <b><span>"
  foo2=${string2#$prefix2}
  foo2="${foo2%%<*}"
  #foo2=${foo2::-6}
  wget -O bitcoin_price.txt https://www.coincadence.com/bitcoin-index/
  string3=$(grep ajax0 bitcoin_price.txt)
  foo3="${string3:49:${#string3}-1}"
  foo3="${foo3%%<*}"
  wget -O iota_price.txt https://www.coingecko.com/en/price_charts/iota/usd
  string4=$(grep "for today is" iota_price.txt)
  prefix4="<b>IOTA price</b> for today is <b><span>"
  foo4=${string4#$prefix4}
  foo4="${foo4%%<*}"
} &> /dev/null

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

printf "${GREEN}Current Price of Ethereum${NC} : \$${foo1}\n${GREEN}Current Price of Litecoin${NC} : ${foo2}\n${GREEN}Current Price of Bitcoin${NC}  : ${foo3}\n${GREEN}Current Price of IOTA${NC}     : ${foo4}\n"
rm -r ethereum_price.txt
rm -r litecoin_price.txt
rm -r bitcoin_price.txt
rm -r iota_price.txt
