#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nbOccurences += 1;
    }
  }
  return nbOccurences;
};
