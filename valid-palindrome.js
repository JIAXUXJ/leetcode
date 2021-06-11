/**
 * @param {string} s
 * @return {boolean}
 */
 var isPalindrome = function(s) {

  let left = 0;
  let right = 0;
  let i;
  const regx = /[A-Z]|[a-z]|[0-9]/g;
  let extractStr = s.match(regx);
  if(!extractStr){
    return true;
  }
  extractStr = extractStr.toString().toLowerCase();

  for(i = 0; i < extractStr.length; i++) {
    if(extractStr[i] !== extractStr[extractStr.length - 1 - i]){
      return false;
    }
  }
  return true;
};