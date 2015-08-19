# downloads php
cd ../imgs
dir=3000_words
rm -rf $dir && mkdir $dir && cd $dir

if [ ! -f appendix_1.php ];then  wget http://lcprichi.hkbu.edu.hk/search/appendix_1.php;fi

# list url
cat appendix_1.php | grep materials/word | cut -d. -f3 | awk '{ print "http://lcprichi.hkbu.edu.hk" $1}' > tmp

# save gif
#if [ ! -d $dir ];then mkdir $dir;fi

while read line
do
	wget $line # wait too long ??
done < tmp
rm tmp
