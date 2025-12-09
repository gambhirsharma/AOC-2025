const demo_file = "../data/demo.txt"
const data_file = "../data/data.txt"

const parseFile = async (file_name:string): Promise<Array<string[]>> => {
    const file = Bun.file(file_name)
    const text = await file.text()

    const [part1, part2]: string[] = text.split("\n\n")
    const array1 = part1.trim().split("\n")
    const array2 = part2.trim().split("\n")

    return [array1, array2]
}

const processData = await parseFile(data_file)

// ERROR: out of memmory  
// const get_number_range = (data: string[]): number[] => {
//     const numberSet = new Set<number>()
//
//     data.forEach(line => {
//     const [start, end] = line.split('-').map(Number)
//         for (let i = start; i <= end; i++) {
//             numberSet.add(i)
//         }
//     })
//
//     return Array.from(numberSet)
// }


const compute = (processData: Array<string[]>)  => {
    const final_result: number[] = []

    const first_part = processData[0]
    const second_part = processData[1].map(str => Number(str))

    // const valid_number = get_number_range(first_part)
    // for (const num of second_part){
    //     if (valid_number.includes(num)){
    //         final_result.push(Number(num))
    //     }
    // }
    //

     for (const num of second_part) {
        for (const range of first_part) {
            const [start, end] = range.split('-').map(Number);
            if (num >= start && num <= end) {
                final_result.push(num);
                break; // Stop checking ranges once a match is found
            }
        }
    }

    return final_result
}

const final_result = compute(processData)
const length_final_result = final_result.length

console.log(`Length finaly result: ${length_final_result}`)

// console.log(`Finaly result: ${JSON.stringify(final_result)}`)
