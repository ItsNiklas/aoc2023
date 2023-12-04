use std::{
    cmp::min,
    io::{self, Read},
};

struct Card {
    win: Vec<u64>,
    have: Vec<u64>,
}

fn part1(cards: &Vec<Card>) -> u64 {
    cards
        .iter()
        .map(|card| {
            let wins: u32 = card.have.iter().map(|x| card.win.contains(x) as u32).sum();

            if wins > 0 {
                u64::pow(2, wins - 1)
            } else {
                0
            }
        })
        .sum()
}

fn part2(cards: &Vec<Card>) -> u64 {
    let mut res = vec![1 as u64; cards.len()];

    cards.iter().enumerate().for_each(|(i, card)| {
        let wins: u64 = card.have.iter().map(|x| card.win.contains(x) as u64).sum();

        for j in 0..min(wins as usize, cards.len() - 1) {
            *res.get_mut(i + j + 1).unwrap() += res[i];
        }
    });

    res.iter().sum()
}

fn main() {
    let mut inp = String::new();
    io::stdin().read_to_string(&mut inp).unwrap();

    // let mut cards = Vec::<Card>::new();

    let cards = inp
        .lines()
        .map(|line| line.split_once(": ").unwrap().1.split_once(" | ").unwrap())
        .map(|(win, have)| Card {
            win: win
                .split(" ")
                .filter_map(|v| v.parse::<u64>().ok())
                .collect(),
            have: have
                .split(" ")
                .filter_map(|v| v.parse::<u64>().ok())
                .collect(),
        })
        .collect();

    println!("{} {}", part1(&cards), part2(&cards))
}
