/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let array = new Array();
    let i = 0;
    for(i=0;i<arr.length;i+=size){
        array.push(arr.slice(i,i+size));
    }
    if(i-arr.length>size){
        array.push(arr.slice(arr.length-(i-arr.length),arr.length))
    }
    return array
    };
