class Solution {
    // go from right to left
    // record largest
    // compare new value with largest and see if profit is higher
    // save higher profit as maxProfit
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int bigStock = 0;
        
        for(int i = prices.length-1; i>-1;i--) {
            if(bigStock == 0) {
                bigStock = prices[i];
            } else{
                if(bigStock<prices[i]){
                    bigStock=prices[i];
                }else{
                    int profit = bigStock - prices[i];
                    if(profit>maxProfit){
                        maxProfit=profit;
                    }
                }
            }
        }

        return maxProfit;
    }
}
