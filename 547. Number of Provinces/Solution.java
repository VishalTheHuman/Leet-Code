class Solution {
    HashSet<Integer> visited = new HashSet<>();
    int[][] connectedNodes;
    public int findCircleNum(int[][] isConnected) {
        connectedNodes = isConnected;
        int provinces = 0;
        for(int i=0;i<isConnected.length;i++){
            if(!visited.contains(i)){
                provinces++;
                dfs(i);
            }
        }
        return provinces;
    }

    public void dfs(int node){
        visited.add(node);
        for(int i=0;i<connectedNodes.length;i++){
            if(connectedNodes[node][i]==1 && !visited.contains(i)){
                dfs(i);
            }
        }
    }
}
