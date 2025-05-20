#include <iostream>
#include <vector>
#include <unordered_set> // <-- Add this line
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
int main() {
    Solution solution;

    // Test case 1
    vector<int> test1 = {1, 2, 3, 4, 5};
    cout << solution.hasDuplicate(test1) << endl;
    return 0;
}