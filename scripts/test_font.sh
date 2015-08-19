#!/bin/bash
cd ../imgs
dir=font
rm -rf $dir && mkdir $dir && cd $dir

convert -list font | grep Font | cut -d' ' -f4 > tmp

while read font
do
	echo $font
	convert -font ${font} -pointsize 24 label:"陳乃群 王國婷 吳彥諶 楊明仁" ${font}.png
done < tmp
rm tmp
