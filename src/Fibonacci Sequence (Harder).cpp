#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

vector<vector<int>> matrix(int r, int c) {
    return vector<vector<int>>(r, vector<int>(c, 0));
}

vector<vector<int>> mul(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int n = a.size(), m = b.size(), k = b[0].size();
    vector<vector<int>> ret = matrix(n, k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            for (int t = 0; t < m; t++) {
                ret[i][j] = (ret[i][j] + (1LL * a[i][t] * b[t][j]) % MOD) % MOD;
            }
        }
    }
    return ret;
}

vector<vector<int>> mat_pow(vector<vector<int>> mat, int power) {
    int n = mat.size();
    vector<vector<int>> ret = matrix(n, n);
    for (int i = 0; i < n; i++) {
        ret[i][i] = 1;
    }
    for (int bit = 0; bit < 32; bit++) {
        if ((power >> bit) & 1) {
            ret = mul(ret, mat);
        }
        mat = mul(mat, mat);
    }
    return ret;
}

int main() {
    string n;
    cin >> n;

    if (n == "0") {
        cout << 0 << endl;
    } else if (n == "1") {
        cout << 1 << endl;
    } else {
        vector<vector<int>> ST = {{0, 1}};
        vector<vector<int>> MUL = {{1, 1}, {1, 0}};
        vector<vector<int>> finalMul = {{1, 0}, {0, 1}};
        vector<vector<int>> pow_mat = MUL;

        for (int i = n.size() - 1; i >= 0; i--) {
            int v = n[i] - '0';
            for (int j = 0; j < v; j++) {
                finalMul = mul(finalMul, pow_mat);
            }

            vector<vector<int>> newPow = {{1, 0}, {0, 1}};
            for (int j = 0; j < 10; j++) {
                newPow = mul(newPow, pow_mat);
            }

            pow_mat = newPow;
        }

        vector<vector<int>> ans = mul(ST, finalMul);
        cout << ans[0][0] << endl;
    }

    return 0;
}
