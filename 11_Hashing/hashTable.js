class HashTable {
    constructor(size = 10) {
        this.table = new Array(size);
        this.size = size;
    }

    // Hash Function
    hash(key) {
        let total = 0;

        for (let char of key) {
            total += char.charCodeAt(0);
        }
        console.log(total, "total");

        return total % this.size;
    }

    // Insert Data
    set(key, value) {
        const index = this.hash(key);

        // Create bucket if empty
        if (!this.table[index]) {
            this.table[index] = [];
        }

        // Store key-value pair
        this.table[index].push([key, value]);
    }

    // Get Data
    get(key) {
        const index = this.hash(key);
        const bucket = this.table[index];

        if (bucket) {
            for (let pair of bucket) {
                if (pair[0] === key) {
                    return pair[1];
                }
            }
        }

        return undefined;
    }

    // Display Hash Table
    display() {
        console.log(this.table);
    }
}

// Create Hash Table
const users = new HashTable();

// Insert Data
users.set("vinod", "Frontend Developer");
users.set("rahul", "Backend Developer");
users.set("amit", "UI Designer");
console.log(users.hash("vinod"))

// Retrieve Data
console.log(users.get("vinod"));
console.log(users.get("amit"));

// Display Full Table
users.display();