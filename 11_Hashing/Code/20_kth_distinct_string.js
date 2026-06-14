function  kthDistinct(arr, k) {
        let hmap = new Map();
        for(let i = 0; i<arr.length; i++){
            hmap.set(arr[i], (hmap.get(arr[i]) || 0) + 1)
        }
        let dist = []
        for(let [key, value] of hmap){
            if(value == 1){
                dist.push(key)
            }
        }
        if(dist.length < k){
            return "None";
        } else{
            return dist[k-1];
        }
    }


    console.log(kthDistinct(["d","b","c","b","c","a"], 2));