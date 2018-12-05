/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
    // var i = 0, j = s.length - 1;
    // while(i < j){
    //     var head = s[i];
    //     var tail = s[j];
    //     s.replaceAt(i, tail);
    //     s.replaceAt(j, head);
    //     i++;
    //     j--;
    // }
    var res = s.split("").reverse().join("");
    return res;
};