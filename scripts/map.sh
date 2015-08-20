n=1
while read -n1 word
do
	if [  "$word" == "　" ]; then continue;fi
	if [[ "$word" == "" ]]; then continue;fi
    echo "$n $word"
	n=$((n+1))
done < ../3000_words.list
