#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) console.log(error);
  const jsonData = JSON.parse(body);

  let prevId = null;
  let currId = null;
  let count = 0;
  const taskObj = {};

  jsonData.forEach(el => {
    if (el.userId !== prevId && prevId !== null) {
      taskObj[`${prevId}`] = count;
    }
    if (el.completed === true) {
      currId = el.userId;
      if (currId === prevId) count++;
      else count = 1;
    }
    prevId = currId;
  });
  taskObj[`${currId}`] = count;
  console.log(taskObj);
});
