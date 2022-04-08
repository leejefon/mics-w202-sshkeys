const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

function classify(start, grouping) {
  const keyPrefix = 'rsa-4096-';
  const pubkeys = [];

  for (let i = 0; i < grouping; i++) {
    const keyfile = `keys/${keyPrefix}${start + i}.pub`;
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
const startGroup = parseInt(process.argv[2]) || 1;
const runGroupCount = parseInt(process.argv[3]) || 1;

let start = (startGroup - 1) * grouping + 1
for (; start < (startGroup * grouping * runGroupCount); start += grouping) {
  pClassifies.push(classify(start, grouping));
}

Promise
  .all(pClassifies)
  .then((result) => {
    console.log(JSON.stringify(result.map((r) => r.data), null, 2));
  });
