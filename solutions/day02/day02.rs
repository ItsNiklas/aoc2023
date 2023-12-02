use std::{
    cmp::max,
    io::{self, Read},
};

fn part1(inp: &String) -> u64 {
    const MAX_RED: u64 = 12;
    const MAX_GREEN: u64 = 13;
    const MAX_BLUE: u64 = 14;

    // bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
    inp.lines()
        .enumerate()
        .filter_map(|(i, line)| {
            line.split(":")
                .last()?
                .split(", ")
                .filter_map(|pair| {
                    let (n, color) = pair.trim().split_once(" ")?;
                    let n: u64 = n.parse().ok()?;
                    let max = match color {
                        "red" => MAX_RED,
                        "green" => MAX_GREEN,
                        "blue" => MAX_BLUE,
                        _ => return Some(Err(())),
                    };
                    if n > max {
                        Some(Err(()))
                    } else {
                        Some(Ok(()))
                    }
                })
                .all(|x| x.is_ok())
                .then(|| i as u64 + 1)
        })
        .sum()
}

fn part2(inp: &str) -> u64 {
    inp.lines()
        .map(|line| {
            let maxes = line
                .split(":")
                .last()
                .unwrap()
                .split(", ")
                .map(|pair| {
                    let (n, color) = pair.trim().split_once(" ").unwrap();
                    (color, n.parse::<u64>().unwrap())
                })
                .fold(
                    (0, 0, 0),
                    |(max_red, max_green, max_blue), (color, n)| match color {
                        "red" => (max(max_red, n), max_green, max_blue),
                        "green" => (max_red, max(max_green, n), max_blue),
                        "blue" => (max_red, max_green, max(max_blue, n)),
                        _ => panic!(""),
                    },
                );

            maxes.0 * maxes.1 * maxes.2
        })
        .sum()
}

fn main() {
    let mut inp = String::new();
    io::stdin().read_to_string(&mut inp).unwrap();
    inp = inp.replace(";", ",");

    println!("{} {}", part1(&inp), part2(&inp));
}
