use std::io::{self, Read};

struct Mapping {
    dest: u32,
    src: u32,
    length: u32,
}

fn part1(seeds: &Vec<u32>, maps: &Vec<Vec<Mapping>>) -> u32 {
    seeds
        .iter()
        .map(|&s| {
            maps.iter().fold(s, |s, block| {
                match block.iter().find(|&m| m.src <= s && s < m.src + m.length) {
                    Some(m) => s + m.dest - m.src,
                    None => s,
                }
            })
        })
        .min()
        .unwrap()
}

fn part2(seeds2: &Vec<&[u32]>, maps: &Vec<Vec<Mapping>>) -> u32 {
    for i in 0.. {
        // Invert mapping
        let seed: u32 = maps.iter().rev().fold(i, |x, block| {
            match block.iter().find(|&m| m.dest <= x && x < m.dest + m.length) {
                Some(m) => x + m.src - m.dest,
                None => x,
            }
        });

        if seeds2.iter().any(|&s| s[0] <= seed && seed < s[0] + s[1]) {
            return i; // seed is in a valid input range
        }
    }

    panic!()
}

fn main() {
    let mut inp = String::new();
    _ = io::stdin().read_to_string(&mut inp);

    let mut pcs = inp.split("\n\n");

    let seeds: Vec<u32> = pcs
        .next()
        .unwrap()
        .split('_')
        .next_back()
        .unwrap()
        .split(' ')
        .filter_map(|n| n.parse().ok())
        .collect(); // one line

    let maps: Vec<Vec<Mapping>> = pcs
        .map(|p| {
            p.split(':')
                .next_back()
                .unwrap()
                .trim()
                .split("\n")
                .map(|line| {
                    let nums: Vec<u32> = line.split(" ").filter_map(|n| n.parse().ok()).collect(); // one line
                    Mapping {
                        dest: nums[0],
                        src: nums[1],
                        length: nums[2],
                    }
                })
                .collect() // all lines
        })
        .collect(); // all blocks

    let seeds2 = seeds.chunks(2).collect();

    println!("{} {}", part1(&seeds, &maps), part2(&seeds2, &maps));
}
