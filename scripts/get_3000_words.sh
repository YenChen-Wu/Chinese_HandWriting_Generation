#!/bin/bash -e
cd ../imgs
police=7
#font=WenQuanYi-Micro-Hei-Regular     # use convert
font=type${police}					  # use chinesetools php
dir=${font}_3000
rm -rf $dir && mkdir $dir && cd $dir

while read -n 1 word 
do
	if [ ! $word == "　" ];then
		echo $word
		#convert -font $font -pointsize 24 label:$word ${word}.png
		#wget http://www.chinesetools.eu/names/gen_boutons.php?text=${word}&amp;s=76&amp;police=${police}&amp;dispo=1   # disposition=1(horizontal), 2(vertical) WGET can't run
		curl "http://www.chinesetools.eu/names/gen_boutons.php?text=${word}&s=76&police=${police}&dispo=1" -o ${word}.png 2> /dev/null
	fi
done < ../../3000_words.list

