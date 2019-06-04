'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the diagonalDifference function below.
function diagonalDifference(arr) {
    var n = arr.length;
    var i = 0, leftVal = 0, rightVal = 0, leftPointer = 0, rightPointer = n - 1;
    while(i < n){
        // check if length is odd or not, find the midpoint if its odd
        if(n%2 != 0 && leftPointer === rightPointer){
            var midIndex = Math.floor(n%2);
            rightVal += arr[midIndex][midIndex];
            leftVal += arr[midIndex][midIndex];
            leftPointer++, rightPointer--;
        }
        else{
            leftVal += arr[i][leftPointer];
            rightVal += arr[i][rightPointer];
            leftPointer++;
            rightPointer--;
        }
        i++;
    }
    return Math.abs(leftVal - rightVal);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let arr = Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = diagonalDifference(arr);

    ws.write(result + '\n');

    ws.end();
}

