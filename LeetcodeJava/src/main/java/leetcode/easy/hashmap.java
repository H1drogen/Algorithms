package leetcode.easy;

import java.util.HashMap;
import java.util.Map;

public class hashmap {
//    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
//    Each letter in magazine can only be used once in ransomNote.

    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> note = new HashMap<>();
        for (int i = 0; i < ransomNote.length(); i++) {
            char current = ransomNote.charAt(i);
            note.put(current, note.getOrDefault(current, 0) + 1);
        }
        for (int i = 0; i < magazine.length(); i++){
            char letter = magazine.charAt(i);
            if (note.containsKey(letter)){
                if (note.get(letter) == 1){
                    note.remove(letter);
                } else {
                note.put(letter, note.get(letter) - 1);
            }
        }
    }
        return note.isEmpty();
    }

}
