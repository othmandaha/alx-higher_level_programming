#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let size = list.length;
  while (size > 0) {
    newList.push(list[size - 1]);
    size--;
  }
  return newList;
};
