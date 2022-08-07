/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    if (nums.length === 1) {
        
        return false;
    }
    
    var hashSet = new Array(); 
    
    for (let i = 0; i < nums.length; i++) {
        
        if (hashSet.includes(nums[i])) {
            
            return true;
            
        }
        
        hashSet.push(nums[i]);
        
    }
    
    return false;
};