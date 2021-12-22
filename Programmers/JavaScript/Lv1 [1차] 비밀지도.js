function solution(n, arr1, arr2) {
    function decToBin(num) {
        const binNum = num.toString(2);
        return '0'.repeat(n - binNum.length) + binNum;
    }
    
    const binArr1 = arr1.map(val => decToBin(val));
    const binArr2 = arr2.map(val => decToBin(val));
    
    const ansArr = [];
    for (let i = 0; i < n; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            if (binArr1[i][j] === '0' && binArr2[i][j] === '0') {
                row.push(' ');
            } else {
                row.push('#');
            }
        }
        ansArr.push(row.join(''))
    }
    
    return ansArr
}