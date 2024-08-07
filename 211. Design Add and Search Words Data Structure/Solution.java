class WordDictionary {
    HashMap<Character, HashMap> trie, current;
    public WordDictionary() {
        trie = new HashMap<>();
    }
    
    public void addWord(String word) {
        HashMap<Character, HashMap> current = trie;
        for(char x : word.toCharArray()){
            if (!current.containsKey(x)){
                HashMap<Character, HashMap> temp = new HashMap<>();
                current.put(x, temp);
            }
            current = current.get(x);
        }
        current.put('*', new HashMap<Character, HashMap>());
    }

    public boolean search(String word) {
        current = trie;
        return dfs(word);
    }
    
    public boolean dfs(String word) {
        if (word.length()==0 || current.size()==0){
            return false;
        }
        if (word.length()==1){
            if (current.containsKey(word.charAt(0)) && current.get(word.charAt(0)).containsKey('*')){
                return true;
            }else if (word.charAt(0)=='.'){
                for(char x : current.keySet()){
                    if (current.get(x).containsKey('*')){
                        return true;
                    }
                }
                return false;
            }
        }
        
        String substring = word.substring(1);
        if (word.charAt(0)=='.'){
            HashMap<Character, HashMap> temp = current;
            for(char x : current.keySet()){
                current = current.get(x);
                if(dfs(substring)){
                    return true;
                }
                current = temp;
            }
        }else if(current.containsKey(word.charAt(0))){
            current = current.get(word.charAt(0));
            return dfs(substring);
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
