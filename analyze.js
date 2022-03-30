const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

function classify(start, grouping) {
  const keyPrefix = 'rsa-4096-';
  const pubkeys = [];

  for (let i = 0; i < grouping; i++) {
    const keyfile = `${keyPrefix}${start + i}.pub`;
    pubkeys.push(fs.readFileSync(keyfile, 'utf-8'));
  }

  const body = new FormData();
  body.append('type_flag', 'sw');
  body.append('keys', pubkeys.join('\n'));

  return axios({
    url: 'https://rsa.sekan.eu/api/classify',
    method: 'POST',
    data: body,
    headers: body.getHeaders()
  });
}

const pClassifies = [];
const grouping = 5;
const runGroupCount = 1;
const startGroup = process.argv[2] || 1;

for (let i = 1; i < (startGroup * grouping * runGroupCount); i += grouping) {
  pClassifies.push(classify(i, grouping));
}

Promise
  .all(pClassifies)
  .then((result) => {
    console.log(JSON.stringify(result.map((r) => r.data), null, 2));
  });
