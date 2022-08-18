#!/bin/bash
url="https://etherscan.io/nft/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/"
for i in `seq 0 9999`;
do
html_url=${url}${i}
wget -U 'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0' --output-document=${i}.html ${html_url}
sleep .6
done
