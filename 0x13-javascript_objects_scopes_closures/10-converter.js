#!/usr/bin/node

exports.converter = function (base) {
  return (num) => {
    let result = '';
    while (num > 0) {
      const remainder = num % base;
      result =
        (remainder < 10
          ? remainder
          : String.fromCharCode(97 + remainder - 10)) + result;
      num = Math.floor(num / base);
    }
    return result;
  };
};
