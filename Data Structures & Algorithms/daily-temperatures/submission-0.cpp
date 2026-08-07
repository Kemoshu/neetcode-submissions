class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> days;
        vector<int> result(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++) {
            while (!days.empty() && temperatures[i] > temperatures[days.top()]) {
                int prevIndex = days.top();
                days.pop();
                result[prevIndex] = i - prevIndex;
            }
            days.push(i);
        }
        return result;
    }
};
