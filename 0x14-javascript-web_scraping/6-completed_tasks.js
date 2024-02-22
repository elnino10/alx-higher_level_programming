#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');

const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) console.log(error);
  const jsonData = JSON.parse(body);
  const tasksObj = {};
  jsonData.forEach((el) => {
    if (el.completed) {
      if (!tasksObj[el.userId]) {
        tasksObj[el.userId] = 1;
      } else {
        tasksObj[el.userId] += 1;
      }
    }
  });
  console.log(tasksObj);
});
