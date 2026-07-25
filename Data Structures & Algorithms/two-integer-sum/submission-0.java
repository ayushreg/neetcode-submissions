class Solution {
    public int[] twoSum(int[] nums, int target) {

        // create a hash map
        // Our array ints are keys and their index is the value
        HashMap<Integer,Integer> table = new HashMap<>();


        for(int i = 0; i < nums.length; i++){
           int difference = target - nums[i];
           if(table.containsKey(difference)){
                return new int[] {table.get(difference), i};
           }
           else {
                table.put(nums[i], i); // put nums[i] not the difference
           }
        }

        return new int[]{};
    
    }
}