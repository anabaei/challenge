const solution = (password) => {
    // Write your code here
   if(password === null || password === undefined || password === ''){
    return 'weak'   
   }

    if(password.length < 8 || password.length > 22){
        return 'weak'
    }

    if( /[A-Z]/.test(password) &&
        /[a-z]/.test(password) && 
       /[0-9]/.test(password) 
      ){
        let prev = ''
        for(let char in password){
            if(prev.includes(char)){
                prev += char;
            }
            if(prev.length > 2){
                return 'weak'
            }
            prev = char
        }
        return 'strong'
      }
    return 'weak'
}



console.log(solution("mahnazaz3"))