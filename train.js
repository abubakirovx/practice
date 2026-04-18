
function countNumber (word){
    let countedNumber=0
    for(let i=0;i < word.length;i++){
       
        if (!isNaN(word[i])){
            
            countedNumber++
        }
    }
    console.log(`Berilgan tekst ichida ${countedNumber} ta son bor`);
    
}
const randomString ="s4ds63ererdf542gfg73=-5h"
countNumber(randomString)





