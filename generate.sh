for i in {1..8192}
do
    echo $RANDOM | md5sum | head -c 32 >> data/gen.txt;
done
echo >> data/gen.txt;
