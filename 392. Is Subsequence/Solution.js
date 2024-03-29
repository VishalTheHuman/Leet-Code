/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let s_ind = 0;
    let t_ind = 0;
    while (t_ind < t.length && s_ind < s.length){
        if (t[t_ind] == s[s_ind]){
            s_ind++;
        }
        t_ind++;
    }
    return s.length == s_ind
};
