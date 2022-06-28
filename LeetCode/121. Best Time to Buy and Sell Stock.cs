public class Solution {
    public int MaxProfit(int[] prices) {
     int profit = 0, bought = prices[0];
       
        for (int i=1; i<prices.Length; i++)
        {
            if(prices[i] < bought) bought = prices[i];
            else if (profit < prices[i] - bought) profit = prices[i] - bought;
        }
        
        return profit;
    }
}