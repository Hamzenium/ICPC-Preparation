class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> countS;
        unordered_map<char, int> countT;
        for(int i=0; i < s.length(); i++){
            countS[s[i]]++;
            countT[t[i]]++;
        }
        return countS == countT;
    }
};
int main() {
    Solution solution;

    // Test case 1
    string s1 = "anagram";
    string t1 = "nagaram";
    cout << solution.isAnagram(s1, t1) << endl; // Output: 1 (true)

    // Test case 2
    string s2 = "rat";
    string t2 = "car";
    cout << solution.isAnagram(s2, t2) << endl; // Output: 0 (false)

    return 0;
}