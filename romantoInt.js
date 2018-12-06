/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    symbolDict = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
    var len = s.length;
    var last = '';
    var res = 0;
    for(var i = len - 1; i >= 0; i--){
        var cur = s.charAt(i);
        if(symbolDict[cur] < last){
           res = res - symbolDict[cur]; 
        } 
        else{
           res += symbolDict[cur]; 
        } 
        last = symbolDict[cur];
    }
    return res;
};