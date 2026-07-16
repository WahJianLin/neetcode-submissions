class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    containDups(nums){
        const seenArr = [];
        for(let i = 0; i<nums.length; i++){
            if(nums[i]!='.') {
                if(seenArr.includes(nums[i])){
                    return true;
                }
                seenArr.push(nums[i]);
            }
        }
        return false;
    }
    isValidSudoku(board) {
        const thing = [];
        // // checks horizontal
        // for(let a = 0; a<9; a++) {
        //     if(this.containDups(board[a])){
        //         return false;
        //     }
        // }
        // checks vertical
        for(let b = 0; b<9; b++) {
            const vSeq = [];
            //gets vertical sequence
            for(let c = 0; c<9; c++){
                vSeq.push(board[c][b]);
            }
            if(this.containDups(vSeq)){
                return false;
            }
        }
        // checks squares && horizontal
        for(let z = 0; z<9; z+=3){
            let seq1 = [];
            let seq2 = [];
            let seq3 = [];
            for (let y = z; y<z+3; y++){
                if(this.containDups(board[y])){
                    return false;
                }
                seq1 = seq1.concat(board[y].slice(0,3));
                seq2 = seq2.concat(board[y].slice(3,6));
                seq3 = seq3.concat(board[y].slice(6,9));
            }
            if(this.containDups(seq1) || this.containDups(seq2) || this.containDups(seq3)){
                return false;
            }
        }
        return true;
    }
    
}
