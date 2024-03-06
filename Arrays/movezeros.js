// Example usage:
const inputArray = [0, 2, 3, 0, 0, 4, 5, 0, 6];

const moveZerosToCenter=(arr)=>{
   const zeroCount = arr.filter(item => item===0 ).length;
   const rightZeros = Math.floor(zeroCount/2)
   const leftZeros = zeroCount - rightZeros

   const result = []

   for(i=0; i< rightZeros; i++){
    result.push(0)
   }
   for(i=0; i< inputArray.length; i++){
    if(i!==0){
        result.push(i)
    }
   }
   for(i=0; i<leftZeros; i++){
    result.push(0)
   }
    return result;
}


// const resultArray = moveZerosToCenter(inputArray);
// console.log(resultArray); 

//Time complexity is 2n = O(n)
//space = O(n)


// Make space complexity one with two pointers
// one move from left, if it is none zero, then need to swap with 

function moveZerosToCenterMinSpace(inputArray){


    const countZeros = inputArray.filter( item=> item === 0).length

    const leftZeros = Math.floor(countZeros/2);
    const rightZeros = countZeros - leftZeros;
    let zerosadded = 0;

    for(let i=0; i < inputArray.length; i++){
        if(i < leftZeros){
            if(inputArray[i] === 0 ){
                zerosadded +=1;
            }
            else{
                let j = i;
                while(inputArray[j] !==0 && j < inputArray.length ){
                    j+=1;
                }
               
                if(inputArray[j] ===0){
                    while(j>i){
                       j-=1
                       inputArray[j+1] = inputArray[j];
                    }
                    inputArray[i] = 0
                }
            }
        }
        else if(inputArray[i] === 0 && i < inputArray.length - rightZeros ) {
                zerosadded +=1;
                j= inputArray.length -1;
                let temp;
                while(j>i){
                    if(inputArray[j] !== 0){
                        console.log(j)
                        temp = inputArray[j];
                        inputArray[j] = inputArray[i];
                        inputArray[i] = temp;
                    }
                    j -=1
                }

        }
        // else if(i > inputArray.length - rightZeros) {
            
        // }
    }

    console.log(zerosadded)
    return inputArray


}

const resultArray = moveZerosToCenterMinSpace(inputArray);
console.log(resultArray); 