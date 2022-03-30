#!/bin/bash
# Generate a private key and public key pair

# Number of key pairs (default 10)
NUM=${1:-10000}

# Key size (default 4096)
SIZE=${2:-4096}

# Key pair destination
DEST=${3:-`pwd`}

for i in `seq 1 $NUM`
do
	NAME=rsa-$SIZE-$i

	# Public/Private key files
	PRIK=$DEST/$NAME.pem
	PUBK=$DEST/$NAME.pub

	# If either exists, avoid overwrite
	if [ -f "$PRIK" ] || [ -f "$PUBK" ]; then
		echo "A key by that name already exists"
		exit 0
	fi

	openssl genrsa -out "$PRIK" $SIZE &&
	openssl rsa -in "$PRIK" -out "$PUBK" -pubout
	echo $NAME
done

exit

# You'll have to repeat the password when encrypting the key and again
# to output the public key. DO NOT FORGET THE PASSWORD

# Call this file with : sh genkeys.sh

# For number of key pairs
# sh genkeys.sh num

# For 3248 bit keys:
# sh genkeys.sh num 3248

# For a keypair saved to /tmp
# sh genkeys.sh num 4096 /tmp
