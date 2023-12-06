use std::{
    io::{self, Read},
    iter::zip,
};

fn part1(time: &Vec<u64>, distance: &Vec<u64>) -> u64 {
    zip(time, distance).map(|(&t, &d)| part2(t, d)).product()
}

fn part2(t: u64, d: u64) -> u64 {
    (0..=t).filter(|&i| i * (t - i) > d).count() as u64
}

fn main() {
    let mut inp = String::new();
    _ = io::stdin().read_to_string(&mut inp);

    let inpl: Vec<Vec<u64>> = inp
        .lines()
        .map(|line| {
            line.split_whitespace()
                .skip(1)
                .filter_map(|n| n.parse::<u64>().ok())
                .collect()
        })
        .collect();

    let inpl2: Vec<u64> = inp
        .lines()
        .filter_map(|line| {
            line.split(':')
                .next_back()?
                .split_whitespace()
                .collect::<String>()
                .parse()
                .ok()
        })
        .collect();

    println!(
        "{} {}",
        part1(&inpl[0], &inpl[1]),
        part2(inpl2[0], inpl2[1])
    );
}
