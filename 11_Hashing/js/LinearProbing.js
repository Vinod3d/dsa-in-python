class HashTableLinearProbing {
    constructor(size = 5) {
        this.table = new Array(size).fill(null);
        this.size = size;
        this.count = 0; // Tracks number of elements
    }

    _hash(key) {
        let hashValue = 0;
        for (let i = 0; i < key.length; i++) {
            hashValue += key.charCodeAt(i);
        }
        return hashValue % this.size;
    }

    // Insert or update key-value pair with Linear Probing
    set(key, value) {
        // Resize if load factor >= 0.7
        if (this.count / this.size >= 0.7) {
            this._654(this.size * 2);
        }

        let index = this._hash(key);
        let i = 0;

        while (i < this.size) {
            let probeIndex = (index + i) % this.size;
            let current = this.table[probeIndex];

            // If empty slot or slot marked deleted, insert here
            if (current === null || current.isDeleted) {
                this.table[probeIndex] = { key, value, isDeleted: false };
                this.count++;
                return;
            }

            // If key already exists, update value
            if (current.key === key && !current.isDeleted) {
                current.value = value;
                return;
            }

            i++; // Move to next slot
        }

        throw new Error("Hash Table is full!");
    }

    // Retrieve value by key
    get(key) {
        let index = this._hash(key);
        let i = 0;

        while (i < this.size) {
            let probeIndex = (index + i) % this.size;
            let current = this.table[probeIndex];

            if (current === null) {
                return undefined; // Hit empty slot, key doesn't exist
            }

            if (current.key === key && !current.isDeleted) {
                return current.value;
            }

            i++;
        }
        return undefined;
    }

    // Delete value (using Soft Delete / Tombstone marking)
    delete(key) {
        let index = this._hash(key);
        let i = 0;

        while (i < this.size) {
            let probeIndex = (index + i) % this.size;
            let current = this.table[probeIndex];

            if (current === null) {
                return false; // Key not found
            }

            if (current.key === key && !current.isDeleted) {
                current.isDeleted = true; // Mark as deleted (tombstone)
                this.count--;
                return true;
            }

            i++;
        }
        return false;
    }

    // Dynamic Rehashing
    _resize(newSize) {
        console.log(`--- Resizing table from ${this.size} to ${newSize} ---`);
        const oldTable = this.table;
        
        this.size = newSize;
        this.table = new Array(newSize).fill(null);
        this.count = 0;

        for (let entry of oldTable) {
            if (entry !== null && !entry.isDeleted) {
                this.set(entry.key, entry.value);
            }
        }
    }

    display() {
        console.log(this.table.map((item, idx) => {
            if (item === null) return `[${idx}]: Empty`;
            if (item.isDeleted) return `[${idx}]: Deleted (Tombstone)`;
            return `[${idx}]: ${item.key} -> ${item.value}`;
        }).join("\n"));
    }
}

// Verification Open Addressing
console.log("\n--- Testing Linear Probing & Rehashing ---");
const mapLinear = new HashTableLinearProbing(4);
mapLinear.set("A", "Apple");
mapLinear.set("B", "Banana");
mapLinear.set("C", "Cherry"); // Trigger resizing (3/4 = 0.75 >= 0.7)

mapLinear.display();
console.log("Get 'B':", mapLinear.get("B"));
mapLinear.delete("B");
console.log("After deleting 'B':");
mapLinear.display();
console.log("Get 'C' (probe should skip deleted B):", mapLinear.get("C"));