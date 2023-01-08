//SURAJ DHAKAL
//October 4, 2022


//Question 1 hardcoded array called inputtable 

var inputtable = [1,2,3,4,5,6,7,8,9,10];
//to output the array to the console 
console.log ("1) Inputtable:", inputtable)
console.log("\n")

//Question 2 
//a)
//takes each element defined in  inputtable 
//multiplies the values by 5 and adds the result to tbl
 var fiveTable = () => {
    var tbl = []
    inputtable.map((value) => {
      tbl.push(value * 5)

    })
    return tbl
 }
 //prints all the elements 
 console.log ("2.a) Set of Multiples of 5 between 1 nad 51 is : ", fiveTable())
 //new line
 console.log("\n")

 //b)
 //takes each element defined in inputtable 
 //multiplies the values by 13 and adds the result to tbl
 var thirteenTable = () => {
    var tbl = []
    inputtable.map((value) => {
      tbl.push(value * 13)
  })
  return tbl
 }
 //prints the result 
 console.log ("2.b) Set of Multiples of 13 between 1 and 131 is : ", thirteenTable())
 //new line
 console.log("\n")

 //c)
 //uses each element defined in inputtable and multiplies with the same value to get 
 //the sqaures of the numbers and adds it to the new table 
 var squaresTable = () => {
    var tbl = []
    inputtable.map((value) =>{
      tbl.push( value * value)
  })
  return tbl
 }
 //prints the result 
 console.log("2.c) set of squares of the numbers in inputtable : ", squaresTable())
 //prints a newline 
 console.log("\n")


//Question 3 

var oddMultiplesOfFive = () =>{
  //we use the fiveTable from 2.a
  var tbl = fiveTable()
  //to get the last element form tbl
  var lastElement = tbl [tbl.length-1]
  //takes the last element and adds it to the value in tbl and stores the new value 
  fiveTable().map((value) => tbl.push(lastElement + value))
  // checks whether the value is odd 
  return tbl.filter((value)=> value % 2 !=0)
}
//prints the result 
console.log("3) The odd multiples of 5 between 1 nad 100 are:", oddMultiplesOfFive())
//new line
console.log("\n")

//Question 4 
//takes each element in inputtable 
//multiplies the value by 7 and returns the new value in tbl 
var sumEvenMultiplesOfSeven = () =>{
  var tbl = []
  inputtable.map((value) => {
    tbl.push(value * 7 )
  })
  var lastElement = tbl [tbl.length-1]
  // to get other multiples of 7
  tbl.map((value)=> {
    tbl.push( lastElement + value)
  })
  // filter the values to be less than or equal to 100
  tbl = tbl.filter((value)=> value <= 100)
  //check for even multiples of 7
  tbl = tbl.filter((value) => value %2 == 0)
  var sum =0
  // get the sum
  tbl.map((value) => sum = sum + value)
  //return total
  return sum
}
//print the result 
console.log ("4) The sum of even multiples of 7 between 1 and 100 is: ", sumEvenMultiplesOfSeven())
//new line
console.log("\n")

//Questin 5 
//Given Function
//function cylinder_volume(r, h){ 
// var volume = 3.14 * r * r * h; 
// return volume; 
// } 
//since curried function only takes one parameter at a time 
// we are simplifying the volume formula given to be rewritten such that it only takes a single parameter at a time 
var cylinder_volume = () => {
  var num = 3.14
  return (r) => {
    num *= r * r
    return (h) =>{
      num *= h
      return num
    }
  }
}
console.log("5.a) When r =5 and h =10 the volume is :", cylinder_volume()(5)(10))
console.log("\n")
console.log("5.b) when r = 5 and h = 17 the volume is:", cylinder_volume()(5)(17))
console.log("\n")
console.log("5.c) when r = 5 and h = 11 the volume is:", cylinder_volume()(5)(11))
console.log("\n")

// Question 6 
// <table> defines a table and </table> end of the table 
// <th> defines a header cell in table and </th> endtag for that header
// <tr> defines a row in table and </th> endtag for that row
// <td> defines a cell in a table and </td> endtag for that cell in table
// \n is for new line
// write function writes the HTML expression to a document  

makeTag = function(beginTag, endTag){ 
  return function(textcontent){ 
     return beginTag +textcontent +endTag; 
  } 
} 
var buildTableUsingTags = () =>
  makeTag("<table>\n", "</table>\n")(
    makeTag("<tr>\n", "</tr>\n")(makeTag("<th>", "</th>\n")("Course Name") + 
    makeTag("<th>", "</th>\n")("Course Number") +
    makeTag("<th>", "</th>\n")("Professor")) +
    
    makeTag("<tr>\n", "</tr>\n")(makeTag("<td>", "</td>\n")("Programming Languages") +
    makeTag("<td>", "</td>\n")("CSE-3302-001") +
    makeTag("<td>", "</td>\n")("Kelly French")) +

    makeTag("<tr>\n", "</tr>\n")(makeTag("<td>", "</td>\n")("Operating Systems")+
    makeTag("<td>", "</td>\n")("CSE-3320-002") +
    makeTag("<td>", "</td>\n")("Trevor Bakker"))
  )

  document.write(buildTableUsingTags())
  console.log(buildTableUsingTags())
  console.log("\n")

//Question 8 
//Extra Credit 

var is
var generic = () => {
  var tbl = []

  var lastElement = tbl [tbl.length-1]
  tbl.map((value)=> {
    tbl.push( lastElement + value)
  })
  // filter the values to be less than or equal to 100
  tbl = tbl.filter((value)=> value <= 100)
  
  if(value % 2 != 0)
  {
    return tbl.map((value,index))
  }
  if(value % 2 ==0)
  {
    var sum = 0
    tbl = tbl.map((value) => sum = sum +value )
    return sum
  }
} 
console.log( generic())
