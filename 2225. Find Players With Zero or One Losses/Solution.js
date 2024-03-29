/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    let wins = {};
    let lose = {}
    matches.forEach(match =>{
        wins[match[0]] = (wins[match[0]]|0) + 1;
        lose[match[1]] = (lose[match[1]]|0) + 1;
    });
    let answer = [[],[]];
    for(let m in wins){
        if (!(m in lose)){
            answer[0].push(m)
        }
    }
    for(let m in lose){
        if (lose[m] == 1){
            answer[1].push(m)
        }
    }
    answer[0].sort((a,b)=>a-b);
    answer[1].sort((a,b)=>a-b);
    return answer;
};
