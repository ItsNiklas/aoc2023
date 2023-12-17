#pragma GCC optimize("Ofast,unroll-loops")
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000;
const int INF = 1e9;

int N, M;
int inp[MAXN][MAXN];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

struct State {
    int y, x, dir, steps, dist;

    bool operator<(const State &other) const { return dist > other.dist; }
};

vector<vector<vector<vector<int>>>> d;

void dijkstra(bool ultra) {
    d.assign(N, vector<vector<vector<int>>>(
                    M, vector<vector<int>>(5, vector<int>(12, INF))));
    priority_queue<State> pq;
    pq.push({0, 0, -1, -1, 0});

    while (!pq.empty()) {
        auto [y, x, dir, steps, dist] = pq.top();
        pq.pop();

        if (d[y][x][dir + 1][steps + 1] <= dist)
            continue;

        d[y][x][dir + 1][steps + 1] = dist;

        for (int i = 0; i < 4; ++i) {
            int vy = y + dy[i], vx = x + dx[i];
            int new_dir = dir + 1, new_steps = steps + 1;

            if (vy < 0 || vy >= N || vx < 0 || vx >= M)
                continue; // Out of bounds

            if (ultra && i != dir && steps < 4 && dir != -1)
                continue; // Can I turn?

            if (dir == (i + 2) % 4)
                continue; // No backsies

            if ((new_steps = (i != dir) ? 1 : steps + 1) > (ultra ? 10 : 3))
                continue; // Not again

            pq.push({vy, vx, i, new_steps, dist + inp[vy][vx]});
        }
    }
}

int heat(bool ultra) {
    int minHeatLoss = INF;
    for (int dir = 0; dir < 4; ++dir) {
        for (int steps = ultra ? (4 + 1) : (1 + 1); steps < 12; ++steps) {
            minHeatLoss = min(minHeatLoss, d[N - 1][M - 1][dir][steps]);
        }
    }
    return minHeatLoss;
}

int main() {
    string line;
    vector<string> lines;
    while (getline(cin, line)) {
        lines.push_back(line);
    }

    N = lines.size();
    M = lines[0].size();

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            inp[i][j] = lines[i][j] - '0';
        }
    }

    dijkstra(false);
    int part1_result = heat(false);

    dijkstra(true);
    int part2_result = heat(true);

    cout << part1_result << " " << part2_result << endl;
}
