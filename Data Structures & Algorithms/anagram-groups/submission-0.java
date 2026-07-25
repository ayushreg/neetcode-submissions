class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // Hold the frequency array and the coresponding strings 
        HashMap<String, List<String>> answer = new HashMap<>();
        
        // get frequency of each character in each string
        for(int i = 0; i < strs.length; i++){
            String value = strs[i];
            char[] charValue = value.toCharArray();
            int[] freq = new int[26];
            
            for(int j = 0; j < charValue.length; j++){
                freq[charValue[j] - 'a']++;
            }

            // Convert the array into a string so we can store it
            String key = Arrays.toString(freq);

            // Now we need to add it to the list
            // check if the key is in the list
            if(!answer.containsKey(key)){
                // If it doesnt have the key yet, we can make it and have a empty list for it
                answer.put(key, new ArrayList<String>());
            }

            // now we need to get the coresponding list
            List<String> subList = answer.get(key);
            subList.add(strs[i]);
        }

        return new ArrayList<>(answer.values());
    }
}
