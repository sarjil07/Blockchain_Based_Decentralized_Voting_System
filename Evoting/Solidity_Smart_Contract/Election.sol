// SPDX-License-Identifier: MIT
pragma solidity ^0.5.17;
contract Election{
    
    int totalVoteCount=0;
    int candCount=0;
    int max=0;
    
    //Store Accounts Voted
    mapping(address => bool) public voters;

    //Store Candidates 
    mapping(int => int) public candidates;
    

    function addCandidates(int cid,int vcount) public{ 
        candCount=candCount+1;
        candidates[cid]=vcount;

    }
    
    function voteInc(int vid,address addr) public{
        require(!voters[addr]);
        voters[addr]=true;
        totalVoteCount=totalVoteCount+1;
        candidates[vid]=candidates[vid]+1;
    }
    
    function winnerCandidate() public returns(int){
        for (int i=1;i<=candCount;i++){
            if(max<candidates[i]){
                max=candidates[i];
                //return max;
            }
        }
        return max;
    }
    
    
}