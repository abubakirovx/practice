
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


function countString(word1,word2){
    const word_1=word1.split("").sort().join('')
    const word_2=word2.split("").sort().join('')
    
    if(word_1===word_2) console.log("Matn bir xil");
    
    else console.log("Matn bir xil emas");
    
}

countString("salom","maloq")