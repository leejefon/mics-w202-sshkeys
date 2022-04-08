total=10000
grouping=5

for i in `seq 7 $(($total / $grouping))`
do
  echo $i
  node analyze $i > results/$i.json
  sleep 0.3
done
