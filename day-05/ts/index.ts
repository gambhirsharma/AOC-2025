// Part 2
const demo_file = "../data/demo.txt"
const data_file = "../data/data.txt"

const parseFile = async (file_name:string): Promise<Array<string>> => {
    const file = Bun.file(file_name)
    const text = await file.text()

    const [part1, part2]: string[] = text.split("\n\n")
    const array1 = part1.trim().split("\n")
    // const array2 = part2.trim().split("\n")

    return [...array1]
}



const mergeRanges = (ranges: [number, number][]): [number, number][] => {
    // Sort by start
    ranges.sort((a, b) => a[0] - b[0]);

    const merged: [number, number][] = [];

    for (const [start, end] of ranges) {
        if (merged.length === 0) {
            merged.push([start, end]);
        } else {
            const last = merged[merged.length - 1];
            if (start <= last[1] + 1) {
                // Merge overlapping or contiguous ranges
                last[1] = Math.max(last[1], end);
            } else {
                merged.push([start, end]);
            }
        }
    }

    return merged;
};

const computeFreshCount = (rangesStr: string[]): number => {
    const ranges: [number, number][] = rangesStr.map(line => {
        const [start, end] = line.split("-").map(Number);
        return [start, end];
    });

    const merged = mergeRanges(ranges);
    let count = 0;

        for (const [start, end] of merged) {
        count += end - start + 1; // number of IDs in the range
    }

    return count;
}


const process = async () => {
    const rangesStr = await parseFile(data_file);
    const freshCount = computeFreshCount(rangesStr);
    console.log(`Total fresh ingredient IDs: ${freshCount}`);
}


process()
