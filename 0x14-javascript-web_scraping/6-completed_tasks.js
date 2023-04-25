#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const completedTasks = {};
  for (const task of data) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  for (const userId in completedTasks) {
    console.log(`User ${userId}: ${completedTasks[userId]}`);
  }
});
