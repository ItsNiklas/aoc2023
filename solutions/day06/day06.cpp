#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double lf;

ll pred(ll sec, ll runtime) { return (sec) * (runtime - sec); }

ll part1(const vector<ll> &time, const vector<ll> &distance) {
    ll res = 1;

    for (size_t i = 0; i < time.size(); i++) {
        res *= std::ranges::count_if(
            std::views::iota(0, time[i] + 1),
            [i, &time, &distance](ll j) { return pred(j, time[i]) > distance[i]; });
    }

    return res;
}

ll part2(ll time, ll distance) {
    return ranges::count_if(views::iota(0, time + 1), [time, distance](ll j) {
        return pred(j, time) > distance;
    });
}

signed main() {
    vector<ll> time, distance;
    string totaltime;
    string totaldistance;
    string line;

    cin >> line;
    getline(cin, line); // Read the entire line for time
    stringstream ssTime(line);
    ll temp;
    while (ssTime >> temp) {
        time.push_back(temp);
        totaltime += to_string(temp);
    }

    cin >> line;
    getline(cin, line); // Read the entire line for distance
    stringstream ssDistance(line);
    while (ssDistance >> temp) {
        distance.push_back(temp);
        totaldistance += to_string(temp);
    }

    cout << part1(time, distance) << " "
         << part2(stoll(totaltime), stoll(totaldistance)) << endl;
}