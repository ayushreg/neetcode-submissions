class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int product = 1;
        int zeroCount = 0;
    

        // Get the total product of the array
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                zeroCount++;
                continue;
            }
            product *= nums[i];
        }

        // If we have a zero that all elements other than zero will be zero
        // The index with zero will have the product
        // If no zeros are there then we just divide each index by the product

        for(int i = 0; i < nums.length; i++){
            if(zeroCount > 1){
                answer[i] = 0; // If more than one zero than all products are zeros
                continue;
            }
            else if(zeroCount == 1 && nums[i] != 0){
                answer[i] = 0;  // Zero exists, so replace all other indexes with zero
                continue;
            }
   
            // Put the product at the index with zero
            if(nums[i] == 0){
                answer[i] = product;
            }

            if(zeroCount == 0){
                answer[i] = product / nums[i];
            }
        }

        return answer;
    }
}  
