// var A = parseInt().prompt();
// var B = parseInt().prompt();

// if (A > B) {
//   console.log(">");
// } else if (A < B) {
//   console.log("<");
// } else {
//   console.log("==");
// }

//https://velog.io/@zaman17/node.js-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%BD%98%EC%86%94%EB%A1%9C-%EA%B0%92-%EC%9E%85%EB%A0%A5%EB%B0%9B%EA%B8%B0
let input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

const a = Number(input[0]);
const b = Number(input[1]);

if (a > b) {
  console.log(">");
} else if (a < b) {
  console.log("<");
} else {
  console.log("==");
}
