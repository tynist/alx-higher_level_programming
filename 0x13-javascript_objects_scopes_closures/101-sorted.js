#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (nbr, i) {
  return nbr * i;
});

console.log(list);
console.log(newList);
