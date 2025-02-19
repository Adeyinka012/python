function palindrome(str){
    var input = str.replace(/[^A-Z0-9]/ig, "").toLowercase()
    var reverse= input.split('').reverse().join('')
    if(input == reverse){
        console.log("The word is palindrome")

    }
    else{
        console.log("The word is not palindrome");

    }
}
palindrome("school")