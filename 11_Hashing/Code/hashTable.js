class HashTable{
    constructor(size = 10){
        this.table = new Array(size).fill(null).map(()=>[]);
        this.size = size;
    }

    // Hash Function
    hash(key){
        let total = 0;
        for (let i = 0; i < key.length; i++) {
            total += key.charCodeAt(i) * i;
        }
        return total % this.size;
    }

    // dry code
    // key = "Vinod" -> v=118, i=105, n=110, o=111, d=100
    // hash = (118*0 + 105*1 + 110*2 + 111*3 + 100*4) % 10
    // 0 + 105 + 220 + 333 + 400 = 1058
    // 1058 % 10 = 8

    // key "34" -> 3=51, 4=52
    // hash = (51*0 + 52*1) % 10 = 52 % 10 = 2

    // key "35" -> 3=51, 5=53
    // hash = (51*0 + 53*1) % 10 = 53 % 10 = 3

    set(key, value){
        const index = this.hash(key);
        const bucket = this.table[index];

        // check if key already exists
        for (let i = 0; i < bucket.length; i++) {
            const pair = bucket[i];
            if(pair[0] === key){
                pair[1] = value;
                return;
            }
        }

        // Insert new key-value pair
        bucket.push([key, value]);
    }

    // dry run
    // set("Vinod", 123)
    // index = 8
    // bucket = []
    // bucket.push(["Vinod", 123])
    // table = [..., [["Vinod", 123]], ...]

    // index = 3
    // bucket = []
    // bucket.push(["35", 456])
    // table = [..., [["Vinod", 123], ["35", 456]], ...]

    get(key){
        const index = this.hash(key);
        const bucket = this.table[index];
        for (let i = 0; i < bucket.length; i++) {
            const pair = bucket[i];
            if(pair[0] === key){
                return pair[1];
            }
        }
        return undefined;
    }

    // dry run
    // get("Vinod")
    // index = 8
    // bucket = [["Vinod", 123]]
    // for (let i = 0; i < bucket.length; i++) {
    //   const pair = bucket[i];
    //   if(pair[0] === "Vinod"){
    //     return pair[1];
    //   }
    // }
    // return undefined;
    // return 123

    delete(key){
        const index = this.hash(key);
        const bucket = this.table[index];
        for (let i = 0; i < bucket.length; i++) {
            const pair = bucket[i];
            if(pair[0] === key){
                bucket.splice(i, 1);
                return;
            }
        }
        return undefined;
    }

    // dry run
    // delete("Vinod")
    // index = 8
    // bucket = [["Vinod", 123]]
    // for (let i = 0; i < bucket.length; i++) {
    //   const pair = bucket[i];
    //   if(pair[0] === "Vinod"){
    //     bucket.splice(i, 1);
    //     return;
    //   }
    // }
    // return undefined;

    display(){
        for (let i = 0; i < this.table.length; i++) {
            const bucket = this.table[i];
            if (bucket.length > 0) {
                console.log(`${i}: ${JSON.stringify(bucket)}`);
            }
        }
    }
}

const ht = new HashTable(5);
ht.set("Vinod", 123);
ht.set("Suresh", 456);
ht.set("Ramesh", 789);
ht.set("Ravi", 1011);
ht.set("Rahul", 1213);
ht.display();
console.log(ht.get("Vinod"));
console.log(ht.delete("Vinod"));