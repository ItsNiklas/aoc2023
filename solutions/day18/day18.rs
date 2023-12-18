use std::io::{self, Read};

use itertools::Itertools;
use regex::Regex;

fn part1and2(inp: &String, hex: bool) -> i64 {
    let (mut x, mut y, mut b) = (0, 0, 0);
    let mut pnts = vec![(0, 0)];

    let re = Regex::new(r"[a-z0-9]{5}").unwrap();

    for line in inp.lines() {
        let (d, k, c) = line.split_whitespace().collect_tuple().unwrap();
        let (d, k) = if hex {
            (
                c.chars().nth(7).unwrap(),
                i64::from_str_radix(re.find(c).unwrap().as_str(), 16).unwrap(),
            )
        } else {
            (d.chars().next().unwrap(), k.parse().unwrap())
        };

        b += k;

        match d {
            'R' | '0' => x += k,
            'D' | '1' => y += k,
            'L' | '2' => x -= k,
            'U' | '3' => y -= k,
            _ => panic!(),
        }

        pnts.push((y, x));
    }

    // Shoelace + Pick
    pnts.iter()
        .tuple_windows()
        .map(|(a, b)| a.0 * b.1 - a.1 * b.0)
        .sum::<i64>()
        .abs()
        / 2
        + b / 2
        + 1
}

fn main() {
    let mut inp = String::new();
    _ = io::stdin().read_to_string(&mut inp);

    println!("{} {}", part1and2(&inp, false), part1and2(&inp, true));
}
