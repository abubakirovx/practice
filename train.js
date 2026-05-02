 // TASK A

// function countNumber (word){
//     let countedNumber=0
//     for(let i=0;i < word.length;i++){
       
//         if (!isNaN(word[i])){
            
//             countedNumber++
//         }
//     }
//     console.log(`Berilgan tekst ichida ${countedNumber} ta son bor`);
    
// }
// const randomString ="s4ds63ererdf542gfg73=-5h"
// countNumber(randomString)


// const animals =['deer','dog','cat','cow','goose','goat','rabbit','chicken','donkey',"mouse","ayiq",'rat']




// CHALLANGE

// function findAnimal (txt){
//     let count = 0
//     let foundAnimal=[]
//     for(let i=0; i < animals.length; i++){

//         for(let z=0; z < animals[i].length; z++){


//               for(let q=0; q < txt.length; q++){

//                  if(txt.length >= animals[i].length){

//                      if(txt[q]===animals[i][z]){
//                         count++
                   
//                         if(count===animals[i].length){
                           
                           
//                           foundAnimal.push(animals[i])
//                           count=0
//                         }
//                     }
                    
//                  }
                 
//                 }
                
//             }
//             count=0
//     }
//     return foundAnimal;
    
// }

// const javob = findAnimal("aotcdg")
// console.log("JAVOB=>",javob);



// TASK B

// function countString(word1,word2){
//     const word_1=word1.split("").sort().join('')
//     const word_2=word2.split("").sort().join('')
    
//     if(word_1===word_2) console.log("Matn bir xil");
    
//     else console.log("Matn bir xil emas");
    
// }

// countString("salom","maloq")



/*TASK D

function getMaxIndex (arr){
    let max = -Infinity
    let indexMax =0
    for(let i = 0;i<arr.length;i++){
        if(arr[i]>max){
            max = arr[i]
            indexMax=i       
        }
        
    }
    return indexMax
}

const result = getMaxIndex([23,45,21,3,51,9,23])
console.log(result);


function getMaxIndex1 (arr){
    let max = -Infinity
    let indexMax =0
    for(let num of arr){
        if(num>max){
            max = num
            
            indexMax=arr.indexOf(max)

        }
        
    }
    return indexMax
}

const result1 = getMaxIndex1([23,45,21,3,5,9,23])
console.log(result1);
*/


/*E-TASK (NodeJS)

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"*/

// function getReverse(string){
//        let result= string.split("").reverse().join("")
//        return result
// }

// const result =getReverse("hello")
// console.log(result);


/*F-TASK (NodeJS)

Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi*/

// function getDuplicate (text){
//     arr=text.split("").sort()
  
    
//     for(let i=0;i<arr.length;i++){
       
        
//         if(arr[i]==arr[i+1]){
//             return true
//         }
        
       
//     }
//     return false
// }

// const result=getDuplicate("aabcd")
// console.log(result);



/*H-TASK (NodeJS)

shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"
*/

function getPositive(arr){
    let stringArr=''
    for (let i=0;i<arr.length;i++) {
       if(arr[i]>0){
          stringArr+=String(arr[i])
       }
    }
    return stringArr
}

const stringArr = getPositive([1,2,3,-4,-5,6])
console.log(typeof(stringArr),"=>",stringArr);
