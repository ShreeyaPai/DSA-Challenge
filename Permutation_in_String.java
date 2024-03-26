class Solution {
    public boolean checkInclusion(String s1, String s2) {

//if s1 itself is large return false
       if(s1.length()>s2.length()){
           return false;
       } 
       //store freq of s1 and s2
       int[]freq=new int[26];
       //prepare freq length till s1 length,for s1 character add 1 for s2 char subs 1
       for(int i=0;i<s1.length();i++){
           freq[s1.charAt(i)-'a']+=1;
           freq[s2.charAt(i)-'a']-=1;
       }
       //loop till exhaust at that time we'll compare total s2.length()characters with s1.length() characters
       for(int i=0;i<s2.length()-s1.length();i++){
           //chaeck if s1 & s2 are anagram of each other
           if(checkAnagram(freq)){
               return true;
           }
        // if not updated frequently, map to remove s2 first character and add s2 next character
        freq[s2.charAt(i)-'a']+=1;
        freq[s2.charAt(i+s1.length())-'a']-=1;
       } 
       //chaeck for last comparison
       return checkAnagram(freq);
    }
    //check if freq map has all zero, it will be true for anagram
    private boolean checkAnagram(int[]freq){
        for(int i=0;i<freq.length;i++){
            if(freq[i]!=0){
                return false;
            }
        }
        return true;
    }
}
