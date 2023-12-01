#include <bits/stdc++.h>
using namespace std;

vector<string> inp;

int part1() {
    int sum = 0;

    for (auto line : inp) {
        vector<int> nums;
        for (auto c : line) {
            if ('0' <= c and c <= '9') {
                nums.emplace_back(c - '0');
            }
        }

        if (nums.size())
            sum += nums.front() * 10 + nums.back();
    }

    return sum;
}

int part2() {
    int sum = 0;

    unordered_map<string, string> spell = {
        {"one", "1"}, {"two", "2"},   {"three", "3"}, {"four", "4"}, {"five", "5"},
        {"six", "6"}, {"seven", "7"}, {"eight", "8"}, {"nine", "9"},
    };

    unordered_map<string, string> spell2 = {
        {"oneight", "18"},  {"twone", "21"},   {"threeight", "38"}, {"fiveight", "58"},
        {"sevenine", "79"}, {"eightwo", "82"}, {"eighthree", "83"}, {"nineight", "98"},
    };

    for (auto line : inp) {
        vector<int> nums;

        for (auto [k, v] : spell2) {
            size_t pos;
            while ((pos = line.find(k)) != string::npos)
                line.replace(pos, k.length(), v);
        }

        for (auto [k, v] : spell) {
            size_t pos;
            while ((pos = line.find(k)) != string::npos)
                line.replace(pos, k.length(), v);
        }

        for (auto c : line) {
            if ('0' <= c and c <= '9') {
                nums.emplace_back(c - '0');
            }
        }

        sum += nums.front() * 10 + nums.back();
    }

    return sum;
}

int main() {
    string line;
    while (getline(cin, line)) {
        inp.emplace_back(line);
    }

    cout << part1() << endl;
    cout << part2() << endl;
}