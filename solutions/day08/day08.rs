use std::{
    collections::HashMap,
    io::{self, Read},
};

use itertools::Itertools;
use num_integer::lcm;
use regex::Regex;

fn part1(node: &str, instr: &str, nodemap: &HashMap<String, (String, String)>) -> u64 {
    let mut node = node; // Extend lifetime

    instr
        .chars()
        .cycle()
        .enumerate()
        .map(|(i, d)| {
            let tmp = nodemap.get(node).unwrap();
            node = if d == 'L' { &tmp.0 } else { &tmp.1 };

            (i, node)
        })
        .find(|&(_, node)| node.ends_with("Z"))
        .map(|(i, _)| (i + 1) as u64)
        .unwrap()
}

fn part2(instr: &str, nodemap: &HashMap<String, (String, String)>) -> u64 {
    let starts = nodemap.keys().filter(|k| k.ends_with("A")).collect_vec();

    starts
        .iter()
        .map(|&node| part1(node, instr, &nodemap))
        .reduce(lcm)
        .unwrap()
}

fn main() {
    let mut inp = String::new();
    _ = io::stdin().read_to_string(&mut inp);

    let instr = inp.lines().next().unwrap();

    let re = Regex::new(r"\w+").unwrap();
    let nodemap: HashMap<String, (String, String)> = inp
        .lines()
        .skip(2)
        .map(|line| {
            let tup: (String, String, String) = re
                .find_iter(line)
                .map(|mat| mat.as_str().to_string())
                .collect_tuple()
                .unwrap();

            (tup.0, (tup.1, tup.2))
        })
        .collect();

    println!(
        "{} {}",
        part1("AAA", instr, &nodemap),
        part2(instr, &nodemap),
    );
}
