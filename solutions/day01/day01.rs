use std::{
    collections::HashMap,
    io::{self, Read},
};

fn part1(inp: &String) -> u32 {
    inp.lines()
        .map(|line| {
            let digits = line
                .chars()
                .filter_map(|c| c.to_digit(10))
                .collect::<Vec<u32>>();
            digits.first().unwrap() * 10 + digits.last().unwrap()
        })
        .sum()
}

fn part2(inp: &String) -> u32 {
    const DATA: [(&str, &str); 9] = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ];

    let letters: HashMap<_, _> = DATA.iter().cloned().collect();

    inp.lines()
        .map(|line| {
            let line = letters
                .iter()
                .fold(line.to_string(), |acc, (k, v)| acc.replace(k, v));

            let digits = line
                .chars()
                .filter_map(|c| c.to_digit(10))
                .collect::<Vec<u32>>();
            digits.first().unwrap() * 10 + digits.last().unwrap()
        })
        .sum()
}

fn main() {
    let mut inp = String::new();

    io::stdin().read_to_string(&mut inp).unwrap();

    println!("{}", part1(&inp));
    println!("{}", part2(&inp));
}
