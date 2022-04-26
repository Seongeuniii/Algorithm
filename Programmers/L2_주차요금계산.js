function calTime(a, b) {
    const A = a.split(':').map(x => parseInt(x))
    const B = b.split(':').map(x => parseInt(x))
    return (B[0]*60 + B[1]) - (A[0]*60 + A[1])
}

function solution(fees, records) {
    let answer = []
    let inTime = {}
    let totalTime = {}

    records.forEach( record => {
        let [a, b, c] = record.split(' ')

        if (c == 'IN') {
            inTime[b] = a
        } else {
            const result = calTime(inTime[b], a)
            if (b in totalTime) {totalTime[b] += result} 
            else {totalTime[b] = result}
            inTime[b] = 0
        }
    })

    Object
        .entries(inTime)
        .sort((a, b) => parseInt(b[0]) - parseInt(a[0]))
        .forEach(([key, value]) => {
            if (value != 0) {
                const result = calTime(inTime[key], '23:59')
                if (key in totalTime) { totalTime[key] += result } 
                else { totalTime[key] = result }
            }
            let money = 0
            if (totalTime[key] <= fees[0]) { money = fees[1]} 
            else { money = fees[1] + Math.ceil((totalTime[key] - fees[0]) / fees[2]) * fees[3] }
            answer.push(money)
        })
        
    return answer
}