for i in {1..32768}
do
    echo $RANDOM | md5sum | head -c 32 >> gen.txt;
done
echo >> gen.txt;
