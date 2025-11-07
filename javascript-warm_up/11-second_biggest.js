#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

const argumentsList = process.argv;

if (argumentsList.length < 4) {
  console.log('0');
} else {
  let maxNumber = parseInt(argumentsList[2]);
  let secondMaxNumber = maxNumber;
  let count = 0;
  for (let i = 0; i < argumentsList.length; i++) {
    argumentsList[i] = parseInt(argumentsList[i]);
    if (argumentsList[i] > maxNumber) {
      secondMaxNumber = maxNumber;
      maxNumber = argumentsList[i];
      count++;
    }
  }
  if (count === 0) {
    secondMaxNumber = process.argv[3];
    for (let i = 3; i < argumentsList.length; i++) {
      argumentsList[i] = parseInt(argumentsList[i]);
      if (argumentsList[i] > secondMaxNumber) {
        secondMaxNumber = argumentsList[i];
      }
    }
  }
  console.log(secondMaxNumber);
}
