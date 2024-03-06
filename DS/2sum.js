// # arr = [5,3,1,9]
// # sum = 6
// # twoSum(arr, sum)

function twoSum(arr, sum){
  const hashTable = new Set()
  for(let i in arr){
    if(hashTable.has(sum-arr[i])){
        return {a: sum-arr[i],b: arr[i]}
    }
    hashTable.add(arr[i])
  }
}


const arr = [5,3,1,9]
const sum = 6
console.log(twoSum(arr, sum))