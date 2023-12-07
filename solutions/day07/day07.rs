use std::{
    collections::HashMap,
    io::{self, Read},
};

fn hand_power(hand: &str, joker: bool) -> &'static str {
    let counts = hand.chars().fold(HashMap::new(), |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        acc
    });

    let j = hand.matches("J").count();
    let mut bestcard = ' ';

    if joker && 0 < j && j < 5 {
        bestcard = counts
            .iter()
            .filter(|&(key, _)| *key != 'J')
            .max_by_key(|(_, &count)| count)
            .map(|(key, _)| *key)
            .unwrap();
    }

    let cnt: Vec<_> = counts
        .iter()
        .filter_map(|(key, &count)| {
            if joker && *key == 'J' && j < 5 {
                None
            } else if joker && *key == bestcard {
                Some(count + j)
            } else {
                Some(count)
            }
        })
        .collect();

    match *cnt.iter().max().unwrap() {
        5 => "6", // Five of a kind
        4 => "5", // Four of a kind
        3 => {
            if cnt.contains(&2) {
                "4" // Full House
            } else {
                "3" // Three of a kind
            }
        }
        _ => {
            let pairs = cnt.iter().filter(|&n| *n == 2).count();
            match pairs {
                2 => "2", // Two Pair
                1 => "1", // One Pair
                _ => "",  // High card
            }
        }
    }
}

fn hand_eval(hand: &str, cardmap: &HashMap<&str, &str>) -> u64 {
    let hand_power_str = hand_power(hand, *cardmap.get("J").unwrap() == "01").to_string();
    let card_values_str: String = hand
        .chars()
        .map(|c| cardmap.get(&c.to_string().as_str()).unwrap().to_string())
        .collect();

    (hand_power_str + &card_values_str).parse().unwrap()
}

fn part1(inp: &mut Vec<(String, u64)>, cardmap: &HashMap<&str, &str>) -> u64 {
    inp.sort_by_cached_key(|(hand, _)| hand_eval(hand, cardmap));
    inp.iter()
        .enumerate()
        .map(|(i, v)| (i as u64 + 1) * v.1)
        .sum()
}

fn part2(inp: &mut Vec<(String, u64)>, cardmap: &mut HashMap<&str, &str>) -> u64 {
    cardmap.insert("J", "01");
    part1(inp, cardmap)
}

fn main() {
    let mut inp = String::new();
    _ = io::stdin().read_to_string(&mut inp);

    let mut inp: Vec<(String, u64)> = inp
        .lines()
        .map(|line| line.split_whitespace().collect::<Vec<_>>())
        .map(|v| (v[0].to_string(), v[1].parse().unwrap()))
        .collect();

    let mut cardmap = HashMap::from([
        ("A", "14"),
        ("K", "13"),
        ("Q", "12"),
        ("J", "11"),
        ("T", "10"),
        ("9", "09"),
        ("8", "08"),
        ("7", "07"),
        ("6", "06"),
        ("5", "05"),
        ("4", "04"),
        ("3", "03"),
        ("2", "02"),
    ]);

    println!(
        "{} {}",
        part1(&mut inp, &cardmap),
        part2(&mut inp, &mut cardmap)
    );
}
