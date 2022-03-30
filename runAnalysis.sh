grouping=5
total=20

for i in `seq 1 $((total / grouping))`
do
  node analyze $i
  sleep 1
done
