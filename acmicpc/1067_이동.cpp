#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

const double _PI = 3.14159265358979323846;
typedef complex<double> C;

inline C E(double x) { return C(cos(2*_PI*x),-sin(2*_PI*x)); }

void FFT(vector<C>& x, bool invert) {
    int n = (int)x.size(), newN = 1;
	vector<int> scramble;
    while (newN < n) newN <<= 1;
    x.resize(newN);
    scramble.resize(newN);
    int d = 1;
    for (int bit = (newN >> 1); bit; bit >>= 1) {
        for (int i = 0; i < newN; i++) if ((i / d) & 1) scramble[i] |= bit;
        d <<= 1;
    }
    vector<C> v(n), w(n);
    for (int i = 0; i < n; i++) v[i] = x[scramble[i]];
    int inv = (invert ? -1 : 1);
    for (int lv = 2; lv <= n; lv <<= 1) {
        for (int i = 0; i < n; i += lv) {
            for (int k = 0; k < lv / 2; k++) {
                C ve = v[i + k];
                C vo = v[i + k + lv / 2] * E((double)k / lv * inv);
                w[i + k] = ve + vo;
                w[i + k + lv / 2] = ve - vo;
            }
        }
        for (int i = 0; i < n; i++) v[i] = w[i];
    }
    if (invert) for (int i = 0; i < n; i++) x[i] = v[i] / (double)n;
    else for (int i = 0; i < n; i++) x[i] = v[i];
}

vector<int> mul(vector<int>& a, vector<int>& b) {
    vector<C> A(a.begin(), a.end()), B(b.begin(), b.end());
    int n = (int)max(A.size(), B.size());
    int i = 0;
    while ((1 << i) < (n << 1)) i++;
    n = (1 << i);
    A.resize(n);
    B.resize(n);
    FFT(A, 0);
    FFT(B, 0);
    for (int i = 0; i < n; i++) A[i] *= B[i];
    FFT(A, 1);
    vector<int> ret(n);
    for (int i = 0; i < n; i++) ret[i] = round(A[i].real());
    return ret;
}

int main() {
    fastio;
    int n; cin >> n;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i]; //a 입력
    for (int i = 0; i < n; i++) cin >> b[i]; //b 입력
    for (int i = 0; i < n; i++) a.push_back(a[i]); //a 복사
    reverse(b.begin(), b.end()); //b 반전 -> FFT에서 컨볼루션을 위해 재반전하기 때문.
    vector<int> ans = mul(a, b); 
    cout << *max_element(ans.begin(), ans.end()) << '\n';
}
