const arr = [1, 2, 3, 4, 5];

arr.forEach(console.log);

var binary = 0b01000001;

console.log(binary);
console.log(1 === 1.0);

const a = parseInt("a");
console.log(a);

const foo = true;
console.log(foo);
//#6.5 c에서는 선언과 정의가 메모리 주소를 할당하는 가로 구분한다. 선언 - 컴파일러에게 식별자의 존재만 알리는 것  / 정의 - 실제로 컴파일러가 변수를 생성해서 식별자와 메모리 주소가 연결되는 것
// 자바스크립트의 경우 변수를 선언하면 암묵적으로 정의가 이뤄진다. 그래서 모호함.
// 여기서 자바스크립스 변수는 선언한다고 하고 함수는 정의한다고 표현함.

// ## javascript => null로 써야함.
const far = "Lee";
console.log(far);
const far2 = null;

var far3 = "Lee";
console.log(far3);
far3 = null;
console.log(far3);

var num = 0b01100100;
console.log(num);

//자바스크립트는 모든 것이 다 객체임.
//변수 이름은 첫 아이 이름 짓듯이 심사숙고해서 지어야 한다.

// 자바스크립트는 암묵적 type변환을 해서 5 == '5'를 같다고 본다.

const num2 = 2 ** 2;
console.log(num2);
// -5 **2 xxx
// (-5) ** 2 ooo

outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i + j === 3) break outer;
    console.log(`inner [${i}, ${j}]`);
  }
} //레이블 식별자는 이중 중첩문을 탈출할 때 유리하다.

console.log("Done!");

if ("") console.log("1"); //--> / "" -> false
if (true) console.log("2");
if (0) console.log("3");
if ("str") console.log("4");
if (null) console.log("5");

if (!"") console.log("" + "is falsy value");
if (!0) console.log("" + "is falsy value");
if (!NaN) console.log("" + "is falsy value");
if (!false) console.log("" + "is falsy value");
if (!undefined) console.log("" + "is falsy value");

// 9.2까지 읽음

var person = {
  name: "Lee",
  sayHello: function () {
    console.log(`Hello! My name is ${this.name}.`);
  },
};

console.log(typeof person);
console.log(person);
