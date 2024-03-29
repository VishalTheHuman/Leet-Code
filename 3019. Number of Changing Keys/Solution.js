/**
 * @param {string} s
 * @return {number}
 */
var countKeyChanges = function(s) {
    s = s.toLowerCase();
    let curr_key = s[0];
    let count = 0;
    for(let i = 1;i<s.length; i++){
        if (curr_key!=s[i]){
            count++;
        }
        curr_key = s[i];
    }
    return count;
};
