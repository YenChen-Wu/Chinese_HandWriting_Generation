#!/bin/bash -ex
cd ../train_data
police=7
font=WenQuanYi-Micro-Hei-Regular     # use convert
#font=type${police}					  # use chinesetools php
dir=${font}_3000
rm -rf $dir && mkdir $dir && cd $dir

while read num word junk
do
	echo "$num $word"
	convert -font $font -pointsize 150 label:$word ${num}.png
	#curl "http://www.chinesetools.eu/names/gen_boutons.php?text=${word}&s=76&police=${police}&dispo=1" -o ${word}.png 2> /dev/null
done < ../../map

